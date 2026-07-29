from collections import defaultdict


class ShapeMapScaleMixin:

    SHAPE_SCALE_FONTSIZE = 9
    SHAPE_SCALE_COLOR = "#555555"
    TILE_NOUN = "shape"

    def _record_shape_values(self, gdf, shapes):
        weights = self._get_region_id_to_weight(gdf)
        counts = defaultdict(int)
        for region_id, _, _ in shapes:
            counts[region_id] += 1
        for region_id, count in counts.items():
            if region_id in weights and count:
                self._shape_values.append(weights[region_id] / count)

    def _get_shape_unit(self):
        entity = self.datumset[0].query.entity_class_names[0]
        return entity.lower() + "s"

    def _get_shape_scale_text(self, value_min, value_max):
        fmt = self._format_humanized_value
        unit = self._get_shape_unit()
        noun = self.TILE_NOUN
        if value_max - value_min < 1:
            return f"1 {noun} = {fmt(value_min, None)} {unit}"
        return (
            f"1 {noun} = {fmt(value_min, None)}"
            + f" to {fmt(value_max, None)} {unit}"
        )

    def _add_shape_scale_note(self, fig):
        if not self._shape_values:
            return
        text = self._get_shape_scale_text(
            min(self._shape_values), max(self._shape_values)
        )
        fig.text(
            0.01,
            0.01,
            text,
            ha="left",
            va="bottom",
            fontsize=self.SHAPE_SCALE_FONTSIZE,
            color=self.SHAPE_SCALE_COLOR,
        )

    def _plot(self, fig, ax):
        self._shape_values = []
        super()._plot(fig, ax)
        self._add_shape_scale_note(fig)
