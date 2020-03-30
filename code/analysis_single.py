'''
Analyses a single country using the JHU CSSE dataset:
https://github.com/CSSEGISandData

exec(open('analysis_single.py').read())
12-30/3/2020
'''

import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from utils import open_csvs, data_preparation, rm_early_zeros, process_geounit, print_header, print_results, plotting
#import utils
from importlib import reload

### User input ###

country = 'Singapore' # 'US', 'Switzerland' 'United Kingdom' 'Netherlands' 'Denmark' 'Spain' 'France' 'Germany' 'Sweden'
#country = 'Korea, South'
#country = ['New South Wales', 'Australia']
#country = 'EU'
window_length = -1 # from latest data point back into past if positive; if nonpositive, then it searches for optimum for model fitting (recommended)
save_not_show = 0 # if 0, then shows the plot; if 1, then saves it; o.w. it does neither
lang = 'en' # 'de' for German, anything else for English
normalise_by = 1e5 # report case numbers per this many people

### End of user input ###


if __name__ == '__main__':
    df = open_csvs()
    df_ts = data_preparation(df, country)
    df_ts = rm_early_zeros(df_ts)
    df_ts = df_ts[-45:]
    results, model, selected_window_length = process_geounit(df_ts, window_length)

    print_header(normalise_by)
    print_results(country, results, normalise_by, selected_window_length, lang)
    
    if save_not_show in [0, 1]:
        plotting(df_ts, model, save_not_show, country, selected_window_length, lang)
