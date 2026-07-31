class AbstractUnitShapeMap:

    def get_counts(self, region_to_weight, value_per_shape=None):
        return {region_id: 1 for region_id in region_to_weight}

    def _add_shape_scale_note(self, fig):
        pass

    def _use_count_weights(self):
        return False
