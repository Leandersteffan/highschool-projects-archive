
# -*- coding: cp1252 -*-
from tkinter import *
#import tkMessageBox


class Reversi:
    def __init__(self):

        self.spielfeld= [[0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0]]
        self.feld_datei_name = '1.txt'
        self.datei=open(f".\Fields\{self.feld_datei_name}")
        self.spielfeld=self.datei.readlines()
        for i in range(len(self.spielfeld)):
            self.spielfeld[i] = self.spielfeld[i].strip()
            self.spielfeld[i] = self.spielfeld[i].split(' ')
            for j in range(len(self.spielfeld[i])):
                self.spielfeld[i][j] = int(self.spielfeld[i][j])
        self.datei.close()
        self.save_field(self.spielfeld)

    def save_field(self, spielfeld):
        strings_saved_field = [''] * len(spielfeld)
        for i in range(len(spielfeld)):
            for j in range(len(spielfeld[i])):
                strings_saved_field[i] += str(spielfeld[i][j]) + ' '
            strings_saved_field[i] += '\n'
        saved_field_name = '1.txt'
        field_save_datei = open(f'{saved_field_name}', 'w+')
        for i in range(len(strings_saved_field)):
            field_save_datei.write(strings_saved_field[i])
            print(strings_saved_field[i][:-1])
        field_save_datei.close()


#Hauptprogramm
r=Reversi()
print(r.spielfeld)
