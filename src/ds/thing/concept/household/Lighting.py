from ds.thing.concept.CategoryConcept import CategoryConcept


class Lighting(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("ElectricityNationalElectricityNetwork"),
            cls("ElectricityRuralHydroElectricityProjects"),
            cls("Kerosene"),
            cls("SolarPower"),
            cls("BioGas"),
            cls("Other"),
        ]
