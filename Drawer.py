from PIL import Image, ImageDraw
import numpy as np
from SoundToRGB import get_rgb_values


class ImageCreator:
    def __init__(self, filename, data, sample_rate, shape):
        self.filename = filename
        self.data = data
        self.sample_rate = sample_rate
        self.shape = shape

    def draw_image(self, shape):

        width, height = self.get_size()

        images = []

        num_samples = len(self.data)
        normalized_x = np.linspace(0, width, num_samples).astype(int)  # Convert to integers for pixel mapping

        for channel_idx in range(self.shape):
            # Create a new image for each channel
            img = Image.new(mode="RGB", size=(width, height), color=(255, 255, 255))
            draw = ImageDraw.Draw(img)

            # Get RGB values for this channel

            channel_data = self.data if self.shape == 1 else self.data[:, channel_idx]
            channel_colors = get_rgb_values(channel_data)

            for i, x in enumerate(normalized_x):
                if x >= width:  # Ensure no out-of-bounds access
                    break
                draw.line(xy=(x, 0, x, height), fill=channel_colors[i], width=1)

            images.append(img)

        return images

    def get_size(self):
        num_samples = len(self.data)
        duration = num_samples // self.sample_rate

        base_size = 400
        factor = 100

        width = base_size + (factor * duration)

        height = base_size

        max_size = 3000
        width = min(width, max_size)
        height = min(height, max_size)

        return width, height
