from tkinter import ttk
import tkinter as tk
from tkinter import ALL, EventType

class SeqCanvas(tk.Canvas): 
	def __init__(self,parent):
		super().__init__()
		self.configure(bg='black')

		self.bind('<ButtonPress-1>', lambda event: self.scan_mark(event.x, event.y))
		self.bind("<B1-Motion>", lambda event: self.scan_dragto(event.x, event.y, gain=1))


if __name__=="__main__":
	root = tk.Tk()
	root.title('Canvas1 Widget')
	root.geometry('600x400')
	root.configure(bg = 'green')

	canvas1 = MapCanvas(root)
	canvas1.pack(fill = 'both', expand = True)

	root.mainloop()
