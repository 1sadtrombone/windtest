import numpy as np
import matplotlib.pyplot as plt
import datetime

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

def readTimes(start, stop):
    """
    expects unix time to start and stop reading data
    
    returns data within that time (to accuracy greater than a file)
    """

    times = np.arange(start, stop, 86400)
    dates = [datetime.datetime.fromtimestamp(time) for time in times]
    # in case not a full day separating start and stop
    final_date = datetime.datetime.fromtimestamp(stop)
    if f"{dates[-1]:%Y%m%d}" != f"{final_date:%Y%m%d}":
        dates.append(final_date)
    
    datestrings = [f"{date:%Y%m%d}" for date in dates]
    print(datestrings)
    
    data = readDates(datestrings)
    within_bounds = (data[:,0] > start) * (data[:,0] < stop)
    return data[within_bounds]

    
    
