#!/usr/bin/env python3
import re
import json
import csv

PATH = "task1_d.json"
DESTINATION_PATH = "data.csv"

def main():
    with open(PATH, "r") as f:
        file_data = f.read()

    fixed_data = re.sub(r':([a-z]+)=>', r'"\1":', file_data)
    parsed_data = json.loads(fixed_data)

    with open(DESTINATION_PATH, 'w') as f:
        writer = csv.DictWriter(f, parsed_data[0].keys())
        writer.writeheader()
        writer.writerows(parsed_data)

if __name__ == "__main__":
    main()
