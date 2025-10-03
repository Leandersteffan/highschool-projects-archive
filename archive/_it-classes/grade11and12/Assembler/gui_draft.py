import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Text, Scrollbar


class GUI():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Widgets and returns')
        # Textfeld erstellen (rechte Seite)

        self.textfeld_frame = tk.Frame(self.window)
        self.textfeld_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")

        self.textfeld = Text(self.textfeld_frame, wrap=tk.WORD, width=40, height=10)
        self.textfeld.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.textfeld_scrollbar = Scrollbar(self.textfeld_frame, command=self.sync_scroll)
        self.textfeld_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.textfeld['yscrollcommand'] = self.textfeld_scrollbar.set

        self.textfeld.bind("<Key>", lambda event: (self.aktualisiere_zeilennummern(), self.sync_scroll()))
        self.textfeld.bind("<MouseWheel>", lambda event: (self.aktualisiere_zeilennummern(), self.sync_scroll()))

        # Textfeld für Zeilennummern (linke Seite)
        self.zeilennummer_text = tk.Text(self.window, wrap=tk.NONE, width=4, height=10, state=tk.DISABLED, bg='#E0E0E0')
        self.zeilennummer_text.grid(row=0, column=0, sticky="nsew")

        # Nummern für Zeilennummern einfügen
        self.aktualisiere_zeilennummern()

        # Button zum Speichern hinzufügen
        self.speichern_button = tk.Button(self.window, text="Speichern", command=self.combined_funktions_save)
        self.speichern_button.grid(row=3, column=0, columnspan=2, sticky="ew")

        # Konfiguration für das Grid-Layout
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)

        # TEXTFELD IMPORT ENDE

        button_save = tk.Button(self.window, text='Laden', command=self.laden)
        button_save.grid(column=2, row=4, padx=5, pady=5)

        # Program Counter Label in Column 1 ...
        pc_label = tk.Label(self.window, text='Program_Counter')  # Might have to change text to text_variable
        pc_label.grid(column=2, row=1, padx=20, pady=5)

        akku_label = tk.Label(self.window, text='Akkumulator')  # Same as PC_label with the text
        akku_label.grid(column=2, row=2, padx=20, pady=5)

        alu_label = tk.Label(self.window, text='Alu')
        alu_label.grid(column=2, row=3, padx=20, pady=5)

        # GUI starten
        self.window.mainloop()

    def syntax_checking(self):
        pass

    def laden(self):
        with open("gespeicherter_text.txt", "r") as file:
            gespeicherter_text = file.readlines()

        self.textfeld.delete("1.0", tk.END)

        zeilennummern_set = set()
        for line in gespeicherter_text:
            parts = line.split(" ", 1)
            if parts:
                zeilennummer = parts[0].strip().zfill(2)
                text = parts[1].strip() if len(parts) == 2 else ""
                self.textfeld.insert(f"{zeilennummer}.0", f"{text}\n")
                zeilennummern_set.add(zeilennummer)

        max_zeilennummer = self.textfeld.get("1.0", tk.END).count('\n')
        for i in range(1, max_zeilennummer + 1):
            zeilennummer = str(i).zfill(2)
            if zeilennummer not in zeilennummern_set:
                self.textfeld.insert(f"{zeilennummer}.0", "\n")

        self.aktualisiere_zeilennummern()


    def speichern(self):
        text = self.textfeld.get("1.0", tk.END)
        print(text)
        with open("assembler.txt", "w") as file:
            file.write(text)


    def sync_scroll(self, *args):
        yview = self.textfeld.yview()
        self.zeilennummer_text.yview_moveto(yview[0])
        self.textfeld_scrollbar.set(*yview)


    # Funktion zum Aktualisieren der Zeilennummern
    def aktualisiere_zeilennummern(self, event=None):
        self.zeilennummer_text.config(state=tk.NORMAL)
        self.zeilennummer_text.delete("1.0", tk.END)

        # Nummern für Zeilennummern einfügen
        zeilen = self.textfeld.get("1.0", tk.END).count('\n') + 1
        for i in range(0, zeilen + 1):
            self.zeilennummer_text.insert(tk.END, f"{i}\n")

        self.zeilennummer_text.config(state=tk.DISABLED)

    # Import Leander Auslesen, Syntax, in Datei schreiben
    def string_to_dict(self, input_string):
        lines = input_string.split('\n')
        result_dict = {}

        count_newlines = 0

        for line in lines:
            if line.strip():  # Überprüfen, ob die Zeile nicht leer ist (nach Entfernen von Leerzeichen)
                result_dict[count_newlines] = line
                count_newlines += 1
            else:
                result_dict[count_newlines] = None
                count_newlines += 1

        return result_dict

    def check_instruction_syntax(self, instruction):
        # Überprüfe, ob Leerzeichen am Anfang oder am Ende der Anweisung vorhanden sind
        if instruction.startswith(' ') or instruction.endswith(' '):
            return False

        if instruction.startswith("LDA #") and instruction[6:].isdigit():
            # AKKU := xx
            return True
        elif instruction.startswith("LDA ") and instruction[4:].isdigit():
            # AKKU := RAM[xx]
            return True
        elif instruction.startswith("LDA (") and instruction[5:-1].isdigit() and instruction.endswith(')'):
            # AKKU := RAM[RAM[xx]]
            return True
        elif instruction.startswith("STA ") and instruction[4:].isdigit():
            # RAM[xx] := AKKU
            return True
        elif instruction.startswith("STA (") and instruction[5:-1].isdigit() and instruction.endswith(')'):
            # RAM[RAM[xx]] := AKKU
            return True
        elif any(instruction.startswith(op) and instruction[len(op):].isdigit() for op in ["ADD ", "SUB ", "MUL ", "DIV "]):
            # AKKU := AKKU+RAM[xx], AKKU := AKKU-RAM[xx], AKKU := AKKU*RAM[xx], AKKU := AKKU DIV RAM[xx]
            return True
        elif any(instruction.startswith(op) and instruction[len(op):].isdigit() for op in ["JMP ", "JNZ ", "JZE ", "JLE "]):
            # PZ := xx, PZ := RAM[xx], PZ := xx, wenn AKKU <> 0, PZ := RAM[xx], wenn AKKU <> 0, ...
            return True
        elif any(instruction.startswith(op) and (instruction[len(op):].startswith("(") and instruction[len(op):].endswith(")")) for op in ["JMP ", "JNZ ", "JZE ", "JLE "]):
            # PZ := xx, PZ := RAM[xx], PZ := xx, wenn AKKU <> 0, PZ := RAM[xx], wenn AKKU <> 0, ...
            return True
        elif instruction == "STP":
            # STOP
            return True
        else:
            return False

    def check_program_syntax(self, program_dict):
        for key in sorted(program_dict.keys()):
            instruction = program_dict[key]
            instruction = instruction
            if instruction == None:
                pass
            elif not self.check_instruction_syntax(instruction):
                return False
        return True

    def write_to_text_file(self, program_dict, filename):
        with open(filename, 'w') as file:
            for key in sorted(program_dict.keys()):
                content = program_dict[key]
                line_number = str(key).zfill(2)  # Füge ggf. führende Nullen hinzu
                if content is not None:
                    file.write(f"{line_number} {content}\n")
                else:
                    file.write(f"{line_number}\n")

    #methode die ausliest --> in dictunray --> Syntax --> in Datei schreiben
    def combined_funktions_save(self):
        dict = self.string_to_dict(self.textfeld.get("1.0", tk.END))
        if not self.check_program_syntax(dict):
            print("syntax error")
            return False #Label ändern
        self.write_to_text_file(dict, "Assembler_Program.txt")

gui = GUI()
