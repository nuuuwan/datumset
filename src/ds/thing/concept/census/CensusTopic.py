# 🤖 via BuildCategortConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class CensusTopic(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            # 1 - 5
            cls("Schedule"),
            cls("DemographicAndPersonalInformation"),
            cls("Name"),
            cls("RelationshipToHeadOfTheHousehold"),
            cls("Sex"),
            # 6 - 10
            cls("DateOfBirth"),
            cls("Age"),
            cls("MaritalStatus"),
            cls("EthnicGroup"),
            cls("Religion"),
            # 11 - 15
            cls("Citizenship"),
            cls("NICNo"),
            cls("StatusOfClergyOrPriest"),
            cls("EducationalCharacteristics"),
            cls("AbilityToSpeakSinhalaAndTamil"),
            # 16 - 20
            cls("AbilityToSpeakEnglish"),
            cls("AbilityToSpeakSinhalaEnglishAndTamil"),
            cls("Literacy"),
            cls("EnglishLiteracy"),
            cls("SinhalaEnglishAndTamilLiteracy"),
            # 21 - 25
            cls("ComputerLiteracy"),
            cls("DigitalLiteracy"),
            cls("EducationalAttainmentOrHighestLevelOf"),
            cls("SchoolAttendanceOrAttendInEducational"),
            cls("VocationalAndApprenticeshipQualification"),
        ]
