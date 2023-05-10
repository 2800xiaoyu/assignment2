# -*- coding: utf-8 -*-
"""
Created on Sun May  7 10:44:40 2023

@author: xiaoyu
"""

import tkinter as tk
from tkinter import ttk
import math
import my_modules.io as io
import matplotlib
matplotlib.use('Qt5Agg')
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as TkAgg
import doctest

def exiting():
    """
    Exit the program.
    """
    root.quit()
    root.destroy()
    """
    Exit the program.
    """
    root.quit()
    try:
        root.destroy()
    except Exception:
        pass

# Define a function to output the final result and save them into a file
def output():
    io.write_data('../data/output/rescaled.txt', rescaled)
    gw = scale1.get()
    tw = scale2.get()
    pw = scale3.get()
    plot(True, gw, tw, pw)
    print('output success')

# Define a function for testing
def weight_and_add(geology, transport, population, gw, tw, pw):
    output = []
    min_value = math.inf
    max_value = 0
    n_rows = len(geology)
    n_cols = len(geology[0])
    for i in range(n_rows):
        output_row = [] # Create a one-dimensional list in loop
        for j in range(n_cols):
            # Weighted raster = geology * geology_factor + transport * transport_factor + population * population_factor
            wr = geology[i][j]*gw + transport[i][j]*tw + population[i][j]*pw
            min_value = min(wr, min_value) # Find min value in loop for rescaling
            max_value = max(wr, max_value) # Find max value in loop for rescaling
            output_row.append(wr)
        output.append(output_row)
    return output
    
# Initialise data
p0 = None   
# Define a function to plot weighted raster 
def plot(do_output, gw, tw, pw):
    """
    Redraws the canvas

    """
    figure = plt.figure(figsize=(6, 6))
    figure.clear()
    
    canvas.figure= figure
    canvas.draw()
    
    # Weight and addition
    # Create a two-dimensional list to store weighted results
    output = []
    min_value = math.inf
    max_value = 0
    for i in range(n_rows):
        output_row = [] # Create a one-dimensional list in loop
        for j in range(n_cols):
            # Weighted raster = geology * geology_factor + transport * transport_factor + population * population_factor
            wr = geology[i][j]*gw + transport[i][j]*tw + population[i][j]*pw
            min_value = min(wr, min_value) # Find min value in loop for rescaling
            max_value = max(wr, max_value) # Find max value in loop for rescaling
            output_row.append(wr)
        output.append(output_row)

    # Rescale resulting raster to have values in the range [0,255]
    # Create a two-dimensional list to store final results
    global rescaled
    rescaled = []
    for i in range(n_rows):
        rescaled_output = [] # Create a one-dimensional list in loop
        for j in range(n_cols):
            # Rescaled result = (Old_value - minimum_value) / (maximum_value - minimum_value ) * 255
            final_result = (output[i][j] - min_value) / (max_value - min_value) * 255
            rescaled_output.append(final_result)
        rescaled.append(rescaled_output)
    plt.imshow(rescaled)

    if do_output:
        filename = '../data/output/image.png'
        # filename = 'C:/Users/xiaoyu/programming/data/output/images/image' + str(ite) + '.gif    
        plt.savefig(filename)
        
    canvas.figure = figure
    canvas.draw()
    plt.close(figure)

def update(x):
    """
    Updates canvas and scale_label

    Parameters
    ----------
    x : Number.

    Returns
    -------
    None.

    """
    
    
    gw = float(scale1.get())
    tw = float(scale2.get())
    pw = float(scale3.get())
    scale1_label.config(text="Geology: " + str(round(gw,2)))
    scale2_label.config(text="Transport:" + str(round(tw,2)))
    scale3_label.config(text="Population:" + str(round(pw,2)))
    plot(False, gw, tw, pw)
    
if __name__ == '__main__':
    
    # Test
    doctest.testmod()
    
    # Initialise figure for results
    figure = plt.figure(figsize=(5, 5))
    
    # Read data from io
    # Read Geology
    geology, n_rows, n_cols = io.read_data('../data/input/geology.txt')
    
    # Read Transport
    transport, n_rows, n_cols = io.read_data('../data/input/Transport.txt')
    
    # Read Population
    population, n_rows, n_cols = io.read_data('../data/input/Population.txt')
    
    # Define the weight of each factor and initialise them
    gf = 0.5
    tf = 0.2
    pf = 0.3
    
    # GUI
    # Create a GUI called "Site Suitability Weight"
    root = tk.Tk()
    root.title("Site Suitability Weight")
    
    # Import three rasters into GUI
    # Factors raster
    figure1, axs= plt.subplots(1, 3, figsize = (9, 4))
    # Create the first subplot in figure
    #ax1 = figure1.add_subplot()
    axs[0].imshow(geology)
    axs[0].set_title('Geology')
    
    # Create the second subplot in figure
    #ax2 = figure1.add_subplot()
    axs[1].imshow(transport)
    axs[1].set_title('Transport')
    
    # Create the third subplot in figure
    #ax3 = figure1.add_subplot()
    axs[2].imshow(population)
    axs[2].set_title('Population')
    
    # Create a new frame for displaying rasters
    frame_1 = tk.Frame(master=root, padx=20, pady=20)
    frame_1.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor=tk.CENTER)
    
    canvas1 = TkAgg(figure1, master=frame_1)
    canvas1._tkcanvas.pack()
    canvas1.draw()
    plt.close(figure1)
    
    # Create a canvas to display the figure
    # Result canvas
    canvas = TkAgg(figure, master=root)
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    plt.close(figure)
    
    # Define the StringVars to store the scale values
    scale1_value = tk.StringVar()
    scale2_value = tk.StringVar()
    scale3_value = tk.StringVar()
    
    # Create the scales
    # Scale for geology
    scale1 = ttk.Scale(root, from_=0, to=1, command=update)
    scale1.pack()
    scale1_label = ttk.Label(root)
    scale1_label.pack()
    
    # Scale for transport
    scale2 = ttk.Scale(root, from_=0, to=1, command=update)
    scale2.pack()
    scale2_label = ttk.Label(root)
    scale2_label.pack()
    
    # Scale for population
    scale3 = ttk.Scale(root, from_=0, to=1, command=update)
    scale3.pack()
    scale3_label = ttk.Label(root)
    scale3_label.pack()
    
    scale1.set(0)
    scale2.set(0)
    scale3.set(0)
    
    # Create a button widget and link this with output function
    output_button = ttk.Button(root, text="Output", command=output)
    output_button.pack()
    
    # Create a button widget and link this with the exiting function
    exit_button = ttk.Button(root, text="Exit", command=exiting)
    exit_button.pack()
    
    root.mainloop()