import tkinter as tk
from tkinter import ttk
from view import MyView

class ControlPanel(ttk.Notebook):
	def __init__(self, parent, *args, **kwargs):
		super().__init__()
		

if __name__=="__main__":
	root = tk.Tk()
	root.geometry('600x400')
	root.title('ViewPanel Widget')

	myControlPanel1= ControlPanel(root)
	myControlPanel1.pack(fill = 'both', expand = True)

	root.mainloop()
