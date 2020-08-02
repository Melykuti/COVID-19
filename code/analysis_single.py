'''
Analyses a single country using the JHU CSSE dataset:
https://github.com/CSSEGISandData

exec(open('analysis_single.py').read())
12/3-1/5/2020
'''

import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import utils
from importlib import reload

### User input ###

country = 'Israel' # 'US', 'Switzerland' 'United Kingdom' 'Netherlands' 'Denmark' 'Spain' 'France' 'Germany' 'Sweden' 'Singapore' 'Saudi Arabia' 'Tunisia' 'Turkey' 'Azerbaijan' 'Korea, South'
#country = 'Korea, South'
#country = ['New South Wales', 'Australia']
#country = 'EU'
cases = 'confirmed' # 'confirmed' or 'deaths' or 'active' or 'recovered'
window_length = -1 # from latest data point back into past if positive; if nonpositive, then it searches for optimum for model fitting (recommended)
save_not_show = 0 # if 0, then shows the plot; if 1, then saves it; o.w. it does neither
lang = 'en' # 'de' for German, anything else for English
normalise_by = 1e5 # report case numbers per this many people
exp_or_lin = 'lin' # Use 'exp' model (fitting linear model on logarithmic scale) or 'lin' model or 'both' for trying both and selecting the better.
max_display_length = 120 # in days; if positive, then it plots the most recent max_display_length days only
#max_display_length = -1
latest_date = None
#latest_date = 1
panels = 2 # 2 or 3, to plot only two panels or all three, that is, the logarithmically scaled cumulative numbers also

### End of user input ###


if __name__ == '__main__':
    pop_csv = 'world' #None
    df = utils.open_csvs()
    df_ts = utils.data_preparation(df, country, cases)
    #df_ts = utils.rm_early_zeros(df_ts)
    if max_display_length > 0:
        df_ts = df_ts.iloc[-max_display_length:]
    if latest_date != None:
        df_ts = df_ts[:-latest_date]
    #df_ts = df_ts[:50]
    results, model, selected_window_length, e_or_l = utils.process_geounit(
                                                        df_ts, window_length, exp_or_lin)

    utils.print_header(normalise_by, pop_csv)
    utils.print_results(country, results, normalise_by, pop_csv, selected_window_length, e_or_l, lang)
    
    if save_not_show in [0, 1]:
        utils.plotting(df_ts, model, save_not_show, country, selected_window_length,
                       e_or_l, lang, panels)
