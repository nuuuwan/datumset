from ds.thing.concept.CategoryConcept import CategoryConcept


class AgeGroup(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("LessThan10"),
            cls("10~19"),
            cls("20~29"),
            cls("30~39"),
            cls("40~49"),
            cls("50~59"),
            cls("60~69"),
            cls("70~79"),
            cls("80~89"),
            cls("90AndAbove"),
        ]
