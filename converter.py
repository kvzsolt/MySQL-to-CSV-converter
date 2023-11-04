import os
import csv
import data_handler


def converter(tables):
    for table in tables:
        try:
            data = data_handler.get_all_data(table)

            if not data:
                print(f"No data found in table: {table}")
                continue

            fieldnames = list(data[0].keys())
            file_path = os.path.join(".", f"{table}.csv")

            with open(file_path, "w+", encoding="utf-8", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, escapechar='\\')
                writer.writeheader()

                for line in data:
                    string_line = {key: str(value) for key, value in line.items()}
                    writer.writerow(string_line)

        except Exception as e:
            print(f"An error occurred while processing table {table}: {str(e)}")
