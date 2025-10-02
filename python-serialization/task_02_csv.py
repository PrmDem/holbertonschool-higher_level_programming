#!/usr/bin/python3

"""CSV to json conversion module.

This module features a convert_csv_to_json method,
which takes a csv file as its sole argument.
"""
import csv
import json


def convert_csv_to_json(csv_file):
    """reads from a csv file before serialising it.

    Args:
        csv_file (str): name of the file to serialise
    """
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        data = list(csv.DictReader(csvfile))

    with open('output.json', mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)
