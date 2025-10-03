import tkinter as tk
from tkinter import scrolledtext

def speichern():
    text = textfeld.get("1.0", tk.END)
    print(text)
    with open("gespeicherter_text.txt", "w") as file:
        file.write(text)

# GUI erstellen
root = tk.Tk()
root.title("Texteditor")

# Textfeld erstellen
textfeld = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
textfeld.pack(expand=True, fill='both')

# Button zum Speichern hinzufügen
speichern_button = tk.Button(root, text="Speichern", command=speichern)
speichern_button.pack()

# GUI starten
root.mainloop()
