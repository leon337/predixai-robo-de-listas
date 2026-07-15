#!/usr/bin/env python3
"""Bootstrap da V2.1 com correção do seletor de listas por nome + data."""
from __future__ import annotations

import main as app_main


def _format_list_label(app: app_main.PredixAIRoboListas, schedule: app_main.ScheduleList) -> str:
    return f"{schedule.name} — {app._format_date(schedule.date_str)}"


def _build_list_choices(app: app_main.PredixAIRoboListas) -> list[str]:
    app.list_choice_to_id = {}
    if not app.active_profile:
        return []

    choices: list[str] = []
    ordered = sorted(
        app.active_profile.lists,
        key=lambda item: (item.date_str, item.name.casefold(), item.id),
    )
    for schedule in ordered:
        label = _format_list_label(app, schedule)
        if label in app.list_choice_to_id:
            label = f"{label} · {schedule.id[:8]}"
        app.list_choice_to_id[label] = schedule.id
        choices.append(label)
    return choices


def _active_list_label(app: app_main.PredixAIRoboListas) -> str:
    if not app.active_list:
        return ""
    _build_list_choices(app)
    return next(
        (label for label, list_id in app.list_choice_to_id.items() if list_id == app.active_list.id),
        "",
    )


def show_home(self: app_main.PredixAIRoboListas) -> None:
    self._set_page("Início")
    self._clear()
    panel = self._panel("Nova sessão", "Escolha um perfil e uma lista antes de iniciar.")
    app_main.ttk.Label(panel, textvariable=self.status_var, style="Status.TLabel").pack(
        anchor="w", pady=(0, 10)
    )

    profile_combo = app_main.ttk.Combobox(
        panel,
        textvariable=self.profile_var,
        values=[item.name for item in self.profiles],
        state="readonly",
    )
    profile_combo.pack(fill="x", pady=4)
    profile_combo.bind("<<ComboboxSelected>>", lambda _event: self._select_profile_by_name())

    choices = _build_list_choices(self)
    self.list_var.set(_active_list_label(self))
    list_combo = app_main.ttk.Combobox(
        panel,
        textvariable=self.list_var,
        values=choices,
        state="readonly",
    )
    list_combo.pack(fill="x", pady=4)
    list_combo.bind("<<ComboboxSelected>>", lambda _event: self._select_list_by_name())

    resolution, scale = self._screen_signature()
    for text in (
        f"Perfil: {self.active_profile.name if self.active_profile else 'nenhum selecionado'}",
        f"Aplicação: {self.active_profile.application if self.active_profile else '—'}",
        f"Lista: {_format_list_label(self, self.active_list) if self.active_list else 'nenhuma selecionada'}",
        f"Tela atual: {resolution} | escala {scale}",
        f"Compatibilidade: {self._profile_compatibility_text(self.active_profile)}",
    ):
        card = app_main.ttk.Frame(panel, style="Panel2.TFrame", padding=10)
        card.pack(fill="x", pady=3)
        app_main.ttk.Label(card, text=text, style="Body.TLabel").pack(anchor="w")

    actions = app_main.ttk.Frame(panel, style="Panel.TFrame")
    actions.pack(fill="x", pady=(14, 0))
    app_main.ttk.Button(
        actions,
        text="Gerenciar perfis",
        command=self.show_profiles,
        style="Secondary.TButton",
    ).pack(side="left", padx=(0, 6))
    app_main.ttk.Button(
        actions,
        text="Gerenciar listas",
        command=self.show_lists,
        style="Secondary.TButton",
    ).pack(side="left", padx=(0, 6))
    app_main.ttk.Button(
        actions,
        text="Preparar sessão",
        command=self._prepare_session,
        style="Primary.TButton",
    ).pack(side="left")


def select_list_by_name(self: app_main.PredixAIRoboListas) -> None:
    if not self.active_profile:
        return
    if self.running:
        app_main.messagebox.showwarning(
            "Execução ativa",
            "Não é possível trocar a lista durante uma execução.",
        )
        self.list_var.set(_active_list_label(self))
        return

    _build_list_choices(self)
    self.active_list_id = self.list_choice_to_id.get(self.list_var.get())
    self._save_config()
    self.show_home()


def install_patch() -> None:
    cls = app_main.PredixAIRoboListas
    cls.list_choice_to_id = {}
    cls.show_home = show_home
    cls._select_list_by_name = select_list_by_name


if __name__ == "__main__":
    install_patch()
    app_main.main()
