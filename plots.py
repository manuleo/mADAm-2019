# -*- coding: utf-8 -*-

"""Plot functions"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def timeline_supply(dataframe, zone, extras=""):
    '''
    Plots a timeline of food supply in different countries
    Inputs:
        - dataframe (pandas dataframe): dataframe with food supply data for multiple countries
        - zone (str): describes the zone to which countries in the dataframe belong (e.g. "African", "European") [visualization purposes]
        - extras (str): extra information to be displayed in the title of the plot [visualization purposes]
    '''
    dataframe.plot.line(legend = False)
    plt.xlabel("Time (year)")
    plt.ylabel("Food supply (kcal/person/day)")
    plt.title("Food supply for different {} countries (Each line is a country){}".format(zone, extras))