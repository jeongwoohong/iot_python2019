import sqlite3
import csv
import sys

input_file = sys.argv[1] #data_for_updating.csv

con = sqlite3.connect(':memory:')
query = """CREATE TABLE sales
            (customer VARCHAR(20),
            product VARCHAR(40),
            amount FLOAT,
            date DATE);"""
con.execute(query)
con.commit()

data = [('Richard Lucas', 'Notepad',2.50,'2014-01-02'),
        ('Jenny Kim','Binder',4.15,'2014-01-15'),
        ('Svetlana Crow','printer',155.75,'2014-02-03'),
        ('stephen Randolph','Computer',679.40,'2014-02-20')]
for tuple in data:
    print(tuple)
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
con.executemany(statement,data)
con.commit()


file_reader = csv.reader(open(input_file,'r'),delimiter=',')
header = next(file_reader,None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    con.execute("UPDATE sales SET amount=?, date=? WHERE customer=?;",data)
con.commit()

cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()

row_counter = 0
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)
