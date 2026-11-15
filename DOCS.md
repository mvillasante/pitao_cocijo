# API

The `cocijo` command-line interface. Commands that read rainfall data expect a
CSV with `Fecha` (`YYYY-MM-DD`) and `mm` columns.

### cocijo update-readme --data-path PATH --template-path PATH --output-path PATH

Renders a README from a Jinja2 template, filling in the five-number summary of the `mm` column.

**Parameters**
- `--data-path` (required): CSV file with `Fecha` and `mm` columns.
- `--template-path` (required): Jinja2 template to render.
- `--output-path` (required): path of the file to write.

**Returns**
Exits `0` after writing the file; prints nothing.

**Errors**
Exits non-zero when a required option is missing, the CSV cannot be read, the template cannot be found, or the file cannot be written.

### cocijo write-daily-rain-plot --data-path PATH --output-path PATH

Writes a PNG with one series per year showing daily rainfall in millimetres.

**Parameters**
- `--data-path` (required): CSV file with `Fecha` and `mm` columns.
- `--output-path` (required): path of the PNG to write.

**Returns**
Exits `0` after writing the image; prints nothing.

**Errors**
Exits non-zero when a required option is missing, the CSV cannot be read, or the image cannot be written.

### cocijo write-cumulative-rain-plot --data-path PATH --output-path PATH

Writes a PNG with one series per year showing cumulative rainfall in millimetres.

**Parameters**
- `--data-path` (required): CSV file with `Fecha` and `mm` columns.
- `--output-path` (required): path of the PNG to write.

**Returns**
Exits `0` after writing the image; prints nothing.

**Errors**
Exits non-zero when a required option is missing, the CSV cannot be read, or the image cannot be written.

### cocijo version

Prints the installed version.

**Returns**
The version string, for example `0.1.0`.
