import tkinter as tk
from tkinter import ttk
import tools

# create a treeview
class NavPanel(ttk.Treeview): 
	def __init__(self, parent):
		super().__init__()
		
		self.heading('#0', text='Documents', anchor=tk.W)

		self.bind('<Double-1>', self.on_dclick)

	def add_data(self, filename, seqs):
		self.insert('', tk.END, text=filename, iid=filename, open=False)
		child = -1
		for seq in seqs:
			child+=1
			self.insert('', tk.END, text=seq, iid=seq, open=False)
			self.move(seq, filename, child)

	def on_dclick(self, event):
		selection = self.selection()
		tools.load_sequence(selection)


if __name__=="__main__":
	root = tk.Tk()
	root.title('NavigationPanel Widget')
	root.geometry('300x300')
	
	navPanel1 = NavPanel(root)
	navPanel1.pack(side='left', fill='y', expand=True)

	root.mainloop()
