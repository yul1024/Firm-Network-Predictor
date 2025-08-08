"""
基于原生torch的各种场景的dataset的定义。

dataset的职责:
    - 加载数据集。
    - 处理数据，进行必要的转换。
        - 基础的，需要输出是torch.Tensor。

2种实现方法:
    - 预加载: 加载并管理全部的数据。
        - 延迟低，数据处理方便。
        - 需要很大的内容。通常在数据预测任务和文本任务使用。
    - 懒加载: 只加载必要的控制文件，大规模的实际数据会在训练阶段被加载。
        - 可以使用超级大的数据集。通常用于图像、视频等任务。
        - 需要额外的文件管理方法。
        - 数据处理需要提前在data_processing中做好，需要有多版本管理方法。
"""

from __future__ import annotations

import torch
from torch.utils.data import Dataset
import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class DFDataset(Dataset):
    """
    torch中实现dataset的基础。

    此处的实现:
        - 读取数据由pandas完成。
        - 创建的是可随机读写的dataset。

    更好的实践:
        - 轻数据处理，必要的数据处理由分离的processor工具类实现。
        - 考虑统一的train_dataset和val_dataset加载方法。
    """
    def __init__(
        self,
        df: pd.DataFrame,
    ):
        self.data = df.drop(columns=['target']).values
        self.target = df['target'].values

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index) -> dict:
        return dict(
            target=torch.tensor(self.target[index], dtype=torch.float32),
            data=torch.tensor(self.data[index], dtype=torch.float32)
        )

    def process_data(
        self,
        data,
    ) -> torch.Tensor:
        """
        可以用一个工具类来实现，处理完需要是tensor。
        """

