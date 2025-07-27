"""
构建pl.Trainer可使用的callback。
"""

from __future__ import annotations

from lightning.pytorch.callbacks import (
    ModelSummary,
    ModelCheckpoint,
    EarlyStopping,
)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from lightning.pytorch.callbacks import Callback


class CallbackFactory:
    @staticmethod
    def create_model_checkpoint_callback(
        callback_kwargs: dict,
    ) -> Callback:
        model_checkpoint_callback = ModelCheckpoint(
            **callback_kwargs,
        )
        return model_checkpoint_callback

    @staticmethod
    def create_early_stopping_callback(
        callback_kwargs: dict,
    ) -> Callback:
        early_stopping_callback = EarlyStopping(
            **callback_kwargs,
        )
        return early_stopping_callback

    @staticmethod
    def create_model_summary_callback(
        callback_kwargs: dict,
    ) -> Callback:
        model_summary_callback = ModelSummary(
            **callback_kwargs
        )
        return model_summary_callback

