import numpy as np


def get_rgb_values(data):
    data = data.astype(np.int32)
    min_val, max_val = np.min(data), np.max(data)
    normalized = (data - min_val) / (max_val - min_val)

    r = (np.sin(normalized * np.pi * 2) * 127 + 128).astype(int)  # Sine wave for variation
    g = (np.cos(normalized * np.pi * 4) * 127 + 128).astype(int)  # Cosine for complementary variation
    b = ((normalized * 255) % 255).astype(int)  # Simple modulo for blue

    # Combine into RGB tuples
    rgb_colors = [(r[i], g[i], b[i]) for i in range(len(data))]
    return rgb_colors



