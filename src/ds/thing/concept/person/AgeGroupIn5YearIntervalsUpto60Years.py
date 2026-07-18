# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class AgeGroupIn5YearIntervalsUpto60Years(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("00To04Years"),
            cls("05To09Years"),
            cls("1014Years"),
            cls("15To19Years"),
            cls("20To24Years"),
            # 6 - 10
            cls("25To29Years"),
            cls("30To34Years"),
            cls("35To39Years"),
            cls("40To44Years"),
            cls("45To49Years"),
            # 11 - 14
            cls("50To54Years"),
            cls("55To59Years"),
            cls("60To64Years"),
            cls("60YearsAndOver"),
        ]
