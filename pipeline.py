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
from pathlib import Path

from data_loaders import load_data
from data_processor import process_data, create_cleaning_report

logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    if verbose: 
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt="%H:%M:%S",
    )
    


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="process data file and export as csv or json")  

    parser.add_argument("--input", "-i", required=True)
    parser.add_argument("--config", "-c", required=True)                # blank 1: the flag name for the config path
    parser.add_argument("--output", "-o", required=True)
    parser.add_argument("--verbose", "-v", action="store_true")          

    return parser.parse_args()


def validate_input(filepath):
    """Check whether the input path exists and is a file."""
    if Path(filepath).is_file():
        logger.info("Input file validated: %s", filepath)     
        return True                                            
    else:
        logger.error("Input file not found: %s", filepath)     
        return False                                         


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

    df_original = data.copy()                                        # blank 4: save a copy of the data before cleaning

    try:
        data = process_data(data, config)                                 # blank 5: process the data (which function, which two arguments?)
    except ValueError:
        sys.exit(1)

    report = create_cleaning_report(df_before=df_original, df_after=data)                                   # blank 6: build the report from the before and after DataFrames
    print(report)                                               # blank 7: print the report

    logger.info(                                              # blank 8: log level for normal progress
        "Processing complete: %d → %d rows", report["rows_before"], report["rows_after"]   # blank 9: rows after, from the report
    )

    data.to_csv(args.output, index=False)                       # blank 10: save the cleaned DataFrame as CSV
    logger.info("Saved cleaned data to %s", args.output)


if __name__ == "__main__":
    main()
