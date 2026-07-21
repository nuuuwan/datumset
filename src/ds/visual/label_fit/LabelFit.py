import math

import numpy as np

from ds.visual.label_fit.LabelFitGeomMixin import LabelFitGeomMixin


class LabelFit(LabelFitGeomMixin):

    @staticmethod
    def _ray_dist(cx, cy, dx, dy, edges, span):
        ax, ay, ex, ey = edges
        denom = dx * ey - dy * ex
        valid = np.abs(denom) > 1e-12
        safe = np.where(valid, denom, 1.0)
        t = np.where(
            valid,
            ((ax - cx) * ey - (ay - cy) * ex) / safe,
            np.inf,
        )
        s = np.where(
            valid,
            ((ax - cx) * dy - (ay - cy) * dx) / safe,
            np.inf,
        )
        hit = valid & (t > 1e-9) & (s >= -1e-9) & (s <= 1.0 + 1e-9)
        t_hit = np.where(hit, t, np.inf)
        d = float(t_hit.min())
        return d if np.isfinite(d) else span

    @staticmethod
    def _hw_hh(cx, cy, cos_a, sin_a, edges, span):
        rd = LabelFit._ray_dist
        hw = min(
            rd(cx, cy, cos_a, sin_a, edges, span),
            rd(cx, cy, -cos_a, -sin_a, edges, span),
        )
        hh = min(
            rd(cx, cy, -sin_a, cos_a, edges, span),
            rd(cx, cy, sin_a, -cos_a, edges, span),
        )
        return hw, hh

    @classmethod
    def _coarse_scan(cls, poly, n_angles=18):
        edges = cls._edges(poly)
        b = poly.bounds
        span = max(b[2] - b[0], b[3] - b[1]) * 2
        rp = poly.representative_point()
        px0, py0 = rp.x, rp.y
        results = []
        for i in range(n_angles):
            angle_deg = i * 180.0 / n_angles
            theta = math.radians(angle_deg)
            cos_a, sin_a = math.cos(theta), math.sin(theta)
            hw, hh = cls._hw_hh(px0, py0, cos_a, sin_a, edges, span)
            results.append((4 * hw * hh, angle_deg, px0, py0, 2 * hw, 2 * hh))
        results.sort(reverse=True)
        return results, span

    @classmethod
    def _fine_search(cls, poly, angle_results, span):
        edges = cls._edges(poly)
        candidates = cls._interior_candidates(poly)
        best = list(angle_results[0])
        for _, angle_deg, _, _, _, _ in angle_results[:3]:
            theta = math.radians(angle_deg)
            cos_a, sin_a = math.cos(theta), math.sin(theta)
            for px, py in candidates:
                hw, hh = cls._hw_hh(px, py, cos_a, sin_a, edges, span)
                score = 4 * hw * hh
                if score > best[0]:
                    best = [score, angle_deg, px, py, 2 * hw, 2 * hh]
        return best[2], best[3], best[4], best[5], best[1]

    @staticmethod
    def fit_fontsize(label, rect_w, rect_h, ax, renderer):
        temp = ax.text(0, 0, label, fontsize=12)
        bbox = temp.get_window_extent(renderer=renderer)
        temp.remove()
        axes_bb = ax.get_window_extent(renderer=renderer)
        xlim, ylim = ax.get_xlim(), ax.get_ylim()
        rx = axes_bb.width * rect_w / max(xlim[1] - xlim[0], 1e-9)
        ry = axes_bb.height * rect_h / max(ylim[1] - ylim[0], 1e-9)
        ws = rx / max(bbox.width, 1e-9)
        hs = ry / max(bbox.height, 1e-9)
        return max(4, 12 * min(ws, hs) * 0.65)

    @classmethod
    def best_label_fit(cls, geom):
        poly = cls._largest_polygon(geom)
        angle_results, span = cls._coarse_scan(poly)
        return cls._fine_search(poly, angle_results, span)
