from ds.thing.concept.CategoryConcept import CategoryConcept


class LivingQuarters(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("HousingUnit"),
            cls("CollectiveLivingQuarter"),
            cls("NonHousingUnit"),
        ]
