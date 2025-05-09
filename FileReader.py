import hashlib


class Reader:
    def __init__(self, filename):
        self.filename = filename

    def hash_file(self, byte_size):
        with open(self.filename, "rb") as f:
            file_bytes = f.read()
        return hashlib.shake_256(file_bytes).hexdigest(byte_size)


