"""
基于原生torch的dataloader的定义。
"""

from __future__ import annotations

from torch.utils.data import DataLoader

from typing import TYPE_CHECKING, Callable
if TYPE_CHECKING:
    from torch.utils.data import Dataset


class DatasetLoaderFactory:
    @staticmethod
    def create_dataloader(
        dataset: Dataset,
        collate_fn: Callable,
        batch_size: int,
        shuffle: bool,
        num_workers: int,
    ) -> DataLoader:
        dataloader = DataLoader(
            dataset=dataset,
            collate_fn=collate_fn,
            batch_size=batch_size,
            shuffle=shuffle,
            num_workers=num_workers,
        )
        return dataloader

