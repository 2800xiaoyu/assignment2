# Assignment2
This distribution contains data (initial raster and output data), source code, a document with testing explanation and other issues, a LICENCE and a README with software introduction.
README file focuses on explaining how to run and what to expect when it runs.
The document focuses on test explanation and major issues encountered during development and how these were overcome (or not).
The src file contains source codes, and documentation/comments are added in it.
The data file contains input data and output result.
The words in the document and README are around 2100 in total.

# Introduction
The software uses three raster data in UK as input to calculate and show a suitable location of a rock aggregate factory. The value in each raster is a two-dimensional array which has a range of [0, 255]. The raster data represents geology, transport and population respectively and the higher the value of a factor is, the more suitable the location is for the factory.

# Instruction
The software works based on two Python files: model.py and io.py. The main working space is in model.py and io.py file is created to input initial raster data and output the final results.

Once clicking ‘run’ button, a GUI window will appear, which contains three raster files displayed in a canvas and an empty area for final results combined with three factor scales and two operator buttons. In the left canvas, three factors for factory location selection, geology, transport and population are displayed. And in the right empty canvas, the final result will be displayed after weighting factors by using scales. Users can use three sliders to change the weights of each factor and each of factor’s value can be seen on the right of slider. Users can define each slider’s value by looking at the sign on the right. Once they have decided three weights, they can click ‘Output’ button at the bottom. The final result can be output into a file called ‘output’. The output function can be used repeatedly. Users can change sliders and every time if they prefer a result, they can click ‘Output’ button to save it into the file. Finally, the ‘Exit’ button can be used to close the software.

# Software
The software is achieved by two parts which are model.py and io.py. And io file is used to read and write data by defining read_data function and write_data function. And model file is mainly used for software function achievement. Test.py file is used for testing finally.
# read_data function in io.py
Positional argument: 'path'. It represents the path to a CSV file
Return values: 'data', 'n_rows', 'n_cols'. ‘data’ is a list created to store input data. The list is the rows of data and it contains the values in the columns for each row. In addition, the read_data function would check that each raw of ‘data’ contains the same number of values, and it returns the number of lines (n_rows) and the number of values in each line (n_cols) as well as ‘data’. 'n_rows' and 'n_cols' are integers representing the number of rows and columns in the input raster data.

# write_data function in io.py
The write_data() function takes two positional arguments, 'filename' and 'environment' and 'filename' is a string. The function realize that help users to output final images and a rescaled txt. file.

# Weight and addition loop in model.py
As for model, the first idea is creating lists to store weighted sum output and rescaled final result. Because both of these two results are two-dimensional arrays, defining a two-dimensional list and a one-dimensional list are necessary. As for weighting raster, a two-dimensional list is created to store the results.
Calculation: weighted raster = geology * geology_factor + transport * transport_factor + population * population_factor
One-dimensional weighted raster is stored into a list called ‘output_row’ and after loop, the ‘output_row’ is store into ‘output’ list finally. The same situation is in the rescaled process.
Calculation: rescaled result = (Old_value – minimum value) / (maximum value – minimum value).
Through these two loops, the software can walk through the raster values.

# GUI construction in model.py
The next main part is GUI construction. Using root = tk.Tk() to add a GUI called ‘Site Suitability Weight’ to allow users can get the ideal weighted result. Because the software should display three input raster files, a frame called ‘frame_1’ is added to store the first canvas. This canvas is used to show the geology, transport and population raster. And it would be triggered once the software is running. In the source codes, three subplots are created in the first canvas, which are helpful to show three maps. And as for final result, another empty canvas is added on the right of figure. Three scales are defined following the canvas to realize choosing weights by using scales in the GUI. And it is more convenient that adding the scale values and labels beside the scales. These parameters can be defined in GUI after scales. Finally, there are other components like ‘Output’ button and ‘Exit’ button, which are for outputting the rescaled raster map and closing the GUI window.

The model.py defines four functions to realize the basic interaction.
# Plot function in model.py
In this function, the main part is creating an initial figure and completing calculating loops for plotting. Moving the ‘output’ list and ‘rescaled’ list into plot function to realize this.
The plot() function takes four positional arguments: 'do_output', 'gw', 'tw', 'pw'. 'do_output' indicates if the sofrware should save the final result into a file. 'gw', 'tw' and 'pw' are floating-point numbers representing the weight factors for the geology, transport and population raster.

# Update function in model.py
Software requires that the final result should change when users slide the scales. So, an update function is defined to call the changed scale values and let users know each raster data’s value through the label. It is realized by using get() and combined this with scale value. The function begins by retrieving the current values from three scales and converting them to float values. These scales represent interactive controls that allow adjustment of certain parameters. The three scale values are then assigned to the variables gw, tw, and pw respectively.
The update() function takes one positional arguements: 'x'. It is used to pass the function.

# Output and exit function in model.py
Other two functions are ‘output’ and ‘exit’, which are buttons in GUI. The ‘output’ function is created for outputting final images and save them into a file. It is realized by using write_data function from io.py and call it in model.py.

# Weight_and_add function for testing in model.py
Because the four functions created for achievement are not very suitable for testing, another function called 'weight_and_add' which is only for calculating the weighted raster is created.
The weight_and_add function takes six positional arguments: 'geology', 'transport', 'population', 'gw', 'tw' and 'pw'. Formal three are raster list, and latter three are float value for raster weights. The function is created based on loop in plot() and it is used in test.py.
In the test.py, 'unittest' mudule is used to create a class with testing function and these six variables are called in it to calculate the weighted raster value is equal to the ideal value or not. The value of each argument is defined manually and randomly. According to the result shown in the console, the test is successful. It is not related to main work with software, it is only created for testing.
