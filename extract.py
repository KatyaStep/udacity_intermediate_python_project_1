"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path="data/neos.csv"):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neo_objects = []

    # Load NEO data from the given CSV file.
    with open(neo_csv_path, "r", encoding="utf-8") as csv_file:
        data = csv.DictReader(csv_file)
        for line in data:
            designation = line["pdes"]
            name = line["name"]
            diameter = line["diameter"]
            hazardous = line["pha"]
            neo_objects.append(NearEarthObject(designation, name, diameter, hazardous))

    return neo_objects


def load_approaches(cad_json_path="data/cad.json"):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    close_approaches = []

    # Load close approach data from the given JSON file.
    with open(cad_json_path, encoding="utf-8") as json_file:
        content = json.load(json_file)
        data = content["data"]
        for line in data:
            des = line[0]
            time = line[3]
            distance = line[4]
            velocity = line[7]
            close_approaches.append(
                CloseApproach(
                    designation=des, time=time, distance=distance, velocity=velocity
                )
            )

    return close_approaches
