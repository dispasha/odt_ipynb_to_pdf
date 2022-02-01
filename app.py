import tkinter as tk
from tkinter import Frame, Tk,  END,  filedialog, Label, Entry, Button
from converter import convert

class ChooseFile(Frame):
 
    def __init__(self, mode = 'doc'):
        self.mode = mode
        super().__init__()
        self.initUI()
 
    def initUI(self):
        if self.mode == 'doc':
            lbl = Label(self, text="Choose document file:")
        else:
            lbl = Label(self, text="Choose jupyter notebook file:")
        
        lbl.grid(row = 0, column=0, sticky=tk.E)
        self.txt = Entry(self, width=60)  
        self.txt.grid(row = 0, column=1)
        btn = Button(self, text="Browse", command=self.onOpen)  
        btn.grid(row = 0,column = 3, padx=2, sticky=tk.W)

 
    def onOpen(self):
        if self.mode == 'doc':
            ftypes = [('OpenDocument file', ['.odt', '.odf'])]
        elif self.mode == 'jup':
            ftypes = [('IPython file', '.ipynb')]
        dlg = filedialog.Open(self, filetypes = ftypes)
        fl = dlg.show()
        self.txt.delete(0,END)
        self.txt.insert(0,fl)

def main():
    root = Tk()
    innerFrame = Frame(root)
    signone = Label(root, text = "Choose two files to merge them:").grid(column = 0, row = 0, padx=20, pady=50)
    docfile = ChooseFile(mode = 'doc')
    docfile.grid(column = 0, row = 1, padx=20, pady=5, sticky=tk.E)
    jupfile = ChooseFile(mode = 'jup')
    jupfile.grid(column = 0, row = 2, padx=20, pady=5, sticky=tk.E)
    btn = Button(root, command=lambda: convert(docfile.txt.get(), jupfile.txt.get()), text="convert").grid(column = 0, row = 3, padx=20, pady=5)
    root.geometry('640x300')
    root.title("IPynb + odt = ♡pdf♡")
    root.resizable(False,False)
    root.mainloop()
 
 
if __name__ == '__main__':
    main()