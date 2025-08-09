"""
原始丢弃数据的方法。
"""

from __future__ import annotations

import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def original_drop_data(
    df_path: str,
    result_path: str,
):
    result_path = Path(result_path)
    result_path.parent.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(df_path)
    df = df.dropna(subset=['permno'])
    df = df.drop(
        ['id', 'eom', 'source_crsp', 'size_grp', 'obs_main', 'exch_main', 'ret_local',
         'primary_sec', 'gvkey', 'iid', 'permco', 'excntry', 'curcd', 'fx', 'common', 'comp_tpci',
         'crsp_shrcd', 'comp_exchg', 'crsp_exchcd', 'gics', 'sic', 'adjfct', 'naics'], axis=1
    )
    df.to_csv(result_path, index=False)


if __name__ == '__main__':
    df_path_ = r""
    result_path_ = r""

    original_drop_data(
        df_path=df_path_,
        result_path=result_path_,
    )

