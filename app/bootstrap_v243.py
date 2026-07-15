#!/usr/bin/env python3
"""Tela Sobre, diagnóstico e ferramentas operacionais da V2.4.3."""
from __future__ import annotations

import logging
from pathlib import Path
from tkinter import messagebox

import main as app_main
from diagnostics_tools import (
    collect_diagnostics,
    diagnostic_summary,
    export_diagnostic_report,
    open_path,
    read_version,
    run_installer,
)

ROOT_DIR = Path(__file__).resolve().parents[1]
_PREVIOUS_BUILD_SHELL = None
_INSTALLED = False


def _add_card(self, parent, title: str, detail: str) -> None:
    card = app_main.ttk.Frame(parent, style="Panel2.TFrame", padding=10)
    card.pack(fill="x", pady=3)
    app_main.ttk.Label(card, text=title, style="Body.TLabel").pack(anchor="w")
    app_main.ttk.Label(card, text=detail, style="Body.TLabel", wraplength=560, justify="left").pack(anchor="w", pady=(3, 0))


def show_tools(self) -> None:
    self._set_page("Ferramentas")
    self._clear()
    panel = self._panel(
        "Diagnóstico e ferramentas",
        "Consulte o ambiente, abra dados técnicos e repare o atalho da aplicação.",
    )
    items = collect_diagnostics(ROOT_DIR)
    _add_card(self, panel, "Resumo", diagnostic_summary(items))
    _add_card(self, panel, "Versão instalada", read_version(ROOT_DIR))
    _add_card(self, panel, "Sistema", next(item.detail for item in items if item.name == "Sistema"))

    actions = app_main.ttk.Frame(panel, style="Panel.TFrame")
    actions.pack(fill="x", pady=(12, 5))

    def open_logs() -> None:
        try:
            open_path(ROOT_DIR / "logs")
        except Exception as exc:
            messagebox.showerror("Falha ao abrir logs", str(exc))

    def open_backups() -> None:
        try:
            open_path(ROOT_DIR / "backups" / "config")
        except Exception as exc:
            messagebox.showerror("Falha ao abrir backups", str(exc))

    def export_report() -> None:
        try:
            report = export_diagnostic_report(ROOT_DIR, collect_diagnostics(ROOT_DIR))
            logging.getLogger("predixai.runtime").info("Relatório de diagnóstico criado: %s", report)
            messagebox.showinfo("Diagnóstico exportado", f"Relatório criado em:\n{report}")
        except Exception as exc:
            messagebox.showerror("Falha ao exportar diagnóstico", str(exc))

    def repair_installation() -> None:
        if not messagebox.askyesno(
            "Reparar instalação",
            "Executar o reparo do ícone e do atalho da área de trabalho?",
        ):
            return
        try:
            result = run_installer(ROOT_DIR)
            if result.returncode == 0:
                messagebox.showinfo("Reparo concluído", "Ícone e atalho atualizados com sucesso.")
            else:
                detail = (result.stderr or result.stdout or "Falha sem detalhes").strip()
                messagebox.showerror("Falha no reparo", detail[-1500:])
        except Exception as exc:
            messagebox.showerror("Falha no reparo", str(exc))

    for text, command in (
        ("Abrir logs", open_logs),
        ("Abrir backups", open_backups),
        ("Exportar diagnóstico", export_report),
        ("Reparar instalação", repair_installation),
    ):
        app_main.ttk.Button(actions, text=text, command=command, style="Secondary.TButton").pack(
            side="left", padx=(0, 6), pady=3
        )

    status_panel = app_main.ttk.Frame(panel, style="Panel2.TFrame", padding=10)
    status_panel.pack(fill="both", expand=True, pady=(8, 0))
    for item in items:
        app_main.ttk.Label(
            status_panel,
            text=f"[{item.status}] {item.name}: {item.detail}",
            style="Body.TLabel",
            wraplength=570,
            justify="left",
        ).pack(anchor="w", pady=1)


def show_about(self) -> None:
    version = read_version(ROOT_DIR)
    messagebox.showinfo(
        "Sobre — PredixAI Robô de Listas",
        "PredixAI Robô de Listas\n"
        f"Versão {version}\n\n"
        "Perfis, listas datadas, execução controlada, logs, backups e diagnóstico.\n"
        "Projeto PredixAI BR.",
    )


def _build_shell_v243(self) -> None:
    _PREVIOUS_BUILD_SHELL(self)
    nav_parent = next(
        (child for child in self.shell.winfo_children() if isinstance(child, app_main.ttk.Frame) and child is not self.content),
        None,
    )
    candidates = [child for child in self.shell.winfo_children() if isinstance(child, app_main.ttk.Frame)]
    nav_parent = candidates[-2] if len(candidates) >= 2 else nav_parent
    if nav_parent is not None:
        tools_button = app_main.ttk.Button(
            nav_parent,
            text="Ferramentas",
            command=self.show_tools,
            style="Secondary.TButton",
        )
        tools_button.pack(side="left", padx=(0, 5))
        self.nav_buttons["Ferramentas"] = tools_button
        app_main.ttk.Button(
            nav_parent,
            text="Sobre",
            command=self.show_about,
            style="Secondary.TButton",
        ).pack(side="left", padx=(0, 5))


def install_patch() -> None:
    global _PREVIOUS_BUILD_SHELL, _INSTALLED
    if _INSTALLED:
        return
    cls = app_main.PredixAIRoboListas
    _PREVIOUS_BUILD_SHELL = cls._build_shell
    cls._build_shell = _build_shell_v243
    cls.show_tools = show_tools
    cls.show_about = show_about
    _INSTALLED = True
