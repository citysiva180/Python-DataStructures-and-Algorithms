import csv
import json
import pandas as pd

path = r"/Users/shivthedev/Python-DataStructures-and-Algorithms/DataTransformation/data_transform.csv"

# Reading file

df = pd.read_csv(path)
category_array = df["CATEGORY"].unique()
print(category_array)

new_dict = {}
for items in category_array:
    new_dict[items] = []

print(new_dict)


def transform_to_json(path, new_dict):
    json_array = []

    json_dict = new_dict

    try:
        with open(path, "r") as csv_file:
            csv_dict_reader = csv.DictReader(csv_file, delimiter=",")

            for rows in csv_dict_reader:
                for items in category_array:
                    if items == rows["CATEGORY"]:
                        json_dict[items].append(rows)
                        
            json_array.append(json_dict)

        # convert python jsonArray to JSON String and write to file
        with open("output_file_10.json", 'w', encoding='utf-8') as json_file:
            jsonString = json.dumps(json_array, indent=4)
            json_file.write(jsonString)

    except Exception as e:
        print("The Following error occurred during transformation :  ", e)
    finally:
        print("code just executed check output to confirm on success results")


transform_to_json(path, new_dict)
