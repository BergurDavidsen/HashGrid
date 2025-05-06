class SoundToColor:
    def __init__(self):
        # Use distinct RGB values (each hex maps to a unique shade of gray for example)
        self.hex_color_map = {
            '0': (0, 0, 0),
            '1': (16, 16, 16),
            '2': (32, 32, 32),
            '3': (48, 48, 48),
            '4': (64, 64, 64),
            '5': (80, 80, 80),
            '6': (96, 96, 96),
            '7': (112, 112, 112),
            '8': (128, 128, 128),
            '9': (144, 144, 144),
            'a': (160, 160, 160),
            'b': (176, 176, 176),
            'c': (192, 192, 192),
            'd': (208, 208, 208),
            'e': (224, 224, 224),
            'f': (240, 240, 240)
        }

        # Create reverse mapping for decoding
        self.rgb_to_hex_map = {v: k for k, v in self.hex_color_map.items()}

    def get_colors_list(self, hashed_string: str):
        return [self.hex_color_map[char] for char in hashed_string]

    def get_hex_from_rgb(self, rgb):
        return self.rgb_to_hex_map.get(rgb, None)
