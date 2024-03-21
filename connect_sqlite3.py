import sqlite3

# Connect to the database (or create a new one if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object to execute SQL statements
cursor = conn.cursor()

# Create a table (if it doesn't exist)
cursor.execute('''CREATE TABLE IF NOT EXISTS customers
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT)''')

# Insert some data
cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", ('PR', 'pr@email.com'))
conn.commit()  # Commit changes

# Retrieve data
cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
cursor.close()
conn.close()
