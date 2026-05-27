import csv
import sys
import os
from dotenv import load_dotenv


load_dotenv()
key = os.environ.get("GOOGLE_API_KEY")

if key:
    print("Key has been loaded")
else:
    print("Key not loaded")


headers = ["Test1", "Test2", "Test3"]
rows = [
    ["1", "2", "3"],
    ["4", "5", "6"]
]

with open("output.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

zipCode = sys.argv[1]
radiusMiles = sys.argv[2]

print("zip entered was", zipCode, "and radius in miles was", radiusMiles)