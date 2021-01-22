'''
This script analyses multiple countries using the JHU CSSE dataset:
https://github.com/CSSEGISandData

exec(open('analysis_joint.py').read())
13/3-20/12/2020
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

#countries = ['US', 'India', 'Brazil', 'United Kingdom', 'Russia', 'France', 'Italy', 'Spain', 'Netherlands', 'Belgium', 'Germany', 'Austria', 'Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Bulgaria', 'Croatia', 'Serbia', 'Israel', 'Saudi Arabia', 'Iran', 'Singapore', 'Sweden', 'Belarus',  'Switzerland', 'Denmark', 'Japan', 'Korea, South', 'China', 'Australia', 'New Zealand']; cases = 'confirmed'
# Active cases:
countries = ['Italy', 'Russia', 'India', 'Germany', 'Iran', 'Hungary', 'Argentina', 'Bulgaria', 'Switzerland', 'Czechia', 'Austria', 'Peru', 'Japan', 'Belarus', 'Denmark', 'Israel', 'Chile', 'Korea, South', 'Saudi Arabia', 'Australia', 'China', 'Singapore', 'New Zealand']; cases = 'active'
# Confirmed cases:
# 2nd wave/to monitor
#countries = ['US', 'Brazil', 'India', 'Spain', 'Italy', 'Netherlands', 'Belgium', 'Sweden', 'Singapore', 'Germany', 'Switzerland', 'Austria', 'Japan', 'Korea, South', 'Australia', 'China', 'Romania', 'Serbia', 'Bulgaria', 'Iceland', 'Czechia', 'Poland', 'Hungary']; cases = 'confirmed'

#countries = ['Hungary', 'Serbia', 'Montenegro', 'Georgia', 'Korea, South', 'Japan', 'Canada', 'Australia', 'New Zealand', 'Algeria', 'Morocco', 'Tunisia', 'Rwanda', 'Uruguay', 'Thailand', 'Austria']; cases = 'confirmed'
#countries = ['US', 'Brazil', 'Russia', 'United Kingdom', 'France', 'India', 'Spain', 'Italy', 'Netherlands', 'Belgium', 'Sweden', 'Iran', 'Saudi Arabia', 'Belarus', 'Singapore', 'Germany', 'Japan', 'Hungary', 'Korea, South', 'Denmark', 'Switzerland', 'Austria', 'Australia', 'China', 'New Zealand']; cases = 'confirmed'
#countries = ['Argentina', 'Brazil', 'Chile', 'Peru', 'Mexico', 'Canada', 'Russia', 'Belarus', 'United Kingdom', 'India', 'Belgium', 'Sweden', 'Iran', 'Saudi Arabia', 'Qatar', 'Singapore', 'Argentina', 'Korea, South']; cases = 'confirmed'; max_display_length = 90
#countries = ['US', 'Italy', 'Spain', 'Germany', 'France', 'Iran', 'United Kingdom', 'Switzerland', 'Netherlands', 'Belgium', 'Austria', 'Sweden', 'Denmark', 'Japan', 'Hungary', 'Korea, South', 'China'] # ['Hubei', 'China']]
#countries = ['Italy', 'United Kingdom']
#countries = ['United Kingdom']; cases = 'confirmed'
#countries = ['Korea, South']
#countries = ['Turkey']; cases = 'confirmed'
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

    results_list = list()
    for country in countries:
        print(country)

        df_ts = utils.data_preparation(df, country, cases)
        #df_ts = utils.rm_early_zeros(df_ts)
        if max_display_length > 0:
            df_ts = df_ts[-max_display_length:]
        results, model = utils.process_geounit(df_ts, window_length, exp_or_lin)
        results = results.assign(country=country)
        results = results.set_index('country')
        results_list.append(results)

        if save_plots == 1:
            utils.plotting(df_ts, model, 1, country, results.iloc[0,8], results.iloc[0,9], lang, panels)

    utils.print_header(normalise_by, pop_csv)
    df_results = pd.concat(results_list)
    df_results = df_results.sort_values(3, ascending=False)

    for country in df_results.index:
        if window_length > 0:
            utils.print_results(country, df_results.loc[country,:].iloc[0:8], normalise_by, pop_csv,
                                window_length, df_results.loc[country,:].iloc[9], cases, lang)
        else:
            utils.print_results(country, df_results.loc[country,:].iloc[0:8], normalise_by, pop_csv,
                      df_results.loc[country,:].iloc[8], df_results.loc[country,:].iloc[9], cases, lang)
