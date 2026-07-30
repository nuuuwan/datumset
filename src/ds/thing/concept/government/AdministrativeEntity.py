from ds.thing.concept.CategoryConcept import CategoryConcept


class AdministrativeEntity(CategoryConcept):

    @classmethod
    def valid_values(cls):
        return [
            'asst_govt_divisions',
            'gs_divisions',
            'municipal_councils',
            'town_councils',
            'urban_councils',
        ]

    @classmethod
    def map_alias(cls):
        return {
            'asst_govt_divisions': [
                'assistant_government_agend_divisions',
            ],
            'gs_divisions': [
                'grama_sevaka_divisions',
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            'asst_govt_divisions': '#D05D38',
            'gs_divisions': '#3840D0',
            'municipal_councils': '#6CD038',
            'town_councils': '#38C5D0',
            'urban_councils': '#D03899',
        }
