import os
import json

# Define input and output file paths
input_file_path = "guanaco_data.json"
output_dir_path = "split_files"

# Create output directory if it doesn't exist
if not os.path.exists(output_dir_path):
    os.makedirs(output_dir_path)

# Load input JSON file
with open(input_file_path, "r") as f:
    data = json.load(f)

# Calculate number of objects per file
num_objects_per_file = len(data) // 4

# Split data into 4 equal parts
for i in range(4):
    start_index = i * num_objects_per_file
    end_index = start_index + num_objects_per_file
    file_data = data[start_index:end_index]

    # Write split data to output file
    output_file_path = os.path.join(output_dir_path, f"guanaco_data_{i}.json")
    with open(output_file_path, "w") as f:
        json.dump(file_data, f)
