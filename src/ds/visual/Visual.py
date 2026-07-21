from abc import ABC, abstractmethod

import matplotlib.pyplot as plt


class Visual(ABC):

    FIGSIZE = (9, 9)
    DPI = 100

    def __init__(self, datumset, *params):
        self.datumset = datumset
        self.params = params

    def _excluded_dim_keys(self):
        return set()

    def _build_subtitle(self):
        datum = self.datumset[0]
        entity = datum.entity_class.__name__
        other = [
            f"{k}: {v.get_value()}"
            for k, v in datum.dim_idx.items()
            if k not in self._excluded_dim_keys()
        ]
        return " | ".join([entity] + other)

    @abstractmethod
    def _build_title(self):
        pass

    @abstractmethod
    def _image_path(self):
        pass

    @abstractmethod
    def _plot(self, fig, ax):
        pass

    def draw(self):
        fig, ax = plt.subplots(figsize=self.FIGSIZE, dpi=self.DPI)
        self._plot(fig, ax)
        ax.set_title(self._build_subtitle())
        fig.suptitle(self._build_title())
        fig.tight_layout()
        fig.savefig(self._image_path())
        plt.close(fig)
        return fig
