'''
Analyses a single country using the JHU CSSE dataset:
https://github.com/CSSEGISandData

exec(open('analysis_single.py').read())
12/3-11/4/2020
'''

import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
#from utils import open_csvs, data_preparation, rm_early_zeros, process_geounit, print_header, print_results, plotting
import utils
from importlib import reload

### User input ###

country = 'Germany' # 'US', 'Switzerland' 'United Kingdom' 'Netherlands' 'Denmark' 'Spain' 'France' 'Germany' 'Sweden' 'Singapore'
#country = 'Korea, South'
#country = ['New South Wales', 'Australia']
#country = 'EU'
cases = 'confirmed' # 'confirmed' or 'deaths' or 'active' or 'recovered'
window_length = -1 # from latest data point back into past if positive; if nonpositive, then it searches for optimum for model fitting (recommended)
save_not_show = 0 # if 0, then shows the plot; if 1, then saves it; o.w. it does neither
lang = 'en' # 'de' for German, anything else for English
normalise_by = 1e5 # report case numbers per this many people
exp_or_lin = 'both' # Use 'exp' model (fitting linear model on logarithmic scale) or 'lin' model or 'both' for trying both and selecting the better.
max_display_length = 45 # in days; if positive, then it plots the most recent max_display_length days only

### End of user input ###


if __name__ == '__main__':
    df = utils.open_csvs()
    df_ts = utils.data_preparation(df, country, cases)
    df_ts = utils.rm_early_zeros(df_ts)
    if max_display_length > 0:
        df_ts = df_ts[-max_display_length:]
    results, model, selected_window_length, e_or_l = utils.process_geounit(
                                                        df_ts, window_length, exp_or_lin)

    utils.print_header(normalise_by)
    utils.print_results(country, results, normalise_by, selected_window_length, e_or_l, lang)
    
    if save_not_show in [0, 1]:
        utils.plotting(df_ts, model, save_not_show, country, selected_window_length, e_or_l, lang)
