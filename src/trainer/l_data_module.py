"""
lightning提供的DataModule。

优越性:
    - 自动管理数据，自行控制CPU和GPU的memory。
    - 分布式环境支持。
"""

from __future__ import annotations

import lightning as pl
from torch.utils.data import DataLoader
import torch

from typing import TYPE_CHECKING, Literal
# if TYPE_CHECKING:


class LDataModule(pl.LightningDataModule):
    def __init__(
        self,
    ):
        super().__init__()

    def setup(
        self,
        stage: Literal['fit', 'validate', 'test', 'predict'] = None
    ) -> None:
        ...

    def train_dataloader(
        self,
    ) -> DataLoader:
        ...

    def val_dataloader(
        self,
    ) -> DataLoader:
        ...

    # def test_dataloader(
    #     self,
    # ) -> DataLoader:
    #     ...

    # def predict_dataloader(
    #     self,
    # ) -> DataLoader:
    #     ...

    def teardown(
        self,
        stage: Literal['fit', 'validate', 'test', 'predict'] = None
    ) -> None:
        ...

