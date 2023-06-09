from typing import List
from utils.to_get import ExclusiveEnum as eEnum
from utils.to_get import gval


class CellToFindEnum(eEnum):
    rbsId = "rbsId"
    numberOfSectors = "numberOfSectors"
    numberOfCarriers = "numberOfCarriers"
    IubName = "IubName"


class CellToFindIndex:
    def __init__(self) -> None:
        self.rbsId = 0
        self.numberOfSectors = 1
        self.numberOfCarriers = 2
        self.IubName = 3
        self.last_index = 4


class CellToFind:
    def __init__(
        self,
        rbsId: str,
        numberOfSectors: str,
        numberOfCarriers: str,
        IubName: str,
    ) -> None:
        self.rbsId = rbsId
        self.numberOfSectors = numberOfSectors
        self.numberOfCarriers = numberOfCarriers
        self.IubName = IubName

    def __str__(self) -> str:
        scr = f"rbsId: {self.rbsId}" + "\n"
        scr += f"numberOfSectors: {self.numberOfSectors}" + "\n"
        scr += f"numberOfCarriers: {self.numberOfCarriers}" + "\n"
        scr += f"IubName: {self.IubName}" + "\n"
        return scr

    def get_list(self) -> List[str]:
        return [
            self.rbsId,
            self.numberOfSectors,
            self.numberOfCarriers,
            self.IubName,
        ]

    @staticmethod
    def get_header() -> List[str]:
        return [
            "rbsId",
            "numberOfSectors",
            "numberOfCarriers",
            "IubName",
        ]

    @classmethod
    def from_row(cls, row: any, idx: CellToFindIndex):
        return cls(
            rbsId=gval(row[idx.rbsId]),
            numberOfSectors=gval(row[idx.numberOfSectors]),
            numberOfCarriers=gval(row[idx.numberOfCarriers]),
            IubName=gval(row[idx.IubName]),
        )
