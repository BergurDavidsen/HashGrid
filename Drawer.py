from PIL import Image, ImageDraw


class ImageCreator:
    def draw_image(self, color_list:list, cell_size, grid_size, radius=200):

        # Configurable setting
        columns = grid_size # number of columns in the grid

        # Calculate image size
        rows = (len(color_list) + columns - 1) // columns
        img_width = columns * cell_size
        img_height = rows * cell_size

        # Create image
        img = Image.new("RGB", (img_width, img_height), "white")
        draw = ImageDraw.Draw(img)

        # Draw each block
        for i, color in enumerate(color_list):
            row = i // columns
            col = i % columns
            x0 = col * cell_size
            y0 = row * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size
            draw.rectangle([x0, y0, x1, y1], fill=color)

        return img
