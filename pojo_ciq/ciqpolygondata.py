from typing import List
from utils.to_get import ExclusiveEnum as eEnum
from utils.to_get import gval


class PolygonDataEnum(eEnum):
    Site = "Site"
    Sector = "Sector"
    RNC = "RNC"
    Corner_1Lat = "Corner_1Lat"
    Corner_1Lon = "Corner_1Lon"
    Corner_2Lat = "Corner_2Lat"
    Corner_2Lon = "Corner_2Lon"
    Corner_3Lat = "Corner_3Lat"
    Corner_3Lon = "Corner_3Lon"
    Corner_4Lat = "Corner_4Lat"
    Corner_4Lon = "Corner_4Lon"
    Corner_5Lat = "Corner_5Lat"
    Corner_5Lon = "Corner_5Lon"
    Corner_6Lat = "Corner_6Lat"
    Corner_6Lon = "Corner_6Lon"
    Corner_7Lat = "Corner_7Lat"
    Corner_7Lon = "Corner_7Lon"
    Corner_8Lat = "Corner_8Lat"
    Corner_8Lon = "Corner_8Lon"
    Corner_9Lat = "Corner_9Lat"
    Corner_9Lon = "Corner_9Lon"
    Corner_10Lat = "Corner_10Lat"
    Corner_10Lon = "Corner_10Lon"
    Corner_11Lat = "Corner_11Lat"
    Corner_11Lon = "Corner_11Lon"
    Corner_12Lat = "Corner_12Lat"
    Corner_12Lon = "Corner_12Lon"
    Corner_13Lat = "Corner_13Lat"
    Corner_13Lon = "Corner_13Lon"
    Corner_14Lat = "Corner_14Lat"
    Corner_14Lon = "Corner_14Lon"
    Corner_15Lat = "Corner_15Lat"
    Corner_15Lon = "Corner_15Lon"


class PolygonDataIndex:
    def __init__(self) -> None:
        self.Site = 0
        self.Sector = 1
        self.RNC = 2
        self.Corner_1Lat = 3
        self.Corner_1Lon = 4
        self.Corner_2Lat = 5
        self.Corner_2Lon = 6
        self.Corner_3Lat = 7
        self.Corner_3Lon = 8
        self.Corner_4Lat = 9
        self.Corner_4Lon = 10
        self.Corner_5Lat = 11
        self.Corner_5Lon = 12
        self.Corner_6Lat = 13
        self.Corner_6Lon = 14
        self.Corner_7Lat = 15
        self.Corner_7Lon = 16
        self.Corner_8Lat = 17
        self.Corner_8Lon = 18
        self.Corner_9Lat = 19
        self.Corner_9Lon = 20
        self.Corner_10Lat = 21
        self.Corner_10Lon = 22
        self.Corner_11Lat = 23
        self.Corner_11Lon = 24
        self.Corner_12Lat = 25
        self.Corner_12Lon = 26
        self.Corner_13Lat = 27
        self.Corner_13Lon = 28
        self.Corner_14Lat = 29
        self.Corner_14Lon = 30
        self.Corner_15Lat = 31
        self.Corner_15Lon = 32
        self.last_index = 33


class PolygonData:
    def __init__(
        self,
        Site: str,
        Sector: str,
        RNC: str,
        Corner_1Lat: str,
        Corner_1Lon: str,
        Corner_2Lat: str,
        Corner_2Lon: str,
        Corner_3Lat: str,
        Corner_3Lon: str,
        Corner_4Lat: str,
        Corner_4Lon: str,
        Corner_5Lat: str,
        Corner_5Lon: str,
        Corner_6Lat: str,
        Corner_6Lon: str,
        Corner_7Lat: str,
        Corner_7Lon: str,
        Corner_8Lat: str,
        Corner_8Lon: str,
        Corner_9Lat: str,
        Corner_9Lon: str,
        Corner_10Lat: str,
        Corner_10Lon: str,
        Corner_11Lat: str,
        Corner_11Lon: str,
        Corner_12Lat: str,
        Corner_12Lon: str,
        Corner_13Lat: str,
        Corner_13Lon: str,
        Corner_14Lat: str,
        Corner_14Lon: str,
        Corner_15Lat: str,
        Corner_15Lon: str,
    ) -> None:
        self.Site = Site
        self.Sector = Sector
        self.RNC = RNC
        self.Corner_1Lat = Corner_1Lat
        self.Corner_1Lon = Corner_1Lon
        self.Corner_2Lat = Corner_2Lat
        self.Corner_2Lon = Corner_2Lon
        self.Corner_3Lat = Corner_3Lat
        self.Corner_3Lon = Corner_3Lon
        self.Corner_4Lat = Corner_4Lat
        self.Corner_4Lon = Corner_4Lon
        self.Corner_5Lat = Corner_5Lat
        self.Corner_5Lon = Corner_5Lon
        self.Corner_6Lat = Corner_6Lat
        self.Corner_6Lon = Corner_6Lon
        self.Corner_7Lat = Corner_7Lat
        self.Corner_7Lon = Corner_7Lon
        self.Corner_8Lat = Corner_8Lat
        self.Corner_8Lon = Corner_8Lon
        self.Corner_9Lat = Corner_9Lat
        self.Corner_9Lon = Corner_9Lon
        self.Corner_10Lat = Corner_10Lat
        self.Corner_10Lon = Corner_10Lon
        self.Corner_11Lat = Corner_11Lat
        self.Corner_11Lon = Corner_11Lon
        self.Corner_12Lat = Corner_12Lat
        self.Corner_12Lon = Corner_12Lon
        self.Corner_13Lat = Corner_13Lat
        self.Corner_13Lon = Corner_13Lon
        self.Corner_14Lat = Corner_14Lat
        self.Corner_14Lon = Corner_14Lon
        self.Corner_15Lat = Corner_15Lat
        self.Corner_15Lon = Corner_15Lon

    def __str__(self) -> str:
        scr = f"Site: {self.Site}" + "\n"
        scr += f"Sector: {self.Sector}" + "\n"
        scr += f"RNC: {self.RNC}" + "\n"
        scr += f"Corner_1Lat: {self.Corner_1Lat}" + "\n"
        scr += f"Corner_1Lon: {self.Corner_1Lon}" + "\n"
        scr += f"Corner_2Lat: {self.Corner_2Lat}" + "\n"
        scr += f"Corner_2Lon: {self.Corner_2Lon}" + "\n"
        scr += f"Corner_3Lat: {self.Corner_3Lat}" + "\n"
        scr += f"Corner_3Lon: {self.Corner_3Lon}" + "\n"
        scr += f"Corner_4Lat: {self.Corner_4Lat}" + "\n"
        scr += f"Corner_4Lon: {self.Corner_4Lon}" + "\n"
        scr += f"Corner_5Lat: {self.Corner_5Lat}" + "\n"
        scr += f"Corner_5Lon: {self.Corner_5Lon}" + "\n"
        scr += f"Corner_6Lat: {self.Corner_6Lat}" + "\n"
        scr += f"Corner_6Lon: {self.Corner_6Lon}" + "\n"
        scr += f"Corner_7Lat: {self.Corner_7Lat}" + "\n"
        scr += f"Corner_7Lon: {self.Corner_7Lon}" + "\n"
        scr += f"Corner_8Lat: {self.Corner_8Lat}" + "\n"
        scr += f"Corner_8Lon: {self.Corner_8Lon}" + "\n"
        scr += f"Corner_9Lat: {self.Corner_9Lat}" + "\n"
        scr += f"Corner_9Lon: {self.Corner_9Lon}" + "\n"
        scr += f"Corner_10Lat: {self.Corner_10Lat}" + "\n"
        scr += f"Corner_10Lon: {self.Corner_10Lon}" + "\n"
        scr += f"Corner_11Lat: {self.Corner_11Lat}" + "\n"
        scr += f"Corner_11Lon: {self.Corner_11Lon}" + "\n"
        scr += f"Corner_12Lat: {self.Corner_12Lat}" + "\n"
        scr += f"Corner_12Lon: {self.Corner_12Lon}" + "\n"
        scr += f"Corner_13Lat: {self.Corner_13Lat}" + "\n"
        scr += f"Corner_13Lon: {self.Corner_13Lon}" + "\n"
        scr += f"Corner_14Lat: {self.Corner_14Lat}" + "\n"
        scr += f"Corner_14Lon: {self.Corner_14Lon}" + "\n"
        scr += f"Corner_15Lat: {self.Corner_15Lat}" + "\n"
        scr += f"Corner_15Lon: {self.Corner_15Lon}" + "\n"
        return scr

    def get_list(self) -> List[str]:
        return [
            self.Site,
            self.Sector,
            self.RNC,
            self.Corner_1Lat,
            self.Corner_1Lon,
            self.Corner_2Lat,
            self.Corner_2Lon,
            self.Corner_3Lat,
            self.Corner_3Lon,
            self.Corner_4Lat,
            self.Corner_4Lon,
            self.Corner_5Lat,
            self.Corner_5Lon,
            self.Corner_6Lat,
            self.Corner_6Lon,
            self.Corner_7Lat,
            self.Corner_7Lon,
            self.Corner_8Lat,
            self.Corner_8Lon,
            self.Corner_9Lat,
            self.Corner_9Lon,
            self.Corner_10Lat,
            self.Corner_10Lon,
            self.Corner_11Lat,
            self.Corner_11Lon,
            self.Corner_12Lat,
            self.Corner_12Lon,
            self.Corner_13Lat,
            self.Corner_13Lon,
            self.Corner_14Lat,
            self.Corner_14Lon,
            self.Corner_15Lat,
            self.Corner_15Lon,
        ]

    @staticmethod
    def get_header() -> List[str]:
        return [
            "Site",
            "Sector",
            "RNC",
            "Corner_1Lat",
            "Corner_1Lon",
            "Corner_2Lat",
            "Corner_2Lon",
            "Corner_3Lat",
            "Corner_3Lon",
            "Corner_4Lat",
            "Corner_4Lon",
            "Corner_5Lat",
            "Corner_5Lon",
            "Corner_6Lat",
            "Corner_6Lon",
            "Corner_7Lat",
            "Corner_7Lon",
            "Corner_8Lat",
            "Corner_8Lon",
            "Corner_9Lat",
            "Corner_9Lon",
            "Corner_10Lat",
            "Corner_10Lon",
            "Corner_11Lat",
            "Corner_11Lon",
            "Corner_12Lat",
            "Corner_12Lon",
            "Corner_13Lat",
            "Corner_13Lon",
            "Corner_14Lat",
            "Corner_14Lon",
            "Corner_15Lat",
            "Corner_15Lon",
        ]

    @classmethod
    def from_row(cls, row: any, idx: PolygonDataIndex):
        return cls(
            Site=gval(row[idx.Site]),
            Sector=gval(row[idx.Sector]),
            RNC=gval(row[idx.RNC]),
            Corner_1Lat=gval(row[idx.Corner_1Lat]),
            Corner_1Lon=gval(row[idx.Corner_1Lon]),
            Corner_2Lat=gval(row[idx.Corner_2Lat]),
            Corner_2Lon=gval(row[idx.Corner_2Lon]),
            Corner_3Lat=gval(row[idx.Corner_3Lat]),
            Corner_3Lon=gval(row[idx.Corner_3Lon]),
            Corner_4Lat=gval(row[idx.Corner_4Lat]),
            Corner_4Lon=gval(row[idx.Corner_4Lon]),
            Corner_5Lat=gval(row[idx.Corner_5Lat]),
            Corner_5Lon=gval(row[idx.Corner_5Lon]),
            Corner_6Lat=gval(row[idx.Corner_6Lat]),
            Corner_6Lon=gval(row[idx.Corner_6Lon]),
            Corner_7Lat=gval(row[idx.Corner_7Lat]),
            Corner_7Lon=gval(row[idx.Corner_7Lon]),
            Corner_8Lat=gval(row[idx.Corner_8Lat]),
            Corner_8Lon=gval(row[idx.Corner_8Lon]),
            Corner_9Lat=gval(row[idx.Corner_9Lat]),
            Corner_9Lon=gval(row[idx.Corner_9Lon]),
            Corner_10Lat=gval(row[idx.Corner_10Lat]),
            Corner_10Lon=gval(row[idx.Corner_10Lon]),
            Corner_11Lat=gval(row[idx.Corner_11Lat]),
            Corner_11Lon=gval(row[idx.Corner_11Lon]),
            Corner_12Lat=gval(row[idx.Corner_12Lat]),
            Corner_12Lon=gval(row[idx.Corner_12Lon]),
            Corner_13Lat=gval(row[idx.Corner_13Lat]),
            Corner_13Lon=gval(row[idx.Corner_13Lon]),
            Corner_14Lat=gval(row[idx.Corner_14Lat]),
            Corner_14Lon=gval(row[idx.Corner_14Lon]),
            Corner_15Lat=gval(row[idx.Corner_15Lat]),
            Corner_15Lon=gval(row[idx.Corner_15Lon]),
        )
