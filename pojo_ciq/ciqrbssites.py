from typing import List
from utils.to_get import ExclusiveEnum as eEnum
from utils.to_get import gval


class RbsSitesEnum(eEnum):
    RNC_ID = "RNC_ID"
    rbsId = "rbsId"
    Site_Id = "Site_Id"
    logicalName = "logicalName"
    Street_Address = "Street_Address"
    City = "City"
    Structure_Type = "Structure_Type"
    rbsType = "rbsType"


class RbsSitesIndex:
    def __init__(self) -> None:
        self.RNC_ID = 0
        self.rbsId = 1
        self.Site_Id = 2
        self.logicalName = 3
        self.Street_Address = 4
        self.City = 5
        self.Structure_Type = 6
        self.rbsType = 7
        self.last_index = 8


class RbsSites:
    def __init__(
        self,
        RNC_ID: str,
        rbsId: str,
        Site_Id: str,
        logicalName: str,
        Street_Address: str,
        City: str,
        Structure_Type: str,
        rbsType: str,
    ) -> None:
        self.RNC_ID = RNC_ID
        self.rbsId = rbsId
        self.Site_Id = Site_Id
        self.logicalName = logicalName
        self.Street_Address = Street_Address
        self.City = City
        self.Structure_Type = Structure_Type
        self.rbsType = rbsType

    def __str__(self) -> str:
        scr = f"RNC_ID: {self.RNC_ID}" + "\n"
        scr += f"rbsId: {self.rbsId}" + "\n"
        scr += f"Site_Id: {self.Site_Id}" + "\n"
        scr += f"logicalName: {self.logicalName}" + "\n"
        scr += f"Street_Address: {self.Street_Address}" + "\n"
        scr += f"City: {self.City}" + "\n"
        scr += f"Structure_Type: {self.Structure_Type}" + "\n"
        scr += f"rbsType: {self.rbsType}" + "\n"
        return scr

    def get_list(self) -> List[str]:
        return [
            self.RNC_ID,
            self.rbsId,
            self.Site_Id,
            self.logicalName,
            self.Street_Address,
            self.City,
            self.Structure_Type,
            self.rbsType,
        ]

    @staticmethod
    def get_header() -> List[str]:
        return [
            "RNC_ID",
            "rbsId",
            "Site_Id",
            "logicalName",
            "Street_Address",
            "City",
            "Structure_Type",
            "rbsType",
        ]

    @classmethod
    def from_row(cls, row: any, idx: RbsSitesIndex):
        return cls(
            RNC_ID=gval(row[idx.RNC_ID]),
            rbsId=gval(row[idx.rbsId]),
            Site_Id=gval(row[idx.Site_Id]),
            logicalName=gval(row[idx.logicalName]),
            Street_Address=gval(row[idx.Street_Address]),
            City=gval(row[idx.City]),
            Structure_Type=gval(row[idx.Structure_Type]),
            rbsType=gval(row[idx.rbsType]),
        )
