'''
Analyses a single country using the JHU CSSE dataset:
https://github.com/CSSEGISandData

exec(open('analysis_single.py').read())
12-18/3/2020
'''

import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from utils import open_csvs, data_preparation, process_geounit, print_header, print_results, plotting
 
### User input ###

#country = 'Iran' #'Switzerland' #'Netherlands' #'Denmark' # Denmark, Spain, France, Germany, Sweden
#country = 'Korea, South'
#country = ['United Kingdom', 'United Kingdom']
country = ['Northern Territory', 'Australia']
window_length = -1 # from latest data point back into past if positive; if nonpositive, then it searches for optimum for model fitting (recommended)
# Iran used 11 for plot
save_not_show = 0 # if 0, then shows the plot; if 1, then saves it; o.w. it does neither
lang = 'en' # 'de' for German, anything else for English

### End of user input ###


if __name__ == '__main__':
    df = open_csvs()
    df_ts = data_preparation(df, country)
    results, model, selected_window_length = process_geounit(df_ts, window_length)

    print_header()
    print_results(country, results, selected_window_length, lang)
    
    if save_not_show in [0, 1]:
        plotting(df_ts, model, save_not_show, country, selected_window_length, lang)
