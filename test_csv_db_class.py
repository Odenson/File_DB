from class_cvs_database import DataTable

# create a new table with headers, this will only add heading if file of this database does not exit (ie new db)
table = DataTable("employees", ["name", "age", "position"])

# add rows to the table
#table.add(["John Doe", 30, "Manager"])
#table.add(["Jane Smith", 25, "Assistant"])
#table.add(["Jane Doe", 30, "Legend"])
#table.add(["Gary Febb", 51, "Assistant"])
#table.add(["Giordan Febb", 19, "Student"])


'''#amend an existing row
try:
    id = "d3ceb69c-40ef-4e4a-a1b7-7e680ad62de"
    table.amend(id, ["Gary Febb", 51, "Managing Partner"])
    print("Row updated for ID:" + id)
except:
    print("Row not found for id: "+id)
'''
    
# save changes to the file
table.save()

# search for all employees with age 30
results = table.search("age", "30")
print("search result")
for row in results:
    print(row)


#list all records in Table
#records = table.list_all()
#for row in records:
#    print(row)
