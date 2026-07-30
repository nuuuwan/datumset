import matplotlib.colors as mcolors


class VisualContrastMixin:

    CONTRAST_LIGHT_TEXT_COLOR = "#ffffff"
    CONTRAST_DARK_TEXT_COLOR = "#111111"
    CONTRAST_LIGHTNESS_THRESHOLD = 0.5

    def _to_linear_rgb_channel(self, channel_value):
        if channel_value <= 0.04045:
            return channel_value / 12.92
        return ((channel_value + 0.055) / 1.055) ** 2.4

    def _get_relative_luminance(self, color):
        red, green, blue = mcolors.to_rgb(color)
        red = self._to_linear_rgb_channel(red)
        green = self._to_linear_rgb_channel(green)
        blue = self._to_linear_rgb_channel(blue)
        return 0.2126 * red + 0.7152 * green + 0.0722 * blue

    def _get_contrast_text_color(self, background_color):
        luminance = self._get_relative_luminance(background_color)
        if luminance > self.CONTRAST_LIGHTNESS_THRESHOLD:
            return self.CONTRAST_DARK_TEXT_COLOR
        return self.CONTRAST_LIGHT_TEXT_COLOR
