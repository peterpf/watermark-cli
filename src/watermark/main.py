import argparse
import os
import glob
from pathlib import Path
from watermark import add_repeating_watermark
import logging

log = logging.getLogger(__name__)
logging.basicConfig(encoding="utf-8", level=logging.INFO)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Add a repeating diagonal watermark to an image."
    )
    parser.add_argument("pattern", help="Glop pattern of the input images")
    parser.add_argument("output_folder", help="Path to save the watermarked image")
    parser.add_argument("watermark_text", help="Text to use as the watermark")
    parser.add_argument(
        "--opacity",
        type=float,
        default=0.6,
        help="Opacity of the watermark text (default: 0.6)",
    )
    parser.add_argument(
        "--font_size",
        type=int,
        default=12,
        help="Font size of the watermark text (default: 12)",
    )
    parser.add_argument(
        "--occurrence",
        type=int,
        default=3,
        help="Number of times the text should occur in the image",
    )

    args = parser.parse_args()

    # Ensure output path exists
    output_folder = Path(args.output_folder)
    if not output_folder.exists():
        log.warn(f"The output folder doesn't exist, creating: '{str(output_folder)}'")
        os.makedirs(output_folder)

    for input_filepath in glob.glob(args.pattern):
        input_filepath = Path(input_filepath)
        file_ext = input_filepath.suffix
        filename = input_filepath.stem
        output_filepath = output_folder / f"{filename}{file_ext}"

        add_repeating_watermark(
            input_filepath,
            output_filepath,
            args.watermark_text,
            args.opacity,
            args.font_size,
            args.occurrence,
        )

        log.info(f"writing file: '{output_filepath}'")
