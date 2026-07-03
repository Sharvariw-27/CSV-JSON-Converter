def read_csv(filepath):
    # Open the CSV file
    with open(filepath, "r") as file:
        lines = file.readlines()

    # Remove newline characters
    cleaned_lines = []
    for line in lines:
        cleaned_lines.append(line.strip())

    # Split each line into columns
    rows = []
    for line in cleaned_lines:
        rows.append(line.split(","))

    # First row contains headers
    headers = rows[0]

    # Store all dictionaries here
    data = []

    # Start from second row
    for row in rows[1:]:

        record = {}

        # Match every header with its value
        for i in range(len(headers)):
            record[headers[i]] = row[i]

        data.append(record)

    return data


# Testing

#students = read_csv("data/students.csv")

#print(students)
if __name__ == "__main__":
    students = read_csv("data/students.csv")
    print(students)

def write_csv(filepath, data):

    # If there is no data, don't create a file
    if not data:
        print("No data to write.")
        return

    with open(filepath, "w") as file:

        # Write headers
        headers = list(data[0].keys())
        file.write(",".join(headers) + "\n")

        # Write rows
        for record in data:
            row = []

            for header in headers:
                row.append(str(record[header]))

            file.write(",".join(row) + "\n")