import matplotlib.colors as mcolors


class MapGdfMixin:

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

    def _get_rank_colors(self, values, ctx, cmap):
        sorted_values = ctx["values"]
        rank_by_value = {v: i for i, v in enumerate(sorted_values)}
        max_rank = max(1, len(sorted_values) - 1)
        return [
            mcolors.to_hex(cmap(rank_by_value[v] / max_rank)) for v in values
        ]

    def _get_value_gdf(self, sub_datumset, ctx):
        if self.y_cell_key == "Count":
            region_values = self._get_region_percentages(sub_datumset)
        else:
            region_values = self._get_region_values_for(sub_datumset)
        gdf = self._load_gdf().rename(columns={"id": "region_id"})
        gdf["value"] = gdf.apply(
            lambda row: self._lookup_region_value(row, region_values),
            axis=1,
        )
        gdf = gdf[gdf["value"].notna()].copy()
        cmap = self._get_subfigure_cmap(sub_datumset)
        gdf["color"] = self._get_rank_colors(gdf["value"], ctx, cmap)
        return gdf

    def _get_colored_gdf(self, sub_datumset, ctx):
        if ctx["mode"] == "category":
            return self._get_category_gdf(sub_datumset, ctx)
        return self._get_value_gdf(sub_datumset, ctx)
