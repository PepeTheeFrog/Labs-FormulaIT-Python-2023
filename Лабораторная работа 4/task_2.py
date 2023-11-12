import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as csvfile:
        rows = [row for row in csv.DictReader(csvfile)]

    with open(OUTPUT_FILENAME, "w") as jsonfile:
        json.dump(rows, jsonfile, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
