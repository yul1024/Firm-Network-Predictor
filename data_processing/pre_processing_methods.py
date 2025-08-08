"""
数据预处理的部分。

这个工具类构建的目的是:
    - 过于繁重和重复的数据预处理不应该由dataset来进行，而是提前处理好。
    - 以pipeline管理数据处理，保证数据处理的效率和统一。
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
        csv_file_path: str | Path,
        results_dir: str | Path,
    ) -> None:
        """
        将最初始很大的csv文件处理为多个容易操作的jsonl文件。

        构建该方法的原因是原始文件太大，并且部分字段存在问题。

        Args:
            csv_file_path (Union[str, Path]): 原始csv文件的路径。
            results_dir (Union[str, Path]): 要保存处理结果的文件夹。

        Returns:
            None: 保存jsonl文件至指定文件夹。
                即使性能好的机器，这一步也要花半小时。
        """
        results_dir = Path(results_dir)
        for i, chunk in enumerate(pd.read_csv(csv_file_path, chunksize=100000, encoding='utf-8')):
            with jsonlines.open(results_dir / f"{i}.jsonl", mode='w') as writer:
                for record in chunk.to_dict(orient='records'):
                    writer.write(record)

    @staticmethod
    def split_original_csv_file_by_date(
        original_csv_path: str | Path,
        train_data_start_date: int,
        train_data_end_date: int,
        train_data_path: str | Path,
        val_data_path: str | Path,
    ):
        all_data_df = pd.read_csv(original_csv_path)
        df = all_data_df[all_data_df['date'] >= train_data_start_date]
        train_data_df = df[df['date'] <= train_data_end_date]
        valid_data_df = df[df['date'] >= train_data_end_date]
        train_data_df.to_json(train_data_path, orient='records', force_ascii=False)
        valid_data_df.to_json(val_data_path, orient='records', force_ascii=False)

    # ====主要方法。====
    @staticmethod
    def train_val_split(
        jsonl_files_dir: str | Path,
        results_dir: str | Path,
        start_time: int,
        end_time: int,
    ) -> None:
        ...

    # ====工具方法。====
    @staticmethod
    def filter_data_by_time(
        jsonl_files_dir: str | Path,
        results_dir: str | Path,
        start_time: int,
        end_time: int,
    ) -> None:
        """
        筛选指定时间区间的数据。

        这个数据集的特性是:
            - date字段代表时间，数据类型是int。

        Args:
            jsonl_files_dir (Union[str, Path]): 上一步数据的文件夹。
            results_dir (Union[str, Path]): 要保存处理结果的文件夹。
            start_time (int): 最早的时间。
            end_time (int): 最晚的时间。

        Returns:
            None: 复制文件上一步文件夹中的文件，保存筛选结果至指定文件夹。
        """
        jsonl_files_dir = Path(jsonl_files_dir)
        results_dir = Path(results_dir)
        for i, item_path in enumerate(jsonl_files_dir.iterdir()):
            if item_path.is_file() and item_path.suffix == '.jsonl':
                df = pd.read_json(item_path, lines=True)
                df_ = df[df['date'] >= start_time]
                df_ = df_[df_['date'] <= end_time]
                df_.to_json(results_dir / f"{i}.jsonl", orient='records', force_ascii=False)
                print(f"Saved records in {results_dir / f'{i}.jsonl'}")

