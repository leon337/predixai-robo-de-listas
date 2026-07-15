#!/usr/bin/env python3
from __future__ import annotations

import json
import threading
import time
import tkinter as tk
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from tkinter import messagebox, ttk

from pynput import mouse
from pynput.mouse import Button, Controller

ROOT_DIR = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT_DIR / "config"
CONFIG_PATH = CONFIG_DIR / "config_predixai_robo_listas.json"
MAX_SIGNALS = 5


@dataclass
class Signal:
    time_str: str
    direction: str
    status: str = "PENDENTE"


class PredixAIRoboListas:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("PredixAI Robô de Listas")
        self.root.geometry("760x720")
        self.root.minsize(720, 660)
        self.root.attributes("-topmost", True)

        self.colors = {
            "bg": "#07111f",
            "panel": "#0d1b2a",
            "panel2": "#12263a",
            "text": "#f7fbff",
            "muted": "#9db0c4",
            "green": "#70ff00",
            "orange": "#ff8a00",
            "gray": "#7f8c98",
            "red": "#ff4d5a",
        }
        self.root.configure(bg=self.colors["bg"])

        self.mouse_controller = Controller()
        self.coords: dict[str, dict[str, int] | None] = {
            "LARANJA": None,
            "CINZA": None,
        }
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

        self._configure_style()
        self._load_config()
        self._build_shell()
        self.show_home()
        self._tick_clock()

    def _configure_style(self) -> None:
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("App.TFrame", background=self.colors["bg"])
        style.configure("Panel.TFrame", background=self.colors["panel"])
        style.configure("Panel2.TFrame", background=self.colors["panel2"])
        style.configure(
            "Title.TLabel",
            background=self.colors["bg"],
            foreground=self.colors["text"],
            font=("Arial", 21, "bold"),
        )
        style.configure(
            "Subtitle.TLabel",
            background=self.colors["bg"],
            foreground=self.colors["muted"],
            font=("Arial", 10),
        )
        style.configure(
            "Header.TLabel",
            background=self.colors["panel"],
            foreground=self.colors["text"],
            font=("Arial", 14, "bold"),
        )
        style.configure(
            "Body.TLabel",
            background=self.colors["panel2"],
            foreground=self.colors["text"],
            font=("Arial", 10),
        )
        style.configure(
            "Muted.TLabel",
            background=self.colors["panel"],
            foreground=self.colors["muted"],
            font=("Arial", 9),
        )
        style.configure(
            "Status.TLabel",
            background=self.colors["panel"],
            foreground=self.colors["green"],
            font=("Arial", 13, "bold"),
        )
        for name, background, foreground in [
            ("Primary.TButton", self.colors["green"], "#07111f"),
            ("Secondary.TButton", "#1c3550", self.colors["text"]),
            ("Danger.TButton", self.colors["red"], "white"),
            ("Orange.TButton", self.colors["orange"], "white"),
            ("Gray.TButton", self.colors["gray"], "white"),
        ]:
            style.configure(
                name,
                background=background,
                foreground=foreground,
                borderwidth=0,
                padding=9,
                font=("Arial", 10, "bold"),
            )
        style.configure(
            "TEntry",
            fieldbackground="#091625",
            foreground=self.colors["text"],
            padding=8,
        )
        style.configure(
            "TCombobox",
            fieldbackground="#091625",
            foreground=self.colors["text"],
            padding=7,
        )

    def _build_shell(self) -> None:
        self.shell = ttk.Frame(self.root, style="App.TFrame", padding=18)
        self.shell.pack(fill="both", expand=True)

        header = ttk.Frame(self.shell, style="App.TFrame")
        header.pack(fill="x")

        mark = tk.Canvas(
            header,
            width=72,
            height=72,
            bg=self.colors["bg"],
            highlightthickness=0,
        )
        mark.pack(side="left")
        mark.create_oval(5, 5, 67, 67, outline=self.colors["green"], width=2)
        mark.create_text(36, 34, text="P", fill="white", font=("Arial", 31, "bold"))
        mark.create_text(37, 57, text="AI", fill=self.colors["green"], font=("Arial", 8, "bold"))

        brand = ttk.Frame(header, style="App.TFrame")
        brand.pack(side="left", padx=12)
        ttk.Label(brand, text="PredixAI Robô de Listas", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            brand,
            text="Automação local de agendas e cliques controlados",
            style="Subtitle.TLabel",
        ).pack(anchor="w")

        right = ttk.Frame(header, style="App.TFrame")
        right.pack(side="right")
        ttk.Label(right, textvariable=self.clock_var, style="Title.TLabel").pack(anchor="e")
        ttk.Label(right, textvariable=self.status_var, style="Subtitle.TLabel").pack(anchor="e")

        nav = ttk.Frame(self.shell, style="App.TFrame")
        nav.pack(fill="x", pady=(16, 12))
        for label, command in [
            ("Início", self.show_home),
            ("Coordenadas", self.show_calibration),
            ("Agenda", self.show_schedule),
            ("Execução", self.show_execution),
            ("Histórico", self.show_history),
        ]:
            ttk.Button(nav, text=label, command=command, style="Secondary.TButton").pack(
                side="left", padx=(0, 7)
            )

        self.content = ttk.Frame(self.shell, style="App.TFrame")
        self.content.pack(fill="both", expand=True)

    def _clear(self) -> None:
        for child in self.content.winfo_children():
            child.destroy()

    def _panel(self, title: str, subtitle: str) -> ttk.Frame:
        panel = ttk.Frame(self.content, style="Panel.TFrame", padding=18)
        panel.pack(fill="both", expand=True)
        ttk.Label(panel, text=title, style="Header.TLabel").pack(anchor="w")
        ttk.Label(panel, text=subtitle, style="Muted.TLabel").pack(anchor="w", pady=(4, 14))
        return panel

    def show_home(self) -> None:
        self._clear()
        panel = self._panel("Visão geral", "Estado atual da aplicação.")
        ttk.Label(panel, textvariable=self.status_var, style="Status.TLabel").pack(anchor="w", pady=8)

        for text in [
            f"Laranja: {self._coord_text('LARANJA')}",
            f"Cinza: {self._coord_text('CINZA')}",
            self.counter_var.get(),
            self.next_var.get(),
        ]:
            card = ttk.Frame(panel, style="Panel2.TFrame", padding=12)
            card.pack(fill="x", pady=5)
            ttk.Label(card, text=text, style="Body.TLabel").pack(anchor="w")

        actions = ttk.Frame(panel, style="Panel.TFrame")
        actions.pack(fill="x", pady=(18, 0))
        ttk.Button(
            actions,
            text="Calibrar coordenadas",
            command=self.show_calibration,
            style="Secondary.TButton",
        ).pack(side="left", padx=(0, 8))
        ttk.Button(
            actions,
            text="Montar agenda",
            command=self.show_schedule,
            style="Primary.TButton",
        ).pack(side="left")

    def show_calibration(self) -> None:
        self._clear()
        panel = self._panel(
            "Coordenadas",
            "Capture dois pontos globais. A janela permanece acima das demais.",
        )
        self.coord_vars: dict[str, tk.StringVar] = {}

        for key, label, style_name in [
            ("LARANJA", "Botão laranja", "Orange.TButton"),
            ("CINZA", "Botão cinza", "Gray.TButton"),
        ]:
            row = ttk.Frame(panel, style="Panel2.TFrame", padding=14)
            row.pack(fill="x", pady=7)
            left = ttk.Frame(row, style="Panel2.TFrame")
            left.pack(side="left", fill="x", expand=True)
            ttk.Label(left, text=label, style="Body.TLabel").pack(anchor="w")
            var = tk.StringVar(value=self._coord_text(key))
            self.coord_vars[key] = var
            ttk.Label(left, textvariable=var, style="Body.TLabel").pack(anchor="w", pady=(3, 0))
            ttk.Button(
                row,
                text="Calibrar",
                command=lambda item=key: self._capture_coordinate(item),
                style=style_name,
            ).pack(side="right")

        ttk.Button(
            panel,
            text="Testar coordenada laranja",
            command=lambda: self._test_coordinate("LARANJA"),
            style="Secondary.TButton",
        ).pack(fill="x", pady=(18, 7))
        ttk.Button(
            panel,
            text="Testar coordenada cinza",
            command=lambda: self._test_coordinate("CINZA"),
            style="Secondary.TButton",
        ).pack(fill="x", pady=7)

    def _capture_coordinate(self, key: str) -> None:
        if self.capture_listener is not None:
            return
        self.pending_capture = key
        self.status_var.set(f"CALIBRANDO {key}")
        self.root.iconify()

        def on_click(x: int, y: int, button: object, pressed: bool) -> bool | None:
            if pressed:
                self.coords[key] = {"x": int(x), "y": int(y)}
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
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()
        self.root.attributes("-topmost", True)
        self.status_var.set("PRONTO")
        self._save_config()
        for key, var in getattr(self, "coord_vars", {}).items():
            var.set(self._coord_text(key))
        self.pending_capture = None

    def _coord_text(self, key: str) -> str:
        coord = self.coords.get(key)
        if not coord:
            return "não configurado"
        return f"X={coord['x']} | Y={coord['y']}"

    def _test_coordinate(self, key: str) -> None:
        coord = self.coords.get(key)
        if not coord:
            messagebox.showwarning("Coordenada ausente", f"Calibre {key.lower()} primeiro.")
            return
        self.mouse_controller.position = (coord["x"], coord["y"])
        time.sleep(0.35)
        self.mouse_controller.click(Button.left, 1)

    def show_schedule(self) -> None:
        self._clear()
        panel = self._panel("Agenda de sinais", "Adicione um sinal por vez. Limite máximo de cinco.")

        form = ttk.Frame(panel, style="Panel2.TFrame", padding=14)
        form.pack(fill="x", pady=(0, 12))
        self.time_entry = ttk.Entry(form)
        self.time_entry.insert(0, datetime.now().strftime("%H:%M:%S"))
        self.time_entry.pack(fill="x", pady=(0, 8))
        self.direction_var = tk.StringVar(value="PARA_CIMA")
        ttk.Combobox(
            form,
            textvariable=self.direction_var,
            values=["PARA_CIMA", "PARA_BAIXO"],
            state="readonly",
        ).pack(fill="x", pady=(0, 8))
        ttk.Button(
            form,
            text="Adicionar sinal",
            command=self._add_signal,
            style="Primary.TButton",
        ).pack(fill="x")

        self.signal_list = ttk.Frame(panel, style="Panel.TFrame")
        self.signal_list.pack(fill="both", expand=True)
        self._render_signal_list()

        footer = ttk.Frame(panel, style="Panel.TFrame")
        footer.pack(fill="x", pady=(12, 0))
        ttk.Label(footer, textvariable=self.counter_var, style="Muted.TLabel").pack(side="left")
        ttk.Button(
            footer,
            text="Iniciar execuções",
            command=self._start_execution,
            style="Primary.TButton",
        ).pack(side="right")

    def _add_signal(self) -> None:
        if len(self.signals) >= MAX_SIGNALS:
            messagebox.showwarning("Limite atingido", "O limite é de cinco sinais.")
            return
        time_str = self.time_entry.get().strip()
        try:
            datetime.strptime(time_str, "%H:%M:%S")
        except ValueError:
            messagebox.showerror("Horário inválido", "Use o formato HH:MM:SS.")
            return
        if any(item.time_str == time_str for item in self.signals):
            messagebox.showwarning("Horário duplicado", "Já existe um sinal nesse horário.")
            return
        self.signals.append(Signal(time_str, self.direction_var.get()))
        self.signals.sort(key=lambda item: item.time_str)
        self._save_config()
        self._update_summary()
        self._render_signal_list()

    def _render_signal_list(self) -> None:
        if not hasattr(self, "signal_list"):
            return
        for child in self.signal_list.winfo_children():
            child.destroy()
        if not self.signals:
            ttk.Label(self.signal_list, text="Nenhum sinal cadastrado.", style="Muted.TLabel").pack(anchor="w", pady=12)
            return
        for index, signal in enumerate(self.signals):
            row = ttk.Frame(self.signal_list, style="Panel2.TFrame", padding=11)
            row.pack(fill="x", pady=4)
            icon = "▲" if signal.direction == "PARA_CIMA" else "▼"
            ttk.Label(
                row,
                text=f"{index + 1}. {signal.time_str}   {icon} {signal.direction}",
                style="Body.TLabel",
            ).pack(side="left")
            ttk.Button(
                row,
                text="Remover",
                command=lambda pos=index: self._remove_signal(pos),
                style="Danger.TButton",
            ).pack(side="right")

    def _remove_signal(self, index: int) -> None:
        if 0 <= index < len(self.signals):
            self.signals.pop(index)
            self._save_config()
            self._update_summary()
            self._render_signal_list()

    def _update_summary(self) -> None:
        self.counter_var.set(f"{len(self.signals)} / {MAX_SIGNALS} sinais")
        pending = next((item for item in self.signals if item.status == "PENDENTE"), None)
        self.next_var.set(
            f"Próximo: {pending.time_str} — {pending.direction}"
            if pending
            else "Nenhum sinal pendente"
        )

    def _start_execution(self) -> None:
        if not self.signals:
            messagebox.showwarning("Agenda vazia", "Adicione pelo menos um sinal.")
            return
        if not all(self.coords.values()):
            messagebox.showwarning("Calibração pendente", "Calibre os dois pontos primeiro.")
            return
        for signal in self.signals:
            signal.status = "PENDENTE"
        self.running = True
        self.paused = False
        self.status_var.set("EM EXECUÇÃO")
        self.show_execution()
        threading.Thread(target=self._execution_loop, daemon=True).start()

    def show_execution(self) -> None:
        self._clear()
        panel = self._panel("Execução", "Acompanhe a agenda e o próximo sinal.")
        ttk.Label(panel, textvariable=self.status_var, style="Status.TLabel").pack(pady=8)
        ttk.Label(panel, textvariable=self.clock_var, style="Header.TLabel").pack()
        ttk.Label(panel, textvariable=self.next_var, style="Muted.TLabel").pack(pady=(8, 14))
        self.execution_list = ttk.Frame(panel, style="Panel.TFrame")
        self.execution_list.pack(fill="both", expand=True)
        self._render_execution_list()
        actions = ttk.Frame(panel, style="Panel.TFrame")
        actions.pack(fill="x", pady=(12, 0))
        ttk.Button(
            actions,
            text="Pausar/Retomar",
            command=self._toggle_pause,
            style="Secondary.TButton",
        ).pack(side="left")
        ttk.Button(
            actions,
            text="Encerrar",
            command=self._stop_execution,
            style="Danger.TButton",
        ).pack(side="right")

    def _render_execution_list(self) -> None:
        if not hasattr(self, "execution_list"):
            return
        for child in self.execution_list.winfo_children():
            child.destroy()
        icons = {"PENDENTE": "…", "EXECUTANDO": "▶", "CONCLUÍDO": "✓", "ERRO": "!"}
        for signal in self.signals:
            row = ttk.Frame(self.execution_list, style="Panel2.TFrame", padding=10)
            row.pack(fill="x", pady=4)
            ttk.Label(
                row,
                text=f"{icons.get(signal.status, '•')} {signal.time_str} — {signal.direction} — {signal.status}",
                style="Body.TLabel",
            ).pack(anchor="w")

    def _execution_loop(self) -> None:
        try:
            while self.running:
                if self.paused:
                    time.sleep(0.2)
                    continue
                pending = [item for item in self.signals if item.status == "PENDENTE"]
                if not pending:
                    self.running = False
                    self.root.after(0, self._finish_execution)
                    return
                current = pending[0]
                self.root.after(0, self._update_summary)
                if datetime.now().strftime("%H:%M:%S") == current.time_str:
                    current.status = "EXECUTANDO"
                    self.root.after(0, self._render_execution_list)
                    target = "LARANJA" if current.direction == "PARA_CIMA" else "CINZA"
                    coord = self.coords[target]
                    if coord is None:
                        raise RuntimeError(f"Coordenada {target} não configurada")
                    self.mouse_controller.position = (coord["x"], coord["y"])
                    time.sleep(0.35)
                    self.mouse_controller.click(Button.left, 1)
                    current.status = "CONCLUÍDO"
                    self._append_history(
                        f"{current.time_str} — {current.direction} — {target} — X={coord['x']} Y={coord['y']}"
                    )
                    self._save_config()
                    self.root.after(0, self._render_execution_list)
                    self.root.after(0, self._update_summary)
                time.sleep(0.08)
        except Exception as exc:
            self.running = False
            self.status_var.set("ERRO")
            self._append_history(f"ERRO — {exc}")
            self.root.after(0, lambda: messagebox.showerror("Erro na execução", str(exc)))

    def _toggle_pause(self) -> None:
        if not self.running:
            return
        self.paused = not self.paused
        self.status_var.set("PAUSADO" if self.paused else "EM EXECUÇÃO")

    def _stop_execution(self) -> None:
        self.running = False
        self.paused = False
        self.status_var.set("ENCERRADO")
        self._append_history("Execução encerrada manualmente.")

    def _finish_execution(self) -> None:
        self.status_var.set("FINALIZADO")
        self._update_summary()
        self._render_execution_list()
        self._append_history("Agenda finalizada.")
        messagebox.showinfo("PredixAI Robô de Listas", "Todas as execuções foram concluídas.")

    def show_history(self) -> None:
        self._clear()
        panel = self._panel("Histórico", "Registro local das execuções desta sessão.")
        field = tk.Text(
            panel,
            bg="#091625",
            fg=self.colors["text"],
            insertbackground=self.colors["text"],
            relief="flat",
            wrap="word",
            font=("Courier New", 10),
        )
        field.pack(fill="both", expand=True)
        field.insert("1.0", "\n".join(self.history) if self.history else "Nenhuma execução registrada.")
        field.configure(state="disabled")

    def _append_history(self, line: str) -> None:
        self.history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — {line}")

    def _tick_clock(self) -> None:
        self.clock_var.set(datetime.now().strftime("%H:%M:%S"))
        self.root.after(250, self._tick_clock)

    def _save_config(self) -> None:
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        payload = {
            "coordinates": self.coords,
            "signals": [asdict(item) for item in self.signals],
        }
        CONFIG_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def _load_config(self) -> None:
        if not CONFIG_PATH.exists():
            self._update_summary()
            return
        try:
            payload = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
            for key in ("LARANJA", "CINZA"):
                value = payload.get("coordinates", {}).get(key)
                if isinstance(value, dict):
                    self.coords[key] = {"x": int(value["x"]), "y": int(value["y"])}
            self.signals = [
                Signal(str(item["time_str"]), str(item["direction"]), "PENDENTE")
                for item in payload.get("signals", [])[:MAX_SIGNALS]
            ]
        except (OSError, ValueError, TypeError, KeyError):
            self.coords = {"LARANJA": None, "CINZA": None}
            self.signals = []
        self._update_summary()


def main() -> None:
    root = tk.Tk()
    PredixAIRoboListas(root)
    root.mainloop()


if __name__ == "__main__":
    main()
