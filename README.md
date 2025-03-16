# Watermark CLI

CLI to quickly add a watermark text to images as a diagonally repeated pattern.

![Example image with watermark text](docs/img/example.jpg)

-----

## Usage

The CLI signature:

```bash
watermark input_glob_pattern output_folder watermark_text --font_size 20 --occurrence 3 --opacity 0.6
```

| Parameter            | Example              | Description                                                                             |
| -------------------- | -------------------- | --------------------------------------------------------------------------------------- |
| `input_glob_pattern` | `some/folder/*.png`  | Glob pattern for input files                                                            |
| `output_folder`      | `some/output/folder` | The folder to store the watermarked images, named like their corresponding input image. |
| `watermark_text`     | `"Your watermark"`   | The text to appear                                                                      |

| Optional arguments | Default | Description                                                 |
| ------------------ | ------- | ----------------------------------------------------------- |
| `--font_size`      | `12`    | The font size of the watermark                              |
| `--occurrence`     | `3`     | The number of times the watermak should appear in the image |
| `--opacity`        | `0.6`   | The opacity of the white watermark text                     |

Following is a full example:

```bash
hatch run python3 src/watermark/main.py --font_size 20 --occurrence 3 "path/to/input_images/*.png" ./path/to/output "© YOURNAME"
```


## Development

### Build

```bash
hatch build
```

## License

`watermark` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
