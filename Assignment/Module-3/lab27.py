# Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data.

import sqlite3

conn = sqlite3.connect("mydatabase.db")         # connect with database
cursor = conn.cursor()

cursor.execute("""                             
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)       
""")                                            # Create table

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Vivek", 21))        # Insert Data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Meet", 24))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Kashyap", 24))

conn.commit()                                   # Commit changes  

cursor.execute("SELECT * FROM users")           # Fetch data
rows = cursor.fetchall()

print("Users in database:")                     
for n in rows:                
    print(f"ID: {n[0]}, Name: {n[1]}, Age: {n[2]}")

conn.close()            
