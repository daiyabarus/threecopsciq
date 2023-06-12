from typing import List
from utils.to_get import ExclusiveEnum as eEnum
from utils.to_get import gval


class CellToFindEnum(eEnum):
    rbsId = "rbsId"
    sector_Number = "sector_Number"
    carrier = "carrier"
    cell_Number = "cell_Number"
    cell_Identity = "cell_Identity"
    Utran_CellId = "Utran_CellId"
    cell_Range = "cell_Range"
    output_Power = "output_Power"
    latitudeD = "latitudeD"
    latitude = "latitude"
    lat_Hemisphere = "lat_Hemisphere"
    longitudeD = "longitudeD"
    longitude = "longitude"
    geo_Datum = "geo_Datum"
    beam_Direction = "beam_Direction"
    height = "height"
    tma_Type = "tma_Type"
    internalPower = "internalPower"
    ulGain = "ulGain"
    dlTrafficDelayA = "dlTrafficDelayA"
    ulTrafficDelayA = "ulTrafficDelayA"
    dlTrafficDelayB = "dlTrafficDelayB"
    ulTrafficDelayB = "ulTrafficDelayB"
    dl_Attenuation = "dl_Attenuation"
    antenna_Installed = "antenna_Installed"
    antennaType = "antennaType"
    mechanical_Tilt = "mechanical_Tilt"
    electricalTilt = "electricalTilt"
    freqBand_HiEdge_BranchA = "freqBand_HiEdge_BranchA"
    freqBand_LoEdge_BranchA = "freqBand_LoEdge_BranchA"
    freqBand_HiEdge_BranchB = "freqBand_HiEdge_BranchB"
    freqBand_LoEdgeBranchB = "freqBand_LoEdgeBranchB"
    dlFeeder_Attenuation_BranchA = "dlFeeder_Attenuation_BranchA"
    ulFeeder_Attenuation_BranchA = "ulFeeder_Attenuation_BranchA"
    dlFeeder_Delay_BranchA = "dlFeeder_Delay_BranchA"
    ulFeeder_Delay_BranchA = "ulFeeder_Delay_BranchA"
    dlFeeder_Attenuation_BranchB = "dlFeeder_Attenuation_BranchB"
    ulFeeder_Attenuation_BranchB = "ulFeeder_Attenuation_BranchB"
    dlFeeder_Delay_BranchB = "dlFeeder_Delay_BranchB"
    ulFeeder_Delay_BranchB = "ulFeeder_Delay_BranchB"
    antenna_Supervision = "antenna_Supervision"
    antenna_Supervision_Threshold = "antenna_Supervision_Threshold"
    scrambling_code = "scrambling_code"
    primary_CPICH_Power = "primary_CPICH_Power"
    maximum_Transmission_Power = "maximum_Transmission_Power"
    sib1Plmn_Scope_Value_Tag = "sib1Plmn_Scope_Value_Tag"
    tCell = "tCell"
    uarfcn_Dl = "uarfcn_Dl"
    uarfcn_Ul = "uarfcn_Ul"
    Rx_Diversity = "Rx_Diversity"
    radioBuildingBlock = "radioBuildingBlock"
    usedFreqThresh2dRscp = "usedFreqThresh2dRscp"
    qRxLevMin = "qRxLevMin"
    hoType = "hoType"
    sHcsRat = "sHcsRat"
    MocnCellProfile = "MocnCellProfile"


class CellToFindIndex:
    def __init__(self) -> None:
        self.rbsId = 0
        self.sector_Number = 1
        self.carrier = 2
        self.cell_Number = 3
        self.cell_Identity = 4
        self.Utran_CellId = 5
        self.cell_Range = 6
        self.output_Power = 7
        self.latitudeD = 8
        self.latitude = 9
        self.lat_Hemisphere = 10
        self.longitudeD = 11
        self.longitude = 12
        self.geo_Datum = 13
        self.beam_Direction = 14
        self.height = 15
        self.tma_Type = 16
        self.internalPower = 17
        self.ulGain = 18
        self.dlTrafficDelayA = 19
        self.ulTrafficDelayA = 20
        self.dlTrafficDelayB = 21
        self.ulTrafficDelayB = 22
        self.dl_Attenuation = 23
        self.antenna_Installed = 24
        self.antennaType = 25
        self.mechanical_Tilt = 26
        self.electricalTilt = 27
        self.freqBand_HiEdge_BranchA = 28
        self.freqBand_LoEdge_BranchA = 29
        self.freqBand_HiEdge_BranchB = 30
        self.freqBand_LoEdgeBranchB = 31
        self.dlFeeder_Attenuation_BranchA = 32
        self.ulFeeder_Attenuation_BranchA = 33
        self.dlFeeder_Delay_BranchA = 34
        self.ulFeeder_Delay_BranchA = 35
        self.dlFeeder_Attenuation_BranchB = 36
        self.ulFeeder_Attenuation_BranchB = 37
        self.dlFeeder_Delay_BranchB = 38
        self.ulFeeder_Delay_BranchB = 39
        self.antenna_Supervision = 40
        self.antenna_Supervision_Threshold = 41
        self.scrambling_code = 42
        self.primary_CPICH_Power = 43
        self.maximum_Transmission_Power = 44
        self.sib1Plmn_Scope_Value_Tag = 45
        self.tCell = 46
        self.uarfcn_Dl = 47
        self.uarfcn_Ul = 48
        self.Rx_Diversity = 49
        self.radioBuildingBlock = 50
        self.usedFreqThresh2dRscp = 51
        self.qRxLevMin = 52
        self.hoType = 53
        self.sHcsRat = 54
        self.MocnCellProfile = 55
        self.last_index = 56


class CellToFind:
    def __init__(
        self,
        rbsId: str,
        sector_Number: str,
        carrier: str,
        cell_Number: str,
        cell_Identity: str,
        Utran_CellId: str,
        cell_Range: str,
        output_Power: str,
        latitudeD: str,
        latitude: str,
        lat_Hemisphere: str,
        longitudeD: str,
        longitude: str,
        geo_Datum: str,
        beam_Direction: str,
        height: str,
        tma_Type: str,
        internalPower: str,
        ulGain: str,
        dlTrafficDelayA: str,
        ulTrafficDelayA: str,
        dlTrafficDelayB: str,
        ulTrafficDelayB: str,
        dl_Attenuation: str,
        antenna_Installed: str,
        antennaType: str,
        mechanical_Tilt: str,
        electricalTilt: str,
        freqBand_HiEdge_BranchA: str,
        freqBand_LoEdge_BranchA: str,
        freqBand_HiEdge_BranchB: str,
        freqBand_LoEdgeBranchB: str,
        dlFeeder_Attenuation_BranchA: str,
        ulFeeder_Attenuation_BranchA: str,
        dlFeeder_Delay_BranchA: str,
        ulFeeder_Delay_BranchA: str,
        dlFeeder_Attenuation_BranchB: str,
        ulFeeder_Attenuation_BranchB: str,
        dlFeeder_Delay_BranchB: str,
        ulFeeder_Delay_BranchB: str,
        antenna_Supervision: str,
        antenna_Supervision_Threshold: str,
        scrambling_code: str,
        primary_CPICH_Power: str,
        maximum_Transmission_Power: str,
        sib1Plmn_Scope_Value_Tag: str,
        tCell: str,
        uarfcn_Dl: str,
        uarfcn_Ul: str,
        Rx_Diversity: str,
        radioBuildingBlock: str,
        usedFreqThresh2dRscp: str,
        qRxLevMin: str,
        hoType: str,
        sHcsRat: str,
        MocnCellProfile: str,
    ) -> None:
        self.rbsId = rbsId
        self.sector_Number = sector_Number
        self.carrier = carrier
        self.cell_Number = cell_Number
        self.cell_Identity = cell_Identity
        self.Utran_CellId = Utran_CellId
        self.cell_Range = cell_Range
        self.output_Power = output_Power
        self.latitudeD = latitudeD
        self.latitude = latitude
        self.lat_Hemisphere = lat_Hemisphere
        self.longitudeD = longitudeD
        self.longitude = longitude
        self.geo_Datum = geo_Datum
        self.beam_Direction = beam_Direction
        self.height = height
        self.tma_Type = tma_Type
        self.internalPower = internalPower
        self.ulGain = ulGain
        self.dlTrafficDelayA = dlTrafficDelayA
        self.ulTrafficDelayA = ulTrafficDelayA
        self.dlTrafficDelayB = dlTrafficDelayB
        self.ulTrafficDelayB = ulTrafficDelayB
        self.dl_Attenuation = dl_Attenuation
        self.antenna_Installed = antenna_Installed
        self.antennaType = antennaType
        self.mechanical_Tilt = mechanical_Tilt
        self.electricalTilt = electricalTilt
        self.freqBand_HiEdge_BranchA = freqBand_HiEdge_BranchA
        self.freqBand_LoEdge_BranchA = freqBand_LoEdge_BranchA
        self.freqBand_HiEdge_BranchB = freqBand_HiEdge_BranchB
        self.freqBand_LoEdgeBranchB = freqBand_LoEdgeBranchB
        self.dlFeeder_Attenuation_BranchA = dlFeeder_Attenuation_BranchA
        self.ulFeeder_Attenuation_BranchA = ulFeeder_Attenuation_BranchA
        self.dlFeeder_Delay_BranchA = dlFeeder_Delay_BranchA
        self.ulFeeder_Delay_BranchA = ulFeeder_Delay_BranchA
        self.dlFeeder_Attenuation_BranchB = dlFeeder_Attenuation_BranchB
        self.ulFeeder_Attenuation_BranchB = ulFeeder_Attenuation_BranchB
        self.dlFeeder_Delay_BranchB = dlFeeder_Delay_BranchB
        self.ulFeeder_Delay_BranchB = ulFeeder_Delay_BranchB
        self.antenna_Supervision = antenna_Supervision
        self.antenna_Supervision_Threshold = antenna_Supervision_Threshold
        self.scrambling_code = scrambling_code
        self.primary_CPICH_Power = primary_CPICH_Power
        self.maximum_Transmission_Power = maximum_Transmission_Power
        self.sib1Plmn_Scope_Value_Tag = sib1Plmn_Scope_Value_Tag
        self.tCell = tCell
        self.uarfcn_Dl = uarfcn_Dl
        self.uarfcn_Ul = uarfcn_Ul
        self.Rx_Diversity = Rx_Diversity
        self.radioBuildingBlock = radioBuildingBlock
        self.usedFreqThresh2dRscp = usedFreqThresh2dRscp
        self.qRxLevMin = qRxLevMin
        self.hoType = hoType
        self.sHcsRat = sHcsRat
        self.MocnCellProfile = MocnCellProfile

    def __str__(self) -> str:
        scr = f"rbsId: {self.rbsId}" + "\n"
        scr += f"sector_Number: {self.sector_Number}" + "\n"
        scr += f"carrier: {self.carrier}" + "\n"
        scr += f"cell_Number: {self.cell_Number}" + "\n"
        scr += f"cell_Identity: {self.cell_Identity}" + "\n"
        scr += f"Utran_CellId: {self.Utran_CellId}" + "\n"
        scr += f"cell_Range: {self.cell_Range}" + "\n"
        scr += f"output_Power: {self.output_Power}" + "\n"
        scr += f"latitudeD: {self.latitudeD}" + "\n"
        scr += f"latitude: {self.latitude}" + "\n"
        scr += f"lat_Hemisphere: {self.lat_Hemisphere}" + "\n"
        scr += f"longitudeD: {self.longitudeD}" + "\n"
        scr += f"longitude: {self.longitude}" + "\n"
        scr += f"geo_Datum: {self.geo_Datum}" + "\n"
        scr += f"beam_Direction: {self.beam_Direction}" + "\n"
        scr += f"height: {self.height}" + "\n"
        scr += f"tma_Type: {self.tma_Type}" + "\n"
        scr += f"internalPower: {self.internalPower}" + "\n"
        scr += f"ulGain: {self.ulGain}" + "\n"
        scr += f"dlTrafficDelayA: {self.dlTrafficDelayA}" + "\n"
        scr += f"ulTrafficDelayA: {self.ulTrafficDelayA}" + "\n"
        scr += f"dlTrafficDelayB: {self.dlTrafficDelayB}" + "\n"
        scr += f"ulTrafficDelayB: {self.ulTrafficDelayB}" + "\n"
        scr += f"dl_Attenuation: {self.dl_Attenuation}" + "\n"
        scr += f"antenna_Installed: {self.antenna_Installed}" + "\n"
        scr += f"antennaType: {self.antennaType}" + "\n"
        scr += f"mechanical_Tilt: {self.mechanical_Tilt}" + "\n"
        scr += f"electricalTilt: {self.electricalTilt}" + "\n"
        scr += f"freqBand_HiEdge_BranchA: {self.freqBand_HiEdge_BranchA}" + "\n"
        scr += f"freqBand_LoEdge_BranchA: {self.freqBand_LoEdge_BranchA}" + "\n"
        scr += f"freqBand_HiEdge_BranchB: {self.freqBand_HiEdge_BranchB}" + "\n"
        scr += f"freqBand_LoEdgeBranchB: {self.freqBand_LoEdgeBranchB}" + "\n"
        scr += (
            f"dlFeeder_Attenuation_BranchA: {self.dlFeeder_Attenuation_BranchA}" + "\n"
        )
        scr += (
            f"ulFeeder_Attenuation_BranchA: {self.ulFeeder_Attenuation_BranchA}" + "\n"
        )
        scr += f"dlFeeder_Delay_BranchA: {self.dlFeeder_Delay_BranchA}" + "\n"
        scr += f"ulFeeder_Delay_BranchA: {self.ulFeeder_Delay_BranchA}" + "\n"
        scr += (
            f"dlFeeder_Attenuation_BranchB: {self.dlFeeder_Attenuation_BranchB}" + "\n"
        )
        scr += (
            f"ulFeeder_Attenuation_BranchB: {self.ulFeeder_Attenuation_BranchB}" + "\n"
        )
        scr += f"dlFeeder_Delay_BranchB: {self.dlFeeder_Delay_BranchB}" + "\n"
        scr += f"ulFeeder_Delay_BranchB: {self.ulFeeder_Delay_BranchB}" + "\n"
        scr += f"antenna_Supervision: {self.antenna_Supervision}" + "\n"
        scr += (
            f"antenna_Supervision_Threshold: {self.antenna_Supervision_Threshold}"
            + "\n"
        )
        scr += f"scrambling_code: {self.scrambling_code}" + "\n"
        scr += f"primary_CPICH_Power: {self.primary_CPICH_Power}" + "\n"
        scr += f"maximum_Transmission_Power: {self.maximum_Transmission_Power}" + "\n"
        scr += f"sib1Plmn_Scope_Value_Tag: {self.sib1Plmn_Scope_Value_Tag}" + "\n"
        scr += f"tCell: {self.tCell}" + "\n"
        scr += f"uarfcn_Dl: {self.uarfcn_Dl}" + "\n"
        scr += f"uarfcn_Ul: {self.uarfcn_Ul}" + "\n"
        scr += f"Rx_Diversity: {self.Rx_Diversity}" + "\n"
        scr += f"radioBuildingBlock: {self.radioBuildingBlock}" + "\n"
        scr += f"usedFreqThresh2dRscp: {self.usedFreqThresh2dRscp}" + "\n"
        scr += f"qRxLevMin: {self.qRxLevMin}" + "\n"
        scr += f"hoType: {self.hoType}" + "\n"
        scr += f"sHcsRat: {self.sHcsRat}" + "\n"
        scr += f"MocnCellProfile: {self.MocnCellProfile}" + "\n"
        return scr

    def get_list(self) -> List[str]:
        return [
            self.rbsId,
            self.sector_Number,
            self.carrier,
            self.cell_Number,
            self.cell_Identity,
            self.Utran_CellId,
            self.cell_Range,
            self.output_Power,
            self.latitudeD,
            self.latitude,
            self.lat_Hemisphere,
            self.longitudeD,
            self.longitude,
            self.geo_Datum,
            self.beam_Direction,
            self.height,
            self.tma_Type,
            self.internalPower,
            self.ulGain,
            self.dlTrafficDelayA,
            self.ulTrafficDelayA,
            self.dlTrafficDelayB,
            self.ulTrafficDelayB,
            self.dl_Attenuation,
            self.antenna_Installed,
            self.antennaType,
            self.mechanical_Tilt,
            self.electricalTilt,
            self.freqBand_HiEdge_BranchA,
            self.freqBand_LoEdge_BranchA,
            self.freqBand_HiEdge_BranchB,
            self.freqBand_LoEdgeBranchB,
            self.dlFeeder_Attenuation_BranchA,
            self.ulFeeder_Attenuation_BranchA,
            self.dlFeeder_Delay_BranchA,
            self.ulFeeder_Delay_BranchA,
            self.dlFeeder_Attenuation_BranchB,
            self.ulFeeder_Attenuation_BranchB,
            self.dlFeeder_Delay_BranchB,
            self.ulFeeder_Delay_BranchB,
            self.antenna_Supervision,
            self.antenna_Supervision_Threshold,
            self.scrambling_code,
            self.primary_CPICH_Power,
            self.maximum_Transmission_Power,
            self.sib1Plmn_Scope_Value_Tag,
            self.tCell,
            self.uarfcn_Dl,
            self.uarfcn_Ul,
            self.Rx_Diversity,
            self.radioBuildingBlock,
            self.usedFreqThresh2dRscp,
            self.qRxLevMin,
            self.hoType,
            self.sHcsRat,
            self.MocnCellProfile,
        ]

    @staticmethod
    def get_header() -> List[str]:
        return [
            "rbsId",
            "sector_Number",
            "carrier",
            "cell_Number",
            "cell_Identity",
            "Utran_CellId",
            "cell_Range",
            "output_Power",
            "latitudeD",
            "latitude",
            "lat_Hemisphere",
            "longitudeD",
            "longitude",
            "geo_Datum",
            "beam_Direction",
            "height",
            "tma_Type",
            "internalPower",
            "ulGain",
            "dlTrafficDelayA",
            "ulTrafficDelayA",
            "dlTrafficDelayB",
            "ulTrafficDelayB",
            "dl_Attenuation",
            "antenna_Installed",
            "antennaType",
            "mechanical_Tilt",
            "electricalTilt",
            "freqBand_HiEdge_BranchA",
            "freqBand_LoEdge_BranchA",
            "freqBand_HiEdge_BranchB",
            "freqBand_LoEdgeBranchB",
            "dlFeeder_Attenuation_BranchA",
            "ulFeeder_Attenuation_BranchA",
            "dlFeeder_Delay_BranchA",
            "ulFeeder_Delay_BranchA",
            "dlFeeder_Attenuation_BranchB",
            "ulFeeder_Attenuation_BranchB",
            "dlFeeder_Delay_BranchB",
            "ulFeeder_Delay_BranchB",
            "antenna_Supervision",
            "antenna_Supervision_Threshold",
            "scrambling_code",
            "primary_CPICH_Power",
            "maximum_Transmission_Power",
            "sib1Plmn_Scope_Value_Tag",
            "tCell",
            "uarfcn_Dl",
            "uarfcn_Ul",
            "Rx_Diversity",
            "radioBuildingBlock",
            "usedFreqThresh2dRscp",
            "qRxLevMin",
            "hoType",
            "sHcsRat",
            "MocnCellProfile",
        ]

    @classmethod
    def from_row(cls, row: any, idx: CellToFindIndex):
        return cls(
            rbsId=gval(row[idx.rbsId]),
            sector_Number=gval(row[idx.sector_Number]),
            carrier=gval(row[idx.carrier]),
            cell_Number=gval(row[idx.cell_Number]),
            cell_Identity=gval(row[idx.cell_Identity]),
            Utran_CellId=gval(row[idx.Utran_CellId]),
            cell_Range=gval(row[idx.cell_Range]),
            output_Power=gval(row[idx.output_Power]),
            latitudeD=gval(row[idx.latitudeD]),
            latitude=gval(row[idx.latitude]),
            lat_Hemisphere=gval(row[idx.lat_Hemisphere]),
            longitudeD=gval(row[idx.longitudeD]),
            longitude=gval(row[idx.longitude]),
            geo_Datum=gval(row[idx.geo_Datum]),
            beam_Direction=gval(row[idx.beam_Direction]),
            height=gval(row[idx.height]),
            tma_Type=gval(row[idx.tma_Type]),
            internalPower=gval(row[idx.internalPower]),
            ulGain=gval(row[idx.ulGain]),
            dlTrafficDelayA=gval(row[idx.dlTrafficDelayA]),
            ulTrafficDelayA=gval(row[idx.ulTrafficDelayA]),
            dlTrafficDelayB=gval(row[idx.dlTrafficDelayB]),
            ulTrafficDelayB=gval(row[idx.ulTrafficDelayB]),
            dl_Attenuation=gval(row[idx.dl_Attenuation]),
            antenna_Installed=gval(row[idx.antenna_Installed]),
            antennaType=gval(row[idx.antennaType]),
            mechanical_Tilt=gval(row[idx.mechanical_Tilt]),
            electricalTilt=gval(row[idx.electricalTilt]),
            freqBand_HiEdge_BranchA=gval(row[idx.freqBand_HiEdge_BranchA]),
            freqBand_LoEdge_BranchA=gval(row[idx.freqBand_LoEdge_BranchA]),
            freqBand_HiEdge_BranchB=gval(row[idx.freqBand_HiEdge_BranchB]),
            freqBand_LoEdgeBranchB=gval(row[idx.freqBand_LoEdgeBranchB]),
            dlFeeder_Attenuation_BranchA=gval(row[idx.dlFeeder_Attenuation_BranchA]),
            ulFeeder_Attenuation_BranchA=gval(row[idx.ulFeeder_Attenuation_BranchA]),
            dlFeeder_Delay_BranchA=gval(row[idx.dlFeeder_Delay_BranchA]),
            ulFeeder_Delay_BranchA=gval(row[idx.ulFeeder_Delay_BranchA]),
            dlFeeder_Attenuation_BranchB=gval(row[idx.dlFeeder_Attenuation_BranchB]),
            ulFeeder_Attenuation_BranchB=gval(row[idx.ulFeeder_Attenuation_BranchB]),
            dlFeeder_Delay_BranchB=gval(row[idx.dlFeeder_Delay_BranchB]),
            ulFeeder_Delay_BranchB=gval(row[idx.ulFeeder_Delay_BranchB]),
            antenna_Supervision=gval(row[idx.antenna_Supervision]),
            antenna_Supervision_Threshold=gval(row[idx.antenna_Supervision_Threshold]),
            scrambling_code=gval(row[idx.scrambling_code]),
            primary_CPICH_Power=gval(row[idx.primary_CPICH_Power]),
            maximum_Transmission_Power=gval(row[idx.maximum_Transmission_Power]),
            sib1Plmn_Scope_Value_Tag=gval(row[idx.sib1Plmn_Scope_Value_Tag]),
            tCell=gval(row[idx.tCell]),
            uarfcn_Dl=gval(row[idx.uarfcn_Dl]),
            uarfcn_Ul=gval(row[idx.uarfcn_Ul]),
            Rx_Diversity=gval(row[idx.Rx_Diversity]),
            radioBuildingBlock=gval(row[idx.radioBuildingBlock]),
            usedFreqThresh2dRscp=gval(row[idx.usedFreqThresh2dRscp]),
            qRxLevMin=gval(row[idx.qRxLevMin]),
            hoType=gval(row[idx.hoType]),
            sHcsRat=gval(row[idx.sHcsRat]),
            MocnCellProfile=gval(row[idx.MocnCellProfile]),
        )
