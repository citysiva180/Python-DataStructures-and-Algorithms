import json
import pandas as pd
import csv

path = r"/Users/shivthedev/Python-DataStructures-and-Algorithms/DataTransformation/data_transform.csv"

# Reading file


def transform_to_json(path):
    json_array = []
    try:
        with open(path, "r") as csv_file:
            csv_dict_reader = csv.DictReader(csv_file, delimiter=",")
            for row in csv_dict_reader:
                json_array.append(row)

        # convert python jsonArray to JSON String and write to file
        with open("output_file.json", 'w', encoding='utf-8') as json_file:
            jsonString = json.dumps(json_array, indent=4)
            json_file.write(jsonString)

    except Exception as e:
        print("The Following error occurred during transformation :  ", e)
    finally:
        print("code just executed check output to confirm on success results")


transform_to_json(path)
