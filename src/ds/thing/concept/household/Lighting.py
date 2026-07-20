from ds.thing.concept.CategoryConcept import CategoryConcept


class Lighting(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "electricity_national_electricity_network",
            "electricity_rural_hydro_electricity_projects",
            "kerosene",
            "solar_power",
            "bio_gas",
            "other",
            #
            "electricity_grid",
            "solar_grid",
            "solar_standalone",
            "generator",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "kerosene_lamp": "kerosene",
        }
