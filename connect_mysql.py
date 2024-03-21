import mysql.connector

# Replace placeholders with your actual credentials
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythondatabase"
)

mycursor = mydb.cursor()

# Create a table (if it doesn't exist)
mycursor.execute('''CREATE TABLE IF NOT EXISTS customers
                      (id INT AUTO_INCREMENT PRIMARY KEY,
                       name VARCHAR(255),
                       email VARCHAR(255))''')

# Insert some data
mycursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)", ('PR', 'pr@email.com'))
mydb.commit()

# Retrieve data
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()

for row in myresult:
    print(row)

mycursor.close()
mydb.close()
