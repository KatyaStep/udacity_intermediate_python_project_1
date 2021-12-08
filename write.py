"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
from helpers import datetime_to_str
from math import isnan


def write_to_csv(results, filename='data/output-results.csv'):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')

    # TODO: Write the results to a CSV file, following the specification in the instructions.
    with open(filename, 'w', encoding='UTF8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fieldnames)

        for approach in results:
            if approach.neo.name is None:
                name = ''
            else:
                name = approach.neo.name

            if approach.neo.hazardous == 'N' or approach.neo.hazardous == 0:
                potentially_hazardous = False
            if approach.neo.hazardous == 'Y' or approach.neo.hazardous == 1:
                potentially_hazardous = True

            if isnan(float(approach.neo.diameter)):
                diameter = 'nan'
            else:
                diameter = float(approach.neo.diameter)

            data = [approach.time, approach.distance, approach.velocity, approach.neo.designation, name,
                    diameter, potentially_hazardous]

            csv_writer.writerow(data)


def write_to_json(results, filename='data/output-results.json'):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    data = []
    for approach in results:
        if approach.neo.name is None:
            name = ''
        else:
            name = str(approach.neo.name)

        if approach.neo.hazardous == 'N' or approach.neo.hazardous == 0:
            potentially_hazardous = False
        if approach.neo.hazardous == 'Y' or approach.neo.hazardous == 1:
            potentially_hazardous = True

        data.append({
            'datetime_utc': datetime_to_str(approach.time),
            'distance_au': float(approach.distance),
            'velocity_km_s': float(approach.velocity),
            'neo': {
                'designation': str(approach.neo.designation),
                'name': name,
                'diameter_km': float(approach.neo.diameter),
                'potentially_hazardous': potentially_hazardous
            },
        })

    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
