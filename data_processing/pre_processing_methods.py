"""
原始数据集的预处理操作。
"""

from __future__ import annotations

import pandas as pd
import jsonlines
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class PreProcessingMethods:
    # ====主要方法。====
    @staticmethod
    def split_csv_to_jsonl_files(
        path_to_csv: str | Path,
        dir_to_save: str | Path,
    ) -> None:
        """
        将最初始很大的csv文件处理为多个容易操作的jsonl文件。

        构建该方法的原因是原始文件太大，并且部分字段存在问题。

        Args:
            path_to_csv (Union[str, Path]): 原始csv文件的路径。
            dir_to_save (Union[str, Path]): 要保存处理结果的文件夹。

        Returns:
            None: 保存jsonl文件至指定文件夹。
                即使性能好的机器，这一步也要花半小时。
        """
        dir_to_save = Path(dir_to_save)
        for i, chunk in enumerate(pd.read_csv(path_to_csv, chunksize=100000, encoding='utf-8')):
            with jsonlines.open(dir_to_save / f"{i}.jsonl", mode='w') as writer:
                for record in chunk.to_dict(orient='records'):
                    writer.write(record)

    # ====主要方法。====
    @staticmethod
    def train_val_split(
        dir_to_jsonl_files: str | Path,
        dir_to_results: str | Path,
        start_time: int,
        end_time: int,
    ) -> None:
        ...

    # ====工具方法。====
    @staticmethod
    def filter_data_by_time(
        dir_to_jsonl_files: str | Path,
        dir_to_results: str | Path,
        start_time: int,
        end_time: int,
    ) -> None:
        """
        筛选指定时间区间的数据。

        这个数据集的特性是:
            - date字段代表时间，数据类型是int。

        Args:
            dir_to_jsonl_files (Union[str, Path]): 上一步数据的文件夹。
            dir_to_results (Union[str, Path]): 要保存处理结果的文件夹。
            start_time (int): 最早的时间。
            end_time (int): 最晚的时间。

        Returns:
            None: 复制文件上一步文件夹中的文件，保存筛选结果至指定文件夹。
        """
        dir_to_jsonl_files = Path(dir_to_jsonl_files)
        dir_to_results = Path(dir_to_results)
        for i, item_path in enumerate(dir_to_jsonl_files.iterdir()):
            if item_path.is_file() and item_path.suffix == '.jsonl':
                df = pd.read_json(item_path, lines=True)
                df_ = df[df['date'] >= start_time]
                df_ = df_[df_['date'] <= end_time]
                df_.to_json(dir_to_results / f"{i}.jsonl", orient='records', force_ascii=False)
                print(f"Saved records in {dir_to_results / f'{i}.jsonl'}")

