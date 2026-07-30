from utils_future.dcn.DCNUtils import DCNUtils

from ds.visual.map.Map import Map


class Cartogram(Map):

    def _get_colored_gdf(self, sub_datumset, ctx):
        gdf = super()._get_colored_gdf(sub_datumset, ctx)
        weights = self._get_region_id_to_weight(gdf)
        return DCNUtils.run_gdf(gdf, weights)
