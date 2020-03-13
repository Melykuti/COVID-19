'''
exec(open('joint_analysis.py').read())
13/3/2020
'''

import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from country_plot import open_csvs, data_preparation, print_header, analysis, print_results

### User input ###

#countries = ['Italy', 'Japan', 'Denmark', 'France', 'Germany', 'Spain', 'Switzerland']
countries = ['Italy', 'France', 'Spain', 'Germany', 'Switzerland', 'Japan', 'Denmark', 'Netherlands', 'Sweden', 'United Kingdom', 'Austria', 'Korea, South', 'China'] # , 'Belgium'
window_length = 14 # from present back into past

### End of user input ###

# Constants
files = ['time_series_19-covid-Confirmed', 'time_series_19-covid-Deaths', 'time_series_19-covid-Recovered']
labels = ['Confirmed', 'Deaths', 'Recovered']

df, filename = open_csvs() # filename is used to create name of image file if saving plot

print_header()

for country in countries:
    df_ts = data_preparation(df, country)
    results, model = analysis(df_ts, window_length)
    print_results(country, results)

