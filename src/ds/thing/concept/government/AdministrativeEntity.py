# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class AdministrativeEntity(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("AssistantGovernmentAgendDivisions"),
            cls("GramaSevakaDivisions"),
            cls("MunicipalCouncils"),
            cls("UrbanCouncils"),
            cls("TownCouncils"),
        ]
