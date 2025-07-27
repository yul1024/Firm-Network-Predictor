"""
构建pl.Trainer可使用的logger。
"""

from __future__ import annotations

from lightning.pytorch.loggers import (
    CSVLogger,
    TensorBoardLogger,
    WandbLogger,
    MLFlowLogger,
)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from lightning.pytorch.loggers import Logger


class LLoggerBuilder:
    ...


class LLoggerFactory:
    @staticmethod
    def create_logger(
        logger_name: str,
    ) -> Logger:
        ...

    @staticmethod
    def create_csv_logger(
        logger_kwargs: dict,
    ) -> Logger:
        csv_logger = CSVLogger(
            **logger_kwargs,
        )
        return csv_logger

    @staticmethod
    def create_tensorboard_logger(
        logger_kwargs: dict,
    ) -> Logger:
        tensorboard_logger = TensorBoardLogger(
            **logger_kwargs,
        )
        return tensorboard_logger

    @staticmethod
    def create_wandb_logger(
        logger_kwargs: dict,
    ) -> Logger:
        wandb_logger = WandbLogger(
            **logger_kwargs,
        )
        return wandb_logger

    @staticmethod
    def create_mlflow_logger(
        logger_kwargs: dict,
    ) -> Logger:
        mlflow_logger = MLFlowLogger(
            **logger_kwargs,
        )
        return mlflow_logger

