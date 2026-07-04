import json
import os


def load_matches(data_path):
    matches = []

    for file in os.listdir(data_path):
        if file.endswith(".json"):
            with open(os.path.join(data_path, file)) as f:
                match = json.load(f)
                matches.append(match)

    print("Number of matches loaded:", len(matches))
    return matches

# if __name__ == "__main__":
#     data_path = "../data/raw_matches"
#     load_matches(data_path)
   