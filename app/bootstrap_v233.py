#!/usr/bin/env python3
"""V2.3.3: versão visível no cabeçalho e histórico responsivo por sessão."""
from __future__ import annotations

import main as app_main
import bootstrap_v22
from version_info import read_app_version


def build_shell(self) -> None:
    version = read_app_version(app_main.ROOT_DIR)
    self.root.title(f"PredixAI Robô de Listas — V{version}")

    style = app_main.ttk.Style()
    style.configure(
        "Version.TLabel",
        background=self.colors["bg"],
        foreground=self.colors["green"],
        font=("Arial", 9, "bold"),
    )
    style.configure(
        "DetailTitle.TLabel",
        background=self.colors["panel2"],
        foreground=self.colors["text"],
        font=("Arial", 12, "bold"),
    )
    style.configure(
        "DetailStatus.TLabel",
        background=self.colors["panel2"],
        foreground=self.colors["green"],
        font=("Arial", 10, "bold"),
    )
    style.configure(
        "History.Treeview",
        background=self.colors["panel2"],
        fieldbackground=self.colors["panel2"],
        foreground=self.colors["text"],
        rowheight=27,
        borderwidth=0,
    )
    style.configure(
        "History.Treeview.Heading",
        background=self.colors["blue"],
        foreground=self.colors["text"],
        font=("Arial", 9, "bold"),
        relief="flat",
    )
    style.map(
        "History.Treeview",
        background=[("selected", self.colors["blue_active"])],
        foreground=[("selected", self.colors["text"])],
    )

    self.shell = app_main.ttk.Frame(self.root, style="App.TFrame", padding=14)
    self.shell.pack(fill="both", expand=True)

    header = app_main.ttk.Frame(self.shell, style="App.TFrame")
    header.pack(fill="x")
    mark = app_main.tk.Canvas(
        header,
        width=58,
        height=58,
        bg=self.colors["bg"],
        highlightthickness=0,
    )
    mark.pack(side="left")
    mark.create_oval(4, 4, 54, 54, outline=self.colors["green"], width=2)
    mark.create_text(29, 27, text="P", fill="white", font=("Arial", 25, "bold"))
    mark.create_text(30, 46, text="AI", fill=self.colors["green"], font=("Arial", 7, "bold"))

    brand = app_main.ttk.Frame(header, style="App.TFrame")
    brand.pack(side="left", padx=10)
    title_row = app_main.ttk.Frame(brand, style="App.TFrame")
    title_row.pack(anchor="w")
    app_main.ttk.Label(
        title_row,
        text="PredixAI Robô de Listas",
        style="Title.TLabel",
    ).pack(side="left")
    app_main.ttk.Label(
        title_row,
        text=f"  V{version}",
        style="Version.TLabel",
    ).pack(side="left", padx=(5, 0), pady=(7, 0))
    app_main.ttk.Label(
        brand,
        text="Perfis, listas datadas e execução controlada",
        style="Subtitle.TLabel",
    ).pack(anchor="w")

    right = app_main.ttk.Frame(header, style="App.TFrame")
    right.pack(side="right")
    app_main.ttk.Label(right, textvariable=self.clock_var, style="Title.TLabel").pack(anchor="e")
    app_main.ttk.Label(right, textvariable=self.status_var, style="Subtitle.TLabel").pack(anchor="e")
    app_main.ttk.Label(right, text=f"Versão instalada: {version}", style="Version.TLabel").pack(anchor="e")

    nav = app_main.ttk.Frame(self.shell, style="App.TFrame")
    nav.pack(fill="x", pady=(12, 10))
    for label, command in (
        ("Início", self.show_home),
        ("Perfis", self.show_profiles),
        ("Listas", self.show_lists),
        ("Agenda", self.show_schedule),
        ("Execução", self.show_execution),
        ("Histórico", self.show_history),
    ):
        button = app_main.ttk.Button(nav, text=label, command=command, style="Secondary.TButton")
        button.pack(side="left", padx=(0, 5))
        self.nav_buttons[label] = button

    self.content = app_main.ttk.Frame(self.shell, style="App.TFrame")
    self.content.pack(fill="both", expand=True)


def session_label(index: int, session: dict) -> str:
    started = str(session.get("started_at", "")).replace("T", " ")
    status = str(session.get("status", "—"))
    name = str(session.get("list_name", "Lista"))
    return f"Sessão {index:03d} — {started} — {name} — {status}"


def show_history(self) -> None:
    self._set_page("Histórico")
    self._clear()
    panel = self._panel(
        "Histórico por sessão",
        "Filtre, selecione uma sessão e consulte o resumo e cada evento.",
    )

    sessions = list(enumerate(self.session_history, start=1))
    sessions.reverse()

    toolbar = app_main.ttk.Frame(panel, style="Panel.TFrame")
    toolbar.pack(fill="x", pady=(0, 8))
    app_main.ttk.Label(toolbar, text="Status", style="Muted.TLabel").pack(side="left", padx=(0, 5))
    filter_var = app_main.tk.StringVar(value="TODOS")
    filter_combo = app_main.ttk.Combobox(
        toolbar,
        textvariable=filter_var,
        values=[
            "TODOS",
            "FINALIZADO",
            "EXPIRADA",
            "CANCELADO",
            "ENCERRADO",
            "INTERROMPIDO",
            "ERRO",
        ],
        state="readonly",
        width=16,
    )
    filter_combo.pack(side="left")
    app_main.ttk.Button(
        toolbar,
        text="Exportar CSV",
        command=lambda: bootstrap_v22.export_history(self),
        style="Secondary.TButton",
    ).pack(side="right", padx=(5, 0))

    app_main.ttk.Label(panel, text="Sessão", style="Muted.TLabel").pack(anchor="w")
    session_var = app_main.tk.StringVar(value="")
    selector = app_main.ttk.Combobox(panel, textvariable=session_var, state="readonly")
    selector.pack(fill="x", pady=(3, 8))

    detail = app_main.ttk.Frame(panel, style="Panel2.TFrame", padding=12)
    detail.pack(fill="both", expand=True)
    mapping: dict[str, dict] = {}

    def render_detail(*_args) -> None:
        for child in detail.winfo_children():
            child.destroy()
        session = mapping.get(session_var.get())
        if not session:
            app_main.ttk.Label(
                detail,
                text="Nenhuma sessão selecionada.",
                style="Body.TLabel",
            ).pack(anchor="w")
            return

        self.selected_session_id = session.get("id")
        events = list(session.get("events", []))
        statuses = ("CLIQUE_ENVIADO", "EXPIRADO", "CANCELADO", "ERRO")
        counts = {
            key: sum(1 for event in events if event.get("status") == key)
            for key in statuses
        }
        selected_label = session_var.get()
        session_number = selected_label.split(" — ", 1)[0]
        final_status = str(session.get("status", "—"))

        app_main.ttk.Label(
            detail,
            text=f"{session_number} — {final_status}",
            style="DetailTitle.TLabel",
        ).pack(anchor="w")
        app_main.ttk.Label(
            detail,
            text=(
                f"Perfil: {session.get('profile_name', '—')}\n"
                f"Lista: {session.get('list_name', '—')} | Data: {session.get('list_date', '—')}\n"
                f"Início: {str(session.get('started_at', '—')).replace('T', ' ')}\n"
                f"Fim: {str(session.get('finished_at', '—')).replace('T', ' ')}"
            ),
            style="Body.TLabel",
            justify="left",
        ).pack(anchor="w", pady=(5, 6))
        app_main.ttk.Label(
            detail,
            text=(
                f"Enviados: {counts['CLIQUE_ENVIADO']}   "
                f"Expirados: {counts['EXPIRADO']}   "
                f"Cancelados: {counts['CANCELADO']}   "
                f"Erros: {counts['ERRO']}"
            ),
            style="DetailStatus.TLabel",
        ).pack(anchor="w", pady=(0, 10))

        events_box = app_main.ttk.Frame(detail, style="Panel2.TFrame")
        events_box.pack(fill="both", expand=True)
        tree = app_main.ttk.Treeview(
            events_box,
            columns=("hora", "status", "detalhe"),
            show="headings",
            style="History.Treeview",
            height=10,
        )
        tree.heading("hora", text="Data e hora")
        tree.heading("status", text="Status")
        tree.heading("detalhe", text="Detalhe")
        tree.column("hora", width=145, minwidth=125, stretch=False)
        tree.column("status", width=105, minwidth=90, stretch=False)
        tree.column("detalhe", width=330, minwidth=220, stretch=True)
        scrollbar = app_main.ttk.Scrollbar(events_box, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        if not events:
            tree.insert("", "end", values=("—", "SEM EVENTOS", "Nenhum evento registrado."))
        else:
            for event in events:
                when = str(event.get("at", "")).replace("T", " ")
                status = str(event.get("status", "INFO"))
                event_detail = str(event.get("detail", "")).replace("\n", " ")
                tree.insert("", "end", values=(when, status, event_detail))

    def render_choices(*_args) -> None:
        mapping.clear()
        selected_filter = filter_var.get()
        labels: list[str] = []
        preferred = ""
        for index, session in sessions:
            if selected_filter != "TODOS" and session.get("status") != selected_filter:
                continue
            label = session_label(index, session)
            mapping[label] = session
            labels.append(label)
            if session.get("id") == getattr(self, "selected_session_id", None):
                preferred = label
        selector.configure(values=labels)
        if not labels:
            session_var.set("")
            render_detail()
            return
        session_var.set(preferred or labels[0])
        render_detail()

    selector.bind("<<ComboboxSelected>>", render_detail)
    filter_var.trace_add("write", render_choices)
    footer = app_main.ttk.Frame(panel, style="Panel.TFrame")
    footer.pack(fill="x", pady=(8, 0))
    app_main.ttk.Button(
        footer,
        text="Limpar histórico",
        command=lambda: bootstrap_v22.clear_history(self, render_choices),
        style="Danger.TButton",
    ).pack(side="right")
    render_choices()


def install_patch() -> None:
    cls = app_main.PredixAIRoboListas
    cls._build_shell = build_shell
    cls.show_history = show_history


if __name__ == "__main__":
    install_patch()
    app_main.main()
