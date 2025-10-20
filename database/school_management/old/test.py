import sqlite3

conn = sqlite3.connect("sample1.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# query = "select * FROM staff where staffNo=?"
# result = cursor.execute(query, (2,))
# query = "INSERT INTO staff VALUES(null, ?,?,?,?,?,?,?)"
# result = cursor.execute(query, ('abtin2', 'abtini2', 'po', 'male', '2020', 2000, 1))
# conn.commit()
# print(dict(result.fetchone())['fName'])
query = "select * FROM staff"
result = cursor.execute(query)
for i,item in enumerate(result.fetchall()):
    if i == 3:
        print(dict(item)['fName'])
