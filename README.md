# 📄 CSV ↔ JSON Converter

A Python command-line application that converts **CSV files to JSON** and **JSON files back to CSV** using Python's built-in libraries. This project demonstrates manual CSV parsing, JSON serialization, file handling, and modular programming.

---

## 📌 Project Overview

The CSV ↔ JSON Converter is designed to help users easily convert data between CSV and JSON formats. It manually parses CSV files without using Python's built-in `csv` module and uses the built-in `json` module for JSON operations.

This project was developed as part of a Backend Development Internship to strengthen knowledge of:

- File Handling
- Data Serialization
- Lists and Dictionaries
- Modular Programming
- Python Functions

---

## ✨ Features

- ✅ Convert CSV to JSON
- ✅ Convert JSON to CSV
- ✅ Manual CSV Parsing
- ✅ Read JSON Files
- ✅ Write JSON Files
- ✅ Menu-Driven Command Line Interface
- ✅ Modular Project Structure

---

## 🛠 Technologies Used

- Python 3.x
- JSON Module
- File Handling
- Lists
- Dictionaries

---

## 📂 Project Structure

```text
CSV-JSON-Converter/
│
├── converter.py          # Main program
├── csv_parser.py         # CSV Reader & Writer
├── json_handler.py       # JSON Reader & Writer
│
├── data/
│   ├── students.csv
│   └── students.json
│
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Sharvariw-27/CSV-JSON-Converter.git
```

### 2. Navigate to the project folder

```bash
cd Converter
```

### 3. Run the application

```bash
python converter.py
```

---

## 📋 Menu

When the program starts, you'll see:

```text
CSV ↔ JSON Converter

1. CSV to JSON
2. JSON to CSV
3. Exit

Enter your choice:
```

---

## 📥 Sample CSV Input

**students.csv**

```csv
Name,Age,City
Alice,20,Pune
Bob,21,Mumbai
Charlie,19,Delhi
```

---

## 📤 JSON Output

**students.json**

```json
[
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
```

---

## 🔄 JSON to CSV Conversion

The application can also convert the JSON file back into a CSV file while preserving all records.

---

## ⚙️ Modules

### converter.py

- Displays the menu
- Handles user input
- Calls the required conversion functions

### csv_parser.py

- Reads CSV files
- Parses CSV data manually
- Writes data into CSV format

### json_handler.py

- Reads JSON files
- Writes JSON files using Python's built-in `json` module

---

## 🧪 Testing

The project was tested using sample student data.

### CSV → JSON

✔ Successfully converted CSV data into JSON format.

### JSON → CSV

✔ Successfully recreated the original CSV file.

---

## 🚀 Future Enhancements

- Support Excel (.xlsx) files
- Graphical User Interface (GUI)
- Drag & Drop File Conversion
- CSV Data Validation
- Nested JSON Support
- Error Handling for Invalid Files

---

## 👩‍💻 Author

**Sharvari Waghale**

Backend Development Internship Project

---

## 📄 License

This project is created for educational and internship purposes.
