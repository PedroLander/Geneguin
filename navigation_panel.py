import tkinter as tk
from tkinter import ttk
import tools

# create a treeview
class NavPanel(ttk.Treeview): 
	def __init__(self, parent):
		super().__init__()
		
		self.heading('#0', text='Documents', anchor=tk.W)

		self.bind('<Double-1>', self.on_dclick)

		# # adding data
		# self.insert('', tk.END, text='Folder 1', iid=0, open=False)
		# self.insert('', tk.END, text='Folder 2', iid=1, open=False)
		# self.insert('', tk.END, text='Folder 3', iid=2, open=False)
		# self.insert('', tk.END, text='Folder 4', iid=3, open=False)

		# # adding children of first node
		# self.insert('', tk.END, text='File 1', iid=5, open=False)
		# self.insert('', tk.END, text='File 2' ,iid=6, open=False)
		# self.move(5, 1, 0)
		# self.move(6, 1, 1)
		

	def add_data(self, filename, seqs):
		self.insert('', tk.END, text=filename, iid=filename, open=False)
		child = -1
		for seq in seqs:
			child+=1
			self.insert('', tk.END, text=seq, iid=seq, open=False)
			self.move(seq, filename, child)

	def on_dclick(self, event):
		selection = self.selection()
		print('Selection is %s' % ascii(selection))
		tools.load_nuc_sequence(selection)
		tools.load_map_sequence(selection)


if __name__=="__main__":
	root = tk.Tk()
	root.title('NavigationPanel Widget')
	root.geometry('300x300')
	
	navPanel1 = NavPanel(root)
	navPanel1.pack(side='left', fill='y', expand=True)

	root.mainloop()
