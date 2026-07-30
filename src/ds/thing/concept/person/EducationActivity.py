from ds.thing.concept.CategoryConcept import CategoryConcept


class EducationActivity(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            # 1 - 5
            "preschool_education",
            "school_education",
            "degree_or_postgraduate_education",
            "vocational_training_or_technical_education",
            "other_educational_activity",
            # 6 - 6
            "not_studying",
        ]

    @classmethod
    def map_alias(cls):
        return {
            "preschool_education": ["pre_school"],
            "degree_or_postgraduate_education": [
                "undergraduate_or_postgraduate_education"
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            "preschool_education": "#D05D38",
            "school_education": "#3840D0",
            "degree_or_postgraduate_education": "#6CD038",
            "vocational_training_or_technical_education": "#D03899",
            "other_educational_activity": "#cccccc",
            "not_studying": "#cccccc",
        }
