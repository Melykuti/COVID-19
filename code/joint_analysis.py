'''
exec(open('joint_analysis.py').read())
13-18/3/2020
'''

import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from country_plot import open_csvs, data_preparation, analysis, select_window_length, print_header, print_results

### User input ###

countries = ['Italy', 'Spain', 'France', 'Germany', 'United Kingdom', 'Austria', 'Hungary']
#countries = ['Italy', 'Japan', 'Denmark', 'France', 'Germany', 'Spain', 'Switzerland']
#countries = ['Italy', 'France', 'Spain', 'Germany', 'Switzerland', 'Japan', 'Denmark', 'Netherlands', 'Sweden', 'United Kingdom', 'Austria', 'Korea, South', 'China'] # , 'Belgium'
window_length = -1 # from latest data point back into past if positive; if nonpositive, then it searches for optimum for model fitting (recommended)
save_plots = 0 # if 1, then saves all plots; o.w. it neither shows nor saves

### End of user input ###

# Constants
files = ['time_series_19-covid-Confirmed', 'time_series_19-covid-Deaths', 'time_series_19-covid-Recovered']
labels = ['Confirmed', 'Deaths', 'Recovered']

df = open_csvs() # filename is used to create name of image file if saving plot

print_header()

results_dict = dict()
selected_window_length_dict = dict()

for country in countries:
    df_ts = data_preparation(df, country)

    if window_length > 0:
        selected_window_length = window_length
        results, model = analysis(df_ts, window_length)
    else: # do a search over window_lengths for best possible fit
        # minimum and maximum allowed window lengths; we test all in this closed interval
        wl_lo = 4
        wl_hi = 15 # this end point is not included
        R = pd.DataFrame(np.empty((wl_hi-wl_lo, 7)), index=range(wl_lo, wl_hi))
        models = dict()
        for wl in range(wl_lo, wl_hi):
            result_wl, model = analysis(df_ts, wl)
            R.iloc[wl-wl_lo, :] = result_wl
            models[wl] = model
        R = R.astype({2: int, 3: int, 4: int})

        results, selected_window_length = select_window_length(R)
        selected_window_length_dict[country] = selected_window_length
        model = models[selected_window_length]

    results_dict[country] = results
    if save_plots == 1:
        plotting(df_ts, model, 1, country, selected_window_length)

    #results, model = analysis(df_ts, window_length)
    #print_results(country, results)

for country in countries:
    if window_length > 0:
        print_results(country, results_dict[country], window_length)
    else:
        print_results(country, results_dict[country], selected_window_length_dict[country])
