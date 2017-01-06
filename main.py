#!/usr/bin/env python

'''
This is the main method demonstrating Ensemble Partial Least Squares Regression
'''

import os
import numpy as np
import pandas as pd

__author__ = "Samuel Meshoyrer" 
__email__ = "s.meshoyrer@columbia.edu"

def main():
    path = os.path.dirname(os.path.realpath(__file__))
    data = pd.read_csv(path + '/data/alkanes.csv', header = 0)
    cols = data.columns
    data.drop(cols[0], axis = 1, inplace = True)
    cols = cols[1:]
    X = data.as_matrix(columns = cols[:-1])
    y = data.as_matrix(columns = list(cols[-1]))
    
    return

if __name__ == "__main__":
    main()
