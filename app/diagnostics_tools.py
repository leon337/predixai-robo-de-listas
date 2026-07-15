#!/usr/bin/env python3
"""Diagnóstico, relatórios e atalhos operacionais da V2.4.3."""
from __future__ import annotations

import json
import os
import platform
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path


@dataclass(frozen=True)
class DiagnosticItem:
    name: str
    status: str
    detail: str


def read_version(root_dir: Path) -> str:
    try:
        return (root_dir / "VERSION").read_text(encoding="utf-8").strip() or "desconhecida"
    except OSError:
        return "desconhecida"


def collect_diagnostics(root_dir: Path) -> list[DiagnosticItem]:
    required = [
        root_dir / "app" / "main.py",
        root_dir / "app" / "bootstrap_v23_entry.py",
        root_dir / "run.sh",
        root_dir / "install_desktop.sh",
        root_dir / "VERSION",
    ]
    items = [
        DiagnosticItem("Versão", "PASS", read_version(root_dir)),
        DiagnosticItem("Python", "PASS" if sys.version_info >= (3, 10) else "FAIL", platform.python_version()),
        DiagnosticItem("Sistema", "PASS", f"{platform.system()} {platform.release()} | {platform.machine()}"),
        DiagnosticItem("Diretório do projeto", "PASS" if root_dir.is_dir() else "FAIL", str(root_dir)),
        DiagnosticItem("Configuração", "PASS", str(root_dir / "config")),
        DiagnosticItem("Logs", "PASS", str(root_dir / "logs")),
        DiagnosticItem("Backups", "PASS", str(root_dir / "backups" / "config")),
    ]
    for path in required:
        items.append(DiagnosticItem(f"Arquivo {path.name}", "PASS" if path.is_file() else "FAIL", str(path)))
    for command in ("python3", "xdg-open", "bash", "git"):
        resolved = shutil.which(command)
        items.append(DiagnosticItem(f"Comando {command}", "PASS" if resolved else "WARN", resolved or "não encontrado"))
    return items


def diagnostic_summary(items: list[DiagnosticItem]) -> str:
    failures = sum(item.status == "FAIL" for item in items)
    warnings = sum(item.status == "WARN" for item in items)
    if failures:
        return f"FAIL — {failures} falha(s), {warnings} aviso(s)"
    if warnings:
        return f"WARN — {warnings} aviso(s)"
    return "PASS — ambiente aprovado"


def export_diagnostic_report(root_dir: Path, items: list[DiagnosticItem]) -> Path:
    reports_dir = root_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destination = reports_dir / f"diagnostico_v243_{stamp}.txt"
    lines = [
        "PREDIXAI ROBÔ DE LISTAS — DIAGNÓSTICO V2.4.3",
        f"Gerado em: {datetime.now().isoformat(timespec='seconds')}",
        f"Resumo: {diagnostic_summary(items)}",
        "",
    ]
    lines.extend(f"[{item.status}] {item.name}: {item.detail}" for item in items)
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return destination


def open_path(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    opener = shutil.which("xdg-open")
    if not opener:
        raise RuntimeError("Comando xdg-open não encontrado")
    subprocess.Popen([opener, str(path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def run_installer(root_dir: Path) -> subprocess.CompletedProcess[str]:
    installer = root_dir / "install_desktop.sh"
    if not installer.is_file():
        raise FileNotFoundError(installer)
    return subprocess.run(
        ["bash", str(installer)],
        cwd=root_dir,
        text=True,
        capture_output=True,
        check=False,
        env={**os.environ},
    )


def diagnostics_as_json(items: list[DiagnosticItem]) -> str:
    return json.dumps([asdict(item) for item in items], ensure_ascii=False, indent=2)
