'''
This script analyses multiple countries using the JHU CSSE dataset:
https://github.com/CSSEGISandData

exec(open('analysis_joint.py').read())
13-18/3/2020
'''

import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from utils import open_csvs, data_preparation, process_geounit, print_header, print_results, plotting

### User input ###

countries = ['Italy', 'Spain', 'France', 'Germany', 'Switzerland', ['United Kingdom', 'United Kingdom'], 'Netherlands', 'Austria', 'Sweden', 'Denmark', 'Japan', 'Hungary', 'Korea, South', 'China']
#countries = ['Italy', 'Japan', 'Denmark', 'France', 'Germany', 'Spain', 'Switzerland']
#countries = ['Italy', 'France', 'Spain', 'Germany', 'Switzerland', 'Japan', 'Denmark', 'Netherlands', 'Sweden', 'United Kingdom', 'Austria', 'Korea, South', 'China'] # , 'Belgium'
window_length = -1 # from latest data point back into past if positive; if nonpositive, then it searches for optimum for model fitting (recommended)
save_plots = 0 # if 1, then saves all plots; otherwise it neither shows nor saves
lang = 'en' # 'de' for German, anything else for English

### End of user input ###


if __name__ == '__main__':
    df = open_csvs() # filename is used to create name of image file if saving plot

    results_dict = dict()
    selected_window_length_dict = dict()

    for country in countries:
        print(country)
        if isinstance(country, str):
            country_key = country
        elif len(country)==2: # if it's a pair of [Province/State, Country/Region]
            country_key = country[0].replace(',', '_').replace(' ', '_') + '__' +\
                          country[1].replace(',', '_').replace(' ', '_')

        df_ts = data_preparation(df, country)

        results, model, selected_window_length = process_geounit(df_ts, window_length)

        results_dict[country_key] = results
        selected_window_length_dict[country_key] = selected_window_length
        if save_plots == 1:
            plotting(df_ts, model, 1, country, selected_window_length, lang)

    #results, model = analysis(df_ts, window_length)
    #print_results(country, results)

    print_header()

    for country in countries:
        if isinstance(country, str):
            country_key = country
        elif len(country)==2: # if it's a pair of [Province/State, Country/Region]
            country_key = country[0].replace(',', '_').replace(' ', '_') + '__' +\
                          country[1].replace(',', '_').replace(' ', '_')

        if window_length > 0:
            print_results(country, results_dict[country_key], window_length)
        else:
            print_results(country, results_dict[country_key], selected_window_length_dict[country_key])
