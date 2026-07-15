#!/usr/bin/env python3
"""V2.3.2: preflight temporal e ciclo estruturado de sessão."""
from __future__ import annotations

from copy import deepcopy
from dataclasses import asdict
from datetime import datetime
from uuid import uuid4

import main as app_main
import bootstrap_v22
from execution_preflight import split_signals_by_time


_PREVIOUS_INIT = None
_PREVIOUS_START = None
_PREVIOUS_STOP = None
_PREVIOUS_SHOW_HISTORY = None


def _session_payload(self, started_at: datetime) -> dict:
    return {
        "id": str(uuid4()),
        "started_at": started_at.isoformat(timespec="seconds"),
        "finished_at": None,
        "profile_id": self.active_profile.id if self.active_profile else None,
        "profile_name": self.active_profile.name if self.active_profile else "",
        "list_id": self.active_list.id if self.active_list else None,
        "list_name": self.active_list.name if self.active_list else "",
        "list_date": self.active_list.date_str if self.active_list else "",
        "status": "EM_EXECUÇÃO",
        "events": [],
    }


def init_v232(self, root):
    _PREVIOUS_INIT(self, root)
    self.root.title("PredixAI Robô de Listas — V2.3.2")


def _validate_start(self) -> bool:
    if self.running or (self.execution_thread and self.execution_thread.is_alive()):
        app_main.messagebox.showwarning("Execução ativa", "Já existe uma execução em andamento.")
        return False
    if not self.active_list or not self.active_list.signals:
        app_main.messagebox.showwarning("Lista vazia", "Adicione pelo menos um sinal.")
        return False
    if not self.active_profile or self._profile_compatibility_text(self.active_profile) != "perfil pronto":
        app_main.messagebox.showwarning("Perfil inválido", "Selecione, calibre e teste um perfil compatível.")
        return False
    return True


def _record_expired_attempt(self, expired, now: datetime) -> None:
    session = _session_payload(self, now)
    session["finished_at"] = now.isoformat(timespec="seconds")
    session["status"] = "EXPIRADA"
    session["events"] = [
        {
            "at": now.isoformat(timespec="seconds"),
            "status": "EXPIRADO",
            "detail": f"{signal.date_str} {signal.time_str} — {signal.direction} — EXPIRADO antes do início",
        }
        for signal in expired
    ]
    self.session_history.append(session)
    self.current_session = None
    self._save_config()


def start_execution(self) -> None:
    if not _validate_start(self):
        return

    now = datetime.now()
    expired, future = split_signals_by_time(self.active_list.signals, now)
    if not future:
        self.session_signals = [app_main.Signal(**asdict(item)) for item in deepcopy(self.active_list.signals)]
        for signal in self.session_signals:
            signal.status = "EXPIRADO"
        self.running = False
        self.paused = False
        self.status_var.set("LISTA EXPIRADA")
        self._update_summary()
        self.next_var.set("Nenhum sinal futuro — atualize ou duplique a lista")
        _record_expired_attempt(self, expired, now)
        self.show_execution()
        if hasattr(self, "_refresh_execution_controls"):
            self._refresh_execution_controls()
        app_main.messagebox.showwarning(
            "Lista expirada",
            "Todos os horários desta lista já passaram.\n\n"
            "A sessão não foi iniciada. Atualize os horários ou duplique a lista para outra data.",
        )
        return

    # Abre a sessão antes de iniciar a thread, evitando perda dos primeiros eventos.
    self.current_session = _session_payload(self, now)
    _PREVIOUS_START(self)

    # Registra sinais que já estavam vencidos, quando a lista também possui sinais futuros.
    if self.current_session is not None:
        known = {event.get("detail") for event in self.current_session.get("events", [])}
        for signal in self.session_signals:
            if signal.status != "EXPIRADO":
                continue
            detail = f"{signal.date_str} {signal.time_str} — {signal.direction} — EXPIRADO antes do início"
            if detail not in known:
                self.current_session["events"].append(
                    {"at": now.isoformat(timespec="seconds"), "status": "EXPIRADO", "detail": detail}
                )
        self._save_config()

    # Uma mudança de relógio entre o preflight e o início pode tornar tudo expirado.
    if not self.running and self.current_session is not None:
        bootstrap_v22.close_current_session(self, "EXPIRADA")


def stop_execution(self) -> None:
    was_running = self.running
    _PREVIOUS_STOP(self)
    if was_running and not self.running and self.current_session is not None:
        bootstrap_v22.close_current_session(self, "CANCELADO")


def _walk(widget):
    yield widget
    for child in widget.winfo_children():
        yield from _walk(child)


def show_history(self) -> None:
    _PREVIOUS_SHOW_HISTORY(self)
    for widget in _walk(self.content):
        if isinstance(widget, app_main.ttk.Combobox):
            values = list(widget.cget("values"))
            if "TODOS" in values and "EXPIRADA" not in values:
                widget.configure(values=[*values, "EXPIRADA"])
                break


def install_patch() -> None:
    global _PREVIOUS_INIT, _PREVIOUS_START, _PREVIOUS_STOP, _PREVIOUS_SHOW_HISTORY
    cls = app_main.PredixAIRoboListas
    _PREVIOUS_INIT = cls.__init__
    _PREVIOUS_START = cls._start_execution
    _PREVIOUS_STOP = cls._stop_execution
    _PREVIOUS_SHOW_HISTORY = cls.show_history
    cls.__init__ = init_v232
    cls._start_execution = start_execution
    cls._stop_execution = stop_execution
    cls.show_history = show_history
