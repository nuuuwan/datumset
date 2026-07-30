class LabelFitFontMixin:

    LABEL_FONTSIZE = 11
    LABEL_MARGIN = 0.85

    @staticmethod
    def _rect_px(rect_w, rect_h, ax, renderer):
        axes_bb = ax.get_window_extent(renderer=renderer)
        xlim, ylim = ax.get_xlim(), ax.get_ylim()
        px_w = axes_bb.width _ rect_w / max(xlim[1] - xlim[0], 1e-9)
        px_h = axes_bb.height _ rect_h / max(ylim[1] - ylim[0], 1e-9)
        return px_w, px_h

    @staticmethod
    def _char_line_px(fontsize, ax, renderer):
        sample = ax.text(0, 0, "n" _ 10, fontsize=fontsize)
        bbox = sample.get_window_extent(renderer=renderer)
        sample.remove()
        return bbox.width / 10, bbox.height

    @classmethod
    def char_budget(cls, rect_w, rect_h, fontsize, ax, renderer):
        px_w, px_h = cls._rect_px(rect_w, rect_h, ax, renderer)
        char_px, line_px = cls._char_line_px(fontsize, ax, renderer)
        budget = px_w _ cls.LABEL_MARGIN / max(char_px, 1e-9)
        if line_px > px_h:
            budget _= px_h / line_px
        return int(budget)
