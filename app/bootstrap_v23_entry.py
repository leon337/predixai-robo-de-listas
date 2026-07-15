#!/usr/bin/env python3
"""Entrada da aplicação com proteções de runtime da V2.4.3."""
from __future__ import annotations

import logging
from pathlib import Path
from tkinter import messagebox

import main as app_main
import bootstrap_v22_entry
import bootstrap_v23
import bootstrap_v231
import bootstrap_v232
import bootstrap_v233
import bootstrap_v233_runtime
import bootstrap_v242
import bootstrap_v243
from runtime_guard import SingleInstanceLock, configure_logging, run_startup_diagnostics

ROOT_DIR = Path(__file__).resolve().parents[1]
RUNTIME_DIR = ROOT_DIR / ".runtime"
LOG_DIR = ROOT_DIR / "logs"


def install() -> None:
    bootstrap_v22_entry.install()
    bootstrap_v23.install_patch()
    bootstrap_v231.install_patch()
    bootstrap_v232.install_patch()
    bootstrap_v233.install_patch()
    bootstrap_v233_runtime.install_patch()
    bootstrap_v242.install_patch()
    bootstrap_v243.install_patch()


def run() -> int:
    logger = configure_logging(LOG_DIR)
    lock = SingleInstanceLock(RUNTIME_DIR / "predixai_robo_listas.lock")

    if not lock.acquire():
        logger.warning("Inicialização bloqueada: outra instância já está ativa.")
        messagebox.showwarning(
            "PredixAI Robô de Listas",
            "Outra instância do aplicativo já está aberta.",
        )
        return 2

    try:
        diagnostics = run_startup_diagnostics(ROOT_DIR)
        if not diagnostics.ok:
            details = "\n".join(diagnostics.messages)
            logger.error("Diagnóstico de inicialização falhou: %s", details)
            messagebox.showerror(
                "Falha na inicialização",
                f"O aplicativo não pode iniciar:\n\n{details}",
            )
            return 1

        install()
        logger.info("Aplicação iniciada com diagnóstico aprovado.")
        app_main.main()
        logger.info("Aplicação encerrada normalmente.")
        return 0
    except Exception:
        logger.exception("Falha não tratada durante a execução.")
        messagebox.showerror(
            "Erro inesperado",
            "A aplicação encontrou um erro. Consulte logs/predixai_robo_listas.log.",
        )
        return 1
    finally:
        lock.release()


if __name__ == "__main__":
    raise SystemExit(run())
