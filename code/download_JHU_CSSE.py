'''
exec(open('download_JHU_CSSE.py','r').read())
12/3, 24/3/2020
'''

import os, urllib.request, time

#files = ['https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv',
#'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv',
#'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'] # until 23 March 2020
# Since 24 March 2020
files = ['https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv']

datetime_str = time.strftime('%Y%m%d_%H-%M-%S', time.localtime(time.time()))
for source in files:
    filename = source.split('/')[-1].split('.')
    target = filename[0] + '_' + datetime_str + '.' + filename[1]
    with open(target, 'wb') as t:
        with urllib.request.urlopen(source) as response:
            source=response.read()
        t.write(source)
