import json


def write_json(filepath, data):
    """
    Writes Python data (list/dictionary) to a JSON file.
    """
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)


def read_json(filepath):
    """
    Reads a JSON file and returns it as Python data.
    """
    with open(filepath, "r") as file:
        data = json.load(file)

    return data


# Testing
if __name__ == "__main__":

    students = [
        {
            "Name": "Alice",
            "Age": "20",
            "City": "Pune"
        },
        {
            "Name": "Bob",
            "Age": "21",
            "City": "Mumbai"
        },
        {
            "Name": "Charlie",
            "Age": "19",
            "City": "Delhi"
        }
    ]

    # Write to JSON file
    write_json("data/students.json", students)

    print("JSON file created successfully!")

    # Read the JSON file
    loaded_data = read_json("data/students.json")

    print("\nContents of JSON file:")
    print(loaded_data)