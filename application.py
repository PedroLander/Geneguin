# From https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application
# ------------------------------------------------

# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class Navbar(tk.Frame): 
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		
		#Tabs
		# create a treeview
		tree = ttk.Treeview(self)
		
		tree.heading('#0', text='Documents', anchor=tk.W)
		
		# adding data
		tree.insert('', tk.END, text='Folder 1', iid=0, open=False)
		tree.insert('', tk.END, text='Folder 2', iid=1, open=False)
		tree.insert('', tk.END, text='Folder 3', iid=2, open=False)
		tree.insert('', tk.END, text='Folder 4', iid=3, open=False)
		
		# adding children of first node
		tree.insert('', tk.END, text='File 1', iid=5, open=False)
		tree.insert('', tk.END, text='File 2' ,iid=6, open=False)
		tree.move(5, 1, 0)
		tree.move(6, 1, 1)

		tree.pack(side='left', fill='y', expand=True)
		
class Viewbar(tk.Frame): 
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		#Tabs
		# create a notebook
		notebook = ttk.Notebook(self)
		notebook.pack(pady=10, expand=True)
		
		# create frames
		frame1 = ttk.Frame(notebook, width=400, height=280)
		frame2 = ttk.Frame(notebook, width=400, height=280)
		
		frame1.pack(fill='both', expand=True)
		frame2.pack(fill='both', expand=True)
		
		# add frames to notebook
		notebook.add(frame1, text='View 1')
		notebook.add(frame2, text='View2')
		
class Menubar(tk.Menu): 
	def __init__(self, parent, *args, **kwargs):
		tk.Menu.__init__(self, parent, *args, **kwargs)
		
		self.filemenu = tk.Menu(self, tearoff=0)
		self.filemenu .add_command(label="New")#, command=donothing)
		self.filemenu .add_command(label="Open")#, command=load)
		self.filemenu .add_command(label="Save")#, command=save)
		self.filemenu .add_separator()
		self.filemenu .add_command(label="Exit", command=self.quit)
		self.add_cascade(label="File", menu=self.filemenu)

		self.editmenu = tk.Menu(self, tearoff=0)
		self.editmenu.add_command(label="Delete")#, command=dltlb1)
		self.add_cascade(label="Edit", menu=self.editmenu)

		self.toolmenu = tk.Menu(self, tearoff=0)
		self.toolmenu.add_command(label="Replicate",)# command=replicate)
		self.toolmenu.add_command(label="Transcribe")#, command=transcribe)
		self.toolmenu.add_command(label="Translate")#, command=translate)
		self.add_cascade(label="Tools", menu=self.toolmenu)

		self.helpmenu = tk.Menu(self, tearoff=0)
		self.helpmenu.add_command(label="Help Index")#, command=donothing)
		self.helpmenu.add_command(label="About...")#, command=donothing)
		self.add_cascade(label="Help", menu=self.helpmenu)
		
class Statusbar(tk.Frame): 
		def __init__(self, parent, *args, **kwargs):
			tk.Frame.__init__(self, parent, *args, **kwargs)
			
			#Tabs
			# create a notebook
			notebook = ttk.Notebook(self)
			notebook.pack(pady=10, expand=True)
			
			# create frames
			frame1 = ttk.Frame(notebook, width=400, height=280)
			frame2 = ttk.Frame(notebook, width=400, height=280)
			frame3 = ttk.Frame(notebook, width=400, height=280)
			
			frame1.pack(fill='both', expand=True)
			frame2.pack(fill='both', expand=True)
			frame3.pack(fill='both', expand=True)
			
			# add frames to notebook
			notebook.add(frame1, text='Status')
			notebook.add(frame2, text='Messages')
			notebook.add(frame3, text='Terminal')

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.navbar = Navbar(self)
        self.viewbar = Viewbar(self)
        self.statusbar = Statusbar(self)
        
        self.navbar.pack(side="left", fill="y", expand=True)
        self.viewbar.pack(side="top", fill="x", expand=True)
        self.statusbar.pack(side="top", fill="x", expand=True)
