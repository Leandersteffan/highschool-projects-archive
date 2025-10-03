import mysql.connector

# Database configuration
config = {
    'host': '10.16.100.7',
    'user': 'root',
    'password': '',
    'database': 'schule'
}

try:
    # Connect to the database
    #conn = mysql.connector.connect(**config)
    conn = mysql.connector.connect(
        host = '10.16.100.7',
        user = 'root',
        password = '',
        db = 'universität'
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a sample query
    query = "SELECT * FROM professoren"
    cursor.execute(query)

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()

except mysql.connector.Error as error:
    print(f"Error connecting to MySQL database: {error}")