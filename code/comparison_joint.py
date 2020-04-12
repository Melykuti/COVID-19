'''
Compares the daily increase factor as a function of case number across countries
using the JHU CSSE dataset:
https://github.com/CSSEGISandData

exec(open('comparison_joint.py').read())
12/3-12/4/2020
'''

import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from utils import open_csvs, data_preparation, rm_early_zeros, rm_consecutive_early_zeros, separated, select_window_length, pick_exp_vs_lin, print_header, print_results, load_population_world, load_population_DEU
from importlib import reload

### User input ###

left_bound=0.8
bottom_bound=-10.; top_bound=100.
cycle_linestyle = 0 # if 0, then all lines are solid; if 1, then it cycles through solid, dotted, dashed, dash-dotted
#normalise = 1 # 1 if you want to normalise by population size, o.w. 0
normalise_by = int(1e5) # display case numbers per this many people

#window_length = 4 # from latest data point back into past if positive; if nonpositive, then it searches for optimum for model fitting (recommended)
window_length = -1

save_not_show = 1 # if 0, then shows the plot; if 1, then saves it; o.w. it does neither
lang = 'en' # 'de' for German, anything else for English
cases = 'confirmed' # 'confirmed' or 'deaths' or 'active' or 'recovered'
exp_or_lin = 'exp' # Use 'exp' model (fitting linear model on logarithmic scale) or 'lin' model or 'both' for trying both and selecting the better.

#countries = ['US', 'Italy', 'China', 'Spain', 'Germany', 'Iran', 'France', 'Korea, South', 'Switzerland', 'United Kingdom', 'Netherlands', 'Japan']; left_bound=600; right_bound=None; bottom_bound=0.; top_bound=80.; normalise = 0; filename = 'Joint'; cycle_linestyle = 1
#countries = ['US', 'Italy', 'China', 'Spain', 'Germany', 'Iran', 'France', 'Korea, South', 'Switzerland', 'United Kingdom', 'Netherlands', 'Japan']; left_bound=1.; right_bound=None; bottom_bound=0.; top_bound=80.; normalise = 1; filename = 'Joint'; cycle_linestyle = 1

#countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; left_bound=50.; right_bound=4000.; bottom_bound=0.; top_bound=80.; normalise = 0; filename = 'Visegrad'; cycle_linestyle = 1
#countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; left_bound=2; right_bound=None; bottom_bound=0.; top_bound=80.; normalise = 1; filename = 'Visegrad'; cycle_linestyle = 1

#countries = 'Deutschland'; left_bound=200; right_bound=None; bottom_bound=0.; top_bound=60.; normalise = 0; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1
countries = 'Deutschland'; left_bound=9; right_bound=None; bottom_bound=0.; top_bound=60.; normalise = 1; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1

#countries = ['China', 'EU', 'US']; left_bound=500; right_bound=None; bottom_bound=0.; top_bound=60.; normalise = 0; filename = 'great_powers'; lang = 'en'; cycle_linestyle = 0
#countries = ['China', 'EU', 'US']; left_bound=0.1; right_bound=150.; bottom_bound=0.; top_bound=60.; normalise = 1; filename = 'great_powers'; lang = 'en'; cycle_linestyle = 0

#countries = ['Switzerland', 'United Kingdom']; left_bound=10.; right_bound=None; bottom_bound=0.; top_bound=80.; normalise = 1; filename = 'test';
#countries = ['Italy', 'Spain', 'France', 'Germany', 'Switzerland', ['United Kingdom', 'United Kingdom'], 'Netherlands', 'Austria', 'Sweden', 'Denmark', 'Japan', 'Hungary', 'Korea, South', 'China']
#countries = ['Hungary']; left_bound=50*normalise_by/10e6; right_bound=None; normalise = 1; filename = 'Visegrad'
#countries = ['Iceland']; left_bound=None; right_bound=None; normalise = 0; filename = 'Iceland'
#countries = ['Iceland']; left_bound=0.8; right_bound=None; normalise = 1; filename = 'Iceland'

#, 'Netherlands', 'Austria', 'Sweden', 'Denmark', 'Japan', 'Hungary', 'Korea, South', ]
#countries = [ 'Japan']; left_bound=400; right_bound=None
#countries = ['Italy']
#countries = ['Italy', 'Japan', 'Denmark', 'France', 'Germany', 'Spain', 'Switzerland']
#country = 'France' #'Switzerland' #'Netherlands' #'Denmark' # Denmark, Spain, France, Germany, Sweden
#country = 'Korea, South'
#country = ['United Kingdom', 'United Kingdom']

### End of user input ###

def analysis_exp_minimal(df_ts, window_length):
    '''
    Because of log2, this requires all entries in df_ts to be positive.
    '''
    if len(df_ts)<window_length:
        results = 7 * [0]
        results[-1] = 100
        return results, None
    intl_lo_days = 4
    intl_hi_days = 6
    ylog2 = np.log2(df_ts.iloc[-window_length:].values)
    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(np.arange(len(ylog2)).reshape(-1, 1), ylog2)
    results = [(math.pow(2, model.coef_[0])-1)*100, 0, df_ts.iloc[-1], 0, 0,
                #1/model.coef_[0],
                #df_ts.iloc[-1],
                #int(math.pow(2, model.predict(np.array(len(ylog2)-1+intl_lo_days).reshape(1,-1)))),
                #int(math.pow(2, model.predict(np.array(len(ylog2)-1+intl_hi_days).reshape(1,-1)))),
                model.score(np.arange(len(ylog2)).reshape(-1, 1), ylog2),
                model.predict(np.array(len(ylog2)-1).reshape(-1, 1))[0]-ylog2[-1]]
    return results, model

def analysis_lin_minimal(df_ts, window_length):
    '''
    Because of log2, this requires last entry in df_ts to be positive.
    '''
    if len(df_ts)<window_length:
        results = 7 * [0]
        results[-1] = 100
        return results, None
    intl_lo_days = 4
    intl_hi_days = 6
    y = df_ts.iloc[-window_length:].values
    model = linear_model.LinearRegression(fit_intercept=True)
    model.fit(np.arange(len(y)).reshape(-1, 1), y)
    results = [model.coef_[0]/y[-1]*100, 0, df_ts.iloc[-1], 0, 0,
                #2*y[-1]/model.coef_[0],
                #df_ts.iloc[-1],
                #int(model.predict(np.array(len(y)-1+intl_lo_days).reshape(1,-1))),
                #int(model.predict(np.array(len(y)-1+intl_hi_days).reshape(1,-1))),
                model.score(np.arange(len(y)).reshape(-1, 1), y),
                model.predict(np.array(len(y)-1).reshape(-1, 1))[0]/y[-1]-1]
    return results, model

def process_geounit_minimal(df_ts, window_length, exp_or_lin='both'):
    '''
    This processes one geographical unit.
    df_ts is the time series.
    '''
    df_ts = rm_early_zeros(df_ts)
    if window_length > 0:
        selected_window_length = window_length
        #results, model = analysis_minimal(df_ts, window_length)
        if exp_or_lin=='both':
            results_e, model_e = analysis_exp_minimal(df_ts, window_length)
            results_l, model_l = analysis_lin_minimal(df_ts, window_length)
            results, model, exp_or_lin = pick_exp_vs_lin(results_e, model_e, results_l, model_l)
        elif exp_or_lin=='exp':
            results, model = analysis_exp_minimal(df_ts, window_length)
        else:
            results, model = analysis_lin_minimal(df_ts, window_length)

    else: # do a search over window_lengths for best possible fit
        # minimum and maximum allowed window lengths; we test all in this closed interval
        wl_lo = 4
        wl_hi = 15 # this end point is not included
        # Rule out zeros because we take logarithm; rule out windows longer than the time series df_ts.
        #wl_hi = min(wl_hi, 1+len(df_ts[df_ts[df_ts>0].idxmin():]), 1+len(df_ts))
        wl_hi = min(wl_hi, 1+len(df_ts))
        if wl_hi <= wl_lo: # then abort
            results, model = analysis_exp_minimal([], 1)
            return results, model, window_length, exp_or_lin
        '''
        R = pd.DataFrame(np.zeros((wl_hi-wl_lo, 7)), index=range(wl_lo, wl_hi))
        models = dict()
        for wl in range(wl_lo, wl_hi):
            result_wl, model = analysis_minimal(df_ts, wl)
            R.iloc[wl-wl_lo, :] = result_wl
            models[wl] = model
        #R = R.astype({2: int, 3: int, 4: int})
        results, selected_window_length = select_window_length(R)
        model = models[selected_window_length]
        '''
        if exp_or_lin in ['exp', 'both']:
            R_e = pd.DataFrame(np.zeros((wl_hi-wl_lo, 7)), index=range(wl_lo, wl_hi))
            models_e = dict()
        if exp_or_lin in ['lin', 'both']:
            R_l = pd.DataFrame(np.zeros((wl_hi-wl_lo, 7)), index=range(wl_lo, wl_hi))
            models_l = dict()
        for wl in range(wl_lo, wl_hi): # last wl_hi-1 points must be available and positive <==
            if exp_or_lin in ['exp', 'both']:
                result_wl, model = analysis_exp_minimal(df_ts, wl) # last wl points must be available and positive
                R_e.iloc[wl-wl_lo, :] = result_wl
                models_e[wl] = model
            if exp_or_lin in ['lin', 'both']:
                result_wl, model = analysis_lin_minimal(df_ts, wl)
                R_l.iloc[wl-wl_lo, :] = result_wl
                models_l[wl] = model
        if exp_or_lin in ['exp', 'both']:
            results_e, selected_window_length_e = select_window_length(R_e)
            model_e = models_e[selected_window_length_e]
        if exp_or_lin in ['lin', 'both']:
            results_l, selected_window_length_l = select_window_length(R_l)
            model_l = models_l[selected_window_length_l]
        if exp_or_lin == 'exp':
            results, model, selected_window_length = results_e[:-1], model_e, selected_window_length_e
        if exp_or_lin == 'lin':
            results, model, selected_window_length = results_l[:-1], model_l, selected_window_length_l
        if exp_or_lin == 'both':
            results, model, exp_or_lin = pick_exp_vs_lin(results_e, model_e, results_l, model_l)
            selected_window_length = selected_window_length_e if exp_or_lin=='exp'\
                                     else selected_window_length_l

    return results, model, selected_window_length, exp_or_lin

def plotting_countries(dif_all, save_not_show, latest_date, window_length, left_bound=None, right_bound=None, bottom_bound=None, top_bound=None, cycle_linestyle=0, lang='en'):
    fig, ax1 = plt.subplots(1,1, figsize=(12., 8.))
    #fig, ax1 = plt.subplots(1,1, figsize=(9.6, 6.4))
    if lang=='de':
        if window_length<0:
            ax1.set_title('Lineare Regression mit optimaler Fenstergröße.')
        else:
            ax1.set_title('Lineare Regression mit Fenstergröße von {} Datenpunkten.'.format(window_length))
        ax1.set_xlabel('Fallzahl auf {} Einwohner'.format(separated(str(normalise_by), lang)) if normalise==1 else 'Fallzahl')
        ax1.set_ylabel('Wachstumsrate der Fallzahlen')
        fig.suptitle('Wachstumsrate der Fallzahlen, Stand ' + latest_date.strftime('%d.%m.%Y'))
    else:
        if window_length<0:
            ax1.set_title('Linear regression with optimised window length.')
        else:
            ax1.set_title('Linear regression window length: {} data points.'.format(window_length))
        ax1.set_xlabel('Number of cases per {} people'.format(separated(str(normalise_by), lang)) if normalise==1 else 'Number of cases')
        ax1.set_ylabel('Daily growth rate')
        fig.suptitle('Daily growth rate of number of cases (' + latest_date.strftime('%d %B %Y') + ')')
    #fig.tight_layout()
    #fig.subplots_adjust(bottom=0.2)
    geounit_list = list(dif_all.keys())
    for i in range(len(geounit_list)):
        if cycle_linestyle==1:
            ax1.plot(dif_all[geounit_list[i]], label=geounit_list[i], linestyle=['solid', 'dotted', 'dashed', 'dashdot'][i % 4])
        elif filename == 'great_powers':
            ax1.plot(dif_all[geounit_list[i]], label=geounit_list[i], color=['tab:red', 'tab:blue', 'tab:gray'][i % 3])
        else:
            ax1.plot(dif_all[geounit_list[i]], label=geounit_list[i])
    #for tick in ax1.get_xticklabels():
    #    tick.set_rotation(80)
    #for tick in ax1.get_yticklabels():
    #    tick = str(tick) + '%'
    ax1.set_xscale("log")
    ax1.set_xlim(left=left_bound, right=right_bound)
    ax1.set_xticklabels([float(tick) if float(tick)<1 else separated(str(int(tick)), lang) for tick in ax1.get_xticks()])
    ax1.set_ylim(bottom=bottom_bound, top=top_bound)
    ax1.set_yticklabels([str(int(tick)) + '%' for tick in ax1.get_yticks()])
    ax1.legend()
    ax1.grid(True, axis='y')
    #plt.gcf().text(0.905, 0.87, "© Bence Mélykúti, Melykuti.me, 2020", fontsize=8, color='lightgray', rotation=90) # 0.905, 0.37
    plt.gcf().text(0.905, 0.87, "© Bence Mélykúti, http://COVID19.Melykuti.Be, 2020", fontsize=8, color='lightgray', rotation=90)
    if save_not_show==0:
        plt.show()
    elif save_not_show==1:
        imgfile = filename + '_DGR_' +\
                  latest_date.strftime('%Y-%m-%d') + '_' + str(normalise) + '_' +\
                  str(window_length) + '.png'
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
        if normalise==1:
            #from load_population import load_population_world
            pop_world = load_population_world()
        #labels = ['Confirmed', 'Deaths', 'Recovered']
        # Since 24 March 2020
        #labels = ['confirmed', 'deaths']
        df = open_csvs()
        for country in countries:
            print(country)
            case_no = list()
            dif_optim = list() # list of daily increase factors
            df_ts = data_preparation(df, country, cases)
            #print(df_ts)
            if not isinstance(country, str): # If it's a province or state of a country or region.
                country = country[0]
            if normalise==1:
                if country=='Hubei': #'China':
                    df_ts = normalise_by*df_ts/58500000 # Population of Hubei province
                else:
                    df_ts = normalise_by*df_ts/pop_world[country]
            #print(df_ts)
            df_ts = rm_consecutive_early_zeros(df_ts, 0) #window_length_for_cutoffs-2)
            #print(df_ts)
            df_ts = df_ts[(df_ts>left_bound).idxmax()-wl_hi*pd.DateOffset():]
            #print(df_ts)
            if latest_date==None or latest_date<df_ts.index[-1]:
                latest_date = df_ts.index[-1]

            for i in range(window_length_for_cutoffs-len(df_ts), 1):
                results, model, selected_window_length, e_or_l = process_geounit_minimal(
                                                        df_ts[:len(df_ts)+i], window_length, exp_or_lin)
                #if len(df_ts)+i<=5:
                #    print('index is', i, '  input is\n', df_ts[:len(df_ts)+i], '\nresult is\n', results)
                dif_optim.append(results[0])
                case_no.append(results[2])

            #print(dif_optim)
            #print(case_no, pop_world[country])
            dif_all[country] = pd.Series(dif_optim, index=case_no, name=country)

    else:
        #lang = 'de'
        from DEU import data_preparation_DEU
        if normalise==1:
            #from load_population import load_population_DEU
            pop_DEU = load_population_DEU()
        #reload(DEU)
        allowed_values = \
            ['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen',
            'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
            'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen',
            'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen',
            'Deutschland',
            'alle']
        figures_diff = data_preparation_DEU(cases)
        if normalise==1:
            for j in figures_diff.columns:
                figures_diff[j] = normalise_by*figures_diff[j]/pop_DEU[j]
        # For sensitivity analysis, enter fake values here
        #figures_diff['Baden-Württemberg'][-2] = 2800 # test
        #figures_diff['Baden-Württemberg'][-1] = 3000 # test
        for j in range(0, figures_diff.shape[1]):
        #for j in [0, 1, 2, 16]:
            print(allowed_values[j])
            case_no = list()
            dif_optim = list() # list of daily increase factors
            df_ts = figures_diff.iloc[:,j]
            df_ts = rm_consecutive_early_zeros(df_ts, window_length_for_cutoffs-2)
            if latest_date==None or latest_date<df_ts.index[-1]:
                latest_date = df_ts.index[-1]
            for i in range(window_length_for_cutoffs-len(df_ts), 1):
                results, model, selected_window_length, e_or_l = process_geounit_minimal(
                                                        df_ts[:len(df_ts)+i], window_length, exp_or_lin)
                dif_optim.append(results[0])
                case_no.append(results[2])
                if exp_or_lin=='both':
                    print(e_or_l) # If this is 'both', then it is because process_geounit_minimal() was aborted due to wl_hi <= wl_lo.
            dif_all[allowed_values[j]] = pd.Series(dif_optim, index=case_no)#, name=country)
    
    #print(dif_fixed)
    #dif_fixed = pd.Series(dif_fixed, index=[df_ts.index[t] for t in range(window_length-len(df_ts), 0)])
    #dif_optim = pd.Series(dif_optim, index=[df_ts.index[t] for t in range(window_length-len(df_ts), 0)])
    #dif_fixed = pd.Series(dif_fixed, index=[df_ts.index[len(df_ts)+t-1] for t in range(window_length-len(df_ts), 1)])
    #dif_optim = pd.Series(dif_optim, index=[df_ts.index[len(df_ts)+t-1] for t in range(window_length-len(df_ts), 1)])
    #dif_trivi = pd.Series(dif_trivi, index=[df_ts.index[len(df_ts)+t-1] for t in range(window_length-len(df_ts), 1)])
    #print(dif_fixed)

    #dif_ts = pd.concat([dif_fixed, dif_optim, dif_trivi], axis=1, keys=['fixed window', 'optimised window', 'trivial ratio'])
    #dif_ts = pd.concat([dif_fixed, dif_optim, dif_trivi], axis=1, keys=['fixed window', 'optimised window', 'trivial ratio'])
    #print(df_ts)
    #print(dif_ts)
    print(dif_all)
    #print_header()
    #print_results(country, results, selected_window_length, lang)

    if save_not_show in [0, 1]:
        #if normalise == 1:
        #    left_bound = left_bound*normalise_by/pop_world[country] # but which country?
        plotting_countries(dif_all, save_not_show, latest_date, window_length, left_bound, right_bound, bottom_bound, top_bound, cycle_linestyle, lang)
