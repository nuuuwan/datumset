class VisualTitleMixin:

    TITLE_COLOR = "#333333"
    SUBFIGURE_TITLE_FONTSIZE = 14
    SUBFIGURE_TITLE_PAD = 0

    def _get_subfigure_title_text(self, datumset, excluded_dim_keys):
        varying_dim_keys = self._get_varying_dim_keys()
        parts = []
        first_datum = datumset[0]
        for dim_key in first_datum.query.dim_labels:
            if dim_key in excluded_dim_keys or dim_key not in varying_dim_keys:
                continue
            first_value = first_datum.dim_idx[dim_key].get_value()
            if all(
                datum.dim_idx[dim_key].get_value() == first_value
                for datum in datumset
            ):
                display_value = self._format_visual_value(first_value)
                parts.append(f"{dim_key}={display_value}")
        if parts:
            return " & ".join(parts)
        return "All data"

    def _set_subfigure_title(self, sub_ax, sub_datumset):
        if len(self.display_datumsets) <= 1:
            return
        sub_ax.set_title(
            self._get_subfigure_title_text(
                sub_datumset,
                self._excluded_dim_keys(),
            ),
            fontsize=self.SUBFIGURE_TITLE_FONTSIZE,
            pad=self.SUBFIGURE_TITLE_PAD,
        )

    def _set_square_subfigure_title(self, sub_ax, sub_datumset):
        sub_ax.set_box_aspect(1)
        self._set_subfigure_title(sub_ax, sub_datumset)

    def _get_title_text(self):
        query = self.datumset[0].query
        title = f"{query.entity_part} {query.cell_labels[0]}"
        by_part = []
        for dim_key in self.datumset.get_non_singleton_dims():
            by_part.append(dim_key)
        title += " by " + " & ".join(by_part)
        title = title.replace("Person Count", "Population")
        return title

    def _get_subtitle_text(self):
        where_part = []
        for dim_key in self.datumset.get_singleton_dims():
            dim_value = self.datumset[0].dim_idx[dim_key].get_value()
            display_value = self._format_visual_value(dim_value)
            where_part.append(f"{dim_key}={display_value}")
        subtitle = " & ".join(where_part)
        return subtitle

    def _add_title(self, fig):
        text = self._get_title_text()
        fig.text(
            0.5,
            0.95,
            text,
            ha="center",
            va="center",
            fontsize=12 * min((100 / (len(text) + 1)), 2),
            color=self.TITLE_COLOR,
            zorder=6,
        )

    def _add_subtitle(self, fig):
        text = self._get_subtitle_text()
        fig.text(
            0.5,
            0.91,
            text,
            ha="center",
            va="center",
            fontsize=6 * min((100 / (len(text) + 1)), 2),
            color=self.TITLE_COLOR,
            zorder=6,
        )
