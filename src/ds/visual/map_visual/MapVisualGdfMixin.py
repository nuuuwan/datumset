import matplotlib.colors as mcolors


class MapVisualGdfMixin:

    def _get_category_gdf(self, sub_datumset, ctx):
        winners = self._get_region_winner_category(sub_datumset)
        gdf = self._load_gdf().rename(columns={"id": "region_id"})
        gdf["category"] = gdf.apply(
            lambda row: self._lookup_region_category(row, winners),
            axis=1,
        )
        gdf = gdf[gdf["category"].notna()].copy()
        color_idx = ctx["color_idx"]
        gdf["color"] = gdf["category"].map(
            lambda category: mcolors.to_hex(color_idx[category])
        )
        return gdf

    def _value_to_color(self, value, ctx):
        span = ctx["vmax"] - ctx["vmin"]
        ratio = 0.0 if span == 0 else (value - ctx["vmin"]) / span
        return mcolors.to_hex(ctx["cmap"](ratio))

    def _get_value_gdf(self, sub_datumset, ctx):
        region_values = self._get_region_values_for(sub_datumset)
        gdf = self._load_gdf().rename(columns={"id": "region_id"})
        gdf["value"] = gdf.apply(
            lambda row: self._lookup_region_value(row, region_values),
            axis=1,
        )
        gdf = gdf[gdf["value"].notna()].copy()
        gdf["color"] = gdf["value"].map(
            lambda value: self._value_to_color(value, ctx)
        )
        return gdf

    def _get_colored_gdf(self, sub_datumset, ctx):
        if ctx["mode"] == "category":
            return self._get_category_gdf(sub_datumset, ctx)
        return self._get_value_gdf(sub_datumset, ctx)
