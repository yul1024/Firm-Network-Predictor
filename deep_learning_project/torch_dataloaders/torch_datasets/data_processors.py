"""
dataset中使用到的processor。
"""

from __future__ import annotations

from pathlib import Path

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import torch


class DataProcessor:
    ...

