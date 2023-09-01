# GUI
import tkinter as tk

#Programs
import averagefinder
import backgroundremover
import grapher
import timesplitter
import timesplitterMS
import integrator 

def execute():
    restT.get()
    pulseT.get()
    offset.get()
    initialT.get()
    finalT.get()
    start.get()
    stop.get()

    if(CheckAverageFinder.get()):
        averagefinder.main(float(start.get()),float(stop.get()))
    if(CheckBackgroundRemover.get()):
        backgroundremover.main(restT.get(), pulseT.get(), offset.get(), initialT.get(), finalT.get())
    if(CheckGraph.get()):
        grapher.main()
    if(CheckSplitterV.get()):
        timesplitter.main(restT.get(), pulseT.get(), initialT.get(),finalT.get())
    if(CheckSplitterMS.get()):
        timesplitterMS.main(restT.get(), pulseT.get(), offset.get(), initialT.get(), finalT.get())
    if(CheckIntegrate.get()):
        integrator.main()


# Create the tkinter window
top = tk.Tk()

# Set the window title
top.title("Program Options")

# Input Variables
restT = tk.StringVar()
pulseT = tk.StringVar()
offset = tk.StringVar()
initialT = tk.StringVar()
finalT = tk.StringVar()
start = tk.StringVar()
stop = tk.StringVar()

# Checkboxes Variables
CheckAverageFinder = tk.IntVar()
CheckBackgroundRemover = tk.IntVar()
CheckGraph = tk.IntVar()
CheckSplitterV = tk.IntVar()
CheckSplitterMS = tk.IntVar()
CheckIntegrate = tk.IntVar()

# Input Labels
restT_label = tk.Label(top, text="Rest Time:")
pulseT_label = tk.Label(top, text="Pulse Time:")
offset_label = tk.Label(top, text="Offset:")
initialT_label = tk.Label(top, text="Initial Time:")
finalT_label = tk.Label(top, text="Final Time:")
start_label = tk.Label(top, text="Start:")
stop_label = tk.Label(top, text="Stop:")


# Input Entry Fields
restT_entry = tk.Entry(top, textvariable=restT)
pulseT_entry = tk.Entry(top, textvariable=pulseT)
offset_entry = tk.Entry(top, textvariable=offset)
initialT_entry = tk.Entry(top, textvariable=initialT)
finalT_entry = tk.Entry(top, textvariable=finalT)

start = tk.Entry(top, textvariable=start)
stop = tk.Entry(top, textvariable=stop)

# Checkbox Labels
checkbox_average = tk.Checkbutton(top, text="Average Current", variable=CheckAverageFinder)
checkbox_background_remover = tk.Checkbutton(top, text="Background Remover", variable=CheckBackgroundRemover)
checkbox_graph = tk.Checkbutton(top, text="Graph", variable=CheckGraph)
checkbox_splitterV = tk.Checkbutton(top, text="SplitterV", variable=CheckSplitterV)
checkbox_splitterMS = tk.Checkbutton(top, text="SplitterMS", variable=CheckSplitterMS)
checkbox_integrate = tk.Checkbutton(top, text="Integrate", variable=CheckIntegrate)

# Grid Layout
restT_label.grid(row=0, column=0)
pulseT_label.grid(row=0, column=1)
offset_label.grid(row=0, column=2)
initialT_label.grid(row=0, column=3)
finalT_label.grid(row=0, column=4)

restT_entry.grid(row=1, column=0)
pulseT_entry.grid(row=1, column=1)
offset_entry.grid(row=1, column=2)
initialT_entry.grid(row=1, column=3)
finalT_entry.grid(row=1, column=4)

checkbox_average.grid(row=2, column=1)
start_label.grid(row=2, column = 2)
start.grid(row=3,column=2)
stop_label.grid(row=2, column = 3)
stop.grid(row=3,column=3)

checkbox_background_remover.grid(row=4, column=2)
checkbox_graph.grid(row=5, column=2)
checkbox_splitterV.grid(row=6, column=2)
checkbox_splitterMS.grid(row=7, column=2)
checkbox_integrate.grid(row=8, column=2)

runProgram = tk.Button(top, text = "Run specified programs", command = execute)
runProgram.grid(row=9, column = 2)

# Start the tkinter event loop
top.mainloop()