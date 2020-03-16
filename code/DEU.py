'''
exec(open('DEU.py').read())
15-16/3/2020
'''

import os, datetime
import pandas as pd
from bs4 import BeautifulSoup

from country_plot import analysis, print_header, print_results, plotting

### User input ###

allowed_values = \
    ['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen',
    'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
    'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen',
    'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen',
    'Deutschland',
    'alle']
selection = 'Baden-Württemberg'
#selection = allowed_values[0]
window_length = 10 # from present back into past
window_length_all = dict({'Baden-Württemberg': window_length, 'Bayern': window_length,
    'Berlin': 9, 'Brandenburg': 5, 'Bremen': 11,
    'Hamburg': window_length, 'Hessen': window_length, 'Mecklenburg-Vorpommern': 12,
    'Niedersachsen': 11, 'Nordrhein-Westfalen': 14,
    'Rheinland-Pfalz': 14, 'Saarland': window_length, 'Sachsen': 7,
    'Sachsen-Anhalt': 6, 'Schleswig-Holstein': 7, 'Thüringen': 11,
    'Deutschland': 12})
save_not_show = 0 # if 0, then shows the plot; if 1, then saves it; o.w. it does neither

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

def collect_dates(rows):
    # First 2 rows are the header: month and day.
    t = rows[0].find_all('th')
    months = []
    for j in range(1, len(t)):
        months += int(t[j]['colspan']) * [convert_months_to_nr(t[j].text)]
        #print(months)
    t = rows[1].find_all('th')
    days = []
    for j in t:
        days.append(j.text[:j.text.find('.')]) # cutting .\n from end
    #print(days)
    ymd = list()
    for m, d in zip(months, days):
        ymd.append('2020-{0}-{1}'.format(m, d))
    dates = pd.to_datetime(ymd)
    return dates # pandas DatetimeIndex of dates

def collect_data(rows):
    dates = collect_dates(rows)
    cases_bl = dict()
    for i in range(2, len(rows)-2, 2): # runs from 2 by steps of 2 to 32 (inclusive)
        bundesland = rows[i].find_all('td')[2].find_all('a')[0].text
        #print(i, bundesland)
        cases_bl[bundesland] = list()
        for j in range(3, len(rows[i].find_all('td'))):
            try:
                cases_bl[bundesland].append(int(rows[i].find_all('td')[j].text.replace('.','')))
            except:
                cases_bl[bundesland].append(0)
    #print(cases_bl)
    bundeslaender = list()
    for bl in cases_bl:
        bundeslaender.append(pd.Series(cases_bl[bl], name=bl, index=dates))

    # Deutschland
    #print(rows[34].find_all('th')[0].find_all('a')[1].text)
    i = 34
    cases = []
    for j in range(1, len(rows[i].find_all('th'))):
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
    for j in range(1, len(rows[i].find_all('th'))):
        try:
            cases.append(int(rows[i].find_all('th')[j].text.replace('.','')))
        except:
            cases.append(0)
    #print(cases)
    s35 = pd.Series(cases, name = rows[i].find_all('th')[0].text, index=dates)
    #print(s35)

    #print(pd.concat(bundeslaender + [s34, s35], axis=1))
    return pd.concat(bundeslaender + [s34, s35], axis=1)

def data_preparation():
    raw_html = open_data()

    soup = BeautifulSoup(raw_html, 'lxml')
    #print(soup.prettify())

    tables = soup.find_all('table', {'class':'wikitable sortable mw-collapsible'}) # I expect two tables: 'Bestätigte Infektionsfälle (kumuliert)', 'Bestätigte Todesfälle (kumuliert)'


    if 'Bestätigte Infektionsfälle (kumuliert)' not in tables[0].text or 'Bestätigte Todesfälle (kumuliert)' not in tables[1].text:
        print('ERROR at 0: Data format error, results are unreliable.')

    for i in range(2):
        rows = tables[i].find_all('tr')
        if (i==0 and ('Bundesland' not in rows[0].text or 'Februar' not in rows[0].text or 'März' not in rows[0].text)) or \
           (i==1 and ('Bundesland' not in rows[0].text or 'März' not in rows[0].text)):
            print('ERROR at 1: Data format error with table {}, results are unreliable.'.format(i))

        #dates = collect_dates(rows)
        #print(dates)
        if i==0:
            figures = collect_data(rows) # infections
        else: # i==1
            death_figures = collect_data(rows) # deaths
            # Extend it to the size of cases and fill missing values with 0
            death_figures = pd.DataFrame(death_figures, index=figures.index).fillna(value=0).astype('int64')
            #print(death_figures)
            figures_diff = pd.DataFrame(figures.iloc[:,:17] - death_figures.iloc[:,:17])
    #print(figures_diff)
    return figures_diff

if __name__ == '__main__':
    figures_diff = data_preparation()
    #print(figures_diff[selection], window_length_all[selection])
    print_header()
    if selection != 'alle':
        results, model = analysis(figures_diff[selection], window_length_all[selection])
        print_header()
        print_results(selection, results, 'de')
        if save_not_show in [0, 1]:
            plotting(figures_diff[selection], model, save_not_show, selection, window_length_all[selection], 'de')
    else:
        for selection in allowed_values[:-1]:
            results, model = analysis(figures_diff[selection], window_length_all[selection])
            print_results(selection, results, 'de')
            if save_not_show in [0, 1]:
                plotting(figures_diff[selection], model, save_not_show, selection, window_length_all[selection], 'de')

