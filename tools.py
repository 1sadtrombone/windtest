import numpy as np
import matplotlib.pyplot as plt

def readDate(datestring):
    """
    expects date in format YYYYMMDD
    
    returns contents of corresponding CSV in numpy array
    """

    return np.genfromtxt(f"wind_test_data/{datestring}.CSV", delimiter=',', skip_header=1)

def readDates(datestrings):
    """
    expects array of dates as described in readDate

    returns concatenated numpy array of all contents
    
    complains if the sizes do not match between files
    """

    data = readDate(datestrings[0])
    for i in range(1, len(datestrings)):
        data = np.vstack((data, readDate(datestrings[i])))
    return data
        
