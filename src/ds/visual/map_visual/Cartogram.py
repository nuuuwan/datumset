from utils_future.dcn.DCNUtils import DCNUtils

from ds.visual.map_visual.MapVisual import MapVisual


class Cartogram(MapVisual):

    def _get_region_id_to_weight(self, gdf):
        totals = self._get_region_totals()
        weights = {}
        for _, row in gdf.iterrows():
            weight = self._lookup_region_value(row, totals)
            if weight is not None:
                weights[row["region_id"]] = weight
        return weights

    def _get_colored_gdf(self, sub_datumset, ctx):
        gdf = super()._get_colored_gdf(sub_datumset, ctx)
        weights = self._get_region_id_to_weight(gdf)
        return DCNUtils.run_gdf(gdf, weights)
