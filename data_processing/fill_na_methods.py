"""
填充缺失值的方法。
"""

from __future__ import annotations

import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class FillNAMethods:
    @staticmethod
    def drop_na(
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        ...
