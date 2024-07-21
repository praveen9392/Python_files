import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(r"D:\Python\users.db")

# Create a cursor object
cursor = conn.cursor()

"""# Create a table
cursor.execute('''CREATE TABLE users
                (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert data into the table
cursor.execute("INSERT INTO user (name, password_hash) VALUES ('Praveen',20)")
cursor.execute("INSERT INTO user (name, password_hash) VALUES ('Hari', 25)")

"""
# Commit the transaction
conn.commit()

# Fetch and print all data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
