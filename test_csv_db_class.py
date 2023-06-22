from File_DB.class_cvs_database import DataTable

# create a new table with headers
table = DataTable("employees", ["name", "age", "position"])

# add rows to the table
table.add(["John Doe", 30, "Manager"])
table.add(["Jane Smith", 25, "Assistant"])
table.add(["Jane Doe", 30, "Legend"])
table.add(["Gary Febb", 51, "Assistant"])

# save changes to the file
table.save()

# search for all employees with age 30
results = table.search("age", 30)
print(results)
