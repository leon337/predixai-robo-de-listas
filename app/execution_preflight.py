#!/usr/bin/env python3
"""Funções puras para classificar sinais antes de iniciar uma sessão."""
from __future__ import annotations

from datetime import datetime
from typing import Iterable, Protocol, TypeVar


class ScheduledSignal(Protocol):
    @property
    def scheduled_at(self) -> datetime: ...


T = TypeVar("T", bound=ScheduledSignal)


def split_signals_by_time(signals: Iterable[T], now: datetime | None = None) -> tuple[list[T], list[T]]:
    """Retorna (expirados, futuros), preservando a ordem recebida."""
    reference = now or datetime.now()
    expired: list[T] = []
    future: list[T] = []
    for signal in signals:
        (expired if signal.scheduled_at < reference else future).append(signal)
    return expired, future
