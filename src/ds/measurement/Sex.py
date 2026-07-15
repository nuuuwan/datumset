from ds.measurement.CategoryMeasurement import CategoryMeasurement


class Sex(CategoryMeasurement):
    @classmethod
    def list(cls):
        return [
            cls("Male"),
            cls("Female"),
        ]
