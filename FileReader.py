import hashlib
from scipy.io import wavfile


class Reader:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        result = wavfile.read(self.filename)
        return result
    def hash_file(self, byte_size):
        
        desired_bytes = byte_size
        
        sample_rate, data = self.read_file()
        data_bytes = data.tobytes()
        combined = f"{sample_rate}".encode() + data_bytes
        return hashlib.shake_256(combined).hexdigest(desired_bytes)


