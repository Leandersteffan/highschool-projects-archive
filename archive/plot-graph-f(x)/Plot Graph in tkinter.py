import math
from tkinter import *


class Plot:
    def __init__(self, graph):
        self.graph = str(graph)
        self.plotList = self.createPlotList()
        self.guiList = self.createGuiList(self.plotList)

    def createPlotList(self):
        negativeRange = [-10]
        for i in range(1, 500):
            negativeRange.append(round(negativeRange[i-1] + 0.02, 2))
        positiveRange = [0]
        for i in range(1, 500):
            positiveRange.append(round(positiveRange[i-1] + 0.02, 2))
        fullRange = negativeRange + positiveRange

        plotPositionsList = []
        for element in fullRange:
            toAppend = []
            toAppend.append(element)
            newgraph = self.graph.replace("x", f"({str(element)})")
            toAppend.append(eval(newgraph))
            plotPositionsList.append(toAppend)
        return plotPositionsList

    def createGuiList(self, plotList):
        for i in range(len(plotList)):
            plotList[i][0] = plotList[i][0] * 50 + 500
            plotList[i][1] = -(plotList[i][1] * 50) + 400
        return plotList


class Gui:
    def __init__(self, graph):
        self.modell = Plot(graph)
        self.hauptfenster = Tk()
        self.hauptfenster.title("Graph")
        self.hauptfenster.geometry("1000x800")
        self.hauptfenster.configure(background='white')
        self.canvas = Canvas(self.hauptfenster, height=800, width=1000, bg='white')  # Canvas color change
        self.canvas.place(x=0, y=0)

        self.drawSystem()
        self.plotGuiGraph(self.modell.guiList)

        self.hauptfenster.mainloop()

    def drawSystem(self):
        test = self.canvas.create_line(495, 395, 495, 395, width=1, fill="red")
        for i in range(1, 20): # create net
            x_Achse_netLines = self.canvas.create_line(50 * i, 0, 50 * i, 800, width=1, fill="lightgrey")
            y_Achse_netLines = self.canvas.create_line(0, 50 * i, 1000, 50 * i, width=1, fill="lightgrey")
        x_Achse = self.canvas.create_line(0, 400, 1000, 400)
        y_Achse = self.canvas.create_line(500, 0, 500, 800)
        for i in range(1, 20): # create messurelines
            x_Achse_messure = self.canvas.create_line(50*i, 390, 50*i, 410, width=1)
            y_Achse_messure = self.canvas.create_line(490, 50*i, 510, 50*i, width=1)

    def plotGuiGraph(self, guiList):
        for i in range(len(guiList)):
            graph = self.canvas.create_line(guiList[i][0], guiList[i][1], guiList[i][0] + 1, guiList[i][1], width=2, fill="red")


term = input("f(x) = ")
start = Gui(term)