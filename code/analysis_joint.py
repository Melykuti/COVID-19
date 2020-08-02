'''
This script analyses multiple countries using the JHU CSSE dataset:
https://github.com/CSSEGISandData

exec(open('analysis_joint.py').read())
13/3-1/5/2020
'''

import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import utils
from importlib import reload

### User input ###
max_display_length = 140 #45 # in days; if positive, then it plots the most recent max_display_length days only

#countries = ['US', 'United Kingdom', 'Russia', 'France', 'Italy', 'Spain', 'Netherlands', 'Belgium', 'Saudi Arabia', 'Germany', 'Singapore', 'Sweden', 'Belarus', 'Iran', 'Japan', 'Switzerland', 'Hungary', 'Denmark', 'Austria', 'Korea, South', 'Australia', 'China', 'New Zealand']
# Active cases:
countries = ['US', 'Brazil', 'India', 'Russia', 'France', 'Spain', 'Belgium', 'Saudi Arabia', 'Israel', 'Iran', 'Italy', 'Japan', 'Germany', 'Australia', 'Singapore', 'Belarus', 'China', 'Switzerland', 'Austria', 'Korea, South', 'Denmark', 'Hungary', 'New Zealand']; cases = 'active'
# Confirmed cases:
#countries = ['Hungary', 'Serbia', 'Montenegro', 'Georgia', 'Korea, South', 'Japan', 'Canada', 'Australia', 'New Zealand', 'Algeria', 'Morocco', 'Tunisia', 'Rwanda', 'Uruguay', 'Thailand', 'Austria']; cases = 'confirmed'
#countries = ['US', 'Brazil', 'Russia', 'United Kingdom', 'France', 'India', 'Spain', 'Italy', 'Belgium', 'Sweden', 'Iran', 'Saudi Arabia', 'Belarus', 'Singapore', 'Germany', 'Japan', 'Hungary', 'Korea, South', 'Denmark', 'Switzerland', 'Austria', 'Australia', 'China', 'New Zealand']; cases = 'confirmed'
#countries = ['Argentina', 'Brazil', 'Chile', 'Peru', 'Mexico', 'Canada', 'Russia', 'Belarus', 'United Kingdom', 'India', 'Belgium', 'Sweden', 'Iran', 'Saudi Arabia', 'Qatar', 'Singapore', 'Argentina', 'Korea, South']; cases = 'confirmed'; max_display_length = 90
#countries = ['US', 'Italy', 'Spain', 'Germany', 'France', 'Iran', 'United Kingdom', 'Switzerland', 'Netherlands', 'Belgium', 'Austria', 'Sweden', 'Denmark', 'Japan', 'Hungary', 'Korea, South', 'China'] # ['Hubei', 'China']]
#countries = ['United Kingdom']
#countries = ['Korea, South']
#countries = ['Italy', 'Spain', 'Japan', 'Korea, South', 'China']
#countries = ['Italy', 'Japan', 'Denmark', 'France', 'Germany', 'Spain', 'Switzerland']
#countries = ['Italy', 'France', 'Spain', 'Germany', 'Switzerland', 'Japan', 'Denmark', 'Netherlands', 'Sweden', 'United Kingdom', 'Austria', 'Korea, South', 'China'] # , 'Belgium'
#cases = 'confirmed' # 'confirmed' or 'deaths' or 'active' or 'recovered'
window_length = -1 # from latest data point back into past if positive; if nonpositive, then it searches for optimum for model fitting (recommended)
save_plots = 1 # if 1, then saves all plots; otherwise it neither shows nor saves
lang = 'en' # 'de' for German, anything else for English
normalise_by = 1e5 # report case numbers per this many people
exp_or_lin = 'both' # Use 'exp' model (fitting linear model on logarithmic scale) or 'lin' model or 'both' for trying both and selecting the better.
panels = 2 # 2 or 3, to plot only two panels or all three, that is, the logarithmically scaled cumulative numbers also

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
        #df_ts = utils.rm_early_zeros(df_ts)
        if max_display_length > 0:
            df_ts = df_ts[-max_display_length:]
        results, model, selected_window_length, e_or_l = utils.process_geounit(
                                                            df_ts, window_length, exp_or_lin)

        results_dict[country_key] = results
        selected_window_length_dict[country_key] = selected_window_length
        exp_or_lin_dict[country_key] = e_or_l
        if save_plots == 1:
            utils.plotting(df_ts, model, 1, country, selected_window_length, e_or_l, lang, panels)

    utils.print_header(normalise_by, pop_csv)

    for country in countries:
        if isinstance(country, str):
            country_key = country
        elif len(country)==2: # if it's a pair of [Province/State, Country/Region]
            country_key = country[0].replace(',', '_').replace(' ', '_') + '__' +\
                          country[1].replace(',', '_').replace(' ', '_')

        if window_length > 0:
            utils.print_results(country, results_dict[country_key], normalise_by, pop_csv,
                                window_length, exp_or_lin_dict[country_key], cases, lang)
        else:
            utils.print_results(country, results_dict[country_key], normalise_by, pop_csv,
                    selected_window_length_dict[country_key], exp_or_lin_dict[country_key], cases, lang)
