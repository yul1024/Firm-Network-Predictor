"""
基于原生torch对于模型的定义。

基础依然是基于torch.nn.Module定义的模型。

约定:
    - 在这个位置的是整体模型，为实验需求需要易于变动。
"""

from __future__ import annotations

import torch
import torch.nn as nn

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class Model(nn.Module):
    def __init__(
        self,
    ):
        super().__init__()
        ...

    def forward(
        self,
        inputs: torch.Tensor
    ) -> torch.Tensor:
        ...

    def freeze(
        self,
    ) -> None:
        ...

