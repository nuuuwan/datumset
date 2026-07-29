from collections import defaultdict


class HexMapScaleMixin:

    HEX_SCALE_FONTSIZE = 9
    HEX_SCALE_COLOR = "#555555"
    TILE_NOUN = "hexagon"

    def _record_hex_values(self, gdf, hexes):
        weights = self._get_region_id_to_weight(gdf)
        counts = defaultdict(int)
        for region_id, _, _ in hexes:
            counts[region_id] += 1
        for region_id, count in counts.items():
            if region_id in weights and count:
                self._hex_values.append(weights[region_id] / count)

    def _get_hex_unit(self):
        entity = self.datumset[0].query.entity_class_names[0]
        return entity.lower() + "s"

    def _get_hex_scale_text(self, value_min, value_max):
        fmt = self._format_humanized_value
        unit = self._get_hex_unit()
        noun = self.TILE_NOUN
        if value_max - value_min < 1:
            return f"1 {noun} = {fmt(value_min, None)} {unit}"
        return (
            f"1 {noun} = {fmt(value_min, None)}"
            + f" to {fmt(value_max, None)} {unit}"
        )

    def _add_hex_scale_note(self, fig):
        if not self._hex_values:
            return
        text = self._get_hex_scale_text(
            min(self._hex_values), max(self._hex_values)
        )
        fig.text(
            0.01,
            0.01,
            text,
            ha="left",
            va="bottom",
            fontsize=self.HEX_SCALE_FONTSIZE,
            color=self.HEX_SCALE_COLOR,
        )

    def _plot(self, fig, ax):
        self._hex_values = []
        super()._plot(fig, ax)
        self._add_hex_scale_note(fig)
