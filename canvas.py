from tkinter import ttk
import tkinter as tk

class MyCanvas(tk.Canvas): 
	def __init__(self,parent):
		super().__init__()
		self.configure(bg='black')

if __name__=="__main__":
	root = tk.Tk()
	root.title('Canvas1 Widget')
	root.geometry('600x400')
	root.configure(bg = 'green')

	canvas1 = MyCanvas(root)
	canvas1.pack(fill = 'both', expand = True)

	root.mainloop()
