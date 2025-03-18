import argparse
import os
import glob
from pathlib import Path
from watermark import add_repeating_watermark
from tqdm import tqdm
import logging

log = logging.getLogger(__name__)
logging.basicConfig(encoding="utf-8", level=logging.INFO)


def main():
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
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a dry-run: show what will happen without executing any actions",
    )

    args = parser.parse_args()

    dry_run = args.dry_run

    # Ensure output path exists
    output_folder = Path(args.output_folder)
    if not output_folder.exists():
        log.warn(f"The output folder doesn't exist, creating: '{str(output_folder)}'")
        if not dry_run:
            os.makedirs(output_folder)

    matched_input_files = glob.glob(args.pattern)
    if len(matched_input_files) == 0:
        log.info("No input files found for pattern: '%s'", args.pattern)
        return
    matched_input_filepaths = [Path(f) for f in matched_input_files]

    for input_filepath in tqdm(matched_input_filepaths):
        output_filepath = (
            output_folder / f"{input_filepath.stem}{input_filepath.suffix}"
        )

        log.info("Adding watermark to %s", input_filepath)
        if not dry_run:
            add_repeating_watermark(
                input_filepath,
                output_filepath,
                args.watermark_text,
                args.opacity,
                args.font_size,
                args.occurrence,
            )


if __name__ == "__main__":
    main()
