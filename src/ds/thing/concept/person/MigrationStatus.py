from ds.thing.concept.CategoryConcept import CategoryConcept


class MigrationStatus(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'foreign',
            'local',
            'migrant',
        ]

    @classmethod
    def get_color_map(cls):
        return {
            'foreign': '#3840D0',
            'local': '#D05D38',
            'migrant': '#6CD038',
        }
