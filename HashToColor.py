import colorsys

class HashToColor:
    def __init__(self):
        # Create a colorful and reversible hex-to-RGB mapping using HSV hue rotation
        self.hex_digits = "0123456789abcdef"
        self.hex_color_map = {}

        for i, char in enumerate(self.hex_digits):
            hue = i / 16.0  # evenly spaced hues
            rgb_float = colorsys.hsv_to_rgb(hue, 1, 1)  # full saturation and brightness
            rgb = tuple(int(255 * c) for c in rgb_float)
            self.hex_color_map[char] = rgb

        # Create reverse mapping for decoding
        self.rgb_to_hex_map = {v: k for k, v in self.hex_color_map.items()}

    def get_colors_list(self, hashed_string: str):
        return [self.hex_color_map[char] for char in hashed_string]

    def get_hex_from_rgb(self, rgb):
        return self.rgb_to_hex_map.get(rgb, None)
