import mysql.connector
import tkinter as tk

mydb = mysql.connector.connect(
    host="10.16.100.7",
    user="root",
    password="",
    db="universitaet"
)

cursor = mydb.cursor()

# Fetch data from the professoren table
cursor.execute("SELECT * FROM professoren")
result = cursor.fetchall()
print(result)

# Close the cursor and connection
cursor.close()
mydb.close()

# Create the Tkinter application
root = tk.Tk()

# Create a text widget to display the results
text_widget = tk.Text(root)
text_widget.pack()

# Insert the results into the text widget
for row in result:
    text_widget.insert(tk.END, str(row) + '\n')

# Start the Tkinter event loop
root.mainloop()

"""# Insert a new row into the professoren table
insert_query = 'INSERT INTO `professoren` (`persnr`, `name`, `rang`, `raum`) VALUES (0816, "Frank", "c4", 102)'
cursor.execute(insert_query)

mydb.commit()  # Commit the transaction

# Close the cursor and connection
cursor.close()
mydb.close()"""