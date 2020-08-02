'''
Compares the daily increase factor as a function of case number across countries
using the JHU CSSE dataset:
https://github.com/CSSEGISandData

exec(open('comparison_joint.py').read())
12/3-2/5/2020
'''

import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
#from utils import open_csvs, data_preparation, rm_early_zeros, rm_consecutive_early_zeros, separated, select_window_length, pick_exp_vs_lin, print_header, load_population_world, load_population_DEU
import utils
from importlib import reload

### User input ###

left_bound=0.8
bottom_bound=-10.; top_bound=100.
max_display_length = 100 #45 # in days; if positive, then it plots the most recent max_display_length days only
time_start = pd.Timestamp.date(pd.Timestamp('today'))-max_display_length*pd.DateOffset()
cycle_linestyle = 0 # if 0, then all lines are solid; if 1, then it cycles through solid, dotted, dashed, dash-dotted
#normalise = 1 # 1 if you want to normalise by population size, o.w. 0
#normalise = 'xy' # 'xy' or 'y' if you want to normalise by population size ('xy' normalises both x and y values (unless xaxis = 'date'), 'y' normalises only y values), o.w. None; 'y' alone can be normalised only if incr_or_rate=='incr' & xaxis=='cases'
normalise_by = int(1e5) # display case numbers per this many people

window_length = -1 # from latest data point back into past if positive; if nonpositive, then it searches for optimum for model fitting (recommended)
#window_length = 7

save_not_show = 1 # if 0, then shows the plot; if 1, then saves it; o.w. it does neither
lang = 'en' # 'de' for German, anything else for English
cases = 'confirmed' # 'confirmed' or 'deaths' or 'active' or 'recovered'
incr_or_rate = 'rate' # Which to display: 'incr' for daily increment, 'rate' for daily growth rate
xaxis = 'cases' # What to use for x-axis: 'date' for date or 'cases' for number of cases
exp_or_lin = 'lin' # Use 'exp' model (fitting linear model on logarithmic scale) or 'lin' model or 'both' for trying both and selecting the better.

'''
# Drop-in replacement for original:
countries = ['Italy', 'Spain', 'France', 'Germany', 'Iran', 'Turkey', 'United Kingdom', 'Netherlands', 'Switzerland', 'Japan', 'Korea, South', 'China']; left_bound=1000; right_bound=None; bottom_bound=0.; top_bound=60.; normalise = None; filename = 'Joint'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'exp'
'''
countries = ['United Kingdom', 'Spain', 'Sweden', 'Belarus', 'Italy', 'France', 'Germany', 'Iran', 'Turkey', 'Netherlands', 'Switzerland', 'Korea, South', 'Japan', 'China']; left_bound=4.; right_bound=None; bottom_bound=0.; top_bound=30.; normalise = 'xy'; filename = 'Joint'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'lin'
# New
#countries = ['United Kingdom', 'Spain', 'Sweden', 'Belarus', 'Italy', 'France', 'Germany', 'Iran', 'Turkey', 'Netherlands', 'Switzerland', 'Korea, South', 'Japan', 'China']; left_bound=1.; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Joint'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'cases'; exp_or_lin = 'lin'
#countries = ['United Kingdom', 'Spain', 'Sweden', 'Belarus', 'Italy', 'France', 'Germany', 'Iran', 'Turkey', 'Netherlands', 'Switzerland', 'Korea, South', 'Japan', 'China']; left_bound=time_start; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Joint'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'lin'

'''
# Drop-in replacement for original:
countries = ['China', 'EU', 'US']; left_bound=1000; right_bound=None; bottom_bound=0.; top_bound=55.; normalise = None; filename = 'great_powers'; lang = 'en'; cycle_linestyle = 0; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'exp'
'''
#countries = ['China', 'EU', 'US', 'Russia', 'Brazil', 'India']; left_bound=0.1; right_bound=None; bottom_bound=0.; top_bound=30.; normalise = 'xy'; filename = 'great_powers'; lang = 'en'; cycle_linestyle = 0; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'lin'
# New
#countries = ['China', 'EU', 'US', 'Russia', 'Brazil', 'India']; left_bound=0.1; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'great_powers'; lang = 'en'; cycle_linestyle = 0; incr_or_rate = 'incr'; xaxis = 'cases'; exp_or_lin = 'lin'
#countries = ['China', 'EU', 'US', 'Russia', 'Brazil', 'India']; left_bound=time_start; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'great_powers'; lang = 'en'; cycle_linestyle = 0; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'lin'

'''
# Drop-in replacement for original:
countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; left_bound=50.; right_bound=10000; bottom_bound=0.; top_bound=80.; normalise = None; filename = 'Visegrad'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'exp'
'''
#countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; left_bound=2; right_bound=None; bottom_bound=0.; top_bound=35.; normalise = 'xy'; filename = 'Visegrad'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'lin'
# New
#countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; left_bound=2; right_bound=1100; bottom_bound=0.; top_bound=30.; normalise = 'xy'; filename = 'Visegrad'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'cases'; exp_or_lin = 'lin'
#countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; left_bound=time_start; right_bound=None; bottom_bound=0.; top_bound=30.; normalise = 'xy'; filename = 'Visegrad'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'lin'

'''
# Drop-in replacement for original:
#countries = 'Deutschland'; left_bound=200; right_bound=None; bottom_bound=0.; top_bound=60.; normalise = None; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'exp'
'''
#countries = 'Deutschland'; left_bound=9; right_bound=None; bottom_bound=0.; top_bound=27.5; normalise = 'xy'; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'lin'
# New
#countries = 'Deutschland'; left_bound=9; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'cases'; exp_or_lin = 'lin'
#countries = 'Deutschland'; left_bound=pd.to_datetime('2020-03-01'); right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date';# exp_or_lin = 'lin' left_bound=time_start;

# Nordic countries
#countries = ['Norway', 'Sweden', 'Finland', 'Denmark', 'Iceland']; left_bound=2; right_bound=None; bottom_bound=0.; top_bound=80.; normalise = 'xy'; filename = 'Nordic'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'lin'
#countries = ['Norway', 'Sweden', 'Finland', 'Denmark', 'Iceland']; left_bound=2; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Nordic'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'cases'; exp_or_lin = 'lin'
#countries = ['Norway', 'Sweden', 'Finland', 'Denmark', 'Iceland']; left_bound=time_start; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Nordic'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'lin'

# DACH
#countries = ['Germany', 'Switzerland', 'Liechtenstein', 'Austria']; left_bound=2; right_bound=None; bottom_bound=0.; top_bound=80.; normalise = 'xy'; filename = 'DACH'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'lin'
#countries = ['Germany', 'Switzerland', 'Liechtenstein', 'Austria']; left_bound=2; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'DACH'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'cases'; exp_or_lin = 'lin'
#countries = ['Germany', 'Switzerland', 'Liechtenstein', 'Austria']; left_bound=time_start; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'DACH'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'lin'

#countries = ['United Kingdom', 'Spain', 'Sweden', 'Denmark', 'Italy', 'France', 'Germany', 'Netherlands', 'Belgium']; left_bound=time_start; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'WesternEurope'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'lin'

# Death toll
#cases = 'deaths'; countries = ['US', 'Brazil', 'United Kingdom', 'Spain', 'Sweden', 'Belarus', 'Italy', 'France', 'Belgium', 'Germany']; left_bound=1; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Joint'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'cases'; exp_or_lin = 'lin'
#cases = 'deaths'; countries = ['US', 'Brazil', 'United Kingdom', 'Spain', 'Sweden', 'Belarus', 'Italy', 'France', 'Belgium', 'Germany']; left_bound=time_start; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Joint'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'lin'
#cases = 'deaths'; countries = ['United Kingdom', 'Spain', 'Sweden', 'Denmark', 'Italy', 'France', 'Germany', 'Netherlands', 'Belgium']; left_bound=time_start; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'WesternEurope'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'lin'

#cases = 'deaths'; countries = ['Italy', 'Spain', 'US', 'United Kingdom', 'France', 'Netherlands', 'Belgium', 'Sweden', 'Germany']; left_bound=0.1; right_bound=None; bottom_bound=0.; top_bound=3.; normalise = 'xy'; filename = 'deathtoll'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'cases'; exp_or_lin = 'lin'
#cases = 'deaths'; countries = ['Italy', 'Spain', 'US', 'United Kingdom', 'France', 'Netherlands', 'Belgium', 'Sweden', 'Germany']; left_bound=pd.to_datetime('2020-03-01'); right_bound=None; bottom_bound=0.; top_bound=3.; normalise = 'xy'; filename = 'deathtoll'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'lin'

#cases = 'deaths'; countries = ['China', 'EU', 'US', 'Russia', 'Brazil', 'India']; left_bound=0.01; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'great_powers'; lang = 'en'; cycle_linestyle = 0; incr_or_rate = 'incr'; xaxis = 'cases'; exp_or_lin = 'lin'
#cases = 'deaths'; countries = ['China', 'EU', 'US', 'Russia', 'Brazil', 'India']; left_bound=time_start; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'great_powers'; lang = 'en'; cycle_linestyle = 0; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'lin'

#cases = 'deaths'; countries = ['Norway', 'Sweden', 'Finland', 'Denmark', 'Iceland']; left_bound=0.01; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Nordic'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'cases'; exp_or_lin = 'lin'

# Testing

#countries = ['China', 'EU', 'US']; left_bound=1000; right_bound=None; bottom_bound=0.; top_bound=None; normalise = None; filename = 'great_powers'; lang = 'en'; cycle_linestyle = 0
#countries = ['China', 'EU', 'US']; left_bound=pd.to_datetime('2020-03-01'); right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'y'; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'exp'; filename = 'great_powers'; lang = 'en'; cycle_linestyle = 0

#countries = ['Japan', 'Korea, South', 'China']; left_bound=None; right_bound=None; bottom_bound=0.; top_bound=80.; normalise = 'xy'; filename = 'Joint'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'lin'

#countries = 'Deutschland'; left_bound=1; right_bound=None; bottom_bound=0.; top_bound=60.; normalise = 'xy'; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'exp'; cases = 'deaths'
#countries = 'Deutschland'; left_bound=1; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'cases'; exp_or_lin = 'exp'; cases = 'deaths'
#countries = 'Deutschland'; left_bound=time_start; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'exp'; cases = 'deaths'




#countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; left_bound=pd.to_datetime('2020-03-01'); right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Visegrad'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'exp'
#countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; left_bound=pd.to_datetime('2020-03-15'); right_bound=pd.to_datetime('2020-04-02'); bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Visegrad'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'exp'

#countries = 'Deutschland'; left_bound=200; right_bound=None; bottom_bound=0.; top_bound=60.; normalise = None; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'exp'
#countries = 'Deutschland'; left_bound=9; right_bound=None; bottom_bound=0.; top_bound=60.; normalise = 'xy'; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'exp'

#countries = ['US', 'Italy', 'China', 'Spain', 'Germany', 'Iran', 'France', 'Korea, South', 'Switzerland', 'United Kingdom', 'Netherlands', 'Japan']; left_bound=1000; right_bound=None; bottom_bound=0.; top_bound=60.; normalise = None; filename = 'Joint'; cycle_linestyle = 1
#countries = ['US', 'Italy', 'China', 'Spain', 'Germany', 'Iran', 'France', 'Korea, South', 'Switzerland', 'United Kingdom', 'Netherlands', 'Japan']; left_bound=1.; right_bound=None; bottom_bound=0.; top_bound=80.; normalise = 'y'; filename = 'Joint'; cycle_linestyle = 1

#countries = ['Switzerland', 'United Kingdom']; left_bound=10.; right_bound=None; bottom_bound=0.; top_bound=80.; normalise = 'y'; filename = 'test';
#countries = ['Italy', 'Spain', 'France', 'Germany', 'Switzerland', ['United Kingdom', 'United Kingdom'], 'Netherlands', 'Austria', 'Sweden', 'Denmark', 'Japan', 'Hungary', 'Korea, South', 'China']
#countries = ['Hungary']; left_bound=50*normalise_by/10e6; right_bound=None; normalise = 'y'; filename = 'Visegrad'
#countries = ['Iceland']; left_bound=None; right_bound=None; normalise = None; filename = 'Iceland'
#countries = ['Iceland']; left_bound=0.8; right_bound=None; normalise = 'y'; filename = 'Iceland'

#, 'Netherlands', 'Austria', 'Sweden', 'Denmark', 'Japan', 'Hungary', 'Korea, South', ]
#countries = [ 'Japan']; left_bound=400; right_bound=None
#countries = ['Italy']
#countries = ['Italy', 'Japan', 'Denmark', 'France', 'Germany', 'Spain', 'Switzerland']
#country = 'France' #'Switzerland' #'Netherlands' #'Denmark' # Denmark, Spain, France, Germany, Sweden
#country = 'Korea, South'
#country = ['United Kingdom', 'United Kingdom']

### End of user input ###

def call_process_geounit_minimal(df_ts, latest_date, window_length, exp_or_lin='both'):
    '''
    This processes one geographical unit.
    df_ts is the time series.
    '''
    case_no = list()
    dif_optim = list() # list of daily increase factors
    #latest_date = None
    df_ts = utils.rm_consecutive_early_zeros(df_ts, 0) #window_length_for_cutoffs-2)
    #print(df_ts)
    if isinstance(left_bound, int) or isinstance(left_bound, float):
        df_ts = df_ts[(df_ts>left_bound).idxmax()-wl_hi*pd.DateOffset():]
    elif left_bound is not None:
        df_ts = df_ts[left_bound-wl_hi*pd.DateOffset():]
    #print(df_ts)
    if latest_date==None or latest_date<df_ts.index[-1]:
        latest_date = df_ts.index[-1]

    for i in range(window_length_for_cutoffs-len(df_ts), 1):
        #results, model, selected_window_length, e_or_l = process_geounit_minimal(
        #                                        df_ts[:len(df_ts)+i], window_length, exp_or_lin)
        results, model, selected_window_length, e_or_l = utils.process_geounit(
                                            df_ts[:len(df_ts)+i], window_length, exp_or_lin, 'minimal')
        #print(results)
        if incr_or_rate == 'incr':
            dif_optim.append(results[0])
        else: # 'rate'
            dif_optim.append(results[1])
        if xaxis == 'cases':
            case_no.append(results[3])
        #else: # 'date'
        #    case_no.append(df_ts.index[len(df_ts)+i-1])
    if xaxis == 'date':
        case_no = df_ts.index[window_length_for_cutoffs-1:]

    return df_ts, dif_optim, case_no, latest_date, e_or_l

def plotting_countries(dif_all, save_not_show, latest_date, window_length, exp_or_lin, left_bound=None, right_bound=None, bottom_bound=None, top_bound=None, cycle_linestyle=0, lang='en'):
    fig, ax1 = plt.subplots(1,1, figsize=(12., 8.))
    #fig, ax1 = plt.subplots(1,1, figsize=(9.6, 6.4))
    space_below = 0.2 # in the case of dates which are rotated
    if lang=='de':
        if cases=='confirmed':
            case_txt_0 = 'Fallzahlen'
            case_txt_0zl = 'den täglichen Zuwachs der Fallzahlen'
            case_txt_0ze = 'den Logarithmus des täglichen Zuwachses der Fallzahlen'
            case_txt_1 = 'Fallzahl'
        elif cases=='deaths':
            case_txt_0 = 'Todesfälle'
            case_txt_0zl = 'die täglichen neuen Todesfälle'
            case_txt_0ze = 'den Logarithmus der täglichen neuen Todesfälle'
            case_txt_1 = 'Todesfälle'
        if window_length<0:
            #ax1.set_title('Lineare Regression auf {0}{1} mit optimaler Fenstergröße.'.format('den Logarithmus des ' if exp_or_lin=='exp' else '', case_txt_0))
            ax1.set_title('Lineare Regression auf {0} mit optimaler Fenstergröße.'.format(case_txt_0ze if exp_or_lin=='exp' else case_txt_0zl))
        else:
            #ax1.set_title('Lineare Regression auf {0}{1} mit Fenstergröße von {2} Datenpunkten.'.format('den Logarithmus des ' if exp_or_lin=='exp' else '', case_txt_0, window_length))
            ax1.set_title('Lineare Regression auf {0} mit Fenstergröße von {1} Datenpunkten.'.format(case_txt_0ze if exp_or_lin=='exp' else case_txt_0zl, window_length))

        if xaxis == 'cases':
            if normalise=='xy':
                ax1.set_xlabel('{0} auf {1} Einwohner'.format(case_txt_1, utils.separated(str(normalise_by), lang)) if normalise=='xy' else case_txt_1)
            else:
                ax1.set_xlabel(case_txt_1)
            '''
            if cases=='confirmed':
                ax1.set_xlabel('{0} auf {1} Einwohner'.format(case_txt_1, utils.separated(str(normalise_by), lang)) if normalise=='xy' else 'Fallzahl')
            elif cases=='deaths':
                ax1.set_xlabel('{0} auf {1} Einwohner'.format(case_txt_1, utils.separated(str(normalise_by), lang)) if normalise=='xy' else 'Todesfälle')
            '''
        #else:
        #    fig.subplots_adjust(bottom=space_below)

        if incr_or_rate == 'rate':
            ax1.set_ylabel('Wachstumsrate der {}'.format(case_txt_0))
            fig.suptitle('Tägliche Wachstumsrate der {}, Stand '.format(case_txt_0) + latest_date.strftime('%d.%m.%Y'))
        else:
            if normalise is None:
                ax1.set_ylabel('Täglicher Zuwachs')
                fig.suptitle('Täglicher Zuwachs der {}, Stand '.format(case_txt_0) + latest_date.strftime('%d.%m.%Y'))
            else:
                ax1.set_ylabel('Täglicher Zuwachs auf {} Einwohner'.format( utils.separated(str(normalise_by), lang)))
                fig.suptitle('Täglicher Zuwachs der {0} auf {1} Einwohner, Stand {2}'.format(case_txt_0, utils.separated(str(normalise_by), lang), latest_date.strftime('%d.%m.%Y')))

    else: # i.e. 'en'
        if cases=='confirmed':
            case_txt_0 = 'case numbers'
            case_txt_0zl = 'daily new cases'
            case_txt_0ze = 'logarithm of daily new cases'
            case_txt_1 = 'cases'
        elif cases=='deaths':
            case_txt_0 = 'number of deaths'
            case_txt_0zl = 'daily numbers of deaths'
            case_txt_0ze = 'logarithm of daily numbers of deaths'
            case_txt_1 = 'deaths'

        if window_length<0:
            #ax1.set_title('Linear regression for {0}{1} with optimised window length.'.format('logarithm of ' if exp_or_lin=='exp' else '', case_txt_0))
            ax1.set_title('Linear regression for the {0} with optimised window length.'.format(case_txt_0ze if exp_or_lin=='exp' else case_txt_0zl))
        else:
            #ax1.set_title('Linear regression for {0}{1}. Window length: {2} data points.'.format('logarithm of ' if exp_or_lin=='exp' else '', case_txt_0, window_length))
            ax1.set_title('Linear regression for the {0}. Window length: {1} data points.'.format(case_txt_0ze if exp_or_lin=='exp' else case_txt_0zl, window_length))

        if xaxis == 'cases':
            if cases=='confirmed':
                ax1.set_xlabel('Number of {0} per {1} people'.format(case_txt_1, utils.separated(str(normalise_by), lang)) if normalise=='xy' else 'Number of cases')
            elif cases=='deaths':
                ax1.set_xlabel('Number of {0} per {1} people'.format(case_txt_1, utils.separated(str(normalise_by), lang)) if normalise=='xy' else 'Number of deaths')
        #else:
        #    fig.subplots_adjust(bottom=space_below)

        if incr_or_rate == 'rate':
            ax1.set_ylabel('Daily growth rate')
            fig.suptitle('Daily growth rate of number of {} ('.format(case_txt_1) +\
             latest_date.strftime('%d %B %Y')+')')
        else:
            if normalise is None:
                ax1.set_ylabel('Daily increment')
                fig.suptitle('Daily increment of number of {} ('.format(case_txt_1) +\
                 latest_date.strftime('%d %B %Y')+')')
            else:
                ax1.set_ylabel('Daily increment per {} people'.format(utils.separated(str(normalise_by), lang)))
                fig.suptitle('Daily increment of number of {0} per {1} people ({2})'.format(case_txt_1, utils.separated(str(normalise_by), lang), latest_date.strftime('%d %B %Y')))

    #fig.tight_layout()

    geounit_list = list(dif_all.keys())
    for i in range(len(geounit_list)):
        if cycle_linestyle==1:
            ax1.plot(dif_all[geounit_list[i]], label=geounit_list[i], linestyle=['solid', 'dotted', 'dashed', 'dashdot'][i % 4])
        elif filename == 'great_powers':
            #ax1.plot(dif_all[geounit_list[i]], label=geounit_list[i], color=['tab:red', 'tab:blue', 'tab:gray'][i % 3])
            ax1.plot(dif_all[geounit_list[i]], label=geounit_list[i], color=['tab:orange', 'tab:blue', 'tab:gray', 'tab:purple', 'tab:green', 'tab:olive'][i % 6])
        else:
            ax1.plot(dif_all[geounit_list[i]], label=geounit_list[i])

    #for tick in ax1.get_yticklabels():
    #    tick = str(tick) + '%'
    if xaxis == 'cases':
        ax1.set_xscale("log")
        ax1.set_xlim(left=left_bound, right=right_bound)
        ax1.set_xticklabels([float(tick) if float(tick)<1 else utils.separated(str(int(tick)), lang) for tick in ax1.get_xticks()])
    else:
        fig.subplots_adjust(bottom=space_below)
        ax1.set_xlim(left=left_bound, right=right_bound)
        for tick in ax1.get_xticklabels():
            tick.set_rotation(80)

    ax1.set_ylim(bottom=bottom_bound, top=top_bound)
    if incr_or_rate == 'rate':
        ax1.set_yticklabels([str(int(tick)) + '%' for tick in ax1.get_yticks()])
    ax1.legend()
    ax1.grid(True, axis='y')
    #plt.gcf().text(0.905, 0.87, "© Bence Mélykúti, Melykuti.me, 2020", fontsize=8, color='lightgray', rotation=90) # 0.905, 0.37
    #plt.gcf().text(0.905, 0.87, "© Bence Mélykúti, 2020. http://COVID19.Melykuti.Be", fontsize=8, color='lightgray', rotation=90)
    if lang=='de':
        plt.gcf().text(0.905, 0.498, "© Bence Mélykúti, 2020. http://COVID19de.Melykuti.Be", fontsize=8, color='lightgray', rotation=90)
    else: # i.e. 'en'
        plt.gcf().text(0.905, 0.515, "© Bence Mélykúti, 2020. http://COVID19.Melykuti.Be", fontsize=8, color='lightgray', rotation=90)
    if save_not_show==0:
        plt.show()
    elif save_not_show==1:
        imgfile = filename + '_DGR_'\
                  + latest_date.strftime('%Y-%m-%d') + '_' \
                  + (normalise if normalise is not None else '0') + '_' \
                  + str(window_length) + '_' + exp_or_lin + '_' + xaxis + '_' \
                  + incr_or_rate + '_' + cases + '.png'
        plt.savefig(imgfile)
        plt.close(fig)

if __name__ == '__main__':
    if window_length > 0: # we'll omit from time series the early part that is not plotted to save computation
        wl_hi = window_length
    else:
        wl_hi = 15
    fixed_positive_window_length = 2
    if window_length < fixed_positive_window_length:
        if window_length <= 0: # run rm_consecutive_early_zeros w. 0, for i in range from wl_lo=4
            window_length_for_cutoffs = 4 #fixed_positive_window_length
        else: # run rm_consecutive_early_zeros w. 0, for i in range from fixed_positive_window_length=2
            window_length = fixed_positive_window_length
            window_length_for_cutoffs = fixed_positive_window_length
    else: # run rm_consecutive_early_zeros w. 0, for i in range from window_length
        window_length_for_cutoffs = window_length

    dif_all = dict()
    latest_date = None

    if countries != 'Deutschland':
        if normalise=='xy' or normalise=='y':
            pop_world = utils.load_population_world()
        df = utils.open_csvs()
        for country in countries:
            print(country)
            #case_no = list()
            #dif_optim = list() # list of daily increase factors
            df_ts = utils.data_preparation(df, country, cases)
            #print(df_ts)
            if not isinstance(country, str): # If it's a province or state of a country or region.
                country = country[0]
            if normalise=='xy':
                if country=='Hubei': #'China':
                    df_ts = normalise_by*df_ts/58500000 # Population of Hubei province
                else:
                    df_ts = normalise_by*df_ts/pop_world[country]
            #print(df_ts)
            df_ts, dif_optim, case_no, latest_date, e_or_l = call_process_geounit_minimal(
                df_ts, latest_date, window_length, exp_or_lin)
            dif_all[country] = pd.Series(dif_optim, index=case_no)
            if normalise == 'y' and incr_or_rate=='incr':
                dif_all[country] = normalise_by*dif_all[country]/pop_world[country]
            #print(dif_optim)
            #dif_all[country] = pd.Series(dif_optim, index=case_no, name=country)
            #dif_all[country] = pd.Series(dif_optim, index=case_no)

    else:
        #lang = 'de'
        from DEU import data_preparation_DEU
        if normalise=='xy' or normalise=='y':
            pop_DEU = utils.load_population_DEU()
        allowed_values = \
            ['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen',
            'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
            'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen',
            'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen',
            'Deutschland',
            'alle']
        figures_diff = data_preparation_DEU(cases)
        if normalise=='xy':
            for j in figures_diff.columns:
                figures_diff[j] = normalise_by*figures_diff[j]/pop_DEU[j]
        # For sensitivity analysis, enter fake values here
        #figures_diff['Baden-Württemberg'][-2] = 2800 # test
        #figures_diff['Baden-Württemberg'][-1] = 3000 # test
        for j in range(0, figures_diff.shape[1]):
        #for j in [0, 1, 2, 16]:
            print(allowed_values[j])
            #case_no = list()
            #dif_optim = list() # list of daily increase factors
            df_ts = figures_diff.iloc[:,j]
            df_ts, dif_optim, case_no, latest_date, e_or_l = call_process_geounit_minimal(
                df_ts, latest_date, window_length, exp_or_lin)
            dif_all[allowed_values[j]] = pd.Series(dif_optim, index=case_no)
            if normalise == 'y' and incr_or_rate=='incr':
                dif_all[allowed_values[j]] = normalise_by*dif_all[allowed_values[j]]/pop_DEU[j]
    
    #print(df_ts)
    #print(dif_ts)
    print(dif_all)

    if save_not_show in [0, 1]:
        plotting_countries(dif_all, save_not_show, latest_date, window_length, e_or_l, left_bound, right_bound, bottom_bound, top_bound, cycle_linestyle, lang)
