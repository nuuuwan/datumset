from ds.thing.concept.CategoryConcept import CategoryConcept


class Ethnicity(CategoryConcept):

    @classmethod
    def list(cls):
        return (
            cls("Sinhalese"),
            cls("SlTamil"),
            cls("IndTamil"),
            cls("SlMoor"),
            cls("Burgher"),
            cls("Malay"),
            cls("SlChetty"),
            cls("Bharatha"),
            cls("OtherEth"),
            # legacy
            cls("IndianMuslim"),
            cls("European"),
            cls("BurgherAndEurasian"),
            cls("LowCountrySinhalese"),
            cls("UpCountryKandyanSinhalese"),
        )

    @classmethod
    def map_alias(cls, value):
        return {
            "Sri Lanka Chetty": "SlChetty",
            "Other": "OtherEth",
            "Sri Lanka Moor/Muslim": "SlMoor",
            "Sri Lanka Muslim": "SlMoor",
            "Indian Tamil/Malaiyaga Thamilar": "IndTamil",
            "Sri Lanka Tamil": "SlTamil",
            "Indian Tamil": "IndTamil",
        }.get(value, value)
