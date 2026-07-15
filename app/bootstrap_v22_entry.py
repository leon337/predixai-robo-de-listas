#!/usr/bin/env python3
"""Entrada final da V2.2 com ajustes de integração."""
from __future__ import annotations

import main as app_main
import bootstrap_v22


def activate_profile(self, profile):
    if self.running:
        app_main.messagebox.showwarning("Execução ativa", "Não é possível trocar o perfil durante uma execução.")
        return
    self.active_profile_id = profile.id
    self.profile_var.set(profile.name)
    self._save_config()
    self.show_profiles()


def delete_profile(self):
    if self.running:
        app_main.messagebox.showwarning("Execução ativa", "Não é possível excluir perfis durante uma execução.")
        return
    profile = self.active_profile
    if not profile:
        app_main.messagebox.showwarning("Perfil", "Selecione um perfil primeiro.")
        return
    if not app_main.messagebox.askyesno("Excluir perfil", f"Excluir '{profile.name}'? As listas serão preservadas."):
        return
    self.profiles = [item for item in self.profiles if item.id != profile.id]
    self.active_profile_id = self.profiles[0].id if self.profiles else None
    self.profile_var.set(self.active_profile.name if self.active_profile else "")
    self._save_config()
    self.show_profiles()


def show_profiles(self):
    self._set_page("Perfis")
    self._clear()
    panel = self._panel("Perfis de coordenadas", "Perfis são independentes das listas programadas.")
    toolbar = app_main.ttk.Frame(panel, style="Panel.TFrame")
    toolbar.pack(fill="x", pady=(0, 10))
    app_main.ttk.Button(toolbar, text="Novo perfil", command=lambda: self._profile_dialog(), style="Primary.TButton").pack(side="left", padx=(0, 6))
    app_main.ttk.Button(toolbar, text="Editar", command=lambda: self._profile_dialog(self.active_profile) if self.active_profile else app_main.messagebox.showwarning("Perfil", "Selecione um perfil primeiro."), style="Secondary.TButton").pack(side="left", padx=(0, 6))
    app_main.ttk.Button(toolbar, text="Excluir", command=self._delete_profile, style="Danger.TButton").pack(side="left")
    if not self.profiles:
        app_main.ttk.Label(panel, text="Nenhum perfil criado.", style="Muted.TLabel").pack(anchor="w", pady=15)
        return
    for profile in self.profiles:
        selected = profile.id == self.active_profile_id
        row = app_main.ttk.Frame(panel, style="Panel2.TFrame", padding=11)
        row.pack(fill="x", pady=4)
        text = (
            f"{'● ' if selected else ''}{profile.name}\n"
            f"{profile.application} | {profile.monitor} | {profile.resolution} | {profile.scale}\n"
            f"{self._profile_compatibility_text(profile)}"
        )
        app_main.ttk.Label(row, text=text, style="Body.TLabel").pack(side="left", fill="x", expand=True)
        app_main.ttk.Button(row, text="Selecionar", command=lambda item=profile: self._activate_profile(item), style="Secondary.TButton").pack(side="right", padx=(5, 0))
        app_main.ttk.Button(row, text="Calibrar", command=lambda item=profile: self._open_profile_calibration(item), style="Orange.TButton").pack(side="right")


def install():
    bootstrap_v22.install_patch()
    cls = app_main.PredixAIRoboListas
    cls._activate_profile = activate_profile
    cls._delete_profile = delete_profile
    cls.show_profiles = show_profiles


if __name__ == "__main__":
    install()
    app_main.main()
