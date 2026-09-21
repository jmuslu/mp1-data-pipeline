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

logger = logging.getLogger(__name__)


def setup_logging(verbose=False):
    """Configure logging for the pipeline."""
    if verbose: 
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(
        level=level,
        format= "%(asctime)s %(levelname)-8s %(message)s",
        datefmt="%H:%M:%S",
    )
    


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="process data file and export as csv or json")  

    parser.add_argument("--input", "-i", required=True)          
    parser.add_argument("--output", "-o", required=True)         
    parser.add_argument("--format", choices=["csv","json"], default="csv")  
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


if __name__ == "__main__":
    main()
