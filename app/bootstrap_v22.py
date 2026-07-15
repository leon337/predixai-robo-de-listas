#!/usr/bin/env python3
"""Bootstrap V2.2: listas independentes dos perfis e histórico estruturado."""
from __future__ import annotations

import csv
import json
from dataclasses import asdict
from datetime import date, datetime, timedelta
from pathlib import Path
from tkinter import filedialog
from uuid import uuid4

import main as app_main

ORIGINAL_LOAD = app_main.PredixAIRoboListas._load_config
ORIGINAL_START = app_main.PredixAIRoboListas._start_execution
ORIGINAL_FINISH = app_main.PredixAIRoboListas._finish_execution
ORIGINAL_STOP = app_main.PredixAIRoboListas._stop_execution
ORIGINAL_ERROR = app_main.PredixAIRoboListas._handle_execution_error


def list_label(app, schedule):
    return f"{schedule.name} — {app._format_date(schedule.date_str)}"


def list_status(schedule):
    target = datetime.strptime(schedule.date_str, "%Y-%m-%d").date()
    today = date.today()
    if getattr(schedule, "archived", False) or target < today:
        return "HISTÓRICO"
    if target == today:
        return "HOJE"
    if target == today + timedelta(days=1):
        return "AMANHÃ"
    return "FUTURA"


def build_choices(app):
    app.list_choice_to_id = {}
    choices = []
    for item in sorted(app.lists, key=lambda value: (value.date_str, value.name.casefold(), value.id)):
        if getattr(item, "archived", False):
            continue
        label = list_label(app, item)
        if label in app.list_choice_to_id:
            label = f"{label} · {item.id[:8]}"
        app.list_choice_to_id[label] = item.id
        choices.append(label)
    return choices


def active_label(app):
    if not app.active_list:
        return ""
    build_choices(app)
    return next((label for label, item_id in app.list_choice_to_id.items() if item_id == app.active_list.id), "")


def active_list(self):
    return next((item for item in getattr(self, "lists", []) if item.id == self.active_list_id), None)


def schedule_from_dict(data):
    schedule = app_main.ScheduleList(
        data["id"], data["name"], data["date_str"],
        [app_main.Signal(**signal) for signal in data.get("signals", [])],
        data.get("updated_at", ""),
    )
    schedule.description = str(data.get("description", ""))
    schedule.created_at = str(data.get("created_at", schedule.updated_at or datetime.now().isoformat(timespec="seconds")))
    schedule.archived = bool(data.get("archived", False))
    return schedule


def schedule_to_dict(schedule):
    return {
        "id": schedule.id,
        "name": schedule.name,
        "date_str": schedule.date_str,
        "description": getattr(schedule, "description", ""),
        "created_at": getattr(schedule, "created_at", ""),
        "updated_at": schedule.updated_at,
        "archived": bool(getattr(schedule, "archived", False)),
        "signals": [asdict(signal) for signal in schedule.signals],
    }


def load_config(self):
    self.lists = []
    self.session_history = []
    self.current_session = None
    if not app_main.CONFIG_PATH.exists():
        self._update_summary()
        return
    try:
        payload = json.loads(app_main.CONFIG_PATH.read_text(encoding="utf-8"))
        if payload.get("version") == 4:
            self.profiles = [self._profile_from_dict({**item, "lists": []}) for item in payload.get("profiles", [])]
            self.lists = [schedule_from_dict(item) for item in payload.get("lists", [])]
            self.active_profile_id = payload.get("active_profile_id")
            self.active_list_id = payload.get("active_list_id")
            self.history = [str(item) for item in payload.get("legacy_history", [])]
            self.session_history = list(payload.get("session_history", []))
        else:
            ORIGINAL_LOAD(self)
            seen = set()
            migrated = []
            for profile in self.profiles:
                for schedule in profile.lists:
                    if schedule.id not in seen:
                        schedule.description = ""
                        schedule.created_at = schedule.updated_at or datetime.now().isoformat(timespec="seconds")
                        schedule.archived = False
                        migrated.append(schedule)
                        seen.add(schedule.id)
                profile.lists = []
            self.lists = migrated
            if not self.active_list_id and self.lists:
                self.active_list_id = self.lists[0].id
        if self.active_profile:
            self.profile_var.set(self.active_profile.name)
        self.list_var.set(active_label(self))
    except (OSError, ValueError, TypeError, KeyError):
        self.profiles, self.lists, self.history, self.session_history = [], [], [], []
        self.active_profile_id = self.active_list_id = None
    self.session_signals = []
    self._update_summary()
    self._save_config()


def save_config(self):
    app_main.CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    profiles = []
    for profile in self.profiles:
        item = asdict(profile)
        item["lists"] = []
        profiles.append(item)
    payload = {
        "version": 4,
        "active_profile_id": self.active_profile_id,
        "active_list_id": self.active_list_id,
        "profiles": profiles,
        "lists": [schedule_to_dict(item) for item in self.lists],
        "legacy_history": self.history[-1000:],
        "session_history": self.session_history[-500:],
    }
    temp = app_main.CONFIG_PATH.with_suffix(".tmp")
    temp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    temp.replace(app_main.CONFIG_PATH)


def show_home(self):
    self._set_page("Início")
    self._clear()
    panel = self._panel("Nova sessão", "Combine um perfil de coordenadas com uma lista programada.")
    app_main.ttk.Label(panel, textvariable=self.status_var, style="Status.TLabel").pack(anchor="w", pady=(0, 10))
    profile_combo = app_main.ttk.Combobox(panel, textvariable=self.profile_var, values=[item.name for item in self.profiles], state="readonly")
    profile_combo.pack(fill="x", pady=4)
    profile_combo.bind("<<ComboboxSelected>>", lambda _event: self._select_profile_by_name())
    choices = build_choices(self)
    self.list_var.set(active_label(self))
    list_combo = app_main.ttk.Combobox(panel, textvariable=self.list_var, values=choices, state="readonly")
    list_combo.pack(fill="x", pady=4)
    list_combo.bind("<<ComboboxSelected>>", lambda _event: self._select_list_by_name())
    resolution, scale = self._screen_signature()
    for text in (
        f"Perfil: {self.active_profile.name if self.active_profile else 'nenhum selecionado'}",
        f"Aplicação: {self.active_profile.application if self.active_profile else '—'}",
        f"Lista: {list_label(self, self.active_list) if self.active_list else 'nenhuma selecionada'}",
        f"Status da lista: {list_status(self.active_list) if self.active_list else '—'}",
        f"Tela atual: {resolution} | escala {scale}",
        f"Compatibilidade: {self._profile_compatibility_text(self.active_profile)}",
    ):
        card = app_main.ttk.Frame(panel, style="Panel2.TFrame", padding=10)
        card.pack(fill="x", pady=3)
        app_main.ttk.Label(card, text=text, style="Body.TLabel").pack(anchor="w")
    actions = app_main.ttk.Frame(panel, style="Panel.TFrame")
    actions.pack(fill="x", pady=(14, 0))
    app_main.ttk.Button(actions, text="Gerenciar perfis", command=self.show_profiles, style="Secondary.TButton").pack(side="left", padx=(0, 6))
    app_main.ttk.Button(actions, text="Gerenciar listas", command=self.show_lists, style="Secondary.TButton").pack(side="left", padx=(0, 6))
    app_main.ttk.Button(actions, text="Preparar sessão", command=self._prepare_session, style="Primary.TButton").pack(side="left")


def select_profile(self):
    if self.running:
        app_main.messagebox.showwarning("Execução ativa", "Não é possível trocar o perfil durante uma execução.")
        return
    profile = next((item for item in self.profiles if item.name == self.profile_var.get()), None)
    self.active_profile_id = profile.id if profile else None
    self._save_config()
    self.show_home()


def select_list(self):
    if self.running:
        app_main.messagebox.showwarning("Execução ativa", "Não é possível trocar a lista durante uma execução.")
        self.list_var.set(active_label(self))
        return
    build_choices(self)
    self.active_list_id = self.list_choice_to_id.get(self.list_var.get())
    self._save_config()
    self.show_home()


def show_lists(self):
    self._set_page("Listas")
    self._clear()
    panel = self._panel("Listas programadas", "Listas independentes dos perfis, organizadas por data.")
    toolbar = app_main.ttk.Frame(panel, style="Panel.TFrame")
    toolbar.pack(fill="x", pady=(0, 10))
    for text, command, style in (
        ("Nova lista", lambda: self._list_dialog(), "Primary.TButton"),
        ("Editar", lambda: self._list_dialog(self.active_list) if self.active_list else app_main.messagebox.showwarning("Lista", "Selecione uma lista."), "Secondary.TButton"),
        ("Duplicar", lambda: self._list_dialog(self.active_list, True) if self.active_list else app_main.messagebox.showwarning("Lista", "Selecione uma lista."), "Secondary.TButton"),
        ("Arquivar", self._archive_list, "Secondary.TButton"),
        ("Excluir", self._delete_list, "Danger.TButton"),
    ):
        app_main.ttk.Button(toolbar, text=text, command=command, style=style).pack(side="left", padx=(0, 5))
    if not self.lists:
        app_main.ttk.Label(panel, text="Nenhuma lista criada.", style="Muted.TLabel").pack(anchor="w", pady=15)
        return
    groups = ("HOJE", "AMANHÃ", "FUTURA", "HISTÓRICO")
    for group in groups:
        items = [item for item in self.lists if list_status(item) == group]
        if not items:
            continue
        app_main.ttk.Label(panel, text=group, style="Status.TLabel").pack(anchor="w", pady=(10, 3))
        for schedule in sorted(items, key=lambda value: (value.date_str, value.name.casefold())):
            selected = schedule.id == self.active_list_id
            row = app_main.ttk.Frame(panel, style="Panel2.TFrame", padding=10)
            row.pack(fill="x", pady=3)
            times = [item.time_str for item in schedule.signals]
            interval = f"{min(times)}–{max(times)}" if times else "sem horários"
            text = f"{'● ' if selected else ''}{schedule.name}\n{self._format_date(schedule.date_str)} | {len(schedule.signals)} sinal(is) | {interval}"
            description = getattr(schedule, "description", "").strip()
            if description:
                text += f"\n{description}"
            app_main.ttk.Label(row, text=text, style="Body.TLabel").pack(side="left", fill="x", expand=True)
            app_main.ttk.Button(row, text="Selecionar", command=lambda item=schedule: self._activate_list(item), style="Secondary.TButton").pack(side="right")


def list_dialog(self, schedule=None, duplicate=False):
    if self.running:
        app_main.messagebox.showwarning("Execução ativa", "Não é possível alterar listas durante uma execução.")
        return
    dialog = app_main.tk.Toplevel(self.root)
    dialog.title("Nova lista" if not schedule or duplicate else "Editar lista")
    dialog.geometry("440x390")
    dialog.transient(self.root)
    dialog.grab_set()
    frame = app_main.ttk.Frame(dialog, padding=16)
    frame.pack(fill="both", expand=True)
    base_date = datetime.strptime(schedule.date_str, "%Y-%m-%d").date() if schedule else date.today()
    name_var = app_main.tk.StringVar(value=f"{schedule.name} - cópia" if schedule and duplicate else (schedule.name if schedule else ""))
    day_var = app_main.tk.StringVar(value=f"{base_date.day:02d}")
    month_var = app_main.tk.StringVar(value=f"{base_date.month:02d}")
    year_var = app_main.tk.StringVar(value=str(base_date.year))
    description_var = app_main.tk.StringVar(value=getattr(schedule, "description", "") if schedule else "")
    app_main.ttk.Label(frame, text="Nome da lista").pack(anchor="w", pady=(3, 2))
    app_main.ttk.Entry(frame, textvariable=name_var).pack(fill="x")
    app_main.ttk.Label(frame, text="Data da lista").pack(anchor="w", pady=(12, 2))
    date_row = app_main.ttk.Frame(frame)
    date_row.pack(fill="x")
    for label, variable, start, end, width in (("Dia", day_var, 1, 31, 5), ("Mês", month_var, 1, 12, 5), ("Ano", year_var, 2020, 2100, 8)):
        box = app_main.ttk.Frame(date_row)
        box.pack(side="left", padx=(0, 8))
        app_main.ttk.Label(box, text=label).pack(anchor="w")
        app_main.ttk.Spinbox(box, from_=start, to=end, width=width, textvariable=variable).pack()
    app_main.ttk.Label(frame, text="Descrição (opcional)").pack(anchor="w", pady=(12, 2))
    app_main.ttk.Entry(frame, textvariable=description_var).pack(fill="x")
    app_main.ttk.Label(frame, text="Após salvar, adicione os horários na aba Agenda.", style="Muted.TLabel").pack(anchor="w", pady=(12, 2))

    def save():
        name = name_var.get().strip()
        try:
            parsed = date(int(year_var.get()), int(month_var.get()), int(day_var.get())).isoformat()
        except (ValueError, TypeError):
            app_main.messagebox.showerror("Data inválida", "Revise dia, mês e ano.", parent=dialog)
            return
        if not name:
            app_main.messagebox.showerror("Nome obrigatório", "Informe um nome.", parent=dialog)
            return
        current_id = schedule.id if schedule and not duplicate else None
        if any(item.id != current_id and item.name.casefold() == name.casefold() and item.date_str == parsed for item in self.lists):
            app_main.messagebox.showerror("Lista duplicada", "Já existe uma lista com esse nome nessa data.", parent=dialog)
            return
        now = datetime.now().isoformat(timespec="seconds")
        if schedule and not duplicate:
            schedule.name = name
            schedule.date_str = parsed
            schedule.description = description_var.get().strip()
            schedule.updated_at = now
            for signal in schedule.signals:
                signal.date_str = parsed
            selected = schedule
        else:
            copied = [app_main.Signal(str(uuid4()), parsed, item.time_str, item.direction, "AGENDADO") for item in schedule.signals] if schedule else []
            selected = app_main.ScheduleList(str(uuid4()), name, parsed, copied, now)
            selected.description = description_var.get().strip()
            selected.created_at = now
            selected.archived = False
            self.lists.append(selected)
        self.active_list_id = selected.id
        self.list_var.set(list_label(self, selected))
        self._save_config()
        dialog.destroy()
        self.show_schedule()

    app_main.ttk.Button(frame, text="Salvar lista", command=save, style="Primary.TButton").pack(fill="x", pady=(18, 0))


def activate_list(self, schedule):
    if self.running:
        app_main.messagebox.showwarning("Execução ativa", "Não é possível trocar de lista durante uma execução.")
        return
    self.active_list_id = schedule.id
    self.list_var.set(list_label(self, schedule))
    self._save_config()
    self.show_lists()


def delete_list(self):
    if self.running:
        app_main.messagebox.showwarning("Execução ativa", "Não é possível excluir listas durante uma execução.")
        return
    if not self.active_list:
        app_main.messagebox.showwarning("Lista", "Selecione uma lista.")
        return
    if not app_main.messagebox.askyesno("Excluir lista", f"Excluir definitivamente '{self.active_list.name}'?"):
        return
    deleted_id = self.active_list.id
    self.lists = [item for item in self.lists if item.id != deleted_id]
    self.active_list_id = self.lists[0].id if self.lists else None
    self._save_config()
    self.show_lists()


def archive_list(self):
    if self.running:
        app_main.messagebox.showwarning("Execução ativa", "Não é possível arquivar listas durante uma execução.")
        return
    if not self.active_list:
        app_main.messagebox.showwarning("Lista", "Selecione uma lista.")
        return
    self.active_list.archived = not bool(getattr(self.active_list, "archived", False))
    self.active_list.updated_at = datetime.now().isoformat(timespec="seconds")
    self._save_config()
    self.show_lists()


def prepare_session(self):
    if self.running:
        app_main.messagebox.showwarning("Execução ativa", "Encerre a execução atual.")
        return
    if not self.active_profile:
        app_main.messagebox.showwarning("Perfil obrigatório", "Selecione ou crie um perfil.")
        return
    if self._profile_compatibility_text(self.active_profile) != "perfil pronto":
        app_main.messagebox.showwarning("Perfil incompatível", "Recalibre e teste o perfil para esta tela.")
        self.show_profiles()
        return
    if not self.active_list:
        app_main.messagebox.showwarning("Lista obrigatória", "Selecione ou crie uma lista.")
        self.show_lists()
        return
    if getattr(self.active_list, "archived", False):
        app_main.messagebox.showwarning("Lista arquivada", "Restaure ou duplique essa lista antes de executar.")
        return
    self.session_signals = [app_main.Signal(**asdict(item)) for item in self.active_list.signals]
    for signal in self.session_signals:
        signal.status = "AGENDADO"
    self.status_var.set("PRONTO")
    self._update_summary()
    self.show_schedule()


def start_execution(self):
    before = self.running
    ORIGINAL_START(self)
    if not before and self.running:
        self.current_session = {
            "id": str(uuid4()),
            "started_at": datetime.now().isoformat(timespec="seconds"),
            "finished_at": None,
            "profile_id": self.active_profile.id if self.active_profile else None,
            "profile_name": self.active_profile.name if self.active_profile else "",
            "list_id": self.active_list.id if self.active_list else None,
            "list_name": self.active_list.name if self.active_list else "",
            "list_date": self.active_list.date_str if self.active_list else "",
            "status": "EM_EXECUÇÃO",
            "events": [],
        }
        self._save_config()


def append_history(self, line):
    stamped = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — {line}"
    self.history.append(stamped)
    if self.current_session is not None:
        event_status = next((status for status in ("CLIQUE_ENVIADO", "EXPIRADO", "CANCELADO", "ERRO") if status in line), "INFO")
        self.current_session["events"].append({"at": datetime.now().isoformat(timespec="seconds"), "status": event_status, "detail": line})
    self._save_config()


def close_current_session(self, status):
    if self.current_session is None:
        return
    self.current_session["finished_at"] = datetime.now().isoformat(timespec="seconds")
    self.current_session["status"] = status
    self.session_history.append(self.current_session)
    self.current_session = None
    self._save_config()


def finish_execution(self):
    ORIGINAL_FINISH(self)
    close_current_session(self, "FINALIZADO")


def stop_execution(self):
    was_running = self.running
    ORIGINAL_STOP(self)
    if was_running and not self.running:
        close_current_session(self, "ENCERRADO")


def handle_error(self, message):
    ORIGINAL_ERROR(self, message)
    close_current_session(self, "ERRO")


def show_history(self):
    self._set_page("Histórico")
    self._clear()
    panel = self._panel("Histórico por sessão", "Sessões agrupadas, filtráveis e exportáveis.")
    toolbar = app_main.ttk.Frame(panel, style="Panel.TFrame")
    toolbar.pack(fill="x", pady=(0, 8))
    filter_var = app_main.tk.StringVar(value="TODOS")
    app_main.ttk.Combobox(toolbar, textvariable=filter_var, values=["TODOS", "FINALIZADO", "ENCERRADO", "ERRO"], state="readonly", width=15).pack(side="left")
    container = app_main.ttk.Frame(panel, style="Panel.TFrame")
    container.pack(fill="both", expand=True)

    def render(*_args):
        for child in container.winfo_children():
            child.destroy()
        selected = filter_var.get()
        sessions = [item for item in reversed(self.session_history) if selected == "TODOS" or item.get("status") == selected]
        if not sessions:
            app_main.ttk.Label(container, text="Nenhuma sessão estruturada registrada.", style="Muted.TLabel").pack(anchor="w", pady=10)
            return
        for session in sessions:
            events = session.get("events", [])
            counts = {key: sum(1 for event in events if event.get("status") == key) for key in ("CLIQUE_ENVIADO", "EXPIRADO", "CANCELADO", "ERRO")}
            row = app_main.ttk.Frame(container, style="Panel2.TFrame", padding=10)
            row.pack(fill="x", pady=3)
            started = session.get("started_at", "").replace("T", " ")
            text = (
                f"{started} — {session.get('list_name', 'Lista')} ({session.get('list_date', '')})\n"
                f"Perfil: {session.get('profile_name', '—')} | Status: {session.get('status', '—')}\n"
                f"Enviados: {counts['CLIQUE_ENVIADO']} | Expirados: {counts['EXPIRADO']} | Cancelados: {counts['CANCELADO']} | Erros: {counts['ERRO']}"
            )
            app_main.ttk.Label(row, text=text, style="Body.TLabel").pack(anchor="w")
            details = "\n".join(f"  {event.get('at', '').replace('T', ' ')} — {event.get('detail', '')}" for event in events)
            if details:
                app_main.ttk.Label(row, text=details, style="Body.TLabel", wraplength=580).pack(anchor="w", pady=(5, 0))

    filter_var.trace_add("write", render)
    app_main.ttk.Button(toolbar, text="Exportar CSV", command=lambda: export_history(self), style="Secondary.TButton").pack(side="right", padx=(5, 0))
    app_main.ttk.Button(toolbar, text="Limpar histórico", command=lambda: clear_history(self, render), style="Danger.TButton").pack(side="right")
    render()


def export_history(self):
    if not self.session_history:
        app_main.messagebox.showwarning("Histórico", "Não há sessões para exportar.")
        return
    path = filedialog.asksaveasfilename(title="Exportar histórico", defaultextension=".csv", filetypes=[("CSV", "*.csv")], initialfile=f"predixai_historico_{date.today().isoformat()}.csv")
    if not path:
        return
    with Path(path).open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle, delimiter=";")
        writer.writerow(["sessao_id", "inicio", "fim", "perfil", "lista", "data_lista", "status", "evento_status", "evento_data", "detalhe"])
        for session in self.session_history:
            events = session.get("events", []) or [{}]
            for event in events:
                writer.writerow([session.get("id"), session.get("started_at"), session.get("finished_at"), session.get("profile_name"), session.get("list_name"), session.get("list_date"), session.get("status"), event.get("status"), event.get("at"), event.get("detail")])
    app_main.messagebox.showinfo("Exportação concluída", f"Histórico salvo em:\n{path}")


def clear_history(self, render):
    if not self.session_history:
        return
    if not app_main.messagebox.askyesno("Limpar histórico", "Excluir todo o histórico estruturado?"):
        return
    self.session_history = []
    self.history = []
    self._save_config()
    render()


def install_patch():
    cls = app_main.PredixAIRoboListas
    cls.active_list = property(active_list)
    cls._load_config = load_config
    cls._save_config = save_config
    cls.show_home = show_home
    cls._select_profile_by_name = select_profile
    cls._select_list_by_name = select_list
    cls.show_lists = show_lists
    cls._list_dialog = list_dialog
    cls._activate_list = activate_list
    cls._delete_list = delete_list
    cls._archive_list = archive_list
    cls._prepare_session = prepare_session
    cls._start_execution = start_execution
    cls._append_history = append_history
    cls._finish_execution = finish_execution
    cls._stop_execution = stop_execution
    cls._handle_execution_error = handle_error
    cls.show_history = show_history
    cls.list_choice_to_id = {}


if __name__ == "__main__":
    install_patch()
    app_main.main()
