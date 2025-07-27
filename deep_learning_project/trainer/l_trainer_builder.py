"""
基于lightning构建的trainer。
"""

from __future__ import annotations

from .l_data_module import LDataModule
from .l_model import LModel

import torch
import lightning as pl
from pathlib import Path
from omegaconf import OmegaConf

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class LTrainerBuilder:
    ...

