"""
基于原生torch的各种场景的dataset的定义。
"""

from __future__ import annotations

import torch
from torch.utils.data import Dataset
import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class BasicDataset(Dataset):
    def __init__(
        self,
    ):
        ...

    def __len__(
        self
    ) -> int:
        ...

    def __getitem__(
        self,
        index: int
    ) -> dict:
        ...

    def process_data(
        self,
    ) -> torch.Tensor:
        ...

