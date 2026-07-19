from ds.thing.concept.CategoryConcept import CategoryConcept


class Lighting(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("electricity_national_electricity_network"),
            cls("electricity_rural_hydro_electricity_projects"),
            cls("kerosene"),
            cls("solar_power"),
            cls("bio_gas"),
            cls("other"),
        ]
