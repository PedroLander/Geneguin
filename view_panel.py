import tkinter as tk
from tkinter import ttk
from view import MyView

class ViewPanel(ttk.Notebook):
	def __init__(self, parent, *args, **kwargs):
		super().__init__()
		

if __name__=="__main__":
	root = tk.Tk()
	root.geometry('600x400')
	root.title('ViewPanel Widget')

	myViewPanel1= ViewPanel(root)
	myViewPanel1.pack(fill = 'both', expand = True)

	root.mainloop()
