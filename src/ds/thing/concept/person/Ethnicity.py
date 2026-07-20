from ds.thing.concept.CategoryConcept import CategoryConcept


class Ethnicity(CategoryConcept):

    @classmethod
    def list(cls):
        return (
            cls("sinhala"),
            cls("sri_lanka_tamil"),
            cls("ind_and_malaiyaga_tamil"),
            cls("sri_lanka_moor_or_muslim"),
            cls("burgher"),
            cls("malay"),
            cls("sri_lanka_chetty"),
            cls("bharatha"),
            cls("other_eth"),
            cls("veddahs"),
            cls("other"),
            # legacy
            cls("indian_muslim"),
            cls("european"),
            cls("burgher_and_eurasian"),
            cls("low_country_sinhalese"),
            cls("up_country_kandyan_sinhalese"),
        )

    @classmethod
    def map_alias(cls, value):

        return {
            "veddas": "veddahs",
        }
