from typing import List
from utils.to_get import ExclusiveEnum as eEnum
from utils.to_get import gval


class abs_CellRelectionPriorityEnum(eEnum):
    RNC = "RNC"
    UtranCell = "UtranCell"
    cellReselectionPriority = "cellReselectionPriority"
    sPrioritySearch1 = "sPrioritySearch1"
    sPrioritySearch2 = "sPrioritySearch2"
    threshServingLow = "threshServingLow"


class abs_CellRelectionPriorityIndex:
    def __init__(self) -> None:
        self.RNC = 0
        self.UtranCell = 1
        self.cellReselectionPriority = 2
        self.sPrioritySearch1 = 3
        self.sPrioritySearch2 = 4
        self.threshServingLow = 5
        self.last_index = 6


class abs_CellRelectionPriority:
    def __init__(
        self,
        RNC: str,
        UtranCell: str,
        cellReselectionPriority: str,
        sPrioritySearch1: str,
        sPrioritySearch2: str,
        threshServingLow: str,
    ) -> None:
        self.RNC = RNC
        self.UtranCell = UtranCell
        self.cellReselectionPriority = cellReselectionPriority
        self.sPrioritySearch1 = sPrioritySearch1
        self.sPrioritySearch2 = sPrioritySearch2
        self.threshServingLow = threshServingLow

    def __str__(self) -> str:
        scr = f"RNC: {self.RNC}" + "\n"
        scr += f"UtranCell: {self.UtranCell}" + "\n"
        scr += f"cellReselectionPriority: {self.cellReselectionPriority}" + "\n"
        scr += f"sPrioritySearch1: {self.sPrioritySearch1}" + "\n"
        scr += f"sPrioritySearch2: {self.sPrioritySearch2}" + "\n"
        scr += f"threshServingLow: {self.threshServingLow}" + "\n"
        return scr

    def get_list(self) -> List[str]:
        return [
            self.RNC,
            self.UtranCell,
            self.cellReselectionPriority,
            self.sPrioritySearch1,
            self.sPrioritySearch2,
            self.threshServingLow,
        ]

    @staticmethod
    def get_header() -> List[str]:
        return [
            "RNC",
            "UtranCell",
            "cellReselectionPriority",
            "sPrioritySearch1",
            "sPrioritySearch2",
            "threshServingLow",
        ]

    @classmethod
    def from_row(cls, row: any, idx: abs_CellRelectionPriorityIndex):
        return cls(
            RNC=gval(row[idx.RNC]),
            UtranCell=gval(row[idx.UtranCell]),
            cellReselectionPriority=gval(row[idx.cellReselectionPriority]),
            sPrioritySearch1=gval(row[idx.sPrioritySearch1]),
            sPrioritySearch2=gval(row[idx.sPrioritySearch2]),
            threshServingLow=gval(row[idx.threshServingLow]),
        )
