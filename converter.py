
'''from csv_parser import read_csv
from json_handler import write_json, read_json

# Read CSV
students = read_csv("data/students.csv")

# Write JSON
write_json("data/students.json", students)

print("CSV successfully converted to JSON!")

# Read JSON back
json_data = read_json("data/students.json")

print("\nJSON Data:")
print(json_data)'''

'''from csv_parser import read_csv, write_csv
from json_handler import read_json, write_json

choice = input("Enter conversion (csv_to_json / json_to_csv): ")

if choice == "csv_to_json":
    data = read_csv("data/students.csv")
    write_json("data/students.json", data)
    print("CSV successfully converted to JSON!")

elif choice == "json_to_csv":
    data = read_json("data/students.json")
    write_csv("data/students.csv", data)
    print("JSON successfully converted to CSV!")

else:
    print("Invalid choice.")'''

from csv_parser import read_csv, write_csv
from json_handler import read_json, write_json
import json


print("=" * 45)
print("      CSV <--> JSON CONVERTER")
print("=" * 45)

print("\nChoose an option:")
print("1. Convert CSV to JSON")
print("2. Convert JSON to CSV")

choice = input("\nEnter your choice (1 or 2): ")

if choice == "1":

    # Read CSV
    data = read_csv("data/students.csv")

    # Write JSON
    write_json("data/students.json", data)

    print("\nCSV successfully converted to JSON!")

    print("\nGenerated JSON:\n")
    print(json.dumps(data, indent=4))

elif choice == "2":

    # Read JSON
    data = read_json("data/students.json")

    # Write CSV
    write_csv("data/students_from_json.csv", data)

    print("\nJSON successfully converted to CSV!")

    print("\nGenerated CSV:\n")

    headers = list(data[0].keys())
    print(",".join(headers))

    for record in data:
        row = []

        for header in headers:
            row.append(str(record[header]))

        print(",".join(row))

else:
    print("\nInvalid choice!")