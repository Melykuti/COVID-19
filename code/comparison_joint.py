'''
Compares the daily increase factor as a function of case number across countries
using the JHU CSSE dataset:
https://github.com/CSSEGISandData

exec(open('comparison_joint.py').read())
12-22/3/2020
'''

import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from utils import open_csvs, data_preparation, rm_early_zeros, rm_consecutive_early_zeros, select_window_length, print_header, print_results, load_population_world, load_population_DEU
from importlib import reload

### User input ###

lower_bound=0.8
#normalise = 1 # 1 if you want to normalise by population size, o.w. 0
normalise_by = int(1e5)

#window_length = 4 # from latest data point back into past if positive; if nonpositive, then it searches for optimum for model fitting (recommended)
window_length = -1

save_not_show = 1 # if 0, then shows the plot; if 1, then saves it; o.w. it does neither
lang = 'en' # 'de' for German, anything else for English

#countries = ['China', 'Italy', 'Spain', 'Germany', 'Iran', 'France', 'Korea, South', 'Switzerland', ['United Kingdom', 'United Kingdom'], 'Japan']; lower_bound=400; upper_bound=None; normalise = 0; filename = 'Joint'
#countries = ['China', 'Italy', 'Spain', 'Germany', 'Iran', 'France', 'Korea, South', 'Switzerland', ['United Kingdom', 'United Kingdom'], 'Japan']; lower_bound=0.8; upper_bound=None; normalise = 1; filename = 'Joint'

#countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; lower_bound=50.; upper_bound=2000; normalise = 0; filename = 'Visegrad'
countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; lower_bound=50*normalise_by/10e6; upper_bound=None; normalise = 1; filename = 'Visegrad'

#countries = 'Deutschland'; lower_bound=50; upper_bound=None; normalise = 0; filename = 'Deutschland'; lang = 'de'
#countries = 'Deutschland'; lower_bound=2; upper_bound=None; normalise = 1; filename = 'Deutschland'; lang = 'de'

#countries = ['Switzerland', ['United Kingdom', 'United Kingdom']]
#countries = ['Italy', 'Spain', 'France', 'Germany', 'Switzerland', ['United Kingdom', 'United Kingdom'], 'Netherlands', 'Austria', 'Sweden', 'Denmark', 'Japan', 'Hungary', 'Korea, South', 'China']
#countries = ['Hungary']; lower_bound=50*normalise_by/10e6; upper_bound=None; normalise = 1; filename = 'Visegrad'
#countries = ['Iceland']; lower_bound=0.8; upper_bound=None; normalise = 0; filename = 'Iceland'
#countries = ['Iceland']; lower_bound=0.8; upper_bound=None; normalise = 1; filename = 'Iceland'

#, 'Netherlands', 'Austria', 'Sweden', 'Denmark', 'Japan', 'Hungary', 'Korea, South', ]
#countries = [ 'Japan']; lower_bound=400; upper_bound=None
#countries = ['Italy']
#countries = ['Italy', 'Japan', 'Denmark', 'France', 'Germany', 'Spain', 'Switzerland']
#country = 'France' #'Switzerland' #'Netherlands' #'Denmark' # Denmark, Spain, France, Germany, Sweden
#country = 'Korea, South'
#country = ['United Kingdom', 'United Kingdom']

### End of user input ###

'''
def data_preparation_cases(df, country):

    Similar to data_preparation() but only confirmed cases without Recovered and Deaths

    l = list()
    for i in range(3):
        k = labels[i]
        if isinstance(country, str):
            l.append(df[k][df[k]['Country/Region']==country].iloc[:,4:])
        elif len(country)==2: # if it's a pair of [Province/State, Country/Region]
            l.append(df[k][np.logical_and(df[k]['Province/State']==country[0],
                                          df[k]['Country/Region']==country[1])].iloc[:,4:])
    dft = pd.concat(l, ignore_index=True)
    dft.rename(index={i: labels[i] for i in range(3)}, inplace=True)
    df_ts = dft.loc['Confirmed'] #-dft.loc['Deaths']-dft.loc['Recovered']
    df_ts.rename(index={df_ts.index[i]: pd.to_datetime(df_ts.index)[i] for i in range(len(df_ts.index))}, inplace=True)
    return df_ts
'''

def analysis_minimal(df_ts, window_length):
    '''
    Because of log2, this requires all entries in df_ts to be positive.
    '''
    if len(df_ts)<=window_length:
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

def process_geounit_minimal(df_ts, window_length):
    '''
    This processes one geographical unit.
    df_ts is the time series.
    '''
    df_ts = rm_early_zeros(df_ts)
    if window_length > 0:
        selected_window_length = window_length
        results, model = analysis_minimal(df_ts, window_length)
    else: # do a search over window_lengths for best possible fit
        # minimum and maximum allowed window lengths; we test all in this closed interval
        wl_lo = 4
        wl_hi = 15 # this end point is not included
        # Rule out zeros because we take logarithm; rule out windows longer than the time series df_ts.
        #wl_hi = min(wl_hi, 1+len(df_ts[df_ts[df_ts>0].idxmin():]), 1+len(df_ts))
        wl_hi = min(wl_hi, 1+len(df_ts))
        if wl_hi <= wl_lo: # then abort
            results, model = analysis_minimal([], 1)
            return results, model, window_length
        R = pd.DataFrame(np.zeros((wl_hi-wl_lo, 7)), index=range(wl_lo, wl_hi))
        models = dict()
        for wl in range(wl_lo, wl_hi):
            result_wl, model = analysis_minimal(df_ts, wl)
            R.iloc[wl-wl_lo, :] = result_wl
            models[wl] = model
        #R = R.astype({2: int, 3: int, 4: int})

        results, selected_window_length = select_window_length(R)
        model = models[selected_window_length]

    return results, model, selected_window_length

def plotting_countries(dif_all, save_not_show, latest_date, window_length, lower_bound=None, upper_bound=None, lang='en'):

    #lower_bound = 100
    fig, ax1 = plt.subplots(1,1, figsize=(12., 8.))
    #fig, ax1 = plt.subplots(1,1, figsize=(9.6, 6.4))
    #fig, (ax1, ax2) = plt.subplots(1,2, figsize=(9.6, 4.8))
    if lang=='de':
        if window_length<0:
            ax1.set_title('Lineare Regression mit optimaler Fenstergröße.')
        else:
            ax1.set_title('Lineare Regression mit Fenstergröße von {} Datenpunkten.'.format(window_length))
        ax1.set_xlabel('Fallzahl auf {} Einwohner'.format(normalise_by) if normalise==1 else 'Fallzahl')
        ax1.set_ylabel('Wachstumsrate der Fallzahlen')

        #line0 = 'Mit Fenstergröße {}'.format(window_length)
        #line1 = 'Mit optimaler Fenstergröße'
        #line2 = 'Triviale Quote'
        fig.suptitle('Wachstumsrate der Fallzahlen, Stand ' + latest_date.strftime('%d.%m.%Y'))
    else:
        #line0 = 'With window length {}'.format(window_length)
        #line1 = 'With optimised window length'
        #line2 = 'Trivial ratio'
        if window_length<0:
            ax1.set_title('Linear regression with optimised window length.')
        else:
            ax1.set_title('Linear regression window length: {} data points.'.format(window_length))
        ax1.set_xlabel('Number of cases per {} people'.format(normalise_by) if normalise==1 else 'Number of cases')
        ax1.set_ylabel('Daily increase factor')
        fig.suptitle('Daily increase factor of number of cases (' + latest_date.strftime('%d %B %Y') + ')')
    #fig.tight_layout()
    #fig.subplots_adjust(bottom=0.2)
    for country in dif_all:
        ax1.plot(dif_all[country], label=country)
        '''
        if lower_bound==None:
            if upper_bound==None:
                ax1.plot(dif_all[country], label=country)
            else:
                ax1.plot(dif_all[country][dif_all[country].index<=upper_bound], label=country)
        else:
            if upper_bound==None:
                ax1.plot(dif_all[country][dif_all[country].index>=lower_bound], label=country)
            else:
                ax1.plot(dif_all[country][np.logical_and(dif_all[country].index>=lower_bound,
                    dif_all[country].index<=upper_bound)], label=country)
        '''
    #ax1.plot(df_ts.iloc[:,1], label=line1)
    #ax1.plot(df_ts.iloc[:,2], label=line2)
    #ax2.plot(df_ts[df_ts>0], label=line0)
    #ax2.plot(df_ts[df_ts>0].iloc[-window_length:].index, np.power(2, np.arange(0, window_length)*model.coef_ + model.intercept_), label=line1)
    #ax2.set_yscale("log")
    #for tick in ax1.get_xticklabels():
    #    tick.set_rotation(80)
    #for tick in ax1.get_yticklabels():
    #    tick = str(tick) + '%'
    ax1.set_xscale("log")
    ax1.set_xlim(left=lower_bound, right=upper_bound)
    ax1.set_ylim(bottom=-10., top=100.)
    ax1.set_yticklabels([str(int(tick)) + '%' for tick in ax1.get_yticks()])
    ax1.legend()
    ax1.grid(True, axis='y')
    plt.gcf().text(0.905, 0.87, "© Bence Mélykúti, Melykuti.me, 2020", fontsize=8, color='lightgray', rotation=90) # 0.905, 0.37
    #plt.gcf().text(0.905, 0.615, "© Bence Mélykúti, Melykuti.me, 2020", fontsize=8, color='lightgray', rotation=90)
    if save_not_show==0:
        plt.show()

    elif save_not_show==1:
        '''
        if country == 'Deutschland':
            imgfile = filename + '_DIF_' +\
                      latest_date.strftime('%Y-%m-%d') + '_' + str(normalise) + '_' +\
                      str(window_length) + '.png'
        else:
            #imgfile = 'joint_DIF_' +\
            imgfile = filename + '_DIF_' +\
                      latest_date.strftime('%Y-%m-%d') + '_' + str(normalise) + '_' +\
                      str(window_length) + '.png'
        '''
        imgfile = filename + '_DIF_' +\
                  latest_date.strftime('%Y-%m-%d') + '_' + str(normalise) + '_' +\
                  str(window_length) + '.png'
        plt.savefig(imgfile)
        plt.close(fig)

if __name__ == '__main__':
    fixed_positive_window_length = 2
    if window_length < fixed_positive_window_length:
        if window_length <= 0:
            window_length_for_cutoffs = fixed_positive_window_length
        else:
            window_length = fixed_positive_window_length
            window_length_for_cutoffs = fixed_positive_window_length

    dif_all = dict()
    latest_date = None

    if countries != 'Deutschland':
        if normalise==1:
            #from load_population import load_population_world
            pop_world = load_population_world()
        labels = ['Confirmed', 'Deaths', 'Recovered']
        df = open_csvs()
        for country in countries:
            print(country)
            case_no = list()
            dif_optim = list() # list of daily increase factors
            df_ts = data_preparation(df, country, only_cases=True)
            #print(df_ts)
            if not isinstance(country, str): # If it's a province or state of a country or region.
                country = country[0]
            if normalise==1:
                if country=='China':
                    df_ts = normalise_by*df_ts/58500000 # Population of Hubei province
                else:
                    df_ts = normalise_by*df_ts/pop_world[country]
            #print(df_ts)
            df_ts = rm_consecutive_early_zeros(df_ts, window_length_for_cutoffs-2)
            if latest_date==None or latest_date<df_ts.index[-1]:
                latest_date = df_ts.index[-1]

            for i in range(window_length_for_cutoffs-len(df_ts), 1):
                #results, model, selected_window_length = process_geounit_minimal(df_ts[:len(df_ts)+i], window_length)
                #dif_fixed.append(results[0])
                results, model, selected_window_length = process_geounit_minimal(df_ts[:len(df_ts)+i], window_length)
                dif_optim.append(results[0])
                case_no.append(results[2])
                #dif_trivi.append(((df_ts[len(df_ts)+i-1]/df_ts[len(df_ts)+i-2])-1)*100)

            #if not isinstance(country, str): # If it's a province or state of a country or region.
            #    country = country[0]
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
        figures_diff = data_preparation_DEU(only_cases=True)
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
                results, model, selected_window_length = process_geounit_minimal(df_ts[:len(df_ts)+i], window_length)
                dif_optim.append(results[0])
                case_no.append(results[2])
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
        #    lower_bound = lower_bound*normalise_by/pop_world[country] # but which country?
        plotting_countries(dif_all, save_not_show, latest_date, window_length, lower_bound, upper_bound, lang)
