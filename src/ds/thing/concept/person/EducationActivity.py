from ds.thing.concept.CategoryConcept import CategoryConcept


class EducationActivity(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            "preschool_education",
            "school_education",
            "degree_or_postgrad",
            "vocational_training",
            "other_education",
            "not_studying",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "degree_or_postgrad": [
                "undergraduate_or_postgraduate_education",
                "degree_or_postgraduate_education",
            ],
            "other_education": [
                "other_educational_activity",
            ],
            "preschool_education": [
                "pre_school",
            ],
            "vocational_training": [
                "vocational_training_or_technical_education",
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "preschool_education": "#D05D38",
            "school_education": "#3840D0",
            "degree_or_postgrad": "#6CD038",
            "vocational_training": "#D03899",
            "other_education": "#cccccc",
            "not_studying": "#cccccc",
        }
