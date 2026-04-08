import json
import os 

data_path = "../data/raw_matches"


def load_matches(data_path):
    matches = []

    for file in os.listdir(data_path):
        if file.endswith(".json"):
            with open(os.path.join(data_path, file)) as f:
                match = json.load(f)
                matches.append(match)
    return matches

    #print("Total matches loaded:", len(matches))


    