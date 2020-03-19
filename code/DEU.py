'''
exec(open('DEU.py').read())
15-18/3/2020
'''

import os, datetime
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

from utils import process_geounit, print_header, print_results, plotting

allowed_values = \
    ['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen',
    'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
    'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen',
    'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen',
    'Deutschland',
    'alle']

### User input ###

selection = 'alle' # Choose one of the elements of allowed_values.
#selection = allowed_values[3] # Alternatively, choose an element index from allowed_values.

window_length = -1 # from latest data point back into past if positive; if nonpositive, then it searches for optimum for model fitting (recommended)
window_length_all = dict({bl: window_length for bl in allowed_values[:-1]})
'''
# You can select individual window lengths manually:
window_length_all = dict({'Baden-Württemberg': 7, 'Bayern': window_length,
    'Berlin': 5, 'Brandenburg': 5, 'Bremen': 15,
    'Hamburg': 11, 'Hessen': 11, 'Mecklenburg-Vorpommern': 13,
    'Niedersachsen': 12, 'Nordrhein-Westfalen': 15,
    'Rheinland-Pfalz': 6, 'Saarland': window_length, 'Sachsen': 7,
    'Sachsen-Anhalt': 6, 'Schleswig-Holstein': 8, 'Thüringen': 13,
    'Deutschland': 13})
'''

save_not_show = 1 # if 0, then shows the plot; if 1, then saves it; otherwise it does neither.
# In the case of 'alle', 0 functions as -1.

lang = 'de' # 'de' for German, anything else for English

### End of user input ###


def open_data():
    '''
    Finding and opening your most recent data download if timestamp == None.
    Alternatively, specify a substring of requested timestamp to select which file to open.
    '''
    timestamp = None
    #timestamp = '20200316_12-59-22'
    df=dict()
    lists = list()
    with os.scandir() as it:
        for entry in it:
            if (timestamp==None or timestamp in entry.name) and 'time_series_covid-19_DEU_Wikipedia_' in entry.name and entry.is_file():
                lists.append(entry.name)

    lists.sort()
    #print(lists)
    with open(lists[-1]) as t:
        return t.read()

def convert_months_to_nr(s: str) -> int:
    s = s.replace('\n','')
    if s == 'Januar':
        return 1
    elif s == 'Februar':
        return 2
    elif s == 'März':
        return 3
    elif s == 'April':
        return 4
    elif s == 'Mai':
        return 5
    elif s == 'Juni':
        return 6
    elif s == 'Juli':
        return 7
    elif s == 'August':
        return 8
    elif s == 'September':
        return 9
    elif s == 'Oktober':
        return 10
    elif s == 'November':
        return 11
    elif s == 'Dezember':
        return 12
    else:
        print('ERROR at 2: Data format error, results are unreliable.')
        return -1

def collect_dates(rows, table_no):
    # First 2 rows are the header: month and day.
    t = rows[0].find_all('th')
    months = []
    for j in range(1, len(t)-(table_no==0)):
        months += int(t[j]['colspan']) * [convert_months_to_nr(t[j].text)]
        #print(months)
    t = rows[1].find_all('th')
    days = []
    if table_no==0:
        for j in t[:-1]:
            days.append(j.text[:j.text.find('.')]) # cutting .\n from end
    else:
        for j in t:
            days.append(j.text[:j.text.find('.')]) # cutting .\n from end
    #print(days)
    ymd = list()
    for m, d in zip(months, days):
        ymd.append('2020-{0}-{1}'.format(m, d))
    dates = pd.to_datetime(ymd)
    return dates # pandas DatetimeIndex of dates

def collect_data(rows, table_no):
    dates = collect_dates(rows, table_no)
    cases_bl = dict()
    for i in range(2, len(rows)-2, 2): # runs from 2 by steps of 2 to 32 (inclusive)
        bundesland = rows[i].find_all('td')[2].find_all('a')[0].text
        #print(i, bundesland)
        cases_bl[bundesland] = list()
        # For the first table, leave out the last column (Erkr./100.000 Einw.)
        for j in range(3, len(rows[i].find_all('td'))-(table_no==0)):
            try:
                cases_bl[bundesland].append(int(rows[i].find_all('td')[j].text.replace('.','')))
            except:
                cases_bl[bundesland].append(0)

    bundeslaender = list()
    for bl in cases_bl:
        bundeslaender.append(pd.Series(cases_bl[bl], name=bl, index=dates))

    # Deutschland
    #print(rows[34].find_all('th')[0].find_all('a')[1].text)
    i = 34
    cases = []
    for j in range(1, len(rows[i].find_all('th'))-(table_no==0)):
        try:
            cases.append(int(rows[i].find_all('th')[j].text.replace('.','')))
        except:
            cases.append(0)
    #print(cases)
    s34 = pd.Series(cases, name = rows[i].find_all('th')[0].find_all('a')[1].text, index=dates)
    #print(s34)

    # Zunahme pro Tag
    #print(rows[35].find_all('th')[0].text)
    i = 35
    cases = []
    for j in range(1, len(rows[i].find_all('th'))-(table_no==0)):
        try:
            cases.append(int(rows[i].find_all('th')[j].text.replace('.','')))
        except:
            cases.append(0)
    #print(cases)
    s35 = pd.Series(cases, name = rows[i].find_all('th')[0].text, index=dates)
    #print(s35)

    #print(pd.concat(bundeslaender + [s34, s35], axis=1))
    return pd.concat(bundeslaender + [s34, s35], axis=1)

def data_preparation_DEU():
    raw_html = open_data()

    soup = BeautifulSoup(raw_html, 'lxml')
    #print(soup.prettify())

    tables = soup.find_all('table', {'class':'wikitable sortable mw-collapsible'}) # I expect two tables: 'Bestätigte Infektionsfälle (kumuliert)', 'Bestätigte Todesfälle (kumuliert)'


    if 'Elektronisch übermittelte Fälle (kumuliert)' not in tables[0].text or 'Bestätigte Todesfälle (kumuliert)' not in tables[2].text:
        print('ERROR at 0: Data format error, results are unreliable.')

    for i in [0, 2]: #range(2):
        rows = tables[i].find_all('tr')
         # or 'Februar' not in rows[0].text
        if (i==0 and ('Bundesland' not in rows[0].text or 'März' not in rows[0].text)) or \
           (i==2 and ('Bundesland' not in rows[0].text or 'März' not in rows[0].text)):
            print('ERROR at 1: Data format error with table {}, results are unreliable.'.format(i))

        #dates = collect_dates(rows)
        #print(dates)
        if i==0:
            figures = collect_data(rows, i) # infections
            #print(figures)
        else: # i==2
            death_figures = collect_data(rows, i) # deaths
            #print(death_figures)
            # Extend it to the size of cases and fill missing values with 0
            death_figures = pd.DataFrame(death_figures, index=figures.index).fillna(value=0).astype('int64')
            #print(death_figures)
            figures_diff = pd.DataFrame(figures.iloc[:,:17] - death_figures.iloc[:,:17])
    #print(figures_diff)
    return figures_diff

if __name__ == '__main__':
    figures_diff = data_preparation_DEU()

    print_header()

    #print(figures_diff[selection], window_length_all[selection])

    if selection != 'alle': # single run
        df_ts = figures_diff[selection]

        results, model, selected_window_length = process_geounit(df_ts, window_length)

        print_results(selection, results, selected_window_length, lang)

        if save_not_show in [0, 1]:
            plotting(figures_diff[selection], model, save_not_show, selection,
                selected_window_length, lang)

    else: # analysis of all federal states and complete Germany

        results_dict = dict()
        selected_window_length_dict = dict()

        for selection in allowed_values[:-1]:
            print(selection)
            df_ts = figures_diff[selection]
            results, model, selected_window_length = process_geounit(df_ts, window_length)

            results_dict[selection] = results
            selected_window_length_dict[selection] = selected_window_length
            if save_not_show == 1:
                plotting(figures_diff[selection], model, save_not_show, selection,
                    selected_window_length, lang)

        for selection in allowed_values[:-1]:
            if selection == 'Deutschland':
                print()
            if window_length_all[selection] > 0:
                print_results(selection, results_dict[selection], window_length_all[selection], lang)
            else:
                print_results(selection, results_dict[selection], selected_window_length_dict[selection], lang)

'''
        if window_length > 0:
            selected_window_length = window_length
            results, model = analysis(df_ts, window_length)

        else: # do a search over window_lengths for best possible fit
            # minimum and maximum allowed window lengths; we test all in this closed interval
            wl_lo = 4
            wl_hi = 15 # this end point is not included
            R = pd.DataFrame(np.zeros((wl_hi-wl_lo, 7)), index=range(wl_lo, wl_hi))
            models = dict()
            for wl in range(wl_lo, min(wl_hi, 1+len(df_ts[df_ts[df_ts>0].idxmin():]))):
                result_wl, model = analysis(df_ts, wl)
                R.iloc[wl-wl_lo, :] = result_wl
                models[wl] = model
            R = R.astype({2: int, 3: int, 4: int})

            results, selected_window_length = select_window_length(R)
            model = models[selected_window_length]

        #results, model = analysis(figures_diff[selection], window_length_all[selection])

        print_results(selection, results, selected_window_length, 'de')
        if save_not_show in [0, 1]:
            plotting(figures_diff[selection], model, save_not_show, selection,
                selected_window_length, 'de')

    else: # analysis of all federal states and complete Germany

        results_dict = dict()
        selected_window_length_dict = dict()

        for selection in allowed_values[:-1]:
            print(selection)
            df_ts = figures_diff[selection]

            if window_length_all[selection] > 0:
                selected_window_length = window_length_all[selection]
                results, model = analysis(df_ts, window_length)
            else: # do a search over window_lengths for best possible fit
                # minimum and maximum allowed window lengths; we test all in this closed interval
                wl_lo = 4
                wl_hi = 15 # this end point is not included
                R = pd.DataFrame(np.zeros((wl_hi-wl_lo, 7)), index=range(wl_lo, wl_hi))
                models = dict()
                for wl in range(wl_lo, min(wl_hi, 1+len(df_ts[df_ts[df_ts>0].idxmin():]))):
                    result_wl, model = analysis(df_ts, wl)
                    R.iloc[wl-wl_lo, :] = result_wl
                    models[wl] = model
                R = R.astype({2: int, 3: int, 4: int})

                results, selected_window_length = select_window_length(R)
                selected_window_length_dict[selection] = selected_window_length
                model = models[selected_window_length]

            results_dict[selection] = results
            if save_not_show == 1:
                plotting(df_ts, model, 1, selection, selected_window_length, 'de')

            #results, model = analysis(figures_diff[selection], window_length_all[selection])
            #print_results(selection, results, 'de')
            #if save_not_show in [0, 1]:
            #    plotting(figures_diff[selection], model, save_not_show, selection, window_length_all[selection], 'de')

        for selection in allowed_values[:-1]:
            if selection == 'Deutschland':
                print()
            if window_length_all[selection] > 0:
                print_results(selection, results_dict[selection], window_length_all[selection], 'de')
            else:
                print_results(selection, results_dict[selection], selected_window_length_dict[selection], 'de')
'''
