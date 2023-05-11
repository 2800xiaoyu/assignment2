# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:12:18 2023

@author: xiaoyu
"""

import csv

def read_data(path):
    """
    Read data.

    Parameters
    ----------
    path : String
        Path of the file to be read. The file is expected to be a rectangular
        2D CSV format data with numerical values.

    Returns
    -------
    data : List of lists
        The data in row major order.

    """
    
    # Read input data
    f = open(path, newline='')
    data = []
    
    n_rows = 0
    n_cols = None
    
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
            # print(value)
        if n_cols is None:
            n_cols = len(row)
        assert(n_cols == len(row))
        data.append(row)
        n_rows += 1
    f.close()
    
    return data, n_rows, n_cols

# Define a function to write out result raster to a file
def write_data(filename, environment):
    """
    Write data

    Parameters
    ----------
    filename : String
        The filename of output.
    environment : List
        A reference to a shared environment.

    Returns
    -------
    None.

    """
    f = open(filename, 'w', newline='')
    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in environment:
        writer.writerow(row)
