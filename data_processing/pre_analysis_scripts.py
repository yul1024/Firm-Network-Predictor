"""
对数据集进行初步分析的方法。

实际操作可以结合多种方法，并且以多种形式，例如jupyter-notebook。
这里仅作为记录。
"""

from __future__ import annotations

import pandas as pd
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class SomePreAnalysisMethods:
    @staticmethod
    def check_df(
        df_path: str | Path,
    ):
        df = pd.read_json(df_path, lines=True)
        print(df.info())
        """
        Columns: 444 entries
        """
        print(df.dtypes)
        """
        dtypes: float64(424), int64(16), object(4)
        """
        print(df.select_dtypes(include=['object']))
        """
        size_grp
        array(['micro', 'nano', 'large', None, 'mega', 'small'], dtype=object)
        iid
        array(['01', None, '00X', '02', 1.0, 2.0, '03', 3.0], dtype=object)
        bidask
        array([1, 0])
        excntry
        array(['USA'], dtype=object)
        curcd
        array(['USD'], dtype=object)
        """

    @staticmethod
    def check_date(
        df_path: str | Path,
    ):
        df = pd.read_json(df_path, lines=True)
        print(type(df.loc[0, 'date']))
        """
        numpy.int64
        """


