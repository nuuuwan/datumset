# 🤖 via BuildCategoryConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class EducationActivity(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("PreschoolEducation"),
            cls("SchoolEducation"),
            cls("DegreeOrPostgraduateEducation"),
            cls("VocationalTrainingOrTechnicalEducation"),
            cls("OtherEducationalActivity"),
            # 6 - 6
            cls("NotStudying"),
        ]
