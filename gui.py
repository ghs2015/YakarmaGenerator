from tkinter import *
from tkinter.ttk import Frame, Button, Style
from PIL import ImageTk, Image

from crawler import crawlupdate, crawlinit
from tester import runner
import time
import os

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Buttons")
        self.style = Style()
        self.style.theme_use("default")
        
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)
        
        self.pack(fill=BOTH, expand=1)

        def yakTime():
            for i in range(0, 20):
                time.sleep(float(float(E1.get())*60))
                (runner())
        
        closeButton = Button(self, text="Quit", command = self.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        resetButton = Button(self, text="Reset", command = crawlinit)
        resetButton.pack(side=RIGHT, padx=5, pady=5)
        updateButton = Button(self, text = 'Update', command = crawlupdate)
        updateButton.pack(side=RIGHT, padx=5, pady=5)
        timeButton = Button(self, text = 'MPY', command = yakTime)
        timeButton.pack(side = RIGHT, padx = 5, pady = 5)
        E1 = Entry(self, bd = 5)
        E1.pack(side=RIGHT)
        okButton = Button(self, text="Run", command = runner)
        okButton.pack(side=RIGHT)
        img = ImageTk.PhotoImage(Image.open("logo.gif"))
        panel = Label(self, image = img)
        panel.image=img
        panel.place(x=100, y= 5)

     

def main():
  
    root = Tk()
    root.geometry("600x450+600+600")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()