import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

dir = Path(os.path.abspath(__file__)).parent
font_filepath = dir / "Roboto-Medium.ttf"


def add_repeating_watermark(
    input_image_path,
    output_image_path,
    watermark_text,
    opacity=0.3,
    font_size=40,
    occurrences=3,
):
    # Open the original image
    image = Image.open(input_image_path).convert("RGBA")
    width, height = image.size

    # Create a transparent layer for watermark
    watermark = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark)

    # Load a font (adjust path to TTF if needed)
    font = ImageFont.truetype(font_filepath, font_size)  # Ensure arial.ttf is available

    # Calculate diagonal placement of text
    _, _, txt_width, txt_height = draw.textbbox((0, 0), watermark_text, font=font)
    txt_spacing = int(max(txt_height, (height) / occurrences))
    for y in range(-height, height, txt_spacing):  # Move down diagonally
        # for x in range(-width, width, txt_width):  # Move right diagonally
        draw.text(
            ((width - txt_width) / 2, y),
            watermark_text,
            font=font,
            fill=(255, 255, 255, int(255 * opacity)),
        )

    # Rotate the watermark layer
    watermark = watermark.rotate(45, expand=1)
    # watermark = watermark.crop((0, 0, width, height))
    watermark = watermark.resize((width, height), Image.Resampling.LANCZOS)

    # Blend the watermark with the original image
    watermarked_image = Image.alpha_composite(image, watermark)

    # Convert back to RGB and save
    watermarked_image.convert("RGB").save(output_image_path)
