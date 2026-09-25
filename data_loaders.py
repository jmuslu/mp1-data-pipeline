# data_loaders.py
from pathlib import Path

import logging
import pandas as pd
import json
import yaml


# Do not call logging.basicConfig() here.
# Use the logging configuration from Part 1.
logger = logging.getLogger(__name__)


def load_csv(filepath):
    """Load a CSV file into a DataFrame.
    filepath is a Path object.
    """
    df = pd.read_csv(filepath)
    logger.info("Loaded CSV file: %s (%d rows)", filepath, df.shape[0])

    return df


def load_json(filepath):
    """Load a JSON file into a Python object (dict or list).
    filepath is a Path object.
    """
    with open(filepath, "r") as f:
        data = json.load(f)
    logger.info("Loaded JSON file: %s", filepath)

    return data
    


def load_yaml(filepath):
    """Load a YAML file into a Python object.
    filepath is a Path object.
    """
    with open(filepath, "r") as f:
        data = yaml.safe_load(f)
    logger.info("Loaded YAML file: %s", filepath)

    return data
    


def load_data(filepath):
    """Load a file based on its extension.
    filepath is a string, such as 'fixtures/sample.csv'
    """
    path = ___                    # blank A: turn the string filepath into a Path object

    ext = ___                     # blank B: get the lowercase file extension from path

    if ext == ".csv":
        return ___(___)           # blank C: call the right loader, passing `path`
    elif ext == ".json":
        return ___(___)           # blank D: same idea, for JSON
    elif ext == ".yaml":
        return ___(___)           # blank E: same idea, for YAML
    else:
        logger.___("...")         # blank F: log at the right level, with a message like
                                   #          "Unsupported file format: .txt"
        raise ___(___)            # blank G: raise the right exception type, with a message
