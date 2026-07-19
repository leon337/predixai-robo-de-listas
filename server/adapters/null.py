"""Adaptador sem efeitos externos."""

from __future__ import annotations

from dataclasses import dataclass

from server.contracts import AdapterMode, ReasonCode


@dataclass(frozen=True, slots=True)
class NullAdapterResult:
    accepted: bool
    mode: AdapterMode
    reason_code: ReasonCode
    external_effect: bool = False


class NullAdapter:
    mode = AdapterMode.NULL

    def execute(self, _command: object | None = None) -> NullAdapterResult:
        return NullAdapterResult(
            accepted=True,
            mode=self.mode,
            reason_code=ReasonCode.NULL_ADAPTER_ACTIVE,
            external_effect=False,
        )
