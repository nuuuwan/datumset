from ds.measurement.CategoryMeasurement import CategoryMeasurement


class Religion(CategoryMeasurement):
    @classmethod
    def list(cls):
        return [
            cls("Buddhist"),
            cls("Hindu"),
            cls("Islam"),
            cls("RomanCatholic"),
            cls("OtherChristian"),
            cls("Other"),
        ]
