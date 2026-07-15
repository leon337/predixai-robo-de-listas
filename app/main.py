#!/usr/bin/env python3
from __future__ import annotations

import json
import threading
import time
import tkinter as tk
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from tkinter import messagebox, simpledialog, ttk
from uuid import uuid4

from pynput import mouse
from pynput.mouse import Button, Controller

ROOT_DIR = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT_DIR / "config"
CONFIG_PATH = CONFIG_DIR / "config_predixai_robo_listas.json"
MAX_SIGNALS = 5
PLATFORMS = ("Olymp Trade", "IQ Option", "Outro")


@dataclass
class Signal:
    time_str: str
    direction: str
    status: str = "PENDENTE"


@dataclass
class CoordinateProfile:
    id: str
    name: str
    platform: str
    monitor: str
    resolution: str
    scale: str
    coordinates: dict[str, dict[str, int] | None]
    updated_at: str
    validated: bool = False


class PredixAIRoboListas:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("PredixAI Robô de Listas — V2")
        self.root.geometry("620x620")
        self.root.minsize(560, 520)
        self.root.attributes("-topmost", True)

        self.colors = {
            "bg": "#07111f", "panel": "#0d1b2a", "panel2": "#12263a",
            "text": "#f7fbff", "muted": "#9db0c4", "green": "#70ff00",
            "orange": "#ff8a00", "gray": "#7f8c98", "red": "#ff4d5a",
        }
        self.root.configure(bg=self.colors["bg"])
        self.mouse_controller = Controller()
        self.profiles: list[CoordinateProfile] = []
        self.active_profile_id: str | None = None
        self.signals: list[Signal] = []
        self.running = False
        self.paused = False
        self.capture_listener: mouse.Listener | None = None
        self.pending_capture: str | None = None
        self.history: list[str] = []

        self.clock_var = tk.StringVar(value="--:--:--")
        self.status_var = tk.StringVar(value="PRONTO")
        self.next_var = tk.StringVar(value="Nenhum sinal pendente")
        self.counter_var = tk.StringVar(value="0 / 5 sinais")
        self.profile_var = tk.StringVar(value="")

        self._configure_style()
        self._load_config()
        self._build_shell()
        self.show_home()
        self._tick_clock()

    @property
    def active_profile(self) -> CoordinateProfile | None:
        return next((p for p in self.profiles if p.id == self.active_profile_id), None)

    @property
    def coords(self) -> dict[str, dict[str, int] | None]:
        profile = self.active_profile
        return profile.coordinates if profile else {"LARANJA": None, "CINZA": None}

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
        for name, bg in [("App.TFrame", self.colors["bg"]), ("Panel.TFrame", self.colors["panel"]), ("Panel2.TFrame", self.colors["panel2"])]:
            style.configure(name, background=bg)
        style.configure("Title.TLabel", background=self.colors["bg"], foreground=self.colors["text"], font=("Arial", 19, "bold"))
        style.configure("Subtitle.TLabel", background=self.colors["bg"], foreground=self.colors["muted"], font=("Arial", 9))
        style.configure("Header.TLabel", background=self.colors["panel"], foreground=self.colors["text"], font=("Arial", 13, "bold"))
        style.configure("Body.TLabel", background=self.colors["panel2"], foreground=self.colors["text"], font=("Arial", 10))
        style.configure("Muted.TLabel", background=self.colors["panel"], foreground=self.colors["muted"], font=("Arial", 9))
        style.configure("Status.TLabel", background=self.colors["panel"], foreground=self.colors["green"], font=("Arial", 12, "bold"))
        for name, bg, fg in [
            ("Primary.TButton", self.colors["green"], "#07111f"),
            ("Secondary.TButton", "#1c3550", self.colors["text"]),
            ("Danger.TButton", self.colors["red"], "white"),
            ("Orange.TButton", self.colors["orange"], "white"),
            ("Gray.TButton", self.colors["gray"], "white"),
        ]:
            style.configure(name, background=bg, foreground=fg, borderwidth=0, padding=8, font=("Arial", 9, "bold"))
        style.configure("TEntry", fieldbackground="#091625", foreground=self.colors["text"], padding=7)
        style.configure("TCombobox", fieldbackground="#091625", foreground=self.colors["text"], padding=6)
        style.configure("TSpinbox", fieldbackground="#091625", foreground=self.colors["text"], padding=6)

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
        ttk.Label(brand, text="Perfis de plataforma e agenda controlada", style="Subtitle.TLabel").pack(anchor="w")
        right = ttk.Frame(header, style="App.TFrame")
        right.pack(side="right")
        ttk.Label(right, textvariable=self.clock_var, style="Title.TLabel").pack(anchor="e")
        ttk.Label(right, textvariable=self.status_var, style="Subtitle.TLabel").pack(anchor="e")

        nav = ttk.Frame(self.shell, style="App.TFrame")
        nav.pack(fill="x", pady=(12, 10))
        for label, command in [("Início", self.show_home), ("Perfis", self.show_profiles), ("Agenda", self.show_schedule), ("Execução", self.show_execution), ("Histórico", self.show_history)]:
            ttk.Button(nav, text=label, command=command, style="Secondary.TButton").pack(side="left", padx=(0, 5))
        self.content = ttk.Frame(self.shell, style="App.TFrame")
        self.content.pack(fill="both", expand=True)

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
        self._clear()
        panel = self._panel("Nova sessão", "Escolha o perfil de coordenadas antes de montar a agenda.")
        ttk.Label(panel, textvariable=self.status_var, style="Status.TLabel").pack(anchor="w", pady=(0, 10))
        names = [p.name for p in self.profiles]
        combo = ttk.Combobox(panel, textvariable=self.profile_var, values=names, state="readonly")
        combo.pack(fill="x", pady=5)
        combo.bind("<<ComboboxSelected>>", lambda _event: self._select_profile_by_name())
        if self.active_profile and not self.profile_var.get():
            self.profile_var.set(self.active_profile.name)

        profile = self.active_profile
        resolution, scale = self._screen_signature()
        details = [
            f"Perfil: {profile.name if profile else 'nenhum selecionado'}",
            f"Plataforma: {profile.platform if profile else '—'}",
            f"Tela atual: {resolution} | escala {scale}",
            f"Compatibilidade: {self._profile_compatibility_text(profile)}",
            self.counter_var.get(),
        ]
        for text in details:
            card = ttk.Frame(panel, style="Panel2.TFrame", padding=10)
            card.pack(fill="x", pady=4)
            ttk.Label(card, text=text, style="Body.TLabel").pack(anchor="w")
        actions = ttk.Frame(panel, style="Panel.TFrame")
        actions.pack(fill="x", pady=(14, 0))
        ttk.Button(actions, text="Gerenciar perfis", command=self.show_profiles, style="Secondary.TButton").pack(side="left", padx=(0, 7))
        ttk.Button(actions, text="Iniciar nova sessão", command=self._new_session, style="Primary.TButton").pack(side="left")

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
        profile = next((p for p in self.profiles if p.name == self.profile_var.get()), None)
        self.active_profile_id = profile.id if profile else None
        self._save_config()
        self.show_home()

    def _new_session(self) -> None:
        if not self.active_profile:
            messagebox.showwarning("Perfil obrigatório", "Selecione ou crie um perfil de coordenadas.")
            return
        if self._profile_compatibility_text(self.active_profile) != "perfil pronto":
            messagebox.showwarning("Perfil incompatível", "Recalibre e teste o perfil para esta tela antes de executar.")
            self.show_profiles()
            return
        self.signals = []
        self.running = False
        self.paused = False
        self.status_var.set("SESSÃO NOVA")
        self._update_summary()
        self._save_config()
        self.show_schedule()

    def show_profiles(self) -> None:
        self._clear()
        panel = self._panel("Perfis de coordenadas", "Salve uma calibração para cada plataforma e ambiente de tela.")
        toolbar = ttk.Frame(panel, style="Panel.TFrame")
        toolbar.pack(fill="x", pady=(0, 10))
        ttk.Button(toolbar, text="Novo perfil", command=self._create_profile, style="Primary.TButton").pack(side="left", padx=(0, 6))
        ttk.Button(toolbar, text="Editar nome", command=self._rename_profile, style="Secondary.TButton").pack(side="left", padx=(0, 6))
        ttk.Button(toolbar, text="Excluir", command=self._delete_profile, style="Danger.TButton").pack(side="left")
        if not self.profiles:
            ttk.Label(panel, text="Nenhum perfil criado.", style="Muted.TLabel").pack(anchor="w", pady=15)
            return
        for profile in self.profiles:
            selected = profile.id == self.active_profile_id
            row = ttk.Frame(panel, style="Panel2.TFrame", padding=11)
            row.pack(fill="x", pady=4)
            text = f"{'● ' if selected else ''}{profile.name}\n{profile.platform} | {profile.monitor} | {profile.resolution} | {profile.scale}\n{self._profile_compatibility_text(profile)}"
            ttk.Label(row, text=text, style="Body.TLabel").pack(side="left", fill="x", expand=True)
            ttk.Button(row, text="Selecionar", command=lambda item=profile: self._activate_profile(item), style="Secondary.TButton").pack(side="right", padx=(5, 0))
            ttk.Button(row, text="Calibrar", command=lambda item=profile: self._open_profile_calibration(item), style="Orange.TButton").pack(side="right")

    def _create_profile(self) -> None:
        dialog = tk.Toplevel(self.root)
        dialog.title("Novo perfil")
        dialog.geometry("420x330")
        dialog.transient(self.root)
        dialog.grab_set()
        frame = ttk.Frame(dialog, padding=16)
        frame.pack(fill="both", expand=True)
        name_var = tk.StringVar(value="")
        platform_var = tk.StringVar(value=PLATFORMS[0])
        monitor_var = tk.StringVar(value="Tela principal")
        for label, widget in [
            ("Nome do perfil", ttk.Entry(frame, textvariable=name_var)),
            ("Plataforma", ttk.Combobox(frame, textvariable=platform_var, values=PLATFORMS, state="readonly")),
            ("Monitor/ambiente", ttk.Entry(frame, textvariable=monitor_var)),
        ]:
            ttk.Label(frame, text=label).pack(anchor="w", pady=(5, 2))
            widget.pack(fill="x")
        resolution, scale = self._screen_signature()
        ttk.Label(frame, text=f"Tela detectada: {resolution} | {scale}").pack(anchor="w", pady=10)

        def save() -> None:
            name = name_var.get().strip()
            if not name:
                messagebox.showerror("Nome obrigatório", "Informe um nome para o perfil.", parent=dialog)
                return
            if any(p.name.casefold() == name.casefold() for p in self.profiles):
                messagebox.showerror("Nome duplicado", "Já existe um perfil com esse nome.", parent=dialog)
                return
            profile = CoordinateProfile(str(uuid4()), name, platform_var.get(), monitor_var.get().strip() or "Tela principal", resolution, scale, {"LARANJA": None, "CINZA": None}, datetime.now().isoformat(timespec="seconds"), False)
            self.profiles.append(profile)
            self.active_profile_id = profile.id
            self.profile_var.set(profile.name)
            self._save_config()
            dialog.destroy()
            self._open_profile_calibration(profile)

        ttk.Button(frame, text="Criar e calibrar", command=save, style="Primary.TButton").pack(fill="x", pady=(15, 0))

    def _activate_profile(self, profile: CoordinateProfile) -> None:
        self.active_profile_id = profile.id
        self.profile_var.set(profile.name)
        self._save_config()
        self.show_profiles()

    def _rename_profile(self) -> None:
        profile = self.active_profile
        if not profile:
            messagebox.showwarning("Perfil", "Selecione um perfil primeiro.")
            return
        name = simpledialog.askstring("Editar perfil", "Novo nome:", initialvalue=profile.name, parent=self.root)
        if not name:
            return
        name = name.strip()
        if any(p.id != profile.id and p.name.casefold() == name.casefold() for p in self.profiles):
            messagebox.showerror("Nome duplicado", "Já existe um perfil com esse nome.")
            return
        profile.name = name
        profile.updated_at = datetime.now().isoformat(timespec="seconds")
        self.profile_var.set(name)
        self._save_config()
        self.show_profiles()

    def _delete_profile(self) -> None:
        profile = self.active_profile
        if not profile:
            messagebox.showwarning("Perfil", "Selecione um perfil primeiro.")
            return
        if not messagebox.askyesno("Excluir perfil", f"Excluir '{profile.name}'?"):
            return
        self.profiles = [p for p in self.profiles if p.id != profile.id]
        self.active_profile_id = self.profiles[0].id if self.profiles else None
        self.profile_var.set(self.active_profile.name if self.active_profile else "")
        self._save_config()
        self.show_profiles()

    def _open_profile_calibration(self, profile: CoordinateProfile) -> None:
        self._activate_profile(profile)
        self._clear()
        panel = self._panel(f"Calibrar: {profile.name}", "As novas coordenadas substituem as anteriores somente neste perfil.")
        current_resolution, current_scale = self._screen_signature()
        if profile.resolution != current_resolution or profile.scale != current_scale:
            profile.resolution, profile.scale, profile.validated = current_resolution, current_scale, False
        self.coord_vars: dict[str, tk.StringVar] = {}
        for key, label, style_name in [("LARANJA", "PARA CIMA / Laranja", "Orange.TButton"), ("CINZA", "PARA BAIXO / Cinza", "Gray.TButton")]:
            row = ttk.Frame(panel, style="Panel2.TFrame", padding=12)
            row.pack(fill="x", pady=5)
            left = ttk.Frame(row, style="Panel2.TFrame")
            left.pack(side="left", fill="x", expand=True)
            ttk.Label(left, text=label, style="Body.TLabel").pack(anchor="w")
            var = tk.StringVar(value=self._coord_text(key))
            self.coord_vars[key] = var
            ttk.Label(left, textvariable=var, style="Body.TLabel").pack(anchor="w", pady=(2, 0))
            ttk.Button(row, text="Recalibrar", command=lambda item=key: self._capture_coordinate(item), style=style_name).pack(side="right")
        ttk.Button(panel, text="Testar as duas coordenadas", command=self._test_both_coordinates, style="Secondary.TButton").pack(fill="x", pady=(14, 5))
        ttk.Button(panel, text="Salvar e usar perfil", command=self._confirm_profile, style="Primary.TButton").pack(fill="x", pady=5)

    def _capture_coordinate(self, key: str) -> None:
        if self.capture_listener is not None or not self.active_profile:
            return
        self.pending_capture = key
        self.status_var.set(f"CALIBRANDO {key}")
        self.root.iconify()

        def on_click(x: int, y: int, _button: object, pressed: bool) -> bool | None:
            if pressed:
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
        self.pending_capture = None

    def _coord_text(self, key: str) -> str:
        coord = self.coords.get(key)
        return "não configurado" if not coord else f"X={coord['x']} | Y={coord['y']}"

    def _test_both_coordinates(self) -> None:
        if not all(self.coords.values()):
            messagebox.showwarning("Calibração incompleta", "Calibre os dois pontos primeiro.")
            return
        if not messagebox.askyesno("Teste controlado", "O mouse fará um clique em cada coordenada. Continuar?"):
            return
        for key in ("LARANJA", "CINZA"):
            coord = self.coords[key]
            if coord:
                self.mouse_controller.position = (coord["x"], coord["y"])
                time.sleep(0.4)
                self.mouse_controller.click(Button.left, 1)
                time.sleep(0.5)
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
        self._save_config()
        self.show_home()

    def show_schedule(self) -> None:
        self._clear()
        panel = self._panel("Agenda de sinais", "A sessão começa vazia. Adicione até cinco sinais.")
        if not self.active_profile:
            ttk.Label(panel, text="Selecione um perfil antes de montar a agenda.", style="Muted.TLabel").pack(anchor="w")
            return
        form = ttk.Frame(panel, style="Panel2.TFrame", padding=12)
        form.pack(fill="x", pady=(0, 10))
        now = datetime.now()
        time_row = ttk.Frame(form, style="Panel2.TFrame")
        time_row.pack(fill="x", pady=(0, 7))
        self.hour_var = tk.StringVar(value=f"{now.hour:02d}")
        self.minute_var = tk.StringVar(value=f"{now.minute:02d}")
        self.second_var = tk.StringVar(value=f"{now.second:02d}")
        for var, limit, label in [(self.hour_var, 23, "Hora"), (self.minute_var, 59, "Min"), (self.second_var, 59, "Seg")]:
            box = ttk.Frame(time_row, style="Panel2.TFrame")
            box.pack(side="left", fill="x", expand=True, padx=(0, 5))
            ttk.Label(box, text=label, style="Body.TLabel").pack(anchor="w")
            ttk.Spinbox(box, from_=0, to=limit, width=4, textvariable=var, format="%02.0f", wrap=True, state="readonly").pack(fill="x")
        self.direction_var = tk.StringVar(value="PARA_CIMA")
        ttk.Combobox(form, textvariable=self.direction_var, values=["PARA_CIMA", "PARA_BAIXO"], state="readonly").pack(fill="x", pady=(0, 7))
        ttk.Button(form, text="Adicionar sinal", command=self._add_signal, style="Primary.TButton").pack(fill="x")
        self.signal_list = ttk.Frame(panel, style="Panel.TFrame")
        self.signal_list.pack(fill="both", expand=True)
        self._render_signal_list()
        footer = ttk.Frame(panel, style="Panel.TFrame")
        footer.pack(fill="x", pady=(10, 0))
        ttk.Label(footer, textvariable=self.counter_var, style="Muted.TLabel").pack(side="left")
        ttk.Button(footer, text="Limpar agenda", command=self._clear_schedule, style="Danger.TButton").pack(side="right", padx=(5, 0))
        ttk.Button(footer, text="Iniciar", command=self._start_execution, style="Primary.TButton").pack(side="right")

    def _add_signal(self) -> None:
        if len(self.signals) >= MAX_SIGNALS:
            messagebox.showwarning("Limite atingido", "O limite é de cinco sinais.")
            return
        try:
            hour, minute, second = int(self.hour_var.get()), int(self.minute_var.get()), int(self.second_var.get())
            time_str = f"{hour:02d}:{minute:02d}:{second:02d}"
            datetime.strptime(time_str, "%H:%M:%S")
        except (ValueError, AttributeError):
            messagebox.showerror("Horário inválido", "Revise hora, minuto e segundo.")
            return
        if any(item.time_str == time_str for item in self.signals):
            messagebox.showwarning("Horário duplicado", "Já existe um sinal nesse horário.")
            return
        self.signals.append(Signal(time_str, self.direction_var.get()))
        self.signals.sort(key=lambda item: item.time_str)
        self._update_summary(); self._render_signal_list()

    def _render_signal_list(self) -> None:
        if not hasattr(self, "signal_list"): return
        for child in self.signal_list.winfo_children(): child.destroy()
        if not self.signals:
            ttk.Label(self.signal_list, text="Nenhum sinal cadastrado.", style="Muted.TLabel").pack(anchor="w", pady=10)
            return
        for index, signal in enumerate(self.signals):
            row = ttk.Frame(self.signal_list, style="Panel2.TFrame", padding=9)
            row.pack(fill="x", pady=3)
            icon = "▲" if signal.direction == "PARA_CIMA" else "▼"
            ttk.Label(row, text=f"{index + 1}. {signal.time_str}  {icon} {signal.direction}", style="Body.TLabel").pack(side="left")
            ttk.Button(row, text="Remover", command=lambda pos=index: self._remove_signal(pos), style="Danger.TButton").pack(side="right")

    def _remove_signal(self, index: int) -> None:
        if 0 <= index < len(self.signals):
            self.signals.pop(index); self._update_summary(); self._render_signal_list()

    def _clear_schedule(self) -> None:
        if self.signals and not messagebox.askyesno("Limpar agenda", "Remover todos os sinais desta sessão?"): return
        self.signals = []; self._update_summary(); self._render_signal_list()

    def _update_summary(self) -> None:
        self.counter_var.set(f"{len(self.signals)} / {MAX_SIGNALS} sinais")
        pending = next((item for item in self.signals if item.status == "PENDENTE"), None)
        self.next_var.set(f"Próximo: {pending.time_str} — {pending.direction}" if pending else "Nenhum sinal pendente")

    def _start_execution(self) -> None:
        profile = self.active_profile
        if not self.signals:
            messagebox.showwarning("Agenda vazia", "Adicione pelo menos um sinal."); return
        if not profile or self._profile_compatibility_text(profile) != "perfil pronto":
            messagebox.showwarning("Perfil inválido", "Selecione, calibre e teste um perfil compatível."); return
        for signal in self.signals: signal.status = "PENDENTE"
        self.running = True; self.paused = False; self.status_var.set("EM EXECUÇÃO")
        self.show_execution()
        threading.Thread(target=self._execution_loop, daemon=True).start()

    def show_execution(self) -> None:
        self._clear()
        panel = self._panel("Execução", f"Perfil: {self.active_profile.name if self.active_profile else 'nenhum'}")
        ttk.Label(panel, textvariable=self.status_var, style="Status.TLabel").pack(pady=6)
        ttk.Label(panel, textvariable=self.clock_var, style="Header.TLabel").pack()
        ttk.Label(panel, textvariable=self.next_var, style="Muted.TLabel").pack(pady=(6, 10))
        self.execution_list = ttk.Frame(panel, style="Panel.TFrame")
        self.execution_list.pack(fill="both", expand=True)
        self._render_execution_list()
        actions = ttk.Frame(panel, style="Panel.TFrame")
        actions.pack(fill="x", pady=(10, 0))
        ttk.Button(actions, text="Pausar/Retomar", command=self._toggle_pause, style="Secondary.TButton").pack(side="left")
        ttk.Button(actions, text="Encerrar", command=self._stop_execution, style="Danger.TButton").pack(side="right")

    def _render_execution_list(self) -> None:
        if not hasattr(self, "execution_list"): return
        for child in self.execution_list.winfo_children(): child.destroy()
        icons = {"PENDENTE": "…", "EXECUTANDO": "▶", "CONCLUÍDO": "✓", "ERRO": "!"}
        for signal in self.signals:
            row = ttk.Frame(self.execution_list, style="Panel2.TFrame", padding=9); row.pack(fill="x", pady=3)
            ttk.Label(row, text=f"{icons.get(signal.status, '•')} {signal.time_str} — {signal.direction} — {signal.status}", style="Body.TLabel").pack(anchor="w")

    def _execution_loop(self) -> None:
        try:
            while self.running:
                if self.paused: time.sleep(0.2); continue
                pending = [item for item in self.signals if item.status == "PENDENTE"]
                if not pending:
                    self.running = False; self.root.after(0, self._finish_execution); return
                current = pending[0]
                self.root.after(0, self._update_summary)
                if datetime.now().strftime("%H:%M:%S") == current.time_str:
                    current.status = "EXECUTANDO"; self.root.after(0, self._render_execution_list)
                    target = "LARANJA" if current.direction == "PARA_CIMA" else "CINZA"
                    coord = self.coords[target]
                    if coord is None: raise RuntimeError(f"Coordenada {target} não configurada")
                    self.mouse_controller.position = (coord["x"], coord["y"]); time.sleep(0.35); self.mouse_controller.click(Button.left, 1)
                    current.status = "CONCLUÍDO"
                    self._append_history(f"{self.active_profile.name if self.active_profile else 'perfil'} — {current.time_str} — {current.direction} — X={coord['x']} Y={coord['y']}")
                    self.root.after(0, self._render_execution_list); self.root.after(0, self._update_summary)
                time.sleep(0.08)
        except Exception as exc:
            self.running = False; self.status_var.set("ERRO"); self._append_history(f"ERRO — {exc}")
            self.root.after(0, lambda: messagebox.showerror("Erro na execução", str(exc)))

    def _toggle_pause(self) -> None:
        if self.running:
            self.paused = not self.paused; self.status_var.set("PAUSADO" if self.paused else "EM EXECUÇÃO")

    def _stop_execution(self) -> None:
        self.running = False; self.paused = False; self.status_var.set("ENCERRADO"); self._append_history("Execução encerrada manualmente.")

    def _finish_execution(self) -> None:
        self.status_var.set("FINALIZADO"); self._update_summary(); self._render_execution_list(); self._append_history("Agenda finalizada.")
        messagebox.showinfo("PredixAI Robô de Listas", "Todas as execuções foram concluídas.")

    def show_history(self) -> None:
        self._clear()
        panel = self._panel("Histórico", "Registro das execuções desta abertura do aplicativo.")
        field = tk.Text(panel, bg="#091625", fg=self.colors["text"], insertbackground=self.colors["text"], relief="flat", wrap="word", font=("Courier New", 9))
        field.pack(fill="both", expand=True)
        field.insert("1.0", "\n".join(self.history) if self.history else "Nenhuma execução registrada.")
        field.configure(state="disabled")

    def _append_history(self, line: str) -> None:
        self.history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — {line}")

    def _tick_clock(self) -> None:
        self.clock_var.set(datetime.now().strftime("%H:%M:%S")); self.root.after(250, self._tick_clock)

    def _save_config(self) -> None:
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        payload = {"version": 2, "active_profile_id": self.active_profile_id, "profiles": [asdict(p) for p in self.profiles]}
        CONFIG_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def _load_config(self) -> None:
        if not CONFIG_PATH.exists():
            self._update_summary(); return
        try:
            payload = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
            if payload.get("version") == 2:
                self.profiles = [CoordinateProfile(**item) for item in payload.get("profiles", [])]
                self.active_profile_id = payload.get("active_profile_id")
            else:
                old_coords = payload.get("coordinates", {})
                if any(old_coords.get(key) for key in ("LARANJA", "CINZA")):
                    resolution, scale = self._screen_signature()
                    imported = CoordinateProfile(str(uuid4()), "Perfil importado da V1", "Outro", "Tela principal", resolution, scale, {"LARANJA": old_coords.get("LARANJA"), "CINZA": old_coords.get("CINZA")}, datetime.now().isoformat(timespec="seconds"), False)
                    self.profiles = [imported]; self.active_profile_id = imported.id
            if self.active_profile:
                self.profile_var.set(self.active_profile.name)
        except (OSError, ValueError, TypeError, KeyError):
            self.profiles = []; self.active_profile_id = None
        self.signals = []
        self._update_summary()


def main() -> None:
    root = tk.Tk()
    PredixAIRoboListas(root)
    root.mainloop()


if __name__ == "__main__":
    main()
