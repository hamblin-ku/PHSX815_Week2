#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file

from MySort import MySort
from my_params import params
#import custom matplotlib parameters from file
custom_params = params()
mpl.rcParams.update(custom_params)

#Function to make histograms
def make_plot(data,title, x_label):
    density, bins = np.histogram(data,bins=20, density = True)#, range=(0,maxVal))
    unity_density = density / density.sum() #normalize
    
    fig, ax = plt.subplots(figsize = (6,6))
    widths = bins[:-1] - bins[1:]
    ax.bar(bins[1:], unity_density, width=widths, color = 'g', alpha = 0.75, align = 'edge')


    ax.set_xlabel(x_label)
    ax.set_ylabel('Probability')
    ax.set_title(title)
    return fig, ax

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []
    Nexp = 0
    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)
            Nexp += 1

    Sorter = MySort()
    
    times = Sorter.DefaultSort(times)
    times_avg = Sorter.DefaultSort(times_avg)
    
    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE
    fig, ax = make_plot(times, 'All Measurement times', 't')
    fig_avg, ax_avg  = make_plot(times_avg, 'Experiment Averaged Times', r'$t_{avg}$')
    ax_avg.set_yticks([0,.05, .1, .15, .2])
    ax_avg.set_ylim([0,.17])
    
    #Annotate on the number of data points
    ax.annotate( s = "Nmeas = %d" % (Nmeas), xy = (4,0.35))
    ax.annotate( s = "Nexp = %d" % (Nexp), xy = (4,0.32))
    ax.set_xlim([0,6])
    
    ax_avg.annotate( s = "Nmeas = %d" % (Nmeas), xy = (1.3, 0.146))
    ax_avg.annotate( s = "Nexp = %d" % (Nexp), xy = (1.3 ,0.134))

    plt.tight_layout()
    plt.show()
