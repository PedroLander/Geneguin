from tkinter import ttk
import tkinter as tk

class MapCanvas(tk.Canvas): 
	def __init__(self,parent):
		super().__init__()
		self.configure(bg='black')
		self.bind("<Configure>", self.on_resize)
		self.height = self.winfo_reqheight()
		self.width = self.winfo_reqwidth()
        
	def on_resize(self,event):
		# determine the ratio of old width/height to new width/height
		wscale = float(event.width)/self.width
		hscale = float(event.height)/self.height
		self.width = event.width
		self.height = event.height
		# resize the canvas 
		self.config(width=self.width, height=self.height)
		# rescale all the objects tagged with the "all" tag
		self.scale("all",0,0,wscale,hscale)

if __name__=="__main__":
	root = tk.Tk()
	root.title('Canvas1 Widget')
	root.geometry('600x400')
	root.configure(bg = 'green')

	canvas1 = MyCanvas(root)
	canvas1.pack(fill = 'both', expand = True)

	root.mainloop()



class SeqCanvas(tk.Canvas): 
	def __init__(self,parent):
		super().__init__()
		self.configure(bg='black')
	
	def on_resize(self,event):
		# determine the ratio of old width/height to new width/height
		wscale = float(event.width)/self.width
		hscale = float(event.height)/self.height
		self.width = event.width
		self.height = event.height
		# resize the canvas 
		self.config(width=self.width, height=self.height)
		# rescale all the objects tagged with the "all" tag
		self.scale("all",0,0,wscale,hscale)


if __name__=="__main__":
	root = tk.Tk()
	root.title('Canvas1 Widget')
	root.geometry('600x400')
	root.configure(bg = 'green')

	canvas1 = MyCanvas(root)
	canvas1.pack(fill = 'both', expand = True)

	root.mainloop()
