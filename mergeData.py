import os
import json

# Define input file paths
input_dir_path = "split_files"

# Load data from each split file
data = []
for i in range(4):
    input_file_path = os.path.join(input_dir_path, f"guanaco_data_{i}.json")
    with open(input_file_path, "r") as f:
        file_data = json.load(f)
        data.extend(file_data)

# Write merged data to output file
output_file_path = "guanaco_data.json"
with open(output_file_path, "w") as f:
    json.dump(data, f)
