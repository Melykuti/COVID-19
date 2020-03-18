'''
exec(open('country_plot.py').read())
12-18/3/2020
'''

import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

### User input ###

country = 'Italy' #'Switzerland' #'Netherlands' #'Denmark' # Denmark, Spain, France, Germany, Sweden
#country = 'Korea, South'
window_length = -1 # from latest data point back into past if positive; if nonpositive, then it searches for optimum for model fitting (recommended)
# Iran used 11 for plot
save_not_show = 0 # if 0, then shows the plot; if 1, then saves it; o.w. it does neither

### End of user input ###

# Constants
files = ['time_series_19-covid-Confirmed', 'time_series_19-covid-Deaths', 'time_series_19-covid-Recovered']
labels = ['Confirmed', 'Deaths', 'Recovered']

def open_csvs():
    '''
    Finding and opening your most recent data download if timestamp == None.
    Alternatively, specify a substring of requested timestamp to select which files to open.
    '''
    timestamp = None
    #timestamp = '20200312_21-43'
    df=dict()
    lists = list([list(), list(), list()])
    with os.scandir() as it:
        for entry in it:
            for i in range(3):
                if (timestamp==None or timestamp in entry.name) and files[i] in entry.name and entry.is_file():
                    lists[i].append(entry.name)
    for i in range(3):
        lists[i].sort()
        df[labels[i]] = pd.read_csv(lists[i][-1])
    return df

def data_preparation(df, country):
    l = list()
    for i in range(3):
        k = labels[i]
        l.append(df[k][df[k]['Country/Region']==country].iloc[:,4:])

    dft = pd.concat(l, ignore_index=True)
    dft.rename(index={i: labels[i] for i in range(3)}, inplace=True)
    df_ts = dft.loc['Confirmed']-dft.loc['Deaths']-dft.loc['Recovered']
    df_ts.rename(index={df_ts.index[i]: pd.to_datetime(df_ts.index)[i] for i in range(len(df_ts.index))}, inplace=True)
    return df_ts

def analysis(df_ts, window_length):
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
    # We take l_2 norm of 10*(1-R^2) and last column:
    R.insert(nr_col, nr_col, R[5].apply(lambda x: (10*(1-x))**2)+R[6].apply(lambda x: x**2))
    # Sort and return the row (corresponding to a window_length) with lowest l_2 norm:
    #return R.sort_values(7, axis=0, ascending=True).iloc[0:1,:]
    R_sorted = R.sort_values(7, axis=0, ascending=True)
    print(R_sorted)
    print([R_sorted.iloc[0,i] for i in range(nr_col)])
    print(R_sorted.index[0])
    return [R_sorted.iloc[0,i] for i in range(nr_col)], R_sorted.index[0]

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
    if (results[5]>=0.95 and results[6]<=0.5) or (results[6]>=-0.2 and results[6]<=0.1):
        #print('{0} {1:4.1f}%  {2:6.2f} {3}  {4}  {5}  {6:4.2f} {7:5.2f}'.format(
        # country.ljust(country_width), results[0], results[1], 'Tage' if lang=='de' else 'days',
        # str(results[2]).rjust(7), ('[' + str(results[3]) +', '+ str(results[4]) + ']').rjust(interval_width), results[5], results[6]).replace('.', ',' if lang=='de' else '.'))
        print('{0} {1:4.1f}% {2:6.1f} {3}  {4}  {5}  {6:4.2f} {7:5.2f}  {8}'.format(
         country.ljust(country_width), results[0], results[1], 'Tage' if lang=='de' else 'days',
         str(results[2]).rjust(7), ('[' + str(results[3]) +', '+ str(results[4]) + ']').rjust(interval_width), results[5], results[6], wl).replace('.', ',' if lang=='de' else '.'))
    else:
        #print('{0} {1:4.1f}%  {2:6.2f} {3}  {4}  {5}  {6:4.2f} {7:5.2f}'.format(
        # country.ljust(country_width), results[0], results[1], 'Tage' if lang=='de' else 'days',
        # str(results[2]).rjust(7), ''.rjust(interval_width), results[5], results[6]).replace('.', ',' if lang=='de' else '.'))
        print('{0} {1:4.1f}% {2:6.1f} {3}  {4}  {5}  {6:4.2f} {7:5.2f}  {8}'.format(
        country.ljust(country_width), results[0], results[1], 'Tage' if lang=='de' else 'days',
        str(results[2]).rjust(7), ''.rjust(interval_width), results[5], results[6], wl).replace('.', ',' if lang=='de' else '.'))

def plotting(df_ts, model, save_not_show, country, window_length, lang='en'):
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
    ax1.plot(df_ts[df_ts>0], label=line0)
    ax1.plot(df_ts[df_ts>0].iloc[-window_length:].index, np.power(2, np.arange(0, window_length)*model.coef_ + model.intercept_), label=line1)
    ax2.plot(df_ts[df_ts>0], label=line0)
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

if __name__ == '__main__':
    df = open_csvs()
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
        model = models[selected_window_length]

    print_header()
    print_results(country, results, selected_window_length)#, lang='de')
    
    if save_not_show in [0, 1]:
        plotting(df_ts, model, save_not_show, country, selected_window_length)#, lang='de')
