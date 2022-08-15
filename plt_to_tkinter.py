from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTk

from dna_features_viewer2 import GraphicFeature, GraphicRecord


  
# plot function is created for 
# plotting the graph in 
# tkinter window
def plot():
  
    # the figure that will contain the plot
    fig = Figure(figsize = (5, 5),
                 dpi = 100)
  
    # list of squares
    y = [i**2 for i in range(101)]
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(y)
    
    
    features=[
    GraphicFeature(start=0, end=20, strand=+1, color="#ffd700",
                   label="Small feature"),
    GraphicFeature(start=20, end=500, strand=+1, color="#ffcccc",
                   label="Gene 1 with a very long name"),
    GraphicFeature(start=400, end=700, strand=-1, color="#cffccc",
                   label="Gene 2"),
    GraphicFeature(start=600, end=900, strand=+1, color="#ccccff",
                   label="Gene 3")
]
    record = GraphicRecord(sequence_length=1000, features=features)
    record.plot(figure_width=5)
    
    
    
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTk(record, master = window)
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
  
# the main Tkinter window
window = Tk()
  
# setting the title 
window.title('Plotting in Tkinter')
  
# dimensions of the main window
window.geometry("500x500")
  
# button that displays the plot
plot_button = Button(master = window, 
                     command = plot,
                     height = 2, 
                     width = 10,
                     text = "Plot")
  
# place the button 
# in main window
plot_button.pack()
  
# run the gui
window.mainloop()
