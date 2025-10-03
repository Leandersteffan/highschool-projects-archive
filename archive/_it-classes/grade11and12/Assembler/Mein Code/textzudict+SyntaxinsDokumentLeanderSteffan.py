def string_to_dict(input_string):
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

# Beispielaufruf:
#input_string = "Zeile 1\n\n\nZeile 4\nZeile 5\n\nZeile 7"
'''input_string = """Zeile 1


Zeile 4
Zeile 5

Zeile 7"""
result_dict = string_to_dict(input_string)
print(result_dict)'''



def check_instruction_syntax(instruction):
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

def check_program_syntax(program_dict):
    for key in sorted(program_dict.keys()):
        instruction = program_dict[key]
        if instruction == None:
            pass
        elif not check_instruction_syntax(instruction):
            return False
    return True

# Beispielaufruf:
'''program_dict = {0: "LDA #42", 1: "STA (1021239)", 2: "JNZ 2345", 3: "ADD 20", 4: "STP", 5: None}
result = check_program_syntax(program_dict)
print(result)'''

def write_to_text_file(program_dict, filename):
    with open(filename, 'w') as file:
        for key in sorted(program_dict.keys()):
            content = program_dict[key]
            line_number = str(key).zfill(2)  # Füge ggf. führende Nullen hinzu
            if content is not None:
                file.write(f"{line_number} {content}\n")
            else:
                file.write(f"{line_number}\n")

# Beispielaufruf:
'''program_dict = {0: "LDA #42", 1: "STA 10", 2: None, 3: "ADD 20", 4: "STP", 6: "STP", 12: "STP", 101: "STP"}
write_to_text_file(program_dict, "Assembler_Program.txt")'''

