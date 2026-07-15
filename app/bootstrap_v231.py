#!/usr/bin/env python3
"""V2.3.1: controle determinístico de pausa, retomada e cancelamento."""
from __future__ import annotations

import threading
import time
from datetime import datetime

import main as app_main


ORIGINAL_INIT = app_main.PredixAIRoboListas.__init__
ORIGINAL_START = app_main.PredixAIRoboListas._start_execution


def init_v231(self, root):
    ORIGINAL_INIT(self, root)
    self.root.title("PredixAI Robô de Listas — V2.3.1")
    self.execution_stop_event = threading.Event()
    self.execution_pause_event = threading.Event()
    self.pause_button = None
    self.cancel_button = None


def start_execution(self) -> None:
    if getattr(self, "execution_thread", None) and self.execution_thread.is_alive():
        app_main.messagebox.showwarning("Execução ativa", "Já existe uma execução em andamento.")
        return
    self.execution_stop_event.clear()
    self.execution_pause_event.clear()
    ORIGINAL_START(self)


def refresh_execution_controls(self) -> None:
    if getattr(self, "pause_button", None):
        self.pause_button.configure(text="Retomar" if self.paused else "Pausar")
        self.pause_button.state(["!disabled"] if self.running else ["disabled"])
    if getattr(self, "cancel_button", None):
        self.cancel_button.state(["!disabled"] if self.running else ["disabled"])


def show_execution(self) -> None:
    self._set_page("Execução")
    self._clear()
    panel = self._panel(
        "Execução",
        f"Perfil: {self.active_profile.name if self.active_profile else 'nenhum'} | "
        f"Lista: {self.active_list.name if self.active_list else 'nenhuma'}",
    )
    app_main.ttk.Label(panel, textvariable=self.status_var, style="Status.TLabel").pack(pady=6)
    app_main.ttk.Label(panel, textvariable=self.clock_var, style="Header.TLabel").pack()
    app_main.ttk.Label(panel, textvariable=self.next_var, style="Muted.TLabel").pack(pady=(6, 10))
    self.execution_list = app_main.ttk.Frame(panel, style="Panel.TFrame")
    self.execution_list.pack(fill="both", expand=True)
    self._render_execution_list()

    actions = app_main.ttk.Frame(panel, style="Panel.TFrame")
    actions.pack(fill="x", pady=(10, 0))
    self.pause_button = app_main.ttk.Button(
        actions,
        text="Retomar" if self.paused else "Pausar",
        command=self._toggle_pause,
        style="Secondary.TButton",
    )
    self.pause_button.pack(side="left")
    self.cancel_button = app_main.ttk.Button(
        actions,
        text="Cancelar execução",
        command=self._stop_execution,
        style="Danger.TButton",
    )
    self.cancel_button.pack(side="right")
    self._refresh_execution_controls()


def toggle_pause(self) -> None:
    if not self.running:
        return
    self.paused = not self.paused
    if self.paused:
        self.execution_pause_event.set()
        self.status_var.set("PAUSADO")
        self._append_history("Execução pausada.")
    else:
        self.execution_pause_event.clear()
        self.status_var.set("EM EXECUÇÃO")
        self._append_history("Execução retomada.")
    self._refresh_execution_controls()


def stop_execution(self) -> None:
    if not self.running:
        return
    if not app_main.messagebox.askyesno("Cancelar execução", "Cancelar a execução atual?"):
        return
    self.execution_stop_event.set()
    self.execution_pause_event.clear()
    self.running = False
    self.paused = False
    for signal in self.session_signals:
        if signal.status in {"AGENDADO", "EXECUTANDO"}:
            signal.status = "CANCELADO"
    self.status_var.set("CANCELADO")
    self._append_history("Execução cancelada manualmente.")
    self._update_summary()
    self._render_execution_list()
    self._refresh_execution_controls()


def execution_loop(self) -> None:
    try:
        while self.running and not self.execution_stop_event.is_set():
            if self.execution_pause_event.is_set():
                time.sleep(0.1)
                continue
            pending = [item for item in self.session_signals if item.status == "AGENDADO"]
            if not pending:
                self.running = False
                self.root.after(0, self._finish_execution)
                return
            current = min(pending, key=lambda item: item.scheduled_at)
            now = datetime.now()
            self.root.after(0, self._update_summary)
            if now >= current.scheduled_at:
                delay = (now - current.scheduled_at).total_seconds()
                if delay > 30:
                    current.status = "EXPIRADO"
                    self._append_history(
                        f"{current.id} — {current.date_str} {current.time_str} — EXPIRADO ({delay:.1f}s de atraso)"
                    )
                    self.root.after(0, self._render_execution_list)
                    self.root.after(0, self._update_summary)
                    continue
                current.status = "EXECUTANDO"
                self.root.after(0, self._render_execution_list)
                target = "LARANJA" if current.direction == "PARA_CIMA" else "CINZA"
                coord = self.coords[target]
                if coord is None:
                    raise RuntimeError(f"Coordenada {target} não configurada")
                self.mouse_controller.position = (coord["x"], coord["y"])
                for _ in range(7):
                    if self.execution_stop_event.is_set() or not self.running:
                        current.status = "CANCELADO"
                        self.root.after(0, self._render_execution_list)
                        return
                    if self.execution_pause_event.is_set():
                        current.status = "AGENDADO"
                        self.root.after(0, self._render_execution_list)
                        break
                    time.sleep(0.05)
                else:
                    self.mouse_controller.click(app_main.Button.left, 1)
                    current.status = "CLIQUE_ENVIADO"
                    self._append_history(
                        f"{self.active_profile.name if self.active_profile else 'perfil'} | "
                        f"{self.active_list.name if self.active_list else 'lista'} | {current.id} — "
                        f"{current.date_str} {current.time_str} — {current.direction} — "
                        f"CLIQUE_ENVIADO X={coord['x']} Y={coord['y']}"
                    )
                    self.root.after(0, self._render_execution_list)
                    self.root.after(0, self._update_summary)
            time.sleep(0.05)
    except Exception as exc:
        self.running = False
        for signal in self.session_signals:
            if signal.status == "EXECUTANDO":
                signal.status = "ERRO"
        self._append_history(f"ERRO — {exc}")
        self.root.after(0, self._handle_execution_error, str(exc))


def install_patch() -> None:
    cls = app_main.PredixAIRoboListas
    cls.__init__ = init_v231
    cls._start_execution = start_execution
    cls.show_execution = show_execution
    cls._toggle_pause = toggle_pause
    cls._stop_execution = stop_execution
    cls._execution_loop = execution_loop
    cls._refresh_execution_controls = refresh_execution_controls
