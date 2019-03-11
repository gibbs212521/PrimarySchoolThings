import numpy as np
import os
import sys 
import subprocess


import tkinter as tk
from tkinter import *
from tkinter import ttk

import tkinter.messagebox



LARGE_FONT = ("Consolas", 12)
Large_Font = ("Consolas", 10)
large_font = ("Consolas", 9)
normal_font = ("Consolas", 8)
small_font = ("Consolas", 6)

#f = Figure(figsize=(5,5), dpi = 100) # Figure Settings
#a = f.add_subplot(111)


class textInput():
	""" Class exists for input modules"""

	def __init__(self, fileDirectory, module, length, fileWrite, filePY, fileOutput, filePlot, plotMatrix):
#
		self.fileDirectory = fileDirectory
		self.module = module
		self.length = length
		self.fileWrite = fileWrite
		self.filePY = filePY
		self.fileOutput = fileOutput
		self.filePlot = filePlot
		self.plotMatrix = plotMatrix
#
	def add_line(self, newLine):
#            
		self.newline = newLine
		self.fileWrite.append(newLine)



ModEx1 = textInput('inputExercise1.txt', 'Exercise 1', 20, [],'inputExercise1.py','outputExercie1.txt',None, None)
ModEx2 = textInput('inputExercise2.txt', 'Exercise 2', 20, [],'inputExercise2.py','outputExercie2.txt', 'plotEx2.txt', None) # a)
ModEx3 = textInput('inputExercise3.txt', 'Exercise 3', 20, [],'inputExercise3.py','outputExercie3.txt',None,None)
ModPr1 = textInput('inputPracticum1.txt', 'Practicum 1', 20, [],'inputPracticum2.py','outputPracticum1.txt',None,None)
ModPr2 = textInput('inputPracticum2.txt', 'Practicum 2', 20, [],'inputPracticum2.py','outputPracticum2.txt','plotPr2.txt', None) #a)



def animate(inputTextClass):
	pullData = open(inputTextClass.filePlot,"r").read()
	dataList = pullData.split('\n')
	xList = []
	yList = []
	for eachLine in dataList:
        if len(eachLine) > 1:
		x,y = eachLine.split(',')
		xList.append(int(x))
		yList.append(int(y))
	inputTextClass.plotMatrix.clear()
	inputTextClass.plotMatrix.plot(xList,yList)

def GenerateNewPlot(inputTextClass):
	pullData = open(inputTextClass.filePlot,"r").read()
	dataList = pullData.split('\n')
	xList = []
	yList = []
	for eachLine in dataList:
		if len(eachLine) > 1:
		x,y = eachLine.split(',')
		xList.append(int(x))
		yList.append(y)
	for yVal in range(len(yList)):
		if yVal == 0:
			yList[yVal] = 1
		else:
			yList[yVal] = yList[yVal-1] * (1+np.random.random())
	testVal = ""
	for iteration in range(len(yList)):
		testVal = testVal + str(xList[iteration])+','+str(int(yList[iteration]))+'\n'
	pushData = open(inputTextClass.filePlot,"w")
	pushData.write(testVal)

    

### important for initial start

descriptorStart = "Hover the pointer over any button \n in order to read its description."
descriptionLabel = descriptorStart
buttonFileVal = descriptionLabel  ## INITIAL val



def displayLabel(targetText,filename,align):
	pullData = open(filename,"r").read()
	dataText = pullData.split("\n")
	lineStr = []
	for eachLine in dataText:
		if len(eachLine) > 1:
			lineStr.append(eachLine)
	targetText.config(text=open(filename,"r").read())
	targetText.config(justify=align)

def displayButton(targetButton,filename):
	pullData = open(filename,"r").read()
	dataText = pullData.split("\n")
	lineStr = []
	for eachLine in dataText:
		if len(eachLine) > 1:
			lineStr.append(eachLine)
	targetButton.config(text=open(filename,"r").read())


def refreshText(inputTextClass):
	""" Use textInput Class for inputTextClass """
    
	pushData = open(inputTextClass.fileDirectory,"w")

    for lineCounter in range(inputTextClass.length):
        pushData.write(inputTextClass.fileWrite[lineCounter])

def refreshOutput(inputTextClass):

    ThruPut = str(subprocess.check_output(["py",inputTextClass.filePY]))
    pullData = str(ThruPut[2:-1].replace("\\r\\n","\n"))
    pushData = open(inputTextClass.fileOutput,"w").write(pullData)
    return pullData


def FillTermsEx(textWindow,inputTextClass):
    inputTextClass.fileWrite = textWindow.get("1.0",END)
#            dataLine = inputTextClass.fileWrite.split('\n')
    pushData = open(inputTextClass.fileDirectory,"w")
    for eachLine in inputTextClass.fileWrite: #dataLine:
        pushData.write(eachLine)
        
def ReturnTermsEx(textWindow,inputTextClass):
    inputTextClass.fileWrite = textWindow.get("1.0",END)
#            dataLine = inputTextClass.fileWrite.split('\n')
    pushData = open(inputTextClass.filePY,"w")
    for eachLine in inputTextClass.fileWrite: #dataLine:
        pushData.write(eachLine)



def ExCombinedF5(textWindow, labelWindow, inputTextClass):
    textWindow.get("1.0",END)
    FillTermsEx(textWindow,inputTextClass)
    ReturnTermsEx(textWindow,inputTextClass)
    labelWindow.config(text=refreshOutput(inputTextClass))
    print(refreshOutput(inputTextClass))
    print('_____________')
    print(open(inputTextClass.fileOutput,"r").read().split('\\n'))

def ExCombinedF4(plotWindow,inputTextClass,self):
    GenerateNewPlot(inputTextClass)
    plotWindow= FigureCanvasTkAgg(f,self)
    plotWindow.draw()

def buttonFile(filename):
    buttonFileVal = filename



class SyntaxTutorialPython(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self,*args, **kwargs)
        tk.Tk.iconbitmap(self, 'HECML.ico')

        container = tk.Frame(self)
        container.grid(row=0, column = 0, columnspan= 200, sticky ="nsew")
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames={}

        for F in (StartPage, ExampleOne, ExampleTwo, ExampleThree, PracticumOne, PracticumTwo):
            frame = F(container,self)
            
            self.frames[F] = frame

            frame.grid(row=0,column=0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self,controller):

        frame = self.frames[controller]
        frame.tkraise()
        self.title("Python Syntax Tutorial")

class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text = "Start Page", font =LARGE_FONT)
        label.grid(row = 1, column = 0, pady=5, padx=10, sticky ="nsew")

        descriptionLabel = tk.Label(self, text = descriptorStart, font = normal_font, 
                                    bg='grey', bd = 2, relief = SUNKEN, width = 45, height =10)
        descriptionLabel.grid(row=1,column=3, rowspan = 11, columnspan = 3,
                             pady=40, padx=5, sticky ="nsew")
        displayLabel(descriptionLabel,'startText.txt', CENTER)
        

        buttonEx1 = ttk.Button(self, text="Example 1",
                               command = lambda: controller.show_frame(ExampleOne))
        buttonEx1.grid(row=2,column= 0, pady = 10, padx = 10, sticky='n')
        buttonEx1.bind("<Enter>",lambda _: displayLabel(descriptionLabel,'startExample1Text.txt',CENTER))
        buttonEx1.bind("<Leave>",lambda _: displayLabel(descriptionLabel,'startText.txt',CENTER))


        buttonEx2 = ttk.Button(self, text="Example 2",
                               command = lambda: controller.show_frame(ExampleTwo))
        buttonEx2.grid(row=4,column= 0, pady = 10, padx = 10)
        buttonEx2.bind("<Enter>",lambda _: displayLabel(descriptionLabel,'startExample2Text.txt',CENTER))
        buttonEx2.bind("<Leave>",lambda _: displayLabel(descriptionLabel,'startText.txt',CENTER))

        buttonEx3 = ttk.Button(self, text="Example 3",
                               command = lambda: controller.show_frame(ExampleThree))
        buttonEx3.grid(row=6,column = 0, pady = 10, padx = 10)
        buttonEx3.bind("<Enter>",lambda _: displayLabel(descriptionLabel,'startExample3Text.txt',CENTER))
        buttonEx3.bind("<Leave>",lambda _: displayLabel(descriptionLabel,'startText.txt',CENTER))

        buttonPr1 = ttk.Button(self, text="Practicum 1", 
                               command = lambda: controller.show_frame(PracticumOne))
        buttonPr1.grid(row=8,column = 0, pady = 10, padx = 10)
        buttonPr1.bind("<Enter>",lambda _: displayLabel(descriptionLabel,'startPracticum1Text.txt',CENTER))
        buttonPr1.bind("<Leave>",lambda _: displayLabel(descriptionLabel,'startText.txt',CENTER))

        buttonPr2 = ttk.Button(self, text="Practicum 2", 
                               command = lambda: controller.show_frame(PracticumTwo))
        buttonPr2.grid(row=10,column = 0, pady = 10, padx = 10,sticky='s')
        buttonPr2.bind("<Enter>",lambda _: displayLabel(descriptionLabel,'startPracticum2Text.txt',CENTER))
        buttonPr2.bind("<Leave>",lambda _: displayLabel(descriptionLabel,'startText.txt',CENTER))

        descriptionLabel = tk.Label(self, text = descriptorStart, font = normal_font, 
                                    bg='grey', bd = 2, relief = SUNKEN, width = 45, height =10)
        descriptionLabel.grid(row=1,column=3, rowspan = 11, columnspan = 3,
                             pady=40, padx=5, sticky ="nsew")
        displayLabel(descriptionLabel,'startText.txt', CENTER)
        
            # Icon

        iconPhoto = PhotoImage(file='HECMLsmall.png')
        iconPhotoLabel = Label(self, image=iconPhoto)
        iconPhotoLabel.image = iconPhoto
        iconPhotoLabel.grid(row=2,column=10, pady=00, padx=40, rowspan = 8, sticky="nsew")

        
class ExampleOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text = "Example 1", font =LARGE_FONT)
        label.grid(row = 1, column = 0, pady=10, padx=10)

        buttonEx1 = ttk.Button(self, text="Start Page", 
                               command = lambda: controller.show_frame(StartPage))
        buttonEx1.grid(row=2,column= 0)


        textWindowEx1 = Text(self, bg = "black", fg = "green", font=LARGE_FONT, #height = 30,
                          width = 35, wrap = WORD, relief=SUNKEN, padx=00,pady=00, spacing3=1,
                          bd=5, insertbackground = "white")
        textWindowEx1.insert(INSERT,"## User Input Below ##")
        textWindowEx1.insert(INSERT,"\n## Press F5 to run ##")
        textWindowEx1.grid(row=3, column=2, rowspan= 22, padx =20, sticky = "nsew")
        
        
        textWindowEx1.bind('<F5>',lambda _: ExCombinedF5(textWindowEx1,labelExampleEx1,ModEx1))
                
        
        labelWindowEx1 = Label(self, bg= "black", fg = "green", font=LARGE_FONT, bd=5,
                               width = 35, relief = SUNKEN)
        labelWindowEx1.grid(row=3, column=3,rowspan = 22, sticky = "nsew")

        
        labelExampleEx1 = Label(self, bg= "black", fg = "green", font=LARGE_FONT, bd=5,
                               width = 35, relief = SUNKEN, padx =20,
                              text =" ", 
                              anchor=NW, justify = LEFT)

        labelExampleEx1.grid(row=3, column=3,rowspan = 22, sticky = "nsew")

        exampleWindowEx1 = Label(self, bg= "black", fg = "green", font=LARGE_FONT, bd=5,
                               width = 35, relief = SUNKEN, padx =20)
        displayLabel(exampleWindowEx1,'exampleExercise1.txt',LEFT)
        exampleWindowEx1.grid(row=3, column=5, rowspan =22, sticky="nsew")


            
        
class ExampleTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text = "Example 2", font =LARGE_FONT)
        label.grid(row = 1, column = 0, pady=10, padx=10)

        buttonEx2 = ttk.Button(self, text="Start Page", 
                               command = lambda: controller.show_frame(StartPage))
        buttonEx2.grid(row=2,column= 0)


        textWindowEx2 = Text(self, bg = "black", fg = "green", font=LARGE_FONT, #height = 30,
                          width = 35, wrap = WORD, relief=SUNKEN, padx=00,pady=00, spacing3=1,
                          bd=5, insertbackground = "white")
        textWindowEx2.insert(INSERT,"## User Input Below ##")
        textWindowEx2.insert(INSERT,"\n## Press F5 to run ##")
        textWindowEx2.grid(row=3, column=2, rowspan= 22, padx =20, sticky = "nsew")
        
        
        textWindowEx2.bind('<F5>',lambda _: ExCombinedF5(textWindowEx2,labelExampleEx2,ModEx2))
                
        
        labelWindowEx2 = Label(self, bg= "black", fg = "green", font=LARGE_FONT, bd=5,
                               width = 35, relief = SUNKEN)
        labelWindowEx2.grid(row=3, column=3,rowspan = 22, sticky = "nsew")

        
        labelExampleEx2 = Label(self, bg= "black", fg = "green", font=LARGE_FONT, bd=5,
                               width = 35, relief = SUNKEN, padx =20,
                              text =" ", 
                              anchor=NW, justify = LEFT)

        labelExampleEx2.grid(row=3, column=3,rowspan = 22, sticky = "nsew")

        exampleWindowEx2 = Label(self, bg= "black", fg = "green", font=LARGE_FONT, bd=5,
                               width = 35, relief = SUNKEN, padx =20)
        displayLabel(exampleWindowEx2,'exampleExercise2.txt',LEFT)
        exampleWindowEx2.grid(row=3, column=5, rowspan =22, sticky="nsew")

        
class ExampleThree(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text = "Example 3", font =LARGE_FONT)
        label.grid(row = 1, column = 0, pady=10, padx=10)

        buttonEx3 = ttk.Button(self, text="Start Page", 
                               command = lambda: controller.show_frame(StartPage))
        buttonEx3.grid(row=2,column= 0)


        textWindowEx3 = Text(self, bg = "black", fg = "green", font=LARGE_FONT, #height = 30,
                          width = 35, wrap = WORD, relief=SUNKEN, padx=00,pady=00, spacing3=1,
                          bd=5, insertbackground = "white")
        textWindowEx3.insert(INSERT,"## User Input Below ##")
        textWindowEx3.insert(INSERT,"\n## Press F5 to run ##")
        textWindowEx3.grid(row=3, column=2, rowspan= 22, padx =20, sticky = "nsew")
        
        
        textWindowEx3.bind('<F5>',lambda _: ExCombinedF5(textWindowEx3,labelExampleEx3,ModEx3))
                
        
        labelWindowEx3 = Label(self, bg= "black", fg = "green", font=LARGE_FONT, bd=5,
                               width = 35, relief = SUNKEN)
        labelWindowEx3.grid(row=3, column=3,rowspan = 22, sticky = "nsew")

        
        labelExampleEx3 = Label(self, bg= "black", fg = "green", font=LARGE_FONT, bd=5,
                               width = 35, relief = SUNKEN, padx =20,
                              text =" ", 
                              anchor=NW, justify = LEFT)

        labelExampleEx3.grid(row=3, column=3,rowspan = 22, sticky = "nsew")

        exampleWindowEx3 = Label(self, bg= "black", fg = "green", font=LARGE_FONT, bd=5,
                               width = 35, relief = SUNKEN, padx =20)
        displayLabel(exampleWindowEx3,'exampleExercise3.txt',LEFT)
        exampleWindowEx3.grid(row=3, column=5, rowspan =22, sticky="nsew")

        
class PracticumOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text = "Practicum 1", font =LARGE_FONT)
        label.grid(row = 1, column = 0, pady=10, padx=10)

        buttonPr1 = ttk.Button(self, text="Start Page", 
                               command = lambda: controller.show_frame(StartPage))
        buttonPr1.grid(row=2,column= 0)


        textWindowPr1 = Text(self, bg = "black", fg = "green", font=LARGE_FONT, #height = 30,
                          width = 35, wrap = WORD, relief=SUNKEN, padx=00,pady=00, spacing3=1,
                          bd=5, insertbackground = "white")
        textWindowPr1.insert(INSERT,"## User Input Below ##")
        textWindowPr1.insert(INSERT,"\n## Press F5 to run ##")
        textWindowPr1.grid(row=3, column=2, rowspan= 22, padx =20, sticky = "nsew")
        
        
        textWindowPr1.bind('<F5>',lambda _: ExCombinedF5(textWindowPr1,labelExamplePr1,ModPr1))
                
        
        labelWindowPr1 = Label(self, bg= "black", fg = "green", font=LARGE_FONT, bd=5,
                               width = 35, relief = SUNKEN)
        labelWindowPr1.grid(row=3, column=3,rowspan = 22, sticky = "nsew")

        
        labelExamplePr1 = Label(self, bg= "black", fg = "green", font=LARGE_FONT, bd=5,
                               width = 35, relief = SUNKEN, padx =20,
                              text =" ", 
                              anchor=NW, justify = LEFT)

        labelExamplePr1.grid(row=3, column=3,rowspan = 22, sticky = "nsew")

        exampleWindowPr1 = Label(self, bg= "black", fg = "green", font=LARGE_FONT, bd=5,
                               width = 35, relief = SUNKEN, padx =20)
        displayLabel(exampleWindowPr1,'examplePracticum1.txt',LEFT)
        exampleWindowPr1.grid(row=3, column=5, rowspan =22, sticky="nsew")

        
class PracticumTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text = "Practicum 2", font =LARGE_FONT)
        label.grid(row = 1, column = 0, pady=10, padx=10)

        buttonPr2 = ttk.Button(self, text="Start Page", 
                               command = lambda: controller.show_frame(StartPage))
        buttonPr2.grid(row=2,column= 0)


        textWindowPr2 = Text(self, bg = "black", fg = "green", font=LARGE_FONT, #height = 30,
                          width = 35, wrap = WORD, relief=SUNKEN, padx=00,pady=00, spacing3=1,
                          bd=5, insertbackground = "white")
        textWindowPr2.insert(INSERT,"## User Input Below ##")
        textWindowPr2.insert(INSERT,"\n## Press F5 to run ##")
        textWindowPr2.grid(row=3, column=2, rowspan= 22, padx =20, sticky = "nsew")
        
        
        textWindowPr2.bind('<F5>',lambda _: ExCombinedF5(textWindowPr2,labelExamplePr2,ModPr2))
                
        
        labelWindowPr2 = Label(self, bg= "black", fg = "green", font=LARGE_FONT, bd=5,
                               width = 35, relief = SUNKEN)
        labelWindowPr2.grid(row=3, column=3,rowspan = 22, sticky = "nsew")

        
        labelExamplePr2 = Label(self, bg= "black", fg = "green", font=LARGE_FONT, bd=5,
                               width = 35, relief = SUNKEN, padx =20,
                              text =" ", 
                              anchor=NW, justify = LEFT)

        labelExamplePr2.grid(row=3, column=3,rowspan = 22, sticky = "nsew")

        exampleWindowPr2 = Label(self, bg= "black", fg = "green", font=LARGE_FONT, bd=5,
                               width = 35, relief = SUNKEN, padx =20)
        displayLabel(exampleWindowPr2,'examplePracticum2.txt',LEFT)
        exampleWindowPr2.grid(row=3, column=5, rowspan =22, sticky="nsew")

        
def PlaceHolder():
    print("I DO NOTHING!")


root = SyntaxTutorialPython()

root.title("Python Syntax Tutorial")


menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit Program", command = root.destroy)
subMenu.add_command(label="Return to Main", command = lambda: controller.show_frame(StartPage))
subMenu.add_separator()
subMenu.add_command(label="Reset Module")

navigationMenu = Menu(menu)
menu.add_cascade(label="Navigation", menu=navigationMenu)
navigationMenu.add_command(label="StartPage", command=lambda: controller.show_frame(StartPage))
navigationMenu.add_command(label="Example 1", command=lambda: controller.show_frame(ExampleOne))
navigationMenu.add_command(label="Example 2", command=PlaceHolder)
navigationMenu.add_command(label="Example 3", command=PlaceHolder)
navigationMenu.add_command(label="Practicum 1", command=PlaceHolder)
navigationMenu.add_command(label="Practicum 2", command=PlaceHolder)
navigationMenu.add_command(label="Easter Egg", command= root.destroy)


# Toolbar


toolbar = Frame(root, bg="grey", bd=1, width = 200)

fillerButt = Button(toolbar, text="Toolbar Place Holder Button", command = PlaceHolder)
fillerButt.grid(row = 0, column = 0, padx = 2, pady = 2, columnspan = 2)
insertButt = Button(toolbar, text="Insert Nothing", command = PlaceHolder)
insertButt.grid(row = 0, column = 3, padx = 2, pady=2, columnspan = 2)
toolbarLabel = Label(toolbar, text ="", anchor=W, width = 163, bg = "grey")
toolbarLabel.grid(row=0, column = 5, )

toolbar.grid(row=0, column=0, columnspan = 200, sticky ="nw")


# Status Bar

status = Label(root, text="Si Hoc Videas Vicero", bd=1, relief=SUNKEN,
              anchor=W, width = 200)
status.grid(row=100,column = 0,columnspan=200,sticky ="s")



print(root.grid_size())


#app = MainFrame(root)
root.mainloop()


