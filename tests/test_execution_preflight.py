#!/usr/bin/env python3
from __future__ import annotations

import sys
import unittest
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "app"))

from execution_preflight import split_signals_by_time


@dataclass
class FakeSignal:
    scheduled_at: datetime


class ExecutionPreflightTest(unittest.TestCase):
    def test_separa_expirados_e_futuros(self):
        now = datetime(2026, 7, 15, 18, 0, 0)
        signals = [
            FakeSignal(now - timedelta(seconds=1)),
            FakeSignal(now),
            FakeSignal(now + timedelta(minutes=1)),
        ]
        expired, future = split_signals_by_time(signals, now)
        self.assertEqual(expired, [signals[0]])
        self.assertEqual(future, [signals[1], signals[2]])

    def test_lista_totalmente_expirada(self):
        now = datetime(2026, 7, 15, 18, 0, 0)
        signals = [FakeSignal(now - timedelta(minutes=2)), FakeSignal(now - timedelta(seconds=1))]
        expired, future = split_signals_by_time(signals, now)
        self.assertEqual(len(expired), 2)
        self.assertEqual(future, [])


if __name__ == "__main__":
    unittest.main()
