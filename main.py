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
			
		
class Toolbar(tk.Frame): 
	def __init__(self, parent, *args, **kwargs):
		tk.Frame.__init__(self, parent, *args, **kwargs)
		menubar = tk.Menu(root)
		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="New")#, command=donothing)
		filemenu.add_command(label="Open")#, command=load)
		filemenu.add_command(label="Save")#, command=save)
		filemenu.add_separator()
		filemenu.add_command(label="Exit",)# command=root.quit)
		menubar.add_cascade(label="File", menu=filemenu)

		editmenu = tk.Menu(menubar, tearoff=0)
		editmenu.add_command(label="Delete")#, command=dltlb1)
		menubar.add_cascade(label="Edit", menu=editmenu)

		toolmenu = tk.Menu(menubar, tearoff=0)
		toolmenu.add_command(label="Replicate",)# command=replicate)
		toolmenu.add_command(label="Transcribe")#, command=transcribe)
		toolmenu.add_command(label="Translate")#, command=translate)
		menubar.add_cascade(label="Tools", menu=toolmenu)

		helpmenu = tk.Menu(menubar, tearoff=0)
		helpmenu.add_command(label="Help Index")#, command=donothing)
		helpmenu.add_command(label="About...")#, command=donothing)
		menubar.add_cascade(label="Help", menu=helpmenu)
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
        self.toolbar = Toolbar(self)
        self.viewbar = Viewbar(self)
        self.statusbar = Statusbar(self)
        

        self.navbar.pack(side="left", fill="y", expand=True)
        self.toolbar.pack(side="top", fill="x")
        self.viewbar.pack(side="top", fill="x", expand=True)
        self.statusbar.pack(side="top", fill="x", expand=True)
        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('600x400')
    root.title('Geneguin')
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
