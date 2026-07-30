class AxisFigsizeMixin:

    WIDE_FIGSIZE = (16, 9)
    MAX_NARROW_X_COUNT = 15

    def _get_figsize(self):
        n_x_values = len(self._get_unique_dim_values(self.x_dim_key))
        if n_x_values > self.MAX_NARROW_X_COUNT:
            return self.WIDE_FIGSIZE
        return self.FIGSIZE
