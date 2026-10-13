# MP1 Data Pipeline

This pipeline loads a CSV data file, validates it, cleans it, and saves the result, all driven by a YAML configuration file. `pipeline.py` coordinates the workflow from the command line: it checks that the input and config files exist, loads both, validates the data, processes it, saves the cleaned CSV, and prints a cleaning report. The code is organized as a `src/` package. `data_loaders.py` reads CSV, JSON, and YAML files, and `data_validator.py` confirms that the required columns exist and removes rows with non-numeric values in numeric columns. `data_processor.py` removes duplicates, handles missing values, and removes outliers with the IQR method, and it builds the cleaning report. `data_output.py` creates the output folder if needed and saves the DataFrame as a CSV, while `utils.py` holds the logging setup and input-file check. Settings such as the required columns, numeric columns, and outlier threshold live in `config/config.yaml`, so behavior can change without editing the code.

## Example

```bash
python pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose
```

Output:

```text
21:47:18 DEBUG    __main__ — Arguments parsed: input=fixtures/sample_data.csv, output=output/clean.csv
21:47:18 INFO     src.utils — Input file validated: fixtures/sample_data.csv
21:47:18 INFO     src.utils — Input file validated: config/config.yaml
21:47:18 INFO     src.data_loaders — Loaded CSV file: fixtures\sample_data.csv (100 rows)
21:47:18 INFO     src.data_loaders — Loaded YAML file: config\config.yaml
21:47:18 WARNING  src.data_validator — Removed 2 rows with invalid numeric values in rating
21:47:18 DEBUG    src.data_validator — Validation: 100 -> 98 rows
21:47:18 INFO     __main__ — Validation complete: 100 -> 98 rows
21:47:18 DEBUG    src.data_processor — remove_duplicates: 98 → 96 rows
21:47:18 DEBUG    src.data_processor — handle_missing: 96 → 94 rows
21:47:18 DEBUG    src.data_processor — rating: lower=43.625, upper=106.625, removed=2
21:47:18 INFO     __main__ — Processing complete: 98 → 92 rows
21:47:18 DEBUG    src.data_output — Saved 92 rows to output\clean.csv
21:47:18 INFO     __main__ — Saved cleaned data to output/clean.csv
{'rows_before': 98, 'rows_after': 92, 'rows_removed': 6, 'columns_before': 5, 'columns_after': 5, 'columns_removed': 0}
```
