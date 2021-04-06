'''
exec(open('DEU.py').read())
15/3-20/12/2020
'''

import os, datetime
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from importlib import reload
import utils

allowed_values = \
    ['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen',
    'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
    'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen',
    'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen',
    'Deutschland',
    'alle']

### User input ###

#selection = 'alle' # Choose one of the elements of allowed_values.
#selection = allowed_values[0] # Alternatively, choose an element index from allowed_values.
selection = 'Sachsen'
#selection = 'Deutschland'

cases = 'confirmed' # 'confirmed' or 'deaths' or 'confirmed_minus_deaths'

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

save_not_show = 0 # if 0, then shows the plot; if 1, then saves it; otherwise it does neither.
# In the case of 'alle', 0 functions as -1.

normalise_by = 1e5 # report case numbers per this many people
exp_or_lin = 'both' # Use 'exp' model (fitting linear model on logarithmic scale) or 'lin' model or 'both' for trying both and selecting the better.
max_display_length = 90 # in days; if positive, then it plots the most recent max_display_length days only
#max_display_length = -1
lang = 'de' # 'de' for German, anything else for English

### End of user input ###


def open_data():
    '''
    Finding and opening your most recent data download if timestamp == None.
    Alternatively, specify a substring of requested timestamp to select which file to open.
    '''
    timestamp = None
    #timestamp = '20200427_14-37-31'
    #df=dict()
    lists = list()
    with os.scandir() as it:
        for entry in it:
            if (timestamp==None or timestamp in entry.name) and 'time_series_covid-19_DEU_Wikipedia_' in entry.name and entry.is_file():
                lists.append(entry.name)

    lists.sort()
    #print(lists)
    with open(lists[-1]) as t:
        return t.read()

'''
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
'''

def convert_months_to_nr(s: str) -> int:
    for i in range(13):
        if ['blank', 'Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun',
            'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez'][i] in s:
            return i
    print('ERROR at 2: Data format error, results are unreliable.')
    return -1

def convert_abbr_to_bl(s: str) -> str:
    i = ['BW', 'BY', 'BE', 'BB', 'HB', 'HH', 'HE', 'MV', 'NI', 'NW', 'RP', 'SL', 'SN', 'ST', 'SH', 'TH',
         'Gesamt', 'DifferenzzumVortag'].index(s)
    return allowed_values[i]
'''
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
'''
def extract_number(s):
    '''
    Maps a string with tailing text to an integer:
    123.456 ^(f) -> 123456
    '''
    s = s.replace('\n','').replace('.','').replace('-','0')
    for i in range(len(s)):
        if s[:i+1].isnumeric():
            t = s[:i+1]
    return int(t)

def collect_data_colwise(rows, shift_right=0):
    # Header
    firstrowcells = rows[0].find_all('th')
    col_names = list()
    #for t in range(1, len(firstrowcells)-2):
    for t in range(1+shift_right, len(firstrowcells)-3):
        col_names.append(convert_abbr_to_bl(firstrowcells[t].find('a').text))
    #for t in range(len(firstrowcells)-2, len(firstrowcells)):
    # Deutschland:
    col_names.append(convert_abbr_to_bl(firstrowcells[len(firstrowcells)-3].text.replace('\n','')))
    # Diff.:
    col_names.append(firstrowcells[len(firstrowcells)-2].text.replace('\n',' '))
    # Diff over week.:
    #col_names.append(firstrowcells[len(firstrowcells)-1].text.replace('\n',''))

    # Data rows
    ymd = list()
    cases_date = dict()
    rows_list = list()
    row_counter = 0
    for r in rows[1:-1]:
        #print(r.text)
        tds = r.find_all('td')
        # https://stackoverflow.com/a/1546251/9486169, we remove accidental multiple spaces from date:
        #print(tds[0].text)
        #day, month, year = tds[0].text.replace('\n','').split(' ')
        #print(' '.join(tds[0].text.replace('\n','').split()).split(' '))
        #day, month, year = ' '.join(tds[0].text.replace('\n','').split()).split(' ')[:3]
        #day, month, year = tds[0].text.replace('\n','').split()[:3] # until 1/4/2020
        #text_temp = tds[0].text.replace('\n','')
        #text_temp = tds[shift_right].text.replace('\n','')
        text_temp = tds[shift_right - (row_counter%7 != 0)].text.replace('\n','')
        #print(text_temp[text_temp.find('♠')+1:])
        day, month, year = text_temp[text_temp.find('♠')+1:].split()[:3] # on 12/4/2020
        year = year[:4]
        #print(day, month, year)
        ymd.append('{0}-{1}-{2}'.format(year, convert_months_to_nr(month), day.replace('.', '')))
        cases_date[ymd[-1]]=list()
        #for j in tds[1:]:
        for j in tds[1+shift_right - (row_counter%7 != 0) :-1]:
            # The character - is not the standard minus, it's a longer one so safer to do with
            # try & except.
            try:
             #cases_date[ymd[-1]].append(int(j.text.replace('\n','').replace('.','').replace('-','0')))
                cases_date[ymd[-1]].append(extract_number(j.text))
            except:
                cases_date[ymd[-1]].append(0)
        rows_list.append(pd.Series(cases_date[ymd[-1]], index=col_names))
        row_counter += 1

    #print(col_names)
    #print(pd.concat(cases_date.values(), axis=0, columns=col_names))
    #return pd.concat(list(cases_date.values()), axis=0, columns=col_names)
    return pd.concat(rows_list, axis=1, keys=pd.to_datetime(ymd)).transpose()

def data_preparation_DEU(output):
    raw_html = open_data()

    soup = BeautifulSoup(raw_html, 'lxml')
    #print(soup.prettify())

    #tables = soup.find_all('table', {'class':'wikitable sortable mw-collapsible'}) # I expect two tables: 'Bestätigte Infektionsfälle (kumuliert)', 'Bestätigte Todesfälle (kumuliert)'
    tables = soup.find_all('table', {'class':'wikitable'}) # I expect four tables

    idx_Infektionsfaelle = 0
    idx_Todesfaelle = 2
    #if 'Elektronisch übermittelte Fälle (kumuliert)' not in tables[0].text or 'Bestätigte Todesfälle (kumuliert)' not in tables[2].text:
    #if 'Elektronisch übermittelte Fälle (kumuliert)' not in tables[0].text or 'Bestätigte Todesfälle (kumuliert)' not in tables[3].text:
    #if 'Daten über Infektionsfälle (kumuliert)' not in tables[0].text or 'Bestätigte Todesfälle (kumuliert)' not in tables[3].text:
    #if 'Infektionsfälle (kumuliert)' not in tables[idx_Infektionsfaelle].text or ('Bestätigte Todesfälle (kumuliert)' not in tables[idx_Todesfaelle].text and 'Bestätigte\xa0Todesfälle\xa0(kumuliert)' not in tables[idx_Todesfaelle].text):
    #    print('ERROR at 0: Data format error, results are unreliable.')

    for i in [idx_Infektionsfaelle, idx_Todesfaelle]:
        rows = tables[i].find_all('tr')
         # or 'Februar' not in rows[0].text
        if (i==idx_Infektionsfaelle and ('Datum' not in rows[0].text or 'BW' not in rows[0].text)) or \
           (i==idx_Todesfaelle and ('Datum' not in rows[0].text or 'BW' not in rows[0].text)):
            print('ERROR at 1: Data format error with table {}, results are unreliable.'.format(i))

        #dates = collect_dates(rows)
        #print(dates)
        if i==idx_Infektionsfaelle:
            #figures = collect_data(rows, i) # infections
            figures = collect_data_colwise(rows, 1) # infections
            #figures.loc[pd.to_datetime('2020-04-07'),'Berlin'] = 3845 # temporary hack but I updated Wikipedia table
            #figures.loc[pd.to_datetime('2020-03-20'),'Rheinland-Pfalz'] = 801
            #figures.loc[pd.to_datetime('2020-03-31'),'Sachsen-Anhalt'] = 680
            print(figures)
        else: # i==idx_Todesfaelle
            death_figures = collect_data_colwise(rows, 1) # deaths
            #print(death_figures)
            # Extend it to the size of cases and fill missing values with 0
            death_figures = pd.DataFrame(death_figures, index=figures.index).fillna(value=0).astype('int64')
            print(death_figures)

    if output == 'confirmed':
        figures_diff = pd.DataFrame(figures.iloc[:,:17])
    elif output == 'deaths':
        figures_diff = pd.DataFrame(death_figures.iloc[:,:17])
    elif output == 'confirmed_minus_deaths':
        figures_diff = pd.DataFrame(figures.iloc[:,:17] - death_figures.iloc[:,:17])
    #print(figures_diff)
    return figures_diff


if __name__ == '__main__':
    pop_csv = 'DEU'
    figures_diff = data_preparation_DEU(cases)
    #figures_diff = figures_diff.iloc[:-1,:]
    if max_display_length > 0:
        figures_diff = figures_diff[-max_display_length:]

    utils.print_header(normalise_by, pop_csv)

    if selection != 'alle': # single run
        df_ts = figures_diff[selection]
        df_ts = utils.rm_early_zeros(df_ts)
        results, model = utils.process_geounit(df_ts, window_length, exp_or_lin)

        utils.print_results(selection, results.iloc[0, 0:8], normalise_by, pop_csv,
                                results.iloc[0,8], results.iloc[0,9], 'normal', lang)

        if save_not_show in [0, 1]:
            utils.plotting(figures_diff[selection], model, save_not_show, selection, results.iloc[0,8],
                               results.iloc[0,9], lang)

    else: # analysis of all federal states and complete Germany

        results_list = list()
        for selection in allowed_values[:-1]:
            print(selection)
            df_ts = figures_diff[selection]
            df_ts = utils.rm_early_zeros(df_ts)
            results, model = utils.process_geounit(df_ts, window_length, exp_or_lin)

            results = results.assign(selection=selection)
            results = results.set_index('selection')
            results_list.append(results)
            if save_not_show == 1:
                utils.plotting(figures_diff[selection], model, save_not_show, selection,
                               results.iloc[0,8], results.iloc[0,9], lang)

        df_results = pd.concat(results_list)
        for selection in allowed_values[:-1]:
            if selection == 'Deutschland':
                print()
            if window_length_all[selection] > 0:
                utils.print_results(selection, df_results.loc[selection,:].iloc[0:8], normalise_by,
                                    pop_csv, window_length_all[selection],
                                    df_results.loc[selection,:].iloc[9], 'normal', lang)
            else:
                utils.print_results(selection, df_results.loc[selection,:].iloc[0:8], normalise_by,
                                    pop_csv, df_results.loc[selection,:].iloc[8],
                                    df_results.loc[selection,:].iloc[9], 'normal', lang)
