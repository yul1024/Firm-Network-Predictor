"""
dataloader会使用的collate_fn。

collate_fn的功能应该具有:
    - 以list进入的独立的值转换为一组。
    - 不同长度的序列使用相关padding方法处理为相同长度。

约定:
    - 区别名称: 进入数据以单数命名，collate_fn处理后的数据以复数命名。
    - 可使用dict。复杂情况，使用dict进行控制。
"""

from __future__ import annotations

import torch
from torch.nn.utils.rnn import pad_sequence

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def collate_fn(batch):
    ...

