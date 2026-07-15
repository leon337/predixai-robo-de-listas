#!/usr/bin/env python3
"""Camada V2.3: UX de direção, gestão contextual de listas e histórico mestre-detalhe."""
from __future__ import annotations

from datetime import datetime

import main as app_main
import bootstrap_v22


ORIGINAL_INIT = app_main.PredixAIRoboListas.__init__


def init_v23(self, root):
    ORIGINAL_INIT(self, root)
    self.root.title("PredixAI Robô de Listas — V2.3")
    self.selected_direction = getattr(self, "selected_direction", "PARA_CIMA")
    self.selected_session_id = None


def _set_direction(self, direction: str) -> None:
    if self.running:
        return
    self.selected_direction = direction
    self.direction_var.set(direction)
    if hasattr(self, "direction_up_button"):
        self.direction_up_button.configure(
            style="ActiveNav.TButton" if direction == "PARA_CIMA" else "Secondary.TButton"
        )
    if hasattr(self, "direction_down_button"):
        self.direction_down_button.configure(
            style="ActiveNav.TButton" if direction == "PARA_BAIXO" else "Secondary.TButton"
        )


def show_schedule(self) -> None:
    self._set_page("Agenda")
    self._clear()
    panel = self._panel("Agenda da lista", "Edite a lista selecionada. Durante execução, a agenda fica bloqueada.")
    if not self.active_list:
        app_main.ttk.Label(panel, text="Selecione ou crie uma lista.", style="Muted.TLabel").pack(anchor="w")
        return

    app_main.ttk.Label(
        panel,
        text=f"{self.active_list.name} — {self._format_date(self.active_list.date_str)}",
        style="Status.TLabel",
    ).pack(anchor="w", pady=(0, 8))

    form = app_main.ttk.Frame(panel, style="Panel2.TFrame", padding=10)
    form.pack(fill="x", pady=(0, 10))
    now = datetime.now()
    self.hour_var = app_main.tk.StringVar(value=f"{now.hour:02d}")
    self.minute_var = app_main.tk.StringVar(value=f"{now.minute:02d}")
    self.second_var = app_main.tk.StringVar(value=f"{now.second:02d}")

    time_row = app_main.ttk.Frame(form, style="Panel2.TFrame")
    time_row.pack(anchor="w", pady=(0, 8))
    for variable, limit, label in (
        (self.hour_var, 23, "Hora"),
        (self.minute_var, 59, "Min"),
        (self.second_var, 59, "Seg"),
    ):
        box = app_main.ttk.Frame(time_row, style="Panel2.TFrame")
        box.pack(side="left", padx=(0, 6))
        app_main.ttk.Label(box, text=label, style="Body.TLabel").pack(anchor="w")
        spin = app_main.ttk.Spinbox(box, from_=0, to=limit, width=4, textvariable=variable, format="%02.0f", wrap=True)
        spin.pack()
        spin.bind("<FocusOut>", lambda _event, var=variable, maximum=limit: self._normalize_time_var(var, maximum))
        spin.bind("<Return>", lambda _event, var=variable, maximum=limit: self._normalize_time_var(var, maximum))

    app_main.ttk.Label(form, text="Direção", style="Body.TLabel").pack(anchor="w", pady=(2, 4))
    self.direction_var = app_main.tk.StringVar(value=getattr(self, "selected_direction", "PARA_CIMA"))
    direction_row = app_main.ttk.Frame(form, style="Panel2.TFrame")
    direction_row.pack(anchor="w", pady=(0, 8))
    self.direction_up_button = app_main.ttk.Button(
        direction_row,
        text="▲ PARA CIMA",
        command=lambda: self._set_direction("PARA_CIMA"),
        style="Secondary.TButton",
        width=16,
    )
    self.direction_up_button.pack(side="left", padx=(0, 6))
    self.direction_down_button = app_main.ttk.Button(
        direction_row,
        text="▼ PARA BAIXO",
        command=lambda: self._set_direction("PARA_BAIXO"),
        style="Secondary.TButton",
        width=16,
    )
    self.direction_down_button.pack(side="left")
    self._set_direction(self.direction_var.get())

    add_button = app_main.ttk.Button(form, text="Adicionar sinal", command=self._add_signal, style="Primary.TButton")
    add_button.pack(anchor="w")
    if self.running:
        add_button.state(["disabled"])
        self.direction_up_button.state(["disabled"])
        self.direction_down_button.state(["disabled"])

    self.signal_list = app_main.ttk.Frame(panel, style="Panel.TFrame")
    self.signal_list.pack(fill="both", expand=True)
    self._render_signal_list()

    footer = app_main.ttk.Frame(panel, style="Panel.TFrame")
    footer.pack(fill="x", pady=(10, 0))
    app_main.ttk.Label(footer, textvariable=self.counter_var, style="Muted.TLabel").pack(side="left")
    clear_button = app_main.ttk.Button(footer, text="Limpar lista", command=self._clear_schedule, style="Danger.TButton")
    clear_button.pack(side="right", padx=(5, 0))
    start_button = app_main.ttk.Button(footer, text="Iniciar", command=self._start_execution, style="Primary.TButton")
    start_button.pack(side="right")
    if self.running:
        clear_button.state(["disabled"])
        start_button.state(["disabled"])


def _select_list_card(self, schedule) -> None:
    if self.running:
        return
    self.active_list_id = schedule.id
    self.list_var.set(bootstrap_v22.list_label(self, schedule))
    self._save_config()
    self.show_lists()


def show_lists(self) -> None:
    self._set_page("Listas")
    self._clear()
    panel = self._panel("Listas programadas", "Selecione um cartão; as ações abaixo atuam somente na lista marcada.")

    selection = self.active_list
    toolbar = app_main.ttk.Frame(panel, style="Panel.TFrame")
    toolbar.pack(fill="x", pady=(0, 10))
    new_button = app_main.ttk.Button(toolbar, text="Nova lista", command=lambda: self._list_dialog(), style="Primary.TButton")
    edit_button = app_main.ttk.Button(toolbar, text="Editar", command=lambda: self._list_dialog(self.active_list), style="Secondary.TButton")
    duplicate_button = app_main.ttk.Button(toolbar, text="Duplicar", command=lambda: self._list_dialog(self.active_list, True), style="Secondary.TButton")
    archive_button = app_main.ttk.Button(toolbar, text="Restaurar" if selection and getattr(selection, "archived", False) else "Arquivar", command=self._archive_list, style="Secondary.TButton")
    delete_button = app_main.ttk.Button(toolbar, text="Excluir", command=self._delete_list, style="Danger.TButton")
    for button in (new_button, edit_button, duplicate_button, archive_button, delete_button):
        button.pack(side="left", padx=(0, 5))

    if self.running:
        for button in (new_button, edit_button, duplicate_button, archive_button, delete_button):
            button.state(["disabled"])
    elif not selection:
        for button in (edit_button, duplicate_button, archive_button, delete_button):
            button.state(["disabled"])

    if not self.lists:
        app_main.ttk.Label(panel, text="Nenhuma lista criada.", style="Muted.TLabel").pack(anchor="w", pady=15)
        return

    for group in ("HOJE", "AMANHÃ", "FUTURA", "HISTÓRICO"):
        items = [item for item in self.lists if bootstrap_v22.list_status(item) == group]
        if not items:
            continue
        app_main.ttk.Label(panel, text=group, style="Status.TLabel").pack(anchor="w", pady=(10, 3))
        for schedule in sorted(items, key=lambda value: (value.date_str, value.name.casefold(), value.id)):
            selected = schedule.id == self.active_list_id
            row_style = "Panel2.TFrame"
            row = app_main.ttk.Frame(panel, style=row_style, padding=11)
            row.pack(fill="x", pady=4)
            times = [item.time_str for item in schedule.signals]
            interval = f"{min(times)}–{max(times)}" if times else "sem horários"
            marker = "● SELECIONADA" if selected else "○ Selecionar"
            text = (
                f"{schedule.name}\n"
                f"{self._format_date(schedule.date_str)} | {len(schedule.signals)} sinal(is) | {interval}\n"
                f"Status: {bootstrap_v22.list_status(schedule)}"
            )
            description = getattr(schedule, "description", "").strip()
            if description:
                text += f"\n{description}"
            app_main.ttk.Label(row, text=text, style="Body.TLabel").pack(side="left", fill="x", expand=True)
            button = app_main.ttk.Button(
                row,
                text=marker,
                command=lambda item=schedule: self._select_list_card(item),
                style="ActiveNav.TButton" if selected else "Secondary.TButton",
            )
            button.pack(side="right")
            if self.running:
                button.state(["disabled"])


def _session_label(index: int, session: dict) -> str:
    started = str(session.get("started_at", "")).replace("T", " ")
    status = str(session.get("status", "—"))
    name = str(session.get("list_name", "Lista"))
    return f"Sessão {index:03d} — {started} — {name} — {status}"


def show_history(self) -> None:
    self._set_page("Histórico")
    self._clear()
    panel = self._panel("Histórico por sessão", "Selecione uma sessão para consultar seus sinais e resultado final.")

    sessions = list(enumerate(self.session_history, start=1))
    sessions.reverse()
    toolbar = app_main.ttk.Frame(panel, style="Panel.TFrame")
    toolbar.pack(fill="x", pady=(0, 8))
    filter_var = app_main.tk.StringVar(value="TODOS")
    filter_combo = app_main.ttk.Combobox(
        toolbar,
        textvariable=filter_var,
        values=["TODOS", "FINALIZADO", "ENCERRADO", "CANCELADO", "INTERROMPIDO", "ERRO"],
        state="readonly",
        width=16,
    )
    filter_combo.pack(side="left")
    app_main.ttk.Button(toolbar, text="Exportar CSV", command=lambda: bootstrap_v22.export_history(self), style="Secondary.TButton").pack(side="right", padx=(5, 0))

    body = app_main.ttk.Frame(panel, style="Panel.TFrame")
    body.pack(fill="both", expand=True)
    left = app_main.ttk.Frame(body, style="Panel.TFrame")
    left.pack(side="left", fill="y", padx=(0, 8))
    right = app_main.ttk.Frame(body, style="Panel2.TFrame", padding=12)
    right.pack(side="left", fill="both", expand=True)

    session_var = app_main.tk.StringVar(value="")
    selector = app_main.ttk.Combobox(left, textvariable=session_var, state="readonly", width=52)
    selector.pack(fill="x", pady=(0, 8))
    mapping: dict[str, dict] = {}

    def render_choices(*_args):
        mapping.clear()
        selected_filter = filter_var.get()
        labels = []
        for index, session in sessions:
            if selected_filter != "TODOS" and session.get("status") != selected_filter:
                continue
            label = _session_label(index, session)
            mapping[label] = session
            labels.append(label)
        selector.configure(values=labels)
        if labels:
            if session_var.get() not in mapping:
                session_var.set(labels[0])
            render_detail()
        else:
            session_var.set("")
            for child in right.winfo_children():
                child.destroy()
            app_main.ttk.Label(right, text="Nenhuma sessão encontrada.", style="Body.TLabel").pack(anchor="w")

    def render_detail(*_args):
        for child in right.winfo_children():
            child.destroy()
        session = mapping.get(session_var.get())
        if not session:
            return
        events = list(session.get("events", []))
        counts = {key: sum(1 for event in events if event.get("status") == key) for key in ("CLIQUE_ENVIADO", "EXPIRADO", "CANCELADO", "ERRO")}
        app_main.ttk.Label(right, text=session_var.get(), style="Header.TLabel").pack(anchor="w", pady=(0, 8))
        summary = (
            f"Perfil: {session.get('profile_name', '—')}\n"
            f"Lista: {session.get('list_name', '—')} | Data: {session.get('list_date', '—')}\n"
            f"Início: {str(session.get('started_at', '—')).replace('T', ' ')}\n"
            f"Fim: {str(session.get('finished_at', '—')).replace('T', ' ')}\n"
            f"Status final: {session.get('status', '—')}\n"
            f"Enviados: {counts['CLIQUE_ENVIADO']} | Expirados: {counts['EXPIRADO']} | Cancelados: {counts['CANCELADO']} | Erros: {counts['ERRO']}"
        )
        app_main.ttk.Label(right, text=summary, style="Body.TLabel", justify="left").pack(anchor="w", pady=(0, 10))
        app_main.ttk.Label(right, text="Sinais e eventos", style="Header.TLabel").pack(anchor="w", pady=(0, 5))
        if not events:
            app_main.ttk.Label(right, text="Nenhum evento registrado.", style="Body.TLabel").pack(anchor="w")
        for event in events:
            when = str(event.get("at", "")).replace("T", " ")
            status = event.get("status", "INFO")
            detail = event.get("detail", "")
            card = app_main.ttk.Frame(right, style="Panel.TFrame", padding=8)
            card.pack(fill="x", pady=2)
            app_main.ttk.Label(card, text=f"{when} — {status}\n{detail}", style="Muted.TLabel", wraplength=390).pack(anchor="w")

    selector.bind("<<ComboboxSelected>>", render_detail)
    filter_var.trace_add("write", render_choices)
    app_main.ttk.Button(left, text="Limpar histórico", command=lambda: bootstrap_v22.clear_history(self, render_choices), style="Danger.TButton").pack(fill="x")
    render_choices()


def install_patch() -> None:
    bootstrap_v22.install_patch()
    cls = app_main.PredixAIRoboListas
    cls.__init__ = init_v23
    cls._set_direction = _set_direction
    cls.show_schedule = show_schedule
    cls._select_list_card = _select_list_card
    cls.show_lists = show_lists
    cls.show_history = show_history


if __name__ == "__main__":
    install_patch()
    app_main.main()
