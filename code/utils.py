import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
#import importlib
from importlib import reload

def open_csvs():
    '''
    Finding and opening your most recent data download if timestamp == None.
    Alternatively, specify a substring of requested timestamp to select which files to open.
    '''
    timestamp = None
    #timestamp = '20200312_21-43'
    df=dict()
    lists = list([list(), list()])
    with os.scandir() as it:
        for entry in it:
            for i in range(2):
                if (timestamp==None or timestamp in entry.name) and files[i] in entry.name and entry.is_file():
                    lists[i].append(entry.name)
    for i in range(2):
        lists[i].sort()
        df[labels[i]] = pd.read_csv(lists[i][-1])
    return df

def data_preparation(df, country, only_cases=False):
    l = list()
    for i in range(2):
        k = labels[i]
        if isinstance(country, str):
            l.append(df[k][np.logical_and(df[k]['Province/State'].isna(),
                                          df[k]['Country/Region']==country)].iloc[:,4:])
        elif len(country)==2: # if it's a pair of [Province/State, Country/Region]
            l.append(df[k][np.logical_and(df[k]['Province/State']==country[0],
                                          df[k]['Country/Region']==country[1])].iloc[:,4:])
    dft = pd.concat(l, ignore_index=True)
    #print(dft)
    dft.rename(index={i: labels[i] for i in range(2)}, inplace=True)
    #print(dft)
    if only_cases==True:
        df_ts = dft.loc['confirmed']
    else:
        df_ts = dft.loc['confirmed']-dft.loc['deaths'] # -dft.loc['Recovered'] # Since 24 March 2020, recovered is not available
    df_ts.rename(index={df_ts.index[i]: pd.to_datetime(df_ts.index)[i] for i in range(len(df_ts.index))}, inplace=True)
    return df_ts

def rm_early_zeros(ts):
    '''
    Removes early zeros from a pandas time series. It finds last (most recent) zero in time series and
    omits all elements before and including this last zero. Returns the remaining time series which is
    free of zeros.
    pd.Series([0,0,0,0,1,2,0,0,3,6]) -> pd.Series([3,6])
    '''
    zeroindices = ts[ts==0].index
    if len(zeroindices)==0:
        return ts
    else:
        successor = np.nonzero((ts.index==zeroindices.max()))[0][0] + 1
        return ts[successor:]

def rm_consecutive_early_zeros(ts, keep=1):
    '''
    Removes first consecutive subsequence of early zeros from a pandas time series
    except for the last keep if there are that many.
    rm_consecutive_early_zeros(pd.Series([0,0,0,0,1,2,3,6]), 2) -> pd.Series([0,0,1,2,3,6])
    '''
    zeroindices = ts[ts==0].index
    if len(zeroindices)==0:
        return ts
    else:
        first_pos_index = np.nonzero((ts.index==ts[ts>0].index[0]))[0][0]
        if first_pos_index <= keep:
            return ts
        else:
            return ts[first_pos_index-keep:]

def analysis(df_ts, window_length):
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
    results = [(math.pow(2, model.coef_[0])-1)*100,
                1/model.coef_[0],
                df_ts.iloc[-1],
                int(math.pow(2, model.predict(np.array(len(ylog2)-1+intl_lo_days).reshape(1,-1)))),
                int(math.pow(2, model.predict(np.array(len(ylog2)-1+intl_hi_days).reshape(1,-1)))),
                model.score(np.arange(len(ylog2)).reshape(-1, 1), ylog2),
                model.predict(np.array(len(ylog2)-1).reshape(-1, 1))[0]-ylog2[-1]]
    return results, model

def select_window_length(R):
    # This selects the window length that is good on two aspects: R^2 and matching last value
    nr_col = R.shape[1]
    # We take l_2 norm of 10*(1-R^2) and distance column:
    R.insert(nr_col, nr_col, R[5].apply(lambda x: (10*(1-x))**2)+R[6].apply(lambda x: x**2))
    # Sort and return the row (corresponding to a window_length) with lowest l_2 norm:
    #return R.sort_values(7, axis=0, ascending=True).iloc[0:1,:]
    R_sorted = R.sort_values(7, axis=0, ascending=True)
    #print(R_sorted)
    #print([R_sorted.iloc[0,i] for i in range(nr_col)])
    #print(R_sorted.index[0])
    return [R_sorted.iloc[0,i] for i in range(nr_col)], R_sorted.index[0]

def process_geounit(df_ts, window_length):
    '''
    This processes one geographical unit.
    df_ts is the time series.
    '''
    df_ts = rm_early_zeros(df_ts)
    if window_length > 0:
        selected_window_length = window_length
        results, model = analysis(df_ts, window_length)
    else: # do a search over window_lengths for best possible fit
        # minimum and maximum allowed window lengths; we test all in this closed interval
        wl_lo = 4
        wl_hi = 15 # this end point is not included
        # Rule out zeros because we take logarithm; rule out windows longer than the time series df_ts.
        #wl_hi = min(wl_hi, 1+len(df_ts[df_ts[df_ts>0].idxmin():]), 1+len(df_ts))
        wl_hi = min(wl_hi, 1+len(df_ts))
        if wl_hi <= wl_lo: # then abort
            results, model = analysis([], 1)
            return results, model, window_length
        R = pd.DataFrame(np.zeros((wl_hi-wl_lo, 7)), index=range(wl_lo, wl_hi))
        models = dict()
        for wl in range(wl_lo, wl_hi): # last wl_hi-1 points must be available and positive <==
            result_wl, model = analysis(df_ts, wl) # last wl points must be available and positive
            R.iloc[wl-wl_lo, :] = result_wl
            models[wl] = model
        R = R.astype({2: int, 3: int, 4: int})

        results, selected_window_length = select_window_length(R)
        model = models[selected_window_length]

    return results, model, selected_window_length

def print_header():
    print('The number of currently infected people increases daily by /')
    print('Time it takes for the number of currently infected people to double /')
    print('Latest reported number of infectious cases /')
    print('My estimation for number of infectious cases at present /')
    print('R^2 /')
    #print('Tail difference\n')
    print('Tail difference /')
    print('Window length\n')

def print_results(country, results, wl, lang='en'):
    country_width = 23
    interval_width = 16
    if not isinstance(country, str): # If it's a province or state of a country or region.
        country = country[0]
    if (results[5]>=0.95 and results[6]<=0.5) or (results[6]>=-0.2 and results[6]<=0.1):
        #print('{0} {1:4.1f}%  {2:6.2f} {3}  {4}  {5}  {6:4.2f} {7:5.2f}'.format(
        # country.ljust(country_width), results[0], results[1], 'Tage' if lang=='de' else 'days',
        # str(results[2]).rjust(7), ('[' + str(results[3]) +', '+ str(results[4]) + ']').rjust(interval_width), results[5], results[6]).replace('.', ',' if lang=='de' else '.'))
        print('{0} {1:4.1f}% {2:7.1f} {3}  {4}  {5}  {6:4.2f} {7:5.2f}  {8}'.format(
         country.ljust(country_width), results[0], results[1] if results[1]>=0 else np.NaN, 'Tage' if lang=='de' else 'days',
         str(results[2]).rjust(7), ('[' + str(results[3]) +', '+ str(results[4]) + ']').rjust(interval_width), results[5], results[6], str(wl).rjust(2)).replace('.', ',' if lang=='de' else '.'))
    else:
        #print('{0} {1:4.1f}%  {2:6.2f} {3}  {4}  {5}  {6:4.2f} {7:5.2f}'.format(
        # country.ljust(country_width), results[0], results[1], 'Tage' if lang=='de' else 'days',
        # str(results[2]).rjust(7), ''.rjust(interval_width), results[5], results[6]).replace('.', ',' if lang=='de' else '.'))
        print('{0} {1:4.1f}% {2:7.1f} {3}  {4}  {5}  {6:4.2f} {7:5.2f}  {8}'.format(
        country.ljust(country_width), results[0], results[1] if results[1]>=0 else np.NaN, 'Tage' if lang=='de' else 'days',
        str(results[2]).rjust(7), ''.rjust(interval_width), results[5], results[6], str(wl).rjust(2)).replace('.', ',' if lang=='de' else '.'))

def plotting(df_ts, model, save_not_show, country, window_length, lang='en'):
    if not isinstance(country, str): # If it's a province or state of a country or region.
        country = country[0]
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(9.6, 4.8))
    if lang=='de':
        line0 = 'Beobachtungen'
        line1 = 'Exponentielle Annäherung'
        fig.suptitle(country + ', Stand ' + df_ts.index[-1].strftime('%d.%m.%Y'))
    else:
        line0 = 'Observations'
        line1 = 'Exponential approximation'
        fig.suptitle(country + ', ' + df_ts.index[-1].strftime('%d %B %Y'))
    #fig.tight_layout()
    fig.subplots_adjust(bottom=0.2)
    #ax1.plot(df_ts[df_ts>0], label=line0)
    #ax1.plot(df_ts[df_ts>0].iloc[-window_length:].index, np.power(2, np.arange(0, window_length)*model.coef_ + model.intercept_), label=line1)
    ax1.plot(rm_consecutive_early_zeros(df_ts), label=line0)
    ax1.plot(df_ts.iloc[-window_length:].index, np.power(2, np.arange(0, window_length)*model.coef_ + model.intercept_), label=line1)
    #ax2.plot(df_ts[df_ts>0], label=line0)
    ax2.plot(rm_consecutive_early_zeros(df_ts), label=line0)
    ax2.plot(df_ts[df_ts>0].iloc[-window_length:].index, np.power(2, np.arange(0, window_length)*model.coef_ + model.intercept_), label=line1)
    ax2.set_yscale("log")
    for tick in ax1.get_xticklabels():
        tick.set_rotation(80)
    for tick in ax2.get_xticklabels():
        tick.set_rotation(80)
    ax1.legend()
    #plt.gcf().text(0.005, 0.43, "© Bence Mélykúti, Melykuti.me, 2020", fontsize=8, color='lightgray', rotation=90) # 0.482, 0.76
    plt.gcf().text(0.905, 0.615, "© Bence Mélykúti, Melykuti.me, 2020", fontsize=8, color='lightgray', rotation=90)
    if save_not_show==0:
        plt.show()
    elif save_not_show==1:
        imgfile = country.replace(',', '_').replace(' ', '_') + '_' +\
                  df_ts.index[-1].strftime('%Y-%m-%d') + '.png'
        plt.savefig(imgfile)
        plt.close(fig)

def load_population_world():
    pop = pd.read_csv('population_world.csv', sep='\t')
    pop_ser=pd.Series(pop.Population.apply(lambda x: int(x.replace(',', ''))).values, index=pop.Country)
    countries = dict()
    for country in pop_ser.index:
        country_new = country.strip()
        countries[country_new] = pop_ser.loc[country]
    return countries

def load_population_DEU():
    pop = pd.read_csv('population_DEU.csv', sep='\t')
    pop_ser=pd.Series(pop.insgesamt.values, index=pop.Bundesland)
    countries = dict()
    for country in pop_ser.index:
        country_new = country.strip()
        countries[country_new] = pop_ser.loc[country]
    return countries

# Constants
#files = ['time_series_19-covid-Confirmed', 'time_series_19-covid-Deaths', 'time_series_19-covid-Recovered']
#labels = ['Confirmed', 'Deaths', 'Recovered']# until 23 March 2020
# Since 24 March 2020
files = ['time_series_covid19_confirmed_global', 'time_series_covid19_deaths_global']
labels = ['confirmed', 'deaths']
