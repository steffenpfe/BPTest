"""GUI software module for BP software"""
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import numpy as np

class MyGUI(Frame) :
    def __init__(self, master=None) :
        """This func initializes the window"""
        Frame.__init__(self, master)
        self.master = master
        self.pack()

        #initialize default parameters from file
        self.initParams() 

        #create the frames of the window
        self.frameLeft = Frame(self.master)
        self.frameLeft.pack(side=LEFT)
        self.frameRight = Frame(self.master)
        self.frameRight.pack(side=RIGHT)

        #initialize window
        self.createMenu()
        self.createCanvasPlot()
        self.createWidgets()
        self.createBindings()

    def NewFile(self):
        """Not yet implemented"""
        pass
    def OpenFile(self) :
        """Not yet implemented"""
        pass
    def About (self):
        """Not yet implemented"""
        pass

    def createMenu(self) :
        """This function creates the Menu"""
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New", command=self.NewFile)
        self.filemenu.add_command(label="Open...", command=self.OpenFile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.master.destroy)

        self.helpmenu = Menu(self.master)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="About...", command=self.About)

    def createCanvasPlot(self) :
        """This function initializes the Canvas Plot and the animation function.
            The animation function is: self.animateCanvasPlot
            The animationfunction gets periodically called in order to
            update the CanvasPlot on the GUI."""
        self.fig = Figure(figsize=(9,6), facecolor="white")
        self.axis = self.fig.add_subplot(111)
        canvas = FigureCanvasTkAgg(self.fig, master=self.frameRight)
        canvas._tkcanvas.pack(expand=1)
        #animation
        self.ani = animation.FuncAnimation(self.fig, self.animateCanvasPlot, interval=1000)

    def animateCanvasPlot(self,i) :
        """This function updates the Canvas Plot periodically. The Values
            which are need to update the Plot are read out of a text file."""
        x_arr = []
        y_arr = []
        with open("CanvasValues.txt", "r") as file :
            for i in file :
                line = i.strip() #remove white-spaces
                data = line.split(",")
                x_arr.append(int(data[0]))
                y_arr.append(int(data[1]))
        self.axis.clear()
        self.axis.plot(x_arr, y_arr)
                
        
          
    def createWidgets(self) :
        """This function creates all Widgets of the GUI"""

        #Start-Button
        self.buttonStart = Button(self.frameLeft)
        self.buttonStart.pack()
        self.buttonStart["text"] = "start"
        self.buttonStart["background"] = "green yellow"

        #Variable amount of buttons
        self.createDrinkButtons()

        #End-Button
        self.buttonEnd = Button(self.frameLeft)
        self.buttonEnd.pack()
        self.buttonEnd["text"] = "end"
        self.buttonEnd["background"] = "red"

        #Price-Label
        self.labelPrice = Label(self.frameLeft)
        self.labelPrice.pack(pady=10)
        self.labelPrice["text"] = "0.00 €"
        

    def createDrinkButtons(self) :
        self.drinkButtons = []
        if len(self.drinks) > 0 and len(self.drinks) < 10 :
            for i in range(0, len(self.drinks)) :
                self.drinkButtons.append(Button(self.frameLeft))
                self.drinkButtons[i].pack()
                self.drinkButtons[i]["text"] = self.drinks[i]

        
    def createBindings(self) :
        """This function creates the bindings to the UI"""
        self.buttonStart.bind("<Button-1>", self.buttonHandler)
        self.buttonEnd.bind("<Button-1>", self.buttonHandler)
        for i in range(0, len(self.drinkButtons)) :
            self.drinkButtons[i].bind("<Button-1>", self.buttonHandler)

    def buttonHandler(self, event) :
        """This function is responsible for the callbacks of all buttons."""
        pass        
        

    def initParams(self) :
        """This function will initialize all parameters which are necessary
            for the application out of a text file.
            FILENAME:    params
            allowed parameters:
            DRINKS = Drink1,Drink2,Drink3,Drink3,...,DrinkN
            """
        filename = "params.txt"
        with open(filename, "r") as file :
            for i in file :
                line = i.strip() #remove white-spaces
                if "DRINKS" in line :
                    try :
                        d = line.split("=")[1]
                        d = d.strip()
                        self.drinks = d.split(",")
                        for j in range(0, len(self.drinks)) :
                            self.drinks[j] = self.drinks[j].strip().upper()
                        print(self.drinks)
                    except :
                        print("ERROR: Couldn't read parameters from file", filename, file=stderr)
    
                                    
                
        

        
    
if __name__ == "__main__" :
    root = Tk()
    app = MyGUI(master=root)
    
    app.mainloop
    #root.destroy()
