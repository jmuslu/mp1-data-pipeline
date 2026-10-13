"""
Data Processing Pipeline - CLI Template
DS 3500 - MP1

Usage:
    python pipeline.py --input data.csv --output clean.csv
    python pipeline.py --input data.csv --output results.json --format json --verbose
"""

import argparse
import logging
import sys

from src import (
    create_cleaning_report,
    load_data,
    process_data,
    save_data,
    setup_logging,
    validate_dataframe,
    validate_input,
)

logger = logging.getLogger(__name__)


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="process data file and export as csv or json")  

    parser.add_argument("--input", "-i", required=True)
    parser.add_argument("--config", "-c", required=True)                # blank 1: the flag name for the config path
    parser.add_argument("--output", "-o", required=True)
    parser.add_argument("--verbose", "-v", action="store_true")          

    return parser.parse_args()


def main():
    """Main pipeline function."""
    args = parse_arguments()                          # blank A: call the function that gives you parsed args

    setup_logging(args.verbose)                             # blank B: which function configures logging, using args.verbose?

    logger.debug(                                   # blank C: which log level for "just recording internal details"?
        "Arguments parsed: input=%s, output=%s", args.input, args.output
    )

    if not validate_input(args.input):                       # blank D: which function checks the input file?
        sys.exit(1)                                 # blank E: which sys function stops the program with an exit code?

    if not validate_input(args.config):                              # blank 2: which path are we validating now?
        sys.exit(1)

    try:
        data = load_data(args.input)
        config = load_data(args.config)                                    # blank 3: load the config, same loader as the data
    except ValueError:
        sys.exit(1)

    # blank 11: read the two lists from the "validation" section of config
    #           (chained brackets, like config["processing"]["missing"])
    required_columns = config["validation"]["required_columns"]
    numeric_columns = config["validation"]["numeric_columns"]
    rows_before_validation = len(data)

    # blank 12: its own try/except; call validate_dataframe with the data and
    #           the two lists, and USE the returned DataFrame (assign to data)
    try:
        data = validate_dataframe(data, required_columns, numeric_columns)
    except ValueError:
        sys.exit(1)

    # blank 13: INFO log: "Validation complete: 100 -> 98 rows"
    logger.info("Validation complete: %d -> %d rows", rows_before_validation, len(data))

    # blank 4 (moved): copy AFTER validation, so the report starts from the
    # validated data (the expected output says rows_before is 98, not 100)
    df_original = data.copy()

    try:
        data = process_data(data, config)
    except ValueError:
        sys.exit(1)

    report = create_cleaning_report(df_before=df_original, df_after=data)

    logger.info(
        "Processing complete: %d → %d rows", report["rows_before"], report["rows_after"]
    )

    # blank 14: replace data.to_csv(...) with the new function (data, args.output)
    save_data(data, args.output)
    logger.info("Saved cleaned data to %s", args.output)

    # blank 15: the assignment says the report print goes LAST in main()
    print(report)


if __name__ == "__main__":
    main()
