import math
import typer
from rich import print
from pathlib import Path

from FileReader import Reader
from Drawer import ImageCreator
from SoundToColor import SoundToColor
from Decoder import Decoder

app = typer.Typer(help="🎵🔵 Generate or decode a color grid image from a WAV file hash.")

# Hardcoded byte length for now
BYTE_SIZE = 450  # Change this if needed
CELL_SIZE = 20   # pixels per cell

@app.command()
def generate(
    filename: Path = typer.Argument(..., exists=True, readable=True, help="Path to the WAV file."),
    output: Path = typer.Option("hash_grid.png", help="Output image file name.")
):
    """
    Generate a color grid image from a WAV file's hash.
    """
    try:
        print(f"[green]📂 Reading file:[/green] {filename}")

        fr = Reader(str(filename))
        hashed_string = fr.hash_file(BYTE_SIZE)

        print(f"[blue]🔢 Hashed string length:[/blue] {len(hashed_string)} hex chars")
        stc = SoundToColor()
        color_list = stc.get_colors_list(hashed_string)

        grid_size = int(math.isqrt(len(hashed_string)))  # Square grid
        print(f"[green]🎨 Generating image ({grid_size}x{grid_size})...[/green]")

        image = ImageCreator().draw_image(color_list=color_list, cell_size=CELL_SIZE, grid_size=grid_size)
        image.save(output)
        image.show()

        print(f"[bold green]✅ Image saved to:[/bold green] {output}")

    except Exception as e:
        print(f"[red]❌ Error:[/red] {e}")
        raise typer.Exit(code=1)

@app.command()
def decode(
    image_path: Path = typer.Argument(..., exists=True, readable=True, help="Path to the hash image.")
):
    """
    Decode a color grid image back to its hash string.
    """
    try:
        print(f"[cyan]🖼️ Decoding image:[/cyan] {image_path}")

        stc = SoundToColor()
        decoder = Decoder(str(image_path), CELL_SIZE, grid_size=math.isqrt(2*BYTE_SIZE))
        hashed = decoder.decode_image_to_hash(stc.rgb_to_hex_map)

        print(f"[bold blue]🔓 Decoded hash:[/bold blue] {hashed}")
        print(f"[bold blue]🧮 Length:[/bold blue] {len(hashed)} hex chars")

    except Exception as e:
        print(f"[red]❌ Error:[/red] {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
