# 🤖 via BuildCategortConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class AdministrativeEntity(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            #
            cls("AssistantGovernmentAgendDivisions"),
            cls("GramaSevakaDivisions"),
            cls("MunicipalCouncils"),
            cls("UrbanCouncils"),
            cls("TownCouncils"),
        ]
