import csv
import os


class DataTable:
    def __init__(self, table_name, headers=None):
        """
        Initialize a DataTable object with a specified name and list of headers.
        If the corresponding CSV file exists, load data from it. Otherwise, create an empty table.
        """
        self.table_name = table_name
        self.headers = headers if headers else []
        self.rows = []
        
        # Check if the CSV file exists
        if os.path.isfile(f"{table_name}.csv"):
            self.load()  # Load data from the existing file

    def add(self, row):
        """
        Add a new row to the table.
        """
        self.rows.append(row)

    def delete(self, index):
        """
        Delete a row from the table based on its index.
        """
        if index < len(self.rows):
            del self.rows[index]

    def search(self, field, value):
        """
        Search for rows with a specified value in a specified field.
        Return a list of all matching rows.
        """
        matches = []
        if field in self.headers:
            field_index = self.headers.index(field)
            for row in self.rows:
                if row[field_index] == value:
                    matches.append(row)
        return matches

    def save(self):
        """
        Save changes to the CSV file.
        """
        with open(f"{self.table_name}.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(self.headers)  # Write the header row
            writer.writerows(self.rows)  # Write the data rows

    def load(self):
        """
        Load data from the CSV file.
        """
        with open(f"{self.table_name}.csv", "r") as file:
            reader = csv.reader(file)
            self.headers = next(reader)  # Read the header row
            self.rows = list(reader)  # Read the data rows
