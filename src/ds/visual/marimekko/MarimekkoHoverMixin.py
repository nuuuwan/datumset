class MarimekkoHoverMixin:

    HOVER_BBOX = {
        "boxstyle": "round",
        "fc": "#ffffff",
        "ec": "#cccccc",
    }

    def _init_hover(self):
        self._hover_records = []
        self._hover_annotations = {}

    def _add_hover_annotation(self, sub_ax):
        annotation = sub_ax.annotate(
            "",
            xy=(0, 0),
            xytext=(8, 8),
            textcoords="offset points",
            bbox=self.HOVER_BBOX,
            fontsize=7,
        )
        annotation.set_visible(False)
        self._hover_annotations[sub_ax] = annotation

    def _register_hover(self, sub_ax, rect, category, value):
        text = "%s: %s" % (
            self._format_visual_value(category),
            self._format_humanized_value(float(value), None),
        )
        self._hover_records.append((sub_ax, rect, text))

    def _connect_hover(self, fig):
        fig.canvas.mpl_connect(
            "motion_notify_event",
            lambda event: self._on_hover(fig, event),
        )

    def _find_hover_text(self, sub_ax, event):
        for record_ax, rect, text in self._hover_records:
            if record_ax is sub_ax and rect.contains(event)[0]:
                return text
        return None

    def _hide_hover(self, fig, annotation):
        if annotation.get_visible():
            annotation.set_visible(False)
            fig.canvas.draw_idle()

    def _on_hover(self, fig, event):
        sub_ax = event.inaxes
        annotation = self._hover_annotations.get(sub_ax)
        if annotation is None:
            return
        text = self._find_hover_text(sub_ax, event)
        if text is None:
            self._hide_hover(fig, annotation)
            return
        annotation.xy = (event.xdata, event.ydata)
        annotation.set_text(text)
        annotation.set_visible(True)
        fig.canvas.draw_idle()
