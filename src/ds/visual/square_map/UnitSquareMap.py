from ds.visual.square_map.SquareMap import SquareMap


class UnitSquareMap(SquareMap):

    def get_counts(self, region_to_weight):
        return {region_id: 1 for region_id in region_to_weight}

    def _add_hex_scale_note(self, fig):
        pass
