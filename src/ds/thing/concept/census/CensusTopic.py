# 🤖 via BuildCategortConceptClass.py
from ds.thing.concept.CategoryConcept import CategoryConcept


class CensusTopic(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            #
            cls("Schedule"),
            cls("DemographicAndPersonalInformation"),
            cls("Name"),
            cls("RelationshipToHeadOfTheHousehold"),
            cls("Sex"),
            #
            cls("DateOfBirth"),
            cls("Age"),
            cls("MaritalStatus"),
            cls("EthnicGroup"),
            cls("Religion"),
            #
            cls("Citizenship"),
            cls("NICNo"),
            cls("StatusOfClergyOrPriest"),
            cls("EducationalCharacteristics"),
            cls("AbilityToSpeakSinhalaAndTamil"),
            #
            cls("AbilityToSpeakEnglish"),
            cls("AbilityToSpeakSinhalaEnglishAndTamil"),
            cls("Literacy"),
            cls("EnglishLiteracy"),
            cls("SinhalaEnglishAndTamilLiteracy"),
            #
            cls("ComputerLiteracy"),
            cls("DigitalLiteracy"),
            cls("EducationalAttainmentOrHighestLevelOf"),
            cls("SchoolAttendanceOrAttendInEducational"),
            cls("VocationalAndApprenticeshipQualification"),
        ]
