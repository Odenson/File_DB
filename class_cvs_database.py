import csv
import os
import uuid

class DataTable:
    def __init__(self, table_name, headers=None):
        """
        Initialize a DataTable object with a specified name and list of headers.
        If the corresponding CSV file exists, load data from it. Otherwise, create an empty table.
        """
        self.table_name = table_name
        self.headers = headers if headers else []
        self.rows = []
        self.table_location = self.get_table_location()

        # Ensure "ID" heading is the first column
        self.ensure_id_heading()

        # Check if the CSV file exists
        if self.table_exists():
            self.load()  # Load data from the existing file

    def get_table_location(self):
        """
        Get the file path of the table.
        """
        current_directory = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_directory, f"{self.table_name}.csv")

    def table_exists(self):
        """
        Check if the CSV file exists for the table.
        """
        return os.path.isfile(self.table_location)
            
    def ensure_id_heading(self):
        """
        Ensure "ID" heading is the first column of the headers list.
        If "ID" is already present, move it to the first position.
        If "ID" is not present, add it as the first header.
        """
        if "ID" in self.headers:
            self.headers.remove("ID")  # Remove "ID" if already present
        self.headers.insert(0, "ID")  # Add "ID" as the first header

    def add(self, row):
        """
        Add a new row to the table with a unique ID.
        """
        record_id = str(uuid.uuid4())  # Generate a unique ID
        row_with_id = [record_id] + row
        self.rows.append(row_with_id)

    def delete(self, index):
        """
        Delete a row from the table based on its index.
        """
        if index < len(self.rows):
            del self.rows[index]

    def amend(self, row_id, amended_row):
        """
        Amend an existing row in the table using the row's ID.
        If the incorrect ID is provided, raise an error indicating that the record does not exist.
        """
        for i, row in enumerate(self.rows):
            if row[0] == row_id:
                self.rows[i] = [row_id] + amended_row
                break
        else:
            raise ValueError("Record does not exist")

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
        with open(f"{self.table_location}", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(self.headers)  # Write the header row
            writer.writerows(self.rows)  # Write the data rows

    def load(self):
        """
        Load data from the CSV file.
        """
        with open(f"{self.table_location}", "r") as file:
            reader = csv.reader(file)
            self.headers = next(reader)  # Read the header row
            self.rows = list(reader)  # Read the data rows

    def list_all(self):
        """
        List all records in the current table.
        """
        return self.rows
