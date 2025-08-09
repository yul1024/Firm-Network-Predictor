"""
原始的数据处理方法。
"""

from __future__ import annotations

import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def main(
    original_data_path: str | Path,
    result_dir: str | Path,
):
    df = pd.read_csv(original_data_path)

    df = df.sort_values(['permno', 'date'], ascending=True)
    df['ret'] = df['ret_exc_lead1m']
    df = df.drop(['ret_exc_lead1m', 'ret_exc', 'ret_lag_dif'], axis=1)
    data = df.dropna(subset=['permno', 'ret']).reset_index(drop=True)
    ret = data[['date', 'permno', 'ret']].copy()


if __name__ == '__main__':
    original_data_path_ = r""
    result_dir_ = r""

    main(
        original_data_path=original_data_path_,
        result_dir=result_dir_,
    )

