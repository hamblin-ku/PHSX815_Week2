#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import argparse
import my_params
from Random import Random

def make_plot(data):
    #import custom matplotlib parameters from file
    custom_params = my_params.params()
    mpl.rcParams.update(custom_params)
    
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(myx, 50, density=True, facecolor='g', alpha=0.75)
    ax.set_xlabel('x')
    ax.set_ylabel('Probability')
    ax.set_title('Rayleigh Distribution')

    
# main function for this Python code
if __name__ == "__main__":
    # Set up parser to handle command line arguments
    # Run as 'python PHSX815_HW2_KurtH.py -h' to see all available commands
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", "-s", help="Seed number to use")
    args = parser.parse_args()

    # default seed
    seed = 5555
    if args.seed:
        print("Set seed to %s" % args.seed)
        seed = args.seed
    
    # set random seed for numpy
    np.random.seed(seed)

    # class instance of our Random class using seed
    random = Random(seed)
    
    # create some random data
    N = 10000
        
    # an array of random numbers using our Random class
    myx = np.array([])
    for i in range(0,N):
        myx = np.append( myx, random.Rayleigh())
    make_plot(myx)
    
    plt.show()
