from PIL import Image

class Decoder():
    def __init__(self, filename, cell_size, grid_size):
        self.filename = filename
        self.cell_size = cell_size
        self.grid_size = grid_size
        
    def decode_image_to_hash(self, color_map):
        
        img = Image.open(self.filename)
        pixels = img.load()
        img_width, img_height = img.size
        rows = img_height // self.cell_size

        hex_chars = []

        for row in range(rows):
            for col in range(self.grid_size):
                x = col * self.cell_size + self.cell_size // 2
                y = row * self.cell_size + self.cell_size // 2
                rgb = pixels[x, y]

                if rgb not in color_map:
                    raise ValueError(f"Color {rgb} not found in map")

                hex_char = color_map[rgb]
                hex_chars.append(hex_char)

        return ''.join(hex_chars)

