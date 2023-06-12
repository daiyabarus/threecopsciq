from typing import List
from utils.to_get import ExclusiveEnum as eEnum
from utils.to_get import gval


class intraFreqUtranRelationsEnum(eEnum):
    UtranCellID = "UtranCellID"
    Neigh_1 = "Neigh_1"
    Neigh_2 = "Neigh_2"
    Neigh_3 = "Neigh_3"
    Neigh_4 = "Neigh_4"
    Neigh_5 = "Neigh_5"
    Neigh_6 = "Neigh_6"
    Neigh_7 = "Neigh_7"
    Neigh_8 = "Neigh_8"
    Neigh_9 = "Neigh_9"
    Neigh_10 = "Neigh_10"
    Neigh_11 = "Neigh_11"
    Neigh_12 = "Neigh_12"
    Neigh_13 = "Neigh_13"
    Neigh_14 = "Neigh_14"
    Neigh_15 = "Neigh_15"
    Neigh_16 = "Neigh_16"
    Neigh_17 = "Neigh_17"
    Neigh_18 = "Neigh_18"
    Neigh_19 = "Neigh_19"
    Neigh_20 = "Neigh_20"
    Neigh_21 = "Neigh_21"
    Neigh_22 = "Neigh_22"
    Neigh_23 = "Neigh_23"
    Neigh_24 = "Neigh_24"
    Neigh_25 = "Neigh_25"
    Neigh_26 = "Neigh_26"
    Neigh_27 = "Neigh_27"
    Neigh_28 = "Neigh_28"
    Neigh_29 = "Neigh_29"
    Neigh_30 = "Neigh_30"
    Neigh_31 = "Neigh_31"


class intraFreqUtranRelationsIndex:
    def __init__(self) -> None:
        self.UtranCellID = 0
        self.Neigh_1 = 1
        self.Neigh_2 = 2
        self.Neigh_3 = 3
        self.Neigh_4 = 4
        self.Neigh_5 = 5
        self.Neigh_6 = 6
        self.Neigh_7 = 7
        self.Neigh_8 = 8
        self.Neigh_9 = 9
        self.Neigh_10 = 10
        self.Neigh_11 = 11
        self.Neigh_12 = 12
        self.Neigh_13 = 13
        self.Neigh_14 = 14
        self.Neigh_15 = 15
        self.Neigh_16 = 16
        self.Neigh_17 = 17
        self.Neigh_18 = 18
        self.Neigh_19 = 19
        self.Neigh_20 = 20
        self.Neigh_21 = 21
        self.Neigh_22 = 22
        self.Neigh_23 = 23
        self.Neigh_24 = 24
        self.Neigh_25 = 25
        self.Neigh_26 = 26
        self.Neigh_27 = 27
        self.Neigh_28 = 28
        self.Neigh_29 = 29
        self.Neigh_30 = 30
        self.Neigh_31 = 31
        self.last_index = 32


class intraFreqUtranRelations:
    def __init__(
        self,
        UtranCellID: str,
        Neigh_1: str,
        Neigh_2: str,
        Neigh_3: str,
        Neigh_4: str,
        Neigh_5: str,
        Neigh_6: str,
        Neigh_7: str,
        Neigh_8: str,
        Neigh_9: str,
        Neigh_10: str,
        Neigh_11: str,
        Neigh_12: str,
        Neigh_13: str,
        Neigh_14: str,
        Neigh_15: str,
        Neigh_16: str,
        Neigh_17: str,
        Neigh_18: str,
        Neigh_19: str,
        Neigh_20: str,
        Neigh_21: str,
        Neigh_22: str,
        Neigh_23: str,
        Neigh_24: str,
        Neigh_25: str,
        Neigh_26: str,
        Neigh_27: str,
        Neigh_28: str,
        Neigh_29: str,
        Neigh_30: str,
        Neigh_31: str,
    ) -> None:
        self.UtranCellID = UtranCellID
        self.Neigh_1 = Neigh_1
        self.Neigh_2 = Neigh_2
        self.Neigh_3 = Neigh_3
        self.Neigh_4 = Neigh_4
        self.Neigh_5 = Neigh_5
        self.Neigh_6 = Neigh_6
        self.Neigh_7 = Neigh_7
        self.Neigh_8 = Neigh_8
        self.Neigh_9 = Neigh_9
        self.Neigh_10 = Neigh_10
        self.Neigh_11 = Neigh_11
        self.Neigh_12 = Neigh_12
        self.Neigh_13 = Neigh_13
        self.Neigh_14 = Neigh_14
        self.Neigh_15 = Neigh_15
        self.Neigh_16 = Neigh_16
        self.Neigh_17 = Neigh_17
        self.Neigh_18 = Neigh_18
        self.Neigh_19 = Neigh_19
        self.Neigh_20 = Neigh_20
        self.Neigh_21 = Neigh_21
        self.Neigh_22 = Neigh_22
        self.Neigh_23 = Neigh_23
        self.Neigh_24 = Neigh_24
        self.Neigh_25 = Neigh_25
        self.Neigh_26 = Neigh_26
        self.Neigh_27 = Neigh_27
        self.Neigh_28 = Neigh_28
        self.Neigh_29 = Neigh_29
        self.Neigh_30 = Neigh_30
        self.Neigh_31 = Neigh_31

    def __str__(self) -> str:
        scr = f"UtranCellID: {self.UtranCellID}" + "\n"
        scr += f"Neigh_1: {self.Neigh_1}" + "\n"
        scr += f"Neigh_2: {self.Neigh_2}" + "\n"
        scr += f"Neigh_3: {self.Neigh_3}" + "\n"
        scr += f"Neigh_4: {self.Neigh_4}" + "\n"
        scr += f"Neigh_5: {self.Neigh_5}" + "\n"
        scr += f"Neigh_6: {self.Neigh_6}" + "\n"
        scr += f"Neigh_7: {self.Neigh_7}" + "\n"
        scr += f"Neigh_8: {self.Neigh_8}" + "\n"
        scr += f"Neigh_9: {self.Neigh_9}" + "\n"
        scr += f"Neigh_10: {self.Neigh_10}" + "\n"
        scr += f"Neigh_11: {self.Neigh_11}" + "\n"
        scr += f"Neigh_12: {self.Neigh_12}" + "\n"
        scr += f"Neigh_13: {self.Neigh_13}" + "\n"
        scr += f"Neigh_14: {self.Neigh_14}" + "\n"
        scr += f"Neigh_15: {self.Neigh_15}" + "\n"
        scr += f"Neigh_16: {self.Neigh_16}" + "\n"
        scr += f"Neigh_17: {self.Neigh_17}" + "\n"
        scr += f"Neigh_18: {self.Neigh_18}" + "\n"
        scr += f"Neigh_19: {self.Neigh_19}" + "\n"
        scr += f"Neigh_20: {self.Neigh_20}" + "\n"
        scr += f"Neigh_21: {self.Neigh_21}" + "\n"
        scr += f"Neigh_22: {self.Neigh_22}" + "\n"
        scr += f"Neigh_23: {self.Neigh_23}" + "\n"
        scr += f"Neigh_24: {self.Neigh_24}" + "\n"
        scr += f"Neigh_25: {self.Neigh_25}" + "\n"
        scr += f"Neigh_26: {self.Neigh_26}" + "\n"
        scr += f"Neigh_27: {self.Neigh_27}" + "\n"
        scr += f"Neigh_28: {self.Neigh_28}" + "\n"
        scr += f"Neigh_29: {self.Neigh_29}" + "\n"
        scr += f"Neigh_30: {self.Neigh_30}" + "\n"
        scr += f"Neigh_31: {self.Neigh_31}" + "\n"
        return scr

    def get_list(self) -> List[str]:
        return [
            self.UtranCellID,
            self.Neigh_1,
            self.Neigh_2,
            self.Neigh_3,
            self.Neigh_4,
            self.Neigh_5,
            self.Neigh_6,
            self.Neigh_7,
            self.Neigh_8,
            self.Neigh_9,
            self.Neigh_10,
            self.Neigh_11,
            self.Neigh_12,
            self.Neigh_13,
            self.Neigh_14,
            self.Neigh_15,
            self.Neigh_16,
            self.Neigh_17,
            self.Neigh_18,
            self.Neigh_19,
            self.Neigh_20,
            self.Neigh_21,
            self.Neigh_22,
            self.Neigh_23,
            self.Neigh_24,
            self.Neigh_25,
            self.Neigh_26,
            self.Neigh_27,
            self.Neigh_28,
            self.Neigh_29,
            self.Neigh_30,
            self.Neigh_31,
        ]

    @staticmethod
    def get_header() -> List[str]:
        return [
            "UtranCellID",
            "Neigh_1",
            "Neigh_2",
            "Neigh_3",
            "Neigh_4",
            "Neigh_5",
            "Neigh_6",
            "Neigh_7",
            "Neigh_8",
            "Neigh_9",
            "Neigh_10",
            "Neigh_11",
            "Neigh_12",
            "Neigh_13",
            "Neigh_14",
            "Neigh_15",
            "Neigh_16",
            "Neigh_17",
            "Neigh_18",
            "Neigh_19",
            "Neigh_20",
            "Neigh_21",
            "Neigh_22",
            "Neigh_23",
            "Neigh_24",
            "Neigh_25",
            "Neigh_26",
            "Neigh_27",
            "Neigh_28",
            "Neigh_29",
            "Neigh_30",
            "Neigh_31",
        ]

    @classmethod
    def from_row(cls, row: any, idx: intraFreqUtranRelationsIndex):
        return cls(
            UtranCellID=gval(row[idx.UtranCellID]),
            Neigh_1=gval(row[idx.Neigh_1]),
            Neigh_2=gval(row[idx.Neigh_2]),
            Neigh_3=gval(row[idx.Neigh_3]),
            Neigh_4=gval(row[idx.Neigh_4]),
            Neigh_5=gval(row[idx.Neigh_5]),
            Neigh_6=gval(row[idx.Neigh_6]),
            Neigh_7=gval(row[idx.Neigh_7]),
            Neigh_8=gval(row[idx.Neigh_8]),
            Neigh_9=gval(row[idx.Neigh_9]),
            Neigh_10=gval(row[idx.Neigh_10]),
            Neigh_11=gval(row[idx.Neigh_11]),
            Neigh_12=gval(row[idx.Neigh_12]),
            Neigh_13=gval(row[idx.Neigh_13]),
            Neigh_14=gval(row[idx.Neigh_14]),
            Neigh_15=gval(row[idx.Neigh_15]),
            Neigh_16=gval(row[idx.Neigh_16]),
            Neigh_17=gval(row[idx.Neigh_17]),
            Neigh_18=gval(row[idx.Neigh_18]),
            Neigh_19=gval(row[idx.Neigh_19]),
            Neigh_20=gval(row[idx.Neigh_20]),
            Neigh_21=gval(row[idx.Neigh_21]),
            Neigh_22=gval(row[idx.Neigh_22]),
            Neigh_23=gval(row[idx.Neigh_23]),
            Neigh_24=gval(row[idx.Neigh_24]),
            Neigh_25=gval(row[idx.Neigh_25]),
            Neigh_26=gval(row[idx.Neigh_26]),
            Neigh_27=gval(row[idx.Neigh_27]),
            Neigh_28=gval(row[idx.Neigh_28]),
            Neigh_29=gval(row[idx.Neigh_29]),
            Neigh_30=gval(row[idx.Neigh_30]),
            Neigh_31=gval(row[idx.Neigh_31]),
        )
