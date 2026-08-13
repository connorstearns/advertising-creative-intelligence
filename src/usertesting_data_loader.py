from dataclasses import dataclass

import pandas as pd

from src.normalization import normalize_frame
from src.usertesting_config import SAMPLE_DIR, TABS


@dataclass
class Workbook:
    tabs: dict[str, pd.DataFrame]
    source_label: str
    warnings: list[str]

    def get(self, name: str) -> pd.DataFrame:
        return self.tabs.get(name, pd.DataFrame())


def load_workbook() -> Workbook:
    tabs: dict[str, pd.DataFrame] = {}
    warnings: list[str] = []
    for tab in TABS:
        path = SAMPLE_DIR / f"{tab}.csv"
        if not path.exists():
            warnings.append(f"Optional UserTesting sample tab '{tab}' is unavailable.")
            continue
        try:
            tabs[tab] = normalize_frame(pd.read_csv(path))
        except Exception as exc:
            warnings.append(f"Could not load UserTesting sample tab '{tab}': {exc}")
    return Workbook(tabs=tabs, source_label="Source: illustrative UserTesting pitch data", warnings=warnings)
