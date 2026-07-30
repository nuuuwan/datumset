from ds.thing.concept.CategoryConcept import CategoryConcept


class Lighting(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "national_grid",
            "rural_hydro",
            "kerosene",
            "solar_power",
            "bio_gas",
            "other",
            "electricity_grid",
            "solar_grid",
            "solar_standalone",
            "generator",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "kerosene": [
                "kerosene_lamp",
            ],
            "national_grid": [
                "electricity_national_electricity_network",
            ],
            "rural_hydro": [
                "electricity_rural_hydro_electricity_projects",
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "national_grid": "#D05D38",
            "rural_hydro": "#3840D0",
            "kerosene": "#6CD038",
            "solar_power": "#D03899",
            "bio_gas": "#38C5D0",
            "other": "#cccccc",
            "electricity_grid": "#D0AF38",
            "solar_grid": "#8238D0",
            "solar_standalone": "#38D056",
            "generator": "#D03847",
        }
