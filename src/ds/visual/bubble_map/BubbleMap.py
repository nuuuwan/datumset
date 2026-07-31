from ds.visual.bubble_map.BubbleMapDrawMixin import BubbleMapDrawMixin
from ds.visual.map.Map import Map


class BubbleMap(BubbleMapDrawMixin, Map):

    BUBBLE_FILL_FRACTION = 0.15

    def _use_count_weights(self):
        return self.y_cell_key == "Count"
