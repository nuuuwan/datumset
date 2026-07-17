from ds.thing.concept.CategoryConcept import CategoryConcept


class Ethnicity(CategoryConcept):
    @classmethod
    def list(cls):
        return [
            cls("Sinhalese"),
            cls("SlTamil"),
            cls("IndTamil"),
            cls("SlMoor"),
            cls("Burgher"),
            cls("Malay"),
            cls("SlChetty"),
            cls("Bharatha"),
            cls("OtherEth"),
        ]
