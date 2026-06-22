# CSV to JSON converter tool
import os
import json
import csv

BASE_DIR = os.path.dirname(__file__)
INPUT_FILE = os.path.join(BASE_DIR, "raw_data.csv")
OUTPUT_FILE = os.path.join(BASE_DIR, "data_result.json")

# INPUT_FILE = "raw_data.csv"

def load_csv_data(filename):
    if not os.path.exists(filename):
        print("CSV file not found")
        return []
    with open(filename,encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
        print(data)
        return data
    
dta = load_csv_data(INPUT_FILE)
