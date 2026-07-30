from ds.thing.concept.CategoryConcept import CategoryConcept


class WaterSupplyAvailability(CategoryConcept):
    @classmethod
    def valid_values(cls):
        return [
            'water_all_year',
            'water_shortage',
        ]

    @classmethod
    def map_alias(cls):
        return {
            'water_all_year': [
                'households_with_water_supply_throughout_the_year',
            ],
            'water_shortage': [
                'households_with_no_water_suppply_for_at_least_one_month',
            ],
        }

    @classmethod
    def get_color_map(cls):
        return {
            'water_all_year': '#D05D38',
            'water_shortage': '#3840D0',
        }
