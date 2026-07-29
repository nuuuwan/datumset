from ds.thing.concept.Concept import Concept


class Party(Concept):
    RAW_COLUMNS = True

    @classmethod
    def __class_getitem__(cls, value):
        return cls(value)

    @classmethod
    def from_value(cls, value):
        return cls(value)

    @classmethod
    def get_color_map(cls):
        return {
            # SLFP family (blue)
            "SLFP": "#00058f",
            "PA": "#00058f",
            "UPFA": "#00058f",
            # UNP family (green)
            "UNP": "#00b10c",
            "NDF": "#00b10c",
            "IND16": "#00b10c",
            "SJB": "#88cc00",
            # SLPP / Rajapaksa (dark red)
            "SLPP": "#9e1420",
            "OPPP": "#880000",
            # SLMP (purple)
            "SLMP": "#880088",
            # Muslim & minority parties (dark green)
            "ACMC": "#004400",
            "MNA": "#004400",
            "NC": "#004400",
            "SLMC": "#004400",
            "NUA": "#004400",
            # Independent groups (light grey)
            "IG": "#e0e0e0",
            "IG2": "#e0e0e0",
            "IG3": "#e0e0e0",
            "DUNF": "#8800ff",
            "SB": "#0088ff",
            # Left / JVP-NPP (red)
            "JVP": "#ff0000",
            "NMPP": "#ff0000",
            "NPP": "#ff0000",
            "NPPT": "#ff0000",
            "MEP": "#ff0000",
            "USA": "#ff0000",
            "SLPF": "#ff0000",
            "DNA": "#ff0000",
            "JJB": "#ff0000",
            "LSSP": "#ff0000",
            "CP": "#ff0000",
            "NSSP": "#ff0000",
            "FSP": "#ff0000",
            "SEP": "#ff0000",
            # Tamil / Eastern militant-origin parties (orange-red)
            "ELMSP": "#ff2200",
            "EPDP": "#ff2200",
            "TMVP": "#ff2200",
            "EROS": "#ff2200",
            # Up-country Tamil (orange)
            "CWC": "#ff4400",
            "UPF": "#ff4400",
            # Buddhist nationalist (amber)
            "SU": "#ffcc00",
            "JHU": "#ffcc00",
            # Tamil nationalist (yellow)
            "AITC": "#ffdd00",
            "ITAK": "#ffdd00",
            "TULF": "#ffdd00",
            "ACTC": "#ffdd00",
            "TMK": "#ffdd00",
            "TMTK": "#ffdd00",
            "IND9": "#ffdd00",
            "ELJP": "#ffffff",
            "INDI": "#ffffff",
        }
