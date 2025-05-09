# 🎨 HashGrid

**HashGrid** is a simple CLI tool for generating and decoding color grid images based on the cryptographic hash of a file. The resulting image serves as a visual fingerprint of the file and can be used to verify file identity or integrity.

---

## 🔧 Features

* Generate a visually unique, decodable color grid image from any file
* Decode a previously generated image back into its hash
* Uses colorful, reversible encoding (each hex digit maps to a unique color)

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

**Requirements:**

* Python 3.8+
* Pillow
* Typer
* Rich

---

## 🚀 Usage

### Generate Image

```bash
python main.py generate path/to/your/file.ext --output hash_grid.png
```

This will:

* Hash the file using SHAKE-256
* Convert the hex string into colors
* Generate and display a color grid image
* Save the image to `hash_grid.png` (or your provided filename)

### Decode Image

```bash
python main.py decode path/to/hash_grid.png
```

This will:

* Load the image
* Read colors in the grid
* Convert them back into the original hash string

---

## 📁 Example

```bash
python main.py generate example.txt --output myfile_hash.png
python main.py decode myfile_hash.png
```

---

## 📌 Notes

* By default, the hash is 450 bytes (hex string of 900 characters)
* The grid will be approximately square based on the hash length
* This tool supports any file format

---

## 📜 License

MIT License
