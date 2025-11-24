import os
import sqlite3

os.chdir("Module-4/My_Database")

try:
    db = sqlite3.connect("temp_data.db")
    print("Database Connected...")
except Exception as e:
    print(e)

# create table

tb_crt = "create table Student_Info(id integer primary key autoincrement, name text, age int, city text, grade text)"

try:
    db.execute(tb_crt)
    print("Table Created Successfully...")
except Exception as e:
    print(e)

# Insert Data

# n = int(input("Enter number of records to insert : "))

# for i in range(n):
#     name = input("Enter Name : ")
#     age = int(input("Enter Age : "))
#     city = input("Enter City : ")
#     grade = input("Enter Grade : ")
#     print("-" * 40)

#     ins_qry = f"insert into Student_Info(name, age, city, grade) values('{name}', {age}, '{city}', '{grade}')"

#     try:
#         db.execute(ins_qry)
#         db.commit()
#         print("Data Inserted Successfully...\n")
#     except Exception as e:
#         print(e)

# Update Data

# n = int(input("Enter ID to update record : "))

# column = input("Enter column to update (name, age, city, grade) : ")

# value = input(f"Enter new value for {column} : ")

# update_qry = f"update Student_Info set {column} = '{value}' where id = {n}"

# try:
#     db.execute(update_qry)
#     db.commit()
#     print("Data Updated Successfully...\n")
# except Exception as e:
#     print(e)

# Delete Data

# n = int(input("Enter ID to delete record : "))

# del_qry = f"delete from Student_Info where id = {n}"

# try:
#     db.execute(del_qry)
#     db.commit()
#     print("Data Deleted Successfully...\n")
# except Exception as e:
#     print(e)

# Fetch Data

cr = db.cursor()

sel_qry = "select * from Student_Info"

try:
    cr.execute(sel_qry)
    data = cr.fetchall()
    # data = cr.fetchone()
    # data = cr.fetchmany(2)
    print(data)
    print("Data Fetched Successfully...\n")
except Exception as e:
    print(e)