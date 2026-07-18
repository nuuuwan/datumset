# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class HighestEducationLevel2(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("NeverAttendedSchool"),
            cls("StudiedInASpecialSchoolOrSpecialUnit"),
            cls("PassedGrade15"),
            cls("PassedGrade68"),
            cls("PassedGrade910"),
            # 6 - 8
            cls("PassedGceOOrL"),
            cls("PassedGceAOrL"),
            cls("DegreeOrAbove"),
        ]
