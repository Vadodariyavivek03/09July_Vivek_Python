import pymysql

try:
    db = pymysql.connect(host="localhost", user="root", password="", database="product_db")
    print("Database Connected Successfully...")
except Exception as e:
    print(e)

# Create Table

cr = db.cursor()

# tbl_crt = "create table Product_Info(id integer primary key auto_increment, p_name text, p_price integer, p_qty integer)" 

# try:
#     cr.execute(tbl_crt)
#     print("Table Create Successfully....")
# except Exception as e:
#     print(e)


# Insert Data

# insert_qry = '''insert into Product_Info(p_name, p_price, p_qty) values
#                 ('Laptop', 44500, 2),
#                 ('Bag', 1250, 3),
#                 ('Pendrive', 899, 4), 
#                 ('Mouse', 540, 2),
#                 ('Mobile', 16750, 3),
#                 ('Book', 45, 15),
#                 ('Ball-Pen', 5, 20),
#                 ('Water-bottle', 750, 4)
#                  ('I-Pad', 72599, 1)''' 

# try:
#     cr.execute(insert_qry)
#     db.commit()
#     print("Data Inserted Successfully....")
# except Exception as e:
#     print(e)


# Update Data

# update_qry = "update Product_Info set p_price = 380, p_qty = 1 where id = 4 "

# try:
#     cr.execute(update_qry)
#     db.commit()
#     print("Data Updated Successfully....")
# except Exception as e:
#     print(e)


# Delete Data

# del_qry = "delete from Product_Info where id = 9"

# try:
#     cr.execute(del_qry)
#     db.commit()
#     print("Data Deleted Successfully....")
# except Exception as e:
#     print(e)

# Fetch Data

sel_qry = "select * from Product_Info"

try:
    cr.execute(sel_qry)
    data = cr.fetchall()
    print(data)
except Exception as e:
    print(e)