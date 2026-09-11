"""Runnable examples for File I/O.

The examples use a temporary directory so running this file does not leave
practice files in the repository.
"""

from pathlib import Path
import csv
import json
import tempfile

with tempfile.TemporaryDirectory() as folder:
    base = Path(folder)
    text_file = base / "notes.txt"

    # 1–2. Paths and opening
    print("path:", text_file)
    with open(text_file, "w", encoding="utf-8") as file:
        # 4. Writing
        file.write("Python\nEngineering\n")

    # 3, 8–9. Reading with context manager
    with open(text_file, "r", encoding="utf-8") as file:
        print("read:", file.read())

    # 5. Appending
    with open(text_file, "a", encoding="utf-8") as file:
        file.write("Robotics\n")

    # 6. Modes and 7. text vs binary
    binary_file = base / "data.bin"
    with open(binary_file, "wb") as file:
        file.write(b"ABC")
    with open(binary_file, "rb") as file:
        print("binary:", file.read())

    # 10. read()
    with open(text_file, encoding="utf-8") as file:
        print("read():", file.read())

    # 11. readline()
    with open(text_file, encoding="utf-8") as file:
        print("readline():", file.readline().strip())

    # 12. readlines()
    with open(text_file, encoding="utf-8") as file:
        print("readlines():", [line.strip() for line in file.readlines()])

    # 13. Iterating streams lines
    with open(text_file, encoding="utf-8") as file:
        for line in file:
            print("line:", line.strip())

    # 14–15. CSV structured data
    csv_file = base / "sensors.csv"
    rows = [["name", "value"], ["temperature", "25.5"], ["pressure", "101"]]
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        csv.writer(file).writerows(rows)
    with open(csv_file, newline="", encoding="utf-8") as file:
        print("CSV:", list(csv.reader(file)))

    # 16. JSON
    json_file = base / "config.json"
    data = {"device": "AGV-1", "enabled": True, "speed": 1.5}
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    with open(json_file, encoding="utf-8") as file:
        print("JSON:", json.load(file))

    # 17. File handling errors
    try:
        (base / "missing.txt").read_text(encoding="utf-8")
    except FileNotFoundError as error:
        print("file error:", error)

    # 18. Resource management is handled by every with block above.
