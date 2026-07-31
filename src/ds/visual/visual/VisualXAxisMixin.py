from utils_future import String


class VisualXAxisMixin:

    X_TICK_FONTSIZE = 9
    X_TICK_CHAR_WIDTH_RATIO = 0.62

    def _get_renderer(self, fig):
        if self._renderer is None:
            fig.canvas.draw()
            self._renderer = fig.canvas.get_renderer()
        return self._renderer

    def _get_axis_width_px(self, sub_ax):
        renderer = self._get_renderer(sub_ax.figure)
        return sub_ax.get_window_extent(renderer).width

    def _get_px_per_char(self, sub_ax):
        return (
            self.X_TICK_FONTSIZE
            * sub_ax.figure.dpi
            / 72.0
            * self.X_TICK_CHAR_WIDTH_RATIO
        )

    def _format_x_label_text(self, label):
        return str(self._format_visual_value(label))

    def _shorten_x_label(self, sub_ax, label, slot_px):
        char_limit = max(2, int(slot_px / self._get_px_per_char(sub_ax)))
        return String(self._format_x_label_text(label)).shorten(char_limit)

    def _wrap_x_label(self, label, max_chars_per_line):
        words = self._format_x_label_text(label).split()
        lines = []
        current_line = ""
        for word in words:
            candidate = word if not current_line else f"{current_line} {word}"
            if len(candidate) <= max_chars_per_line:
                current_line = candidate
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        return "\n".join(lines)

    def _get_max_chars_per_x_label_line(self, sub_ax, n_labels):
        slot_px = self._get_axis_width_px(sub_ax) / max(n_labels, 1)
        return max(2, int(slot_px / self._get_px_per_char(sub_ax)))

    def _shorten_formatted_x_label(self, sub_ax, label, slot_px):
        char_limit = max(2, int(slot_px / self._get_px_per_char(sub_ax)))
        return String(str(label)).shorten(char_limit)

    def _get_uniform_x_labels(self, sub_ax, x_labels):
        if not x_labels:
            return []
        max_chars = self._get_max_chars_per_x_label_line(
            sub_ax, len(x_labels)
        )
        if not self._can_shorten_dim(self.x_dim_key):
            return [
                self._wrap_x_label(x_label, max_chars) for x_label in x_labels
            ]
        slot_px = self._get_axis_width_px(sub_ax) / len(x_labels)
        return [
            self._shorten_x_label(sub_ax, x_label, slot_px)
            for x_label in x_labels
        ]

    def _set_x_tick_labels(
        self,
        sub_ax,
        ticks,
        display_labels,
        label_colors=None,
        label_half_widths=None,
    ):
        ticks = list(ticks)
        sub_ax.set_xticks(ticks)
        sub_ax.set_xticklabels(
            display_labels,
            fontsize=self.X_TICK_FONTSIZE,
            rotation=0,
            ha="center",
            va="top",
        )
        sub_ax.tick_params(axis="x", pad=6, length=0)
        if label_colors:
            if label_half_widths is None:
                label_half_widths = [
                    self.X_LABEL_UNDERLINE_HALF for _ in ticks
                ]
            self._underline_x_labels(
                sub_ax,
                ticks,
                label_colors,
                label_half_widths,
            )

    def _style_value_axis_subfigure(
        self,
        sub_ax,
        y_cell_key,
        y_limit,
        sub_datumset,
        x_labels=None,
    ):
        sub_ax.set_ylabel(y_cell_key)
        sub_ax.set_ylim(0, y_limit)
        self._format_cell_y_axis(sub_ax, y_cell_key)
        sub_ax.set_box_aspect(self._get_box_aspect())
        if x_labels:
            display_x_labels = self._get_uniform_x_labels(sub_ax, x_labels)
            self._set_x_tick_labels(
                sub_ax,
                range(len(x_labels)),
                display_x_labels,
                self._get_x_label_colors(sub_datumset, x_labels),
            )
        else:
            sub_ax.set_xticks([])
        self._set_subfigure_title(sub_ax, sub_datumset)
