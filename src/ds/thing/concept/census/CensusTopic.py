# 🤖 via BuildCategortConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class CensusTopic(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 0 - 4
            cls("Schedule"),
            cls("DemographicAndPersonalInformation"),
            cls("Name"),
            cls("RelationshipToHeadOfTheHousehold"),
            cls("Sex"),
            # 5 - 9
            cls("DateOfBirth"),
            cls("Age"),
            cls("MaritalStatus"),
            cls("EthnicGroup"),
            cls("Religion"),
            # 10 - 14
            cls("Citizenship"),
            cls("NICNo"),
            cls("StatusOfClergyOrPriest"),
            cls("EducationalCharacteristics"),
            cls("AbilityToSpeakSinhalaAndTamil"),
            # 15 - 19
            cls("AbilityToSpeakEnglish"),
            cls("AbilityToSpeakSinhalaEnglishAndTamil"),
            cls("Literacy"),
            cls("EnglishLiteracy"),
            cls("SinhalaEnglishAndTamilLiteracy"),
            # 20 - 24
            cls("ComputerLiteracy"),
            cls("DigitalLiteracy"),
            cls("EducationalAttainmentOrHighestLevelOf"),
            cls("SchoolAttendanceOrAttendInEducational"),
            cls("VocationalAndApprenticeshipQualification"),
        ]
