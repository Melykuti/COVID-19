'''
This script analyses multiple countries using the JHU CSSE dataset:
https://github.com/CSSEGISandData

exec(open('analysis_joint.py').read())
13/3-11/4/2020
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

countries = ['US', 'United Kingdom', 'Italy', 'Spain', 'France', 'Russia', 'Germany', 'Netherlands', 'Belgium', 'Iran',  'Sweden', 'Saudi Arabia', 'Japan', 'Singapore', 'Switzerland', 'Belarus', 'Austria', 'Denmark', 'Hungary', 'Korea, South', 'China']
#countries = ['US', 'Italy', 'France', 'Spain', 'Germany', 'United Kingdom', 'Iran', 'Netherlands', 'Belgium', 'Switzerland', 'Sweden', 'Austria', 'Japan', 'Denmark', 'Hungary', 'Korea, South', 'China']
#countries = ['US', 'Italy', 'Spain', 'Germany', 'France', 'Iran', 'United Kingdom', 'Switzerland', 'Netherlands', 'Belgium', 'Austria', 'Sweden', 'Denmark', 'Japan', 'Hungary', 'Korea, South', 'China'] # ['Hubei', 'China']]
#countries = ['United Kingdom']
#countries = ['Korea, South']
#countries = ['Italy', 'Spain', 'Japan', 'Korea, South', 'China']
#countries = ['Italy', 'Japan', 'Denmark', 'France', 'Germany', 'Spain', 'Switzerland']
#countries = ['Italy', 'France', 'Spain', 'Germany', 'Switzerland', 'Japan', 'Denmark', 'Netherlands', 'Sweden', 'United Kingdom', 'Austria', 'Korea, South', 'China'] # , 'Belgium'
cases = 'active' # 'confirmed' or 'deaths' or 'active' or 'recovered'
window_length = -1 # from latest data point back into past if positive; if nonpositive, then it searches for optimum for model fitting (recommended)
save_plots = 0 # if 1, then saves all plots; otherwise it neither shows nor saves
lang = 'en' # 'de' for German, anything else for English
normalise_by = 1e5 # report case numbers per this many people
exp_or_lin = 'both' # Use 'exp' model (fitting linear model on logarithmic scale) or 'lin' model or 'both' for trying both and selecting the better.
max_display_length = 45 # in days; if positive, then it plots the most recent max_display_length days only

### End of user input ###


if __name__ == '__main__':
    pop_csv = 'world'
    df = utils.open_csvs() # filename is used to create name of image file if saving plot

    results_dict = dict()
    selected_window_length_dict = dict()
    exp_or_lin_dict = dict()

    for country in countries:
        print(country)
        if isinstance(country, str):
            country_key = country
        elif len(country)==2: # if it's a pair of [Province/State, Country/Region]
            country_key = country[0].replace(',', '_').replace(' ', '_') + '__' +\
                          country[1].replace(',', '_').replace(' ', '_')

        df_ts = utils.data_preparation(df, country, cases)
        df_ts = utils.rm_early_zeros(df_ts)
        if max_display_length > 0:
            df_ts = df_ts[-max_display_length:]
        results, model, selected_window_length, e_or_l = utils.process_geounit(
                                                            df_ts, window_length, exp_or_lin)

        results_dict[country_key] = results
        selected_window_length_dict[country_key] = selected_window_length
        exp_or_lin_dict[country_key] = e_or_l
        if save_plots == 1:
            utils.plotting(df_ts, model, 1, country, selected_window_length, e_or_l, lang)

    utils.print_header(normalise_by, pop_csv)

    for country in countries:
        if isinstance(country, str):
            country_key = country
        elif len(country)==2: # if it's a pair of [Province/State, Country/Region]
            country_key = country[0].replace(',', '_').replace(' ', '_') + '__' +\
                          country[1].replace(',', '_').replace(' ', '_')

        if window_length > 0:
            utils.print_results(country, results_dict[country_key], normalise_by, pop_csv,
                                window_length, exp_or_lin_dict[country_key])
        else:
            utils.print_results(country, results_dict[country_key], normalise_by, pop_csv,
                                selected_window_length_dict[country_key], exp_or_lin_dict[country_key])
