from scipy.io import wavfile


class Reader:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        result = wavfile.read(self.filename)
        return result

