# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class AgeGroupIn5YearIntervalsUpto60Years(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("0004Years"),
            cls("0509Years"),
            cls("1014Years"),
            cls("1519Years"),
            cls("2024Years"),
            # 6 - 10
            cls("2529Years"),
            cls("3034Years"),
            cls("3539Years"),
            cls("4044Years"),
            cls("4549Years"),
            # 11 - 14
            cls("5054Years"),
            cls("5559Years"),
            cls("6064Years"),
            cls("60YearsAndOver"),
        ]
