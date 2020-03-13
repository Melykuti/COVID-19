'''
exec(open('country_plot.py').read())
12-13/3/2020
'''

import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

### User input ###

country = 'Austria' #'Switzerland' #'Netherlands' #'Denmark' # Denmark, Spain, France, Germany, Sweden
#country = 'Korea, South'
window_length = 14 # from present back into past
save_not_show = 1 # if 0, then shows the plot; if 1, then saves it; o.w. it does neither

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
    return df, lists[0][-1]

def data_preparation(df, country):
    #df, filename = open_csvs() # filename is used to create name of image file if saving plot

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
    intl_lo_days = 3
    intl_hi_days = 5
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

def print_header():
    print('The number of currently infected people increases daily by /')
    print('Time it takes for the number of currently infected people to double /')
    print('Latest reported number of infectious cases /')
    print('My estimation for number of infectious cases at present /')
    print('R^2')
    print('Tail difference\n')

def print_results(country, results):
    country_width = 16
    interval_width = 16
    if results[5]>=0.95 and results[6]<=0.5:
        print('{0} {1:4.1f}%  {2:6.2f} days  {3}  {4}  {5:4.2f}  {6:5.2f}'.format(
         country.ljust(country_width), results[0], results[1],
         str(results[2]).rjust(7), ('[' + str(results[3]) +', '+ str(results[4]) + ']').rjust(interval_width), results[5], results[6]))
    else:
        print('{0} {1:4.1f}%  {2:6.2f} days  {3}  {4}  {5:4.2f}  {6:5.2f}'.format(
         country.ljust(country_width), results[0], results[1],
         str(results[2]).rjust(7), ''.rjust(interval_width), results[5], results[6]))

def plotting(model, save_not_show):
    line0 = 'Observations'
    line1 = 'Exponential approximation'
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(9.6, 4.8))
    #fig.tight_layout()
    fig.suptitle(country)
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
        imgfile = country.replace(',', '_') + '_' + filename.split('_')[-2] + '_'\
                 + filename.split('_')[-1][:-4] + '.png'
        plt.savefig(imgfile)
        plt.close(fig)

if __name__ == '__main__':
    df, filename = open_csvs() # filename is used to create name of image file if saving plot
    df_ts = data_preparation(df, country)
    results, model = analysis(df_ts, window_length)
    print_header()
    print_results(country, results)

    if save_not_show in [0, 1]:
        plotting(model, save_not_show)
