"""
基于lightning的模型的定义。

为了兼容性:
    - 依然使用通用的torch.nn.Module设计底层模型，在最高层封装为pl.LightningModule。
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.optim as optim
import lightning as pl
import torchmetrics

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class LightningModel(pl.LightningModule):
    def __init__(
        self,
    ):
        super().__init__()

    def forward(
        self,
        inputs,
    ):
        ...

    def training_step(
        self,
        batch,
        batch_idx: int,
    ):
        ...

    def configure_optimizers(
        self,
    ):
        ...

    def validation_step(
        self,
        batch,
        batch_idx: int,
    ):
        ...

