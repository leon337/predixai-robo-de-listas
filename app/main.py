#!/usr/bin/env python3
from __future__ import annotations

import json
import threading
import time
import tkinter as tk
from copy import deepcopy
from dataclasses import asdict, dataclass, field
from datetime import date, datetime
from pathlib import Path
from tkinter import messagebox, ttk
from uuid import uuid4

from pynput import mouse
from pynput.mouse import Button, Controller

ROOT_DIR = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT_DIR / "config"
CONFIG_PATH = CONFIG_DIR / "config_predixai_robo_listas.json"
MAX_SIGNALS = 5


@dataclass
class Signal:
    id: str
    date_str: str
    time_str: str
    direction: str
    status: str = "AGENDADO"

    @property
    def scheduled_at(self) -> datetime:
        return datetime.strptime(f"{self.date_str} {self.time_str}", "%Y-%m-%d %H:%M:%S")


@dataclass
class ScheduleList:
    id: str
    name: str
    date_str: str
    signals: list[Signal] = field(default_factory=list)
    updated_at: str = ""


@dataclass
class CoordinateProfile:
    id: str
    name: str
    application: str
    monitor: str
    resolution: str
    scale: str
    coordinates: dict[str, dict[str, int] | None]
    updated_at: str
    validated: bool = False
    lists: list[ScheduleList] = field(default_factory=list)


class PredixAIRoboListas:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("PredixAI Robô de Listas — V2.1")
        self.root.geometry("680x660")
        self.root.minsize(620, 560)
        self.root.attributes("-topmost", True)
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

        self.colors = {
            "bg": "#07111f", "panel": "#0d1b2a", "panel2": "#12263a",
            "text": "#f7fbff", "muted": "#9db0c4", "green": "#70ff00",
            "blue": "#1c3550", "blue_hover": "#294a6c", "blue_active": "#37658f",
            "orange": "#ff8a00", "gray": "#7f8c98", "red": "#ff4d5a",
            "field": "#091625",
        }
        self.root.configure(bg=self.colors["bg"])
        self.mouse_controller = Controller()
        self.profiles: list[CoordinateProfile] = []
        self.active_profile_id: str | None = None
        self.active_list_id: str | None = None
        self.session_signals: list[Signal] = []
        self.running = False
        self.paused = False
        self.execution_thread: threading.Thread | None = None
        self.capture_listener: mouse.Listener | None = None
        self.history: list[str] = []
        self.nav_buttons: dict[str, ttk.Button] = {}
        self.clock_var = tk.StringVar(value="--:--:--")
        self.status_var = tk.StringVar(value="PRONTO")
        self.next_var = tk.StringVar(value="Nenhum sinal agendado")
        self.counter_var = tk.StringVar(value=f"0 / {MAX_SIGNALS} sinais")
        self.profile_var = tk.StringVar(value="")
        self.list_var = tk.StringVar(value="")
        self._configure_style()
        self._load_config()
        self._build_shell()
        self.show_home()
        self._tick_clock()

    @property
    def active_profile(self) -> CoordinateProfile | None:
        return next((item for item in self.profiles if item.id == self.active_profile_id), None)

    @property
    def active_list(self) -> ScheduleList | None:
        profile = self.active_profile
        return next((item for item in profile.lists if item.id == self.active_list_id), None) if profile else None

    @property
    def coords(self) -> dict[str, dict[str, int] | None]:
        return self.active_profile.coordinates if self.active_profile else {"LARANJA": None, "CINZA": None}

    def _screen_signature(self) -> tuple[str, str]:
        resolution = f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}"
        try:
            scale = f"{round(float(self.root.tk.call('tk', 'scaling')) * 75)}%"
        except (tk.TclError, ValueError):
            scale = "desconhecida"
        return resolution, scale

    def _configure_style(self) -> None:
        style = ttk.Style()
        style.theme_use("clam")
        for name, bg in (("App.TFrame", self.colors["bg"]), ("Panel.TFrame", self.colors["panel"]), ("Panel2.TFrame", self.colors["panel2"])):
            style.configure(name, background=bg)
        style.configure("Title.TLabel", background=self.colors["bg"], foreground=self.colors["text"], font=("Arial", 19, "bold"))
        style.configure("Subtitle.TLabel", background=self.colors["bg"], foreground=self.colors["muted"], font=("Arial", 9))
        style.configure("Header.TLabel", background=self.colors["panel"], foreground=self.colors["text"], font=("Arial", 13, "bold"))
        style.configure("Body.TLabel", background=self.colors["panel2"], foreground=self.colors["text"], font=("Arial", 10))
        style.configure("Muted.TLabel", background=self.colors["panel"], foreground=self.colors["muted"], font=("Arial", 9))
        style.configure("Status.TLabel", background=self.colors["panel"], foreground=self.colors["green"], font=("Arial", 12, "bold"))
        for name, bg, fg in (
            ("Primary.TButton", self.colors["green"], "#07111f"),
            ("Secondary.TButton", self.colors["blue"], self.colors["text"]),
            ("ActiveNav.TButton", self.colors["blue_active"], self.colors["text"]),
            ("Danger.TButton", self.colors["red"], "white"),
            ("Orange.TButton", self.colors["orange"], "white"),
            ("Gray.TButton", self.colors["gray"], "white"),
        ):
            hover = self.colors["blue_hover"] if name in {"Secondary.TButton", "ActiveNav.TButton"} else bg
            style.configure(name, background=bg, foreground=fg, borderwidth=0, padding=8, font=("Arial", 9, "bold"))
            style.map(name, background=[("pressed", bg), ("active", hover), ("disabled", "#33465a")], foreground=[("pressed", fg), ("active", fg), ("disabled", "#d6dde5")])
        for widget_name in ("TEntry", "TCombobox", "TSpinbox"):
            style.configure(widget_name, fieldbackground=self.colors["field"], foreground=self.colors["text"], padding=5)
            style.map(widget_name, fieldbackground=[("readonly", self.colors["field"]), ("disabled", "#263646")], foreground=[("readonly", self.colors["text"]), ("disabled", "#aeb9c5")], selectbackground=[("!disabled", self.colors["blue_active"])], selectforeground=[("!disabled", self.colors["text"])])

    def _build_shell(self) -> None:
        self.shell = ttk.Frame(self.root, style="App.TFrame", padding=14)
        self.shell.pack(fill="both", expand=True)
        header = ttk.Frame(self.shell, style="App.TFrame")
        header.pack(fill="x")
        mark = tk.Canvas(header, width=58, height=58, bg=self.colors["bg"], highlightthickness=0)
        mark.pack(side="left")
        mark.create_oval(4, 4, 54, 54, outline=self.colors["green"], width=2)
        mark.create_text(29, 27, text="P", fill="white", font=("Arial", 25, "bold"))
        mark.create_text(30, 46, text="AI", fill=self.colors["green"], font=("Arial", 7, "bold"))
        brand = ttk.Frame(header, style="App.TFrame")
        brand.pack(side="left", padx=10)
        ttk.Label(brand, text="PredixAI Robô de Listas", style="Title.TLabel").pack(anchor="w")
        ttk.Label(brand, text="Perfis, listas datadas e execução controlada", style="Subtitle.TLabel").pack(anchor="w")
        right = ttk.Frame(header, style="App.TFrame")
        right.pack(side="right")
        ttk.Label(right, textvariable=self.clock_var, style="Title.TLabel").pack(anchor="e")
        ttk.Label(right, textvariable=self.status_var, style="Subtitle.TLabel").pack(anchor="e")
        nav = ttk.Frame(self.shell, style="App.TFrame")
        nav.pack(fill="x", pady=(12, 10))
        for label, command in (("Início", self.show_home), ("Perfis", self.show_profiles), ("Listas", self.show_lists), ("Agenda", self.show_schedule), ("Execução", self.show_execution), ("Histórico", self.show_history)):
            button = ttk.Button(nav, text=label, command=command, style="Secondary.TButton")
            button.pack(side="left", padx=(0, 5))
            self.nav_buttons[label] = button
        self.content = ttk.Frame(self.shell, style="App.TFrame")
        self.content.pack(fill="both", expand=True)

    def _set_page(self, page: str) -> None:
        for label, button in self.nav_buttons.items():
            button.configure(style="ActiveNav.TButton" if label == page else "Secondary.TButton")

    def _clear(self) -> None:
        for child in self.content.winfo_children():
            child.destroy()

    def _panel(self, title: str, subtitle: str) -> ttk.Frame:
        panel = ttk.Frame(self.content, style="Panel.TFrame", padding=16)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text=title, style="Header.TLabel").pack(anchor="w")
        ttk.Label(panel, text=subtitle, style="Muted.TLabel").pack(anchor="w", pady=(3, 12))
        return panel

    def show_home(self) -> None:
        self._set_page("Início")
        self._clear()
        panel = self._panel("Nova sessão", "Escolha um perfil e uma lista antes de iniciar.")
        ttk.Label(panel, textvariable=self.status_var, style="Status.TLabel").pack(anchor="w", pady=(0, 10))
        profile_combo = ttk.Combobox(panel, textvariable=self.profile_var, values=[item.name for item in self.profiles], state="readonly")
        profile_combo.pack(fill="x", pady=4)
        profile_combo.bind("<<ComboboxSelected>>", lambda _event: self._select_profile_by_name())
        list_combo = ttk.Combobox(panel, textvariable=self.list_var, values=[item.name for item in self.active_profile.lists] if self.active_profile else [], state="readonly")
        list_combo.pack(fill="x", pady=4)
        list_combo.bind("<<ComboboxSelected>>", lambda _event: self._select_list_by_name())
        resolution, scale = self._screen_signature()
        for text in (
            f"Perfil: {self.active_profile.name if self.active_profile else 'nenhum selecionado'}",
            f"Aplicação: {self.active_profile.application if self.active_profile else '—'}",
            f"Lista: {self.active_list.name if self.active_list else 'nenhuma selecionada'}",
            f"Tela atual: {resolution} | escala {scale}",
            f"Compatibilidade: {self._profile_compatibility_text(self.active_profile)}",
        ):
            card = ttk.Frame(panel, style="Panel2.TFrame", padding=10)
            card.pack(fill="x", pady=3)
            ttk.Label(card, text=text, style="Body.TLabel").pack(anchor="w")
        actions = ttk.Frame(panel, style="Panel.TFrame")
        actions.pack(fill="x", pady=(14, 0))
        ttk.Button(actions, text="Gerenciar perfis", command=self.show_profiles, style="Secondary.TButton").pack(side="left", padx=(0, 6))
        ttk.Button(actions, text="Gerenciar listas", command=self.show_lists, style="Secondary.TButton").pack(side="left", padx=(0, 6))
        ttk.Button(actions, text="Preparar sessão", command=self._prepare_session, style="Primary.TButton").pack(side="left")

    def _profile_compatibility_text(self, profile: CoordinateProfile | None) -> str:
        if not profile:
            return "selecione ou crie um perfil"
        resolution, scale = self._screen_signature()
        if profile.resolution != resolution or profile.scale != scale:
            return "RECALIBRAÇÃO NECESSÁRIA"
        if not profile.validated or not all(profile.coordinates.values()):
            return "calibração ou teste pendente"
        return "perfil pronto"

    def _select_profile_by_name(self) -> None:
        profile = next((item for item in self.profiles if item.name == self.profile_var.get()), None)
        self.active_profile_id = profile.id if profile else None
        self.active_list_id = profile.lists[0].id if profile and profile.lists else None
        self.list_var.set(self.active_list.name if self.active_list else "")
        self._save_config()
        self.show_home()

    def _select_list_by_name(self) -> None:
        if not self.active_profile:
            return
        selected = next((item for item in self.active_profile.lists if item.name == self.list_var.get()), None)
        self.active_list_id = selected.id if selected else None
        self._save_config()
        self.show_home()

    def _prepare_session(self) -> None:
        if self.running:
            messagebox.showwarning("Execução ativa", "Encerre a execução atual antes de preparar outra sessão.")
            return
        if not self.active_profile:
            messagebox.showwarning("Perfil obrigatório", "Selecione ou crie um perfil.")
            return
        if self._profile_compatibility_text(self.active_profile) != "perfil pronto":
            messagebox.showwarning("Perfil incompatível", "Recalibre e teste o perfil para esta tela.")
            self.show_profiles()
            return
        if not self.active_list:
            messagebox.showwarning("Lista obrigatória", "Selecione ou crie uma lista.")
            self.show_lists()
            return
        self.session_signals = [Signal(**asdict(item)) for item in deepcopy(self.active_list.signals)]
        for signal in self.session_signals:
            signal.status = "AGENDADO"
        self.status_var.set("PRONTO")
        self._update_summary()
        self.show_schedule()

    def show_profiles(self) -> None:
        self._set_page("Perfis")
        self._clear()
        panel = self._panel("Perfis de coordenadas", "Cada perfil representa uma aplicação e um ambiente de tela.")
        toolbar = ttk.Frame(panel, style="Panel.TFrame")
        toolbar.pack(fill="x", pady=(0, 10))
        ttk.Button(toolbar, text="Novo perfil", command=lambda: self._profile_dialog(), style="Primary.TButton").pack(side="left", padx=(0, 6))
        ttk.Button(toolbar, text="Editar", command=lambda: self._profile_dialog(self.active_profile) if self.active_profile else messagebox.showwarning("Perfil", "Selecione um perfil primeiro."), style="Secondary.TButton").pack(side="left", padx=(0, 6))
        ttk.Button(toolbar, text="Excluir", command=self._delete_profile, style="Danger.TButton").pack(side="left")
        if not self.profiles:
            ttk.Label(panel, text="Nenhum perfil criado.", style="Muted.TLabel").pack(anchor="w", pady=15)
            return
        for profile in self.profiles:
            selected = profile.id == self.active_profile_id
            row = ttk.Frame(panel, style="Panel2.TFrame", padding=11)
            row.pack(fill="x", pady=4)
            ttk.Label(row, text=f"{'● ' if selected else ''}{profile.name}\n{profile.application} | {profile.monitor} | {profile.resolution} | {profile.scale}\n{self._profile_compatibility_text(profile)} | {len(profile.lists)} lista(s)", style="Body.TLabel").pack(side="left", fill="x", expand=True)
            ttk.Button(row, text="Selecionar", command=lambda item=profile: self._activate_profile(item), style="Secondary.TButton").pack(side="right", padx=(5, 0))
            ttk.Button(row, text="Calibrar", command=lambda item=profile: self._open_profile_calibration(item), style="Orange.TButton").pack(side="right")

    def _profile_dialog(self, profile: CoordinateProfile | None = None) -> None:
        if self.running:
            messagebox.showwarning("Execução ativa", "Não é possível alterar perfis durante uma execução.")
            return
        dialog = tk.Toplevel(self.root)
        dialog.title("Editar perfil" if profile else "Novo perfil")
        dialog.geometry("430x320")
        dialog.transient(self.root)
        dialog.grab_set()
        frame = ttk.Frame(dialog, padding=16)
        frame.pack(fill="both", expand=True)
        name_var = tk.StringVar(value=profile.name if profile else "")
        app_var = tk.StringVar(value=profile.application if profile else "")
        monitor_var = tk.StringVar(value=profile.monitor if profile else "Tela principal")
        for label, widget in (("Nome do perfil", ttk.Entry(frame, textvariable=name_var)), ("Aplicação", ttk.Entry(frame, textvariable=app_var)), ("Monitor/ambiente", ttk.Entry(frame, textvariable=monitor_var))):
            ttk.Label(frame, text=label).pack(anchor="w", pady=(5, 2))
            widget.pack(fill="x")
        resolution, scale = self._screen_signature()
        ttk.Label(frame, text=f"Tela detectada: {resolution} | {scale}").pack(anchor="w", pady=10)

        def save() -> None:
            name, application = name_var.get().strip(), app_var.get().strip()
            if not name or not application:
                messagebox.showerror("Campos obrigatórios", "Informe nome e aplicação.", parent=dialog)
                return
            if any(item.id != (profile.id if profile else None) and item.name.casefold() == name.casefold() for item in self.profiles):
                messagebox.showerror("Nome duplicado", "Já existe um perfil com esse nome.", parent=dialog)
                return
            if profile:
                profile.name, profile.application, profile.monitor = name, application, monitor_var.get().strip() or "Tela principal"
                profile.updated_at = datetime.now().isoformat(timespec="seconds")
                selected = profile
            else:
                selected = CoordinateProfile(str(uuid4()), name, application, monitor_var.get().strip() or "Tela principal", resolution, scale, {"LARANJA": None, "CINZA": None}, datetime.now().isoformat(timespec="seconds"), False, [])
                self.profiles.append(selected)
            self.active_profile_id = selected.id
            self.profile_var.set(selected.name)
            self._save_config()
            dialog.destroy()
            self._open_profile_calibration(selected)

        ttk.Button(frame, text="Salvar", command=save, style="Primary.TButton").pack(fill="x", pady=(15, 0))

    def _activate_profile(self, profile: CoordinateProfile) -> None:
        if self.running:
            messagebox.showwarning("Execução ativa", "Não é possível trocar o perfil durante uma execução.")
            return
        self.active_profile_id = profile.id
        self.active_list_id = profile.lists[0].id if profile.lists else None
        self.profile_var.set(profile.name)
        self.list_var.set(self.active_list.name if self.active_list else "")
        self._save_config()
        self.show_profiles()

    def _delete_profile(self) -> None:
        if self.running:
            messagebox.showwarning("Execução ativa", "Não é possível excluir perfis durante uma execução.")
            return
        profile = self.active_profile
        if not profile:
            messagebox.showwarning("Perfil", "Selecione um perfil primeiro.")
            return
        if not messagebox.askyesno("Excluir perfil", f"Excluir '{profile.name}' e todas as listas vinculadas?"):
            return
        self.profiles = [item for item in self.profiles if item.id != profile.id]
        self.active_profile_id = self.profiles[0].id if self.profiles else None
        self.active_list_id = self.active_profile.lists[0].id if self.active_profile and self.active_profile.lists else None
        self.profile_var.set(self.active_profile.name if self.active_profile else "")
        self.list_var.set(self.active_list.name if self.active_list else "")
        self._save_config()
        self.show_profiles()

    def _open_profile_calibration(self, profile: CoordinateProfile) -> None:
        if self.running:
            messagebox.showwarning("Execução ativa", "Não é possível calibrar durante uma execução.")
            return
        self.active_profile_id = profile.id
        self.profile_var.set(profile.name)
        self._set_page("Perfis")
        self._clear()
        panel = self._panel(f"Calibrar: {profile.name}", "Recalibre quando mudar de monitor, resolução ou layout.")
        current_resolution, current_scale = self._screen_signature()
        if profile.resolution != current_resolution or profile.scale != current_scale:
            profile.resolution, profile.scale, profile.validated = current_resolution, current_scale, False
        self.coord_vars: dict[str, tk.StringVar] = {}
        for key, label, style_name in (("LARANJA", "AÇÃO 1 / PARA CIMA", "Orange.TButton"), ("CINZA", "AÇÃO 2 / PARA BAIXO", "Gray.TButton")):
            row = ttk.Frame(panel, style="Panel2.TFrame", padding=12)
            row.pack(fill="x", pady=5)
            left = ttk.Frame(row, style="Panel2.TFrame")
            left.pack(side="left", fill="x", expand=True)
            ttk.Label(left, text=label, style="Body.TLabel").pack(anchor="w")
            var = tk.StringVar(value=self._coord_text(key))
            self.coord_vars[key] = var
            ttk.Label(left, textvariable=var, style="Body.TLabel").pack(anchor="w", pady=(2, 0))
            ttk.Button(row, text="Recalibrar", command=lambda item=key: self._capture_coordinate(item), style=style_name).pack(side="right")
        ttk.Button(panel, text="Mover cursor para os pontos", command=self._preview_coordinates, style="Secondary.TButton").pack(fill="x", pady=(14, 5))
        ttk.Button(panel, text="Testar cliques", command=self._test_both_coordinates, style="Secondary.TButton").pack(fill="x", pady=5)
        ttk.Button(panel, text="Salvar e usar perfil", command=self._confirm_profile, style="Primary.TButton").pack(fill="x", pady=5)

    def _capture_coordinate(self, key: str) -> None:
        if self.capture_listener is not None or not self.active_profile:
            return
        self.status_var.set(f"CALIBRANDO {key}")
        self.root.iconify()

        def on_click(x: int, y: int, _button: object, pressed: bool) -> bool | None:
            if pressed and self.active_profile:
                self.active_profile.coordinates[key] = {"x": int(x), "y": int(y)}
                self.active_profile.validated = False
                self.active_profile.updated_at = datetime.now().isoformat(timespec="seconds")
                return False
            return None

        self.capture_listener = mouse.Listener(on_click=on_click)
        self.capture_listener.start()
        self.root.after(120, self._poll_capture)

    def _poll_capture(self) -> None:
        if self.capture_listener and self.capture_listener.is_alive():
            self.root.after(120, self._poll_capture)
            return
        self.capture_listener = None
        self.root.deiconify(); self.root.lift(); self.root.focus_force(); self.root.attributes("-topmost", True)
        self.status_var.set("PRONTO")
        self._save_config()
        for key, var in getattr(self, "coord_vars", {}).items():
            var.set(self._coord_text(key))

    def _coord_text(self, key: str) -> str:
        coord = self.coords.get(key)
        return "não configurado" if not coord else f"X={coord['x']} | Y={coord['y']}"

    def _preview_coordinates(self) -> None:
        if not all(self.coords.values()):
            messagebox.showwarning("Calibração incompleta", "Calibre os dois pontos primeiro.")
            return
        for key in ("LARANJA", "CINZA"):
            coord = self.coords[key]
            if coord:
                self.mouse_controller.position = (coord["x"], coord["y"]); time.sleep(0.8)

    def _test_both_coordinates(self) -> None:
        if not all(self.coords.values()):
            messagebox.showwarning("Calibração incompleta", "Calibre os dois pontos primeiro.")
            return
        if not messagebox.askyesno("Teste controlado", "O mouse fará um clique em cada coordenada. Continuar?"):
            return
        for key in ("LARANJA", "CINZA"):
            coord = self.coords[key]
            if coord:
                self.mouse_controller.position = (coord["x"], coord["y"]); time.sleep(0.4); self.mouse_controller.click(Button.left, 1); time.sleep(0.5)
        if self.active_profile:
            self.active_profile.validated = True
            self.active_profile.updated_at = datetime.now().isoformat(timespec="seconds")
            self._save_config()
        messagebox.showinfo("Teste concluído", "As duas coordenadas foram testadas.")

    def _confirm_profile(self) -> None:
        if not self.active_profile or not all(self.coords.values()):
            messagebox.showwarning("Perfil incompleto", "Calibre os dois pontos.")
            return
        if not self.active_profile.validated:
            messagebox.showwarning("Teste pendente", "Teste as duas coordenadas antes de usar o perfil.")
            return
        self._save_config(); self.show_home()

    def show_lists(self) -> None:
        self._set_page("Listas")
        self._clear()
        panel = self._panel("Listas programadas", "Crie listas para hoje, amanhã ou qualquer outra data.")
        if not self.active_profile:
            ttk.Label(panel, text="Selecione um perfil primeiro.", style="Muted.TLabel").pack(anchor="w")
            return
        toolbar = ttk.Frame(panel, style="Panel.TFrame")
        toolbar.pack(fill="x", pady=(0, 10))
        ttk.Button(toolbar, text="Nova lista", command=lambda: self._list_dialog(), style="Primary.TButton").pack(side="left", padx=(0, 6))
        ttk.Button(toolbar, text="Editar", command=lambda: self._list_dialog(self.active_list) if self.active_list else messagebox.showwarning("Lista", "Selecione uma lista primeiro."), style="Secondary.TButton").pack(side="left", padx=(0, 6))
        ttk.Button(toolbar, text="Duplicar", command=lambda: self._list_dialog(self.active_list, True) if self.active_list else messagebox.showwarning("Lista", "Selecione uma lista primeiro."), style="Secondary.TButton").pack(side="left", padx=(0, 6))
        ttk.Button(toolbar, text="Excluir", command=self._delete_list, style="Danger.TButton").pack(side="left")
        if not self.active_profile.lists:
            ttk.Label(panel, text="Nenhuma lista criada.", style="Muted.TLabel").pack(anchor="w", pady=15)
            return
        for schedule in sorted(self.active_profile.lists, key=lambda item: (item.date_str, item.name.casefold())):
            selected = schedule.id == self.active_list_id
            row = ttk.Frame(panel, style="Panel2.TFrame", padding=11)
            row.pack(fill="x", pady=4)
            ttk.Label(row, text=f"{'● ' if selected else ''}{schedule.name}\n{self._format_date(schedule.date_str)} | {len(schedule.signals)} sinal(is)", style="Body.TLabel").pack(side="left", fill="x", expand=True)
            ttk.Button(row, text="Selecionar", command=lambda item=schedule: self._activate_list(item), style="Secondary.TButton").pack(side="right")

    def _list_dialog(self, schedule: ScheduleList | None = None, duplicate: bool = False) -> None:
        if self.running:
            messagebox.showwarning("Execução ativa", "Não é possível alterar listas durante uma execução.")
            return
        dialog = tk.Toplevel(self.root)
        dialog.title("Nova lista" if not schedule or duplicate else "Editar lista")
        dialog.geometry("420x250")
        dialog.transient(self.root)
        dialog.grab_set()
        frame = ttk.Frame(dialog, padding=16)
        frame.pack(fill="both", expand=True)
        name_var = tk.StringVar(value=f"{schedule.name} - cópia" if schedule and duplicate else (schedule.name if schedule else ""))
        date_var = tk.StringVar(value=schedule.date_str if schedule else date.today().isoformat())
        ttk.Label(frame, text="Nome da lista").pack(anchor="w", pady=(5, 2)); ttk.Entry(frame, textvariable=name_var).pack(fill="x")
        ttk.Label(frame, text="Data (AAAA-MM-DD)").pack(anchor="w", pady=(10, 2)); ttk.Entry(frame, textvariable=date_var).pack(fill="x")

        def save() -> None:
            name = name_var.get().strip()
            try:
                parsed_date = datetime.strptime(date_var.get().strip(), "%Y-%m-%d").date().isoformat()
            except ValueError:
                messagebox.showerror("Data inválida", "Use o formato AAAA-MM-DD.", parent=dialog); return
            if not name or not self.active_profile:
                messagebox.showerror("Nome obrigatório", "Informe um nome.", parent=dialog); return
            current_id = schedule.id if schedule and not duplicate else None
            if any(item.id != current_id and item.name.casefold() == name.casefold() and item.date_str == parsed_date for item in self.active_profile.lists):
                messagebox.showerror("Lista duplicada", "Já existe uma lista com esse nome nessa data.", parent=dialog); return
            if schedule and not duplicate:
                schedule.name, schedule.date_str = name, parsed_date
                for signal in schedule.signals: signal.date_str = parsed_date
                schedule.updated_at = datetime.now().isoformat(timespec="seconds")
                selected = schedule
            else:
                copied = [Signal(str(uuid4()), parsed_date, item.time_str, item.direction, "AGENDADO") for item in schedule.signals] if schedule else []
                selected = ScheduleList(str(uuid4()), name, parsed_date, copied, datetime.now().isoformat(timespec="seconds"))
                self.active_profile.lists.append(selected)
            self.active_list_id = selected.id
            self.list_var.set(selected.name)
            self._save_config(); dialog.destroy(); self.show_lists()

        ttk.Button(frame, text="Salvar", command=save, style="Primary.TButton").pack(fill="x", pady=(16, 0))

    def _activate_list(self, schedule: ScheduleList) -> None:
        if self.running:
            messagebox.showwarning("Execução ativa", "Não é possível trocar de lista durante uma execução.")
            return
        self.active_list_id = schedule.id
        self.list_var.set(schedule.name)
        self._save_config(); self.show_lists()

    def _delete_list(self) -> None:
        if self.running:
            messagebox.showwarning("Execução ativa", "Não é possível excluir listas durante uma execução.")
            return
        if not self.active_profile or not self.active_list:
            messagebox.showwarning("Lista", "Selecione uma lista primeiro."); return
        if not messagebox.askyesno("Excluir lista", f"Excluir '{self.active_list.name}'?"):
            return
        self.active_profile.lists = [item for item in self.active_profile.lists if item.id != self.active_list.id]
        self.active_list_id = self.active_profile.lists[0].id if self.active_profile.lists else None
        self.list_var.set(self.active_list.name if self.active_list else "")
        self._save_config(); self.show_lists()

    def show_schedule(self) -> None:
        self._set_page("Agenda")
        self._clear()
        panel = self._panel("Agenda da lista", "Edite a lista selecionada. Durante execução, a agenda fica bloqueada.")
        if not self.active_profile:
            ttk.Label(panel, text="Selecione um perfil primeiro.", style="Muted.TLabel").pack(anchor="w"); return
        if not self.active_list:
            ttk.Label(panel, text="Selecione ou crie uma lista.", style="Muted.TLabel").pack(anchor="w"); return
        ttk.Label(panel, text=f"{self.active_list.name} — {self._format_date(self.active_list.date_str)}", style="Status.TLabel").pack(anchor="w", pady=(0, 8))
        form = ttk.Frame(panel, style="Panel2.TFrame", padding=10)
        form.pack(fill="x", pady=(0, 10))
        now = datetime.now()
        self.hour_var, self.minute_var, self.second_var = tk.StringVar(value=f"{now.hour:02d}"), tk.StringVar(value=f"{now.minute:02d}"), tk.StringVar(value=f"{now.second:02d}")
        time_row = ttk.Frame(form, style="Panel2.TFrame")
        time_row.pack(anchor="w", pady=(0, 7))
        for var, limit, label in ((self.hour_var, 23, "Hora"), (self.minute_var, 59, "Min"), (self.second_var, 59, "Seg")):
            box = ttk.Frame(time_row, style="Panel2.TFrame"); box.pack(side="left", padx=(0, 8))
            ttk.Label(box, text=label, style="Body.TLabel").pack(anchor="w")
            spin = ttk.Spinbox(box, from_=0, to=limit, width=5, textvariable=var, format="%02.0f", wrap=True)
            spin.pack(); spin.bind("<FocusOut>", lambda _event, variable=var, maximum=limit: self._normalize_time_var(variable, maximum)); spin.bind("<Return>", lambda _event, variable=var, maximum=limit: self._normalize_time_var(variable, maximum))
        self.direction_var = tk.StringVar(value="PARA_CIMA")
        ttk.Combobox(form, textvariable=self.direction_var, values=["PARA_CIMA", "PARA_BAIXO"], state="readonly", width=18).pack(anchor="w", pady=(0, 7))
        add_button = ttk.Button(form, text="Adicionar sinal", command=self._add_signal, style="Primary.TButton"); add_button.pack(anchor="w")
        if self.running: add_button.state(["disabled"])
        self.signal_list = ttk.Frame(panel, style="Panel.TFrame"); self.signal_list.pack(fill="both", expand=True); self._render_signal_list()
        footer = ttk.Frame(panel, style="Panel.TFrame"); footer.pack(fill="x", pady=(10, 0))
        ttk.Label(footer, textvariable=self.counter_var, style="Muted.TLabel").pack(side="left")
        clear_button = ttk.Button(footer, text="Limpar lista", command=self._clear_schedule, style="Danger.TButton"); clear_button.pack(side="right", padx=(5, 0))
        start_button = ttk.Button(footer, text="Iniciar", command=self._start_execution, style="Primary.TButton"); start_button.pack(side="right")
        if self.running: clear_button.state(["disabled"]); start_button.state(["disabled"])

    def _normalize_time_var(self, variable: tk.StringVar, maximum: int) -> None:
        try: value = int(variable.get())
        except ValueError: value = 0
        variable.set(f"{max(0, min(maximum, value)):02d}")

    def _add_signal(self) -> None:
        if self.running:
            messagebox.showwarning("Execução ativa", "A agenda está bloqueada durante a execução."); return
        if not self.active_list or len(self.active_list.signals) >= MAX_SIGNALS:
            messagebox.showwarning("Limite", f"Selecione uma lista e respeite o limite de {MAX_SIGNALS} sinais."); return
        try:
            hour, minute, second = int(self.hour_var.get()), int(self.minute_var.get()), int(self.second_var.get())
            if not (0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59): raise ValueError
            time_str = f"{hour:02d}:{minute:02d}:{second:02d}"
        except (ValueError, AttributeError):
            messagebox.showerror("Horário inválido", "Revise hora, minuto e segundo."); return
        if any(item.time_str == time_str for item in self.active_list.signals):
            messagebox.showwarning("Horário duplicado", "Já existe um sinal nesse horário."); return
        self.active_list.signals.append(Signal(str(uuid4()), self.active_list.date_str, time_str, self.direction_var.get()))
        self.active_list.signals.sort(key=lambda item: item.time_str)
        self.active_list.updated_at = datetime.now().isoformat(timespec="seconds")
        self._save_config(); self._sync_session_from_list(); self._render_signal_list()

    def _sync_session_from_list(self) -> None:
        if self.active_list and not self.running:
            self.session_signals = [Signal(**asdict(item)) for item in deepcopy(self.active_list.signals)]
            self._update_summary()

    def _render_signal_list(self) -> None:
        if not hasattr(self, "signal_list"): return
        for child in self.signal_list.winfo_children(): child.destroy()
        if not self.active_list or not self.active_list.signals:
            ttk.Label(self.signal_list, text="Nenhum sinal cadastrado.", style="Muted.TLabel").pack(anchor="w", pady=10); return
        for index, signal in enumerate(self.active_list.signals):
            row = ttk.Frame(self.signal_list, style="Panel2.TFrame", padding=9); row.pack(fill="x", pady=3)
            icon = "▲" if signal.direction == "PARA_CIMA" else "▼"
            ttk.Label(row, text=f"{index + 1}. {self._format_date(signal.date_str)} {signal.time_str}  {icon} {signal.direction}", style="Body.TLabel").pack(side="left")
            button = ttk.Button(row, text="Remover", command=lambda pos=index: self._remove_signal(pos), style="Danger.TButton"); button.pack(side="right")
            if self.running: button.state(["disabled"])

    def _remove_signal(self, index: int) -> None:
        if self.running:
            messagebox.showwarning("Execução ativa", "A agenda está bloqueada durante a execução."); return
        if self.active_list and 0 <= index < len(self.active_list.signals):
            self.active_list.signals.pop(index); self._save_config(); self._sync_session_from_list(); self._render_signal_list()

    def _clear_schedule(self) -> None:
        if self.running:
            messagebox.showwarning("Execução ativa", "A agenda está bloqueada durante a execução."); return
        if not self.active_list: return
        if self.active_list.signals and not messagebox.askyesno("Limpar lista", "Remover todos os sinais desta lista?"): return
        self.active_list.signals = []; self._save_config(); self._sync_session_from_list(); self._render_signal_list()

    def _update_summary(self) -> None:
        self.counter_var.set(f"{len(self.session_signals)} / {MAX_SIGNALS} sinais")
        pending = next((item for item in sorted(self.session_signals, key=lambda signal: signal.scheduled_at) if item.status == "AGENDADO"), None)
        self.next_var.set(f"Próximo: {self._format_date(pending.date_str)} {pending.time_str} — {pending.direction}" if pending else "Nenhum sinal agendado")

    def _start_execution(self) -> None:
        if self.running or (self.execution_thread and self.execution_thread.is_alive()):
            messagebox.showwarning("Execução ativa", "Já existe uma execução em andamento."); return
        if not self.active_list or not self.active_list.signals:
            messagebox.showwarning("Lista vazia", "Adicione pelo menos um sinal."); return
        if not self.active_profile or self._profile_compatibility_text(self.active_profile) != "perfil pronto":
            messagebox.showwarning("Perfil inválido", "Selecione, calibre e teste um perfil compatível."); return
        self.session_signals = [Signal(**asdict(item)) for item in deepcopy(self.active_list.signals)]
        now = datetime.now()
        for signal in self.session_signals: signal.status = "EXPIRADO" if signal.scheduled_at < now else "AGENDADO"
        if not any(item.status == "AGENDADO" for item in self.session_signals):
            self._append_history(f"{self.active_profile.name} | {self.active_list.name} — lista sem sinais futuros; todos expirados.")
            self.status_var.set("FINALIZADO"); self._update_summary(); self.show_execution(); return
        self.running, self.paused = True, False
        self.status_var.set("EM EXECUÇÃO")
        self._update_summary(); self.show_execution()
        self.execution_thread = threading.Thread(target=self._execution_loop, daemon=True); self.execution_thread.start()

    def show_execution(self) -> None:
        self._set_page("Execução")
        self._clear()
        panel = self._panel("Execução", f"Perfil: {self.active_profile.name if self.active_profile else 'nenhum'} | Lista: {self.active_list.name if self.active_list else 'nenhuma'}")
        ttk.Label(panel, textvariable=self.status_var, style="Status.TLabel").pack(pady=6)
        ttk.Label(panel, textvariable=self.clock_var, style="Header.TLabel").pack()
        ttk.Label(panel, textvariable=self.next_var, style="Muted.TLabel").pack(pady=(6, 10))
        self.execution_list = ttk.Frame(panel, style="Panel.TFrame"); self.execution_list.pack(fill="both", expand=True); self._render_execution_list()
        actions = ttk.Frame(panel, style="Panel.TFrame"); actions.pack(fill="x", pady=(10, 0))
        pause_button = ttk.Button(actions, text="Pausar/Retomar", command=self._toggle_pause, style="Secondary.TButton"); pause_button.pack(side="left")
        stop_button = ttk.Button(actions, text="Encerrar", command=self._stop_execution, style="Danger.TButton"); stop_button.pack(side="right")
        if not self.running: pause_button.state(["disabled"]); stop_button.state(["disabled"])

    def _render_execution_list(self) -> None:
        if not hasattr(self, "execution_list"): return
        for child in self.execution_list.winfo_children(): child.destroy()
        icons = {"AGENDADO": "…", "EXECUTANDO": "▶", "CLIQUE_ENVIADO": "✓", "EXPIRADO": "⌛", "CANCELADO": "×", "ERRO": "!"}
        for signal in sorted(self.session_signals, key=lambda item: item.scheduled_at):
            row = ttk.Frame(self.execution_list, style="Panel2.TFrame", padding=9); row.pack(fill="x", pady=3)
            ttk.Label(row, text=f"{icons.get(signal.status, '•')} {self._format_date(signal.date_str)} {signal.time_str} — {signal.direction} — {signal.status}", style="Body.TLabel").pack(anchor="w")

    def _execution_loop(self) -> None:
        try:
            while self.running:
                if self.paused: time.sleep(0.2); continue
                pending = [item for item in self.session_signals if item.status == "AGENDADO"]
                if not pending:
                    self.running = False; self.root.after(0, self._finish_execution); return
                current = min(pending, key=lambda item: item.scheduled_at)
                now = datetime.now(); self.root.after(0, self._update_summary)
                if now >= current.scheduled_at:
                    delay = (now - current.scheduled_at).total_seconds()
                    if delay > 30:
                        current.status = "EXPIRADO"
                        self._append_history(f"{current.id} — {current.date_str} {current.time_str} — EXPIRADO ({delay:.1f}s de atraso)")
                        self.root.after(0, self._render_execution_list); self.root.after(0, self._update_summary); continue
                    current.status = "EXECUTANDO"; self.root.after(0, self._render_execution_list)
                    target = "LARANJA" if current.direction == "PARA_CIMA" else "CINZA"
                    coord = self.coords[target]
                    if coord is None: raise RuntimeError(f"Coordenada {target} não configurada")
                    self.mouse_controller.position = (coord["x"], coord["y"]); time.sleep(0.35)
                    if not self.running: current.status = "CANCELADO"; break
                    self.mouse_controller.click(Button.left, 1); current.status = "CLIQUE_ENVIADO"
                    self._append_history(f"{self.active_profile.name if self.active_profile else 'perfil'} | {self.active_list.name if self.active_list else 'lista'} | {current.id} — {current.date_str} {current.time_str} — {current.direction} — CLIQUE_ENVIADO X={coord['x']} Y={coord['y']}")
                    self.root.after(0, self._render_execution_list); self.root.after(0, self._update_summary)
                time.sleep(0.08)
        except Exception as exc:
            self.running = False
            for signal in self.session_signals:
                if signal.status == "EXECUTANDO": signal.status = "ERRO"
            self._append_history(f"ERRO — {exc}")
            self.root.after(0, self._handle_execution_error, str(exc))

    def _handle_execution_error(self, message: str) -> None:
        self.status_var.set("ERRO"); self._render_execution_list(); messagebox.showerror("Erro na execução", message)

    def _toggle_pause(self) -> None:
        if self.running:
            self.paused = not self.paused
            self.status_var.set("PAUSADO" if self.paused else "EM EXECUÇÃO")
            self._append_history("Execução pausada." if self.paused else "Execução retomada.")

    def _stop_execution(self) -> None:
        if not self.running or not messagebox.askyesno("Encerrar execução", "Encerrar a execução atual?"): return
        self.running, self.paused = False, False
        for signal in self.session_signals:
            if signal.status in {"AGENDADO", "EXECUTANDO"}: signal.status = "CANCELADO"
        self.status_var.set("ENCERRADO"); self._append_history("Execução encerrada manualmente."); self._update_summary(); self._render_execution_list()

    def _finish_execution(self) -> None:
        self.paused = False; self.status_var.set("FINALIZADO"); self._update_summary(); self._render_execution_list(); self._append_history("Sessão finalizada.")
        messagebox.showinfo("PredixAI Robô de Listas", "Sessão finalizada.")

    def show_history(self) -> None:
        self._set_page("Histórico")
        self._clear()
        panel = self._panel("Histórico", "Registro persistente das sessões.")
        field = tk.Text(panel, bg=self.colors["field"], fg=self.colors["text"], insertbackground=self.colors["text"], relief="flat", wrap="word", font=("Courier New", 9))
        field.pack(fill="both", expand=True); field.insert("1.0", "\n".join(self.history) if self.history else "Nenhuma execução registrada."); field.configure(state="disabled")

    def _append_history(self, line: str) -> None:
        self.history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — {line}"); self._save_config()

    def _tick_clock(self) -> None:
        self.clock_var.set(datetime.now().strftime("%H:%M:%S")); self.root.after(250, self._tick_clock)

    def _format_date(self, value: str) -> str:
        try: return datetime.strptime(value, "%Y-%m-%d").strftime("%d/%m/%Y")
        except ValueError: return value

    def _save_config(self) -> None:
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        payload = {"version": 3, "active_profile_id": self.active_profile_id, "active_list_id": self.active_list_id, "profiles": [asdict(profile) for profile in self.profiles], "history": self.history[-1000:]}
        CONFIG_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def _load_config(self) -> None:
        if not CONFIG_PATH.exists(): self._update_summary(); return
        try:
            payload = json.loads(CONFIG_PATH.read_text(encoding="utf-8")); version = payload.get("version", 1)
            if version == 3:
                self.profiles = [self._profile_from_dict(item) for item in payload.get("profiles", [])]
                self.active_profile_id, self.active_list_id = payload.get("active_profile_id"), payload.get("active_list_id")
                self.history = [str(item) for item in payload.get("history", [])]
            elif version == 2:
                self.profiles = [self._migrate_v2_profile(item) for item in payload.get("profiles", [])]
                self.active_profile_id = payload.get("active_profile_id")
            else: self._migrate_v1(payload)
            if self.active_profile:
                self.profile_var.set(self.active_profile.name)
                if not self.active_list and self.active_profile.lists: self.active_list_id = self.active_profile.lists[0].id
                self.list_var.set(self.active_list.name if self.active_list else "")
        except (OSError, ValueError, TypeError, KeyError):
            self.profiles, self.history = [], []
            self.active_profile_id = self.active_list_id = None
        self.session_signals = []; self._update_summary(); self._save_config()

    def _profile_from_dict(self, item: dict) -> CoordinateProfile:
        lists = [ScheduleList(data["id"], data["name"], data["date_str"], [Signal(**signal) for signal in data.get("signals", [])], data.get("updated_at", "")) for data in item.get("lists", [])]
        return CoordinateProfile(item["id"], item["name"], item.get("application", item.get("platform", "Aplicação")), item.get("monitor", "Tela principal"), item.get("resolution", ""), item.get("scale", ""), item.get("coordinates", {"LARANJA": None, "CINZA": None}), item.get("updated_at", ""), bool(item.get("validated", False)), lists)

    def _migrate_v2_profile(self, item: dict) -> CoordinateProfile:
        return CoordinateProfile(item["id"], item["name"], item.get("platform", "Aplicação"), item.get("monitor", "Tela principal"), item.get("resolution", ""), item.get("scale", ""), item.get("coordinates", {"LARANJA": None, "CINZA": None}), item.get("updated_at", ""), bool(item.get("validated", False)), [])

    def _migrate_v1(self, payload: dict) -> None:
        old_coords = payload.get("coordinates", {})
        if not any(old_coords.get(key) for key in ("LARANJA", "CINZA")): return
        resolution, scale = self._screen_signature()
        imported = CoordinateProfile(str(uuid4()), "Perfil importado da V1", "Aplicação", "Tela principal", resolution, scale, {"LARANJA": old_coords.get("LARANJA"), "CINZA": old_coords.get("CINZA")}, datetime.now().isoformat(timespec="seconds"), False, [])
        self.profiles, self.active_profile_id = [imported], imported.id

    def _on_close(self) -> None:
        if self.running and not messagebox.askyesno("Execução ativa", "Existe uma execução ativa. Encerrar e fechar?"): return
        self.running, self.paused = False, False
        self._save_config(); self.root.after(100, self.root.destroy)


def main() -> None:
    root = tk.Tk(); PredixAIRoboListas(root); root.mainloop()


if __name__ == "__main__":
    main()
