from FileReader import Reader
import sys
from Drawer import ImageCreator
import numpy as np
import matplotlib.pyplot as plt


def main():
    filename = sys.argv[1]
    new_image_name = filename.split(".")[0] + ".png"
    fr = Reader(filename)

    sample_rate, data = fr.read_file()

    shape = 1

    if len(data.shape) > 1:
        shape = data.shape[1]

    img = ImageCreator(new_image_name, data, sample_rate, shape)

    finals = img.draw_image(data.shape)

    for final in finals:
        final.show()


# x_axis = np.arange(data.shape[0])
# fig, ax = plt.subplots()
# ax.plot(x_axis, data)
# plt.show()


if __name__ == "__main__":
    main()
