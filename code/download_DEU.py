'''
Downloads the Wikipedia html file for the tables at
https://de.wikipedia.org/wiki/COVID-19-F%C3%A4lle_in_Deutschland#Infektionsf%C3%A4lle_deutschlandweit

exec(open('download_DEU.py','r').read())
16/3/2020
'''

import os, time
import requests

#website_url = requests.get('https://de.wikipedia.org/wiki/COVID-19-F%C3%A4lle_in_Deutschland').text
#website_url = requests.get('https://de.wikipedia.org/wiki/COVID-19-Pandemie_in_Deutschland').text # since 19/3/2020
#website_url = requests.get('https://de.wikipedia.org/wiki/COVID-19-Pandemie/Statistik').text # since 9/6/2020
website_url = requests.get('https://de.wikipedia.org/wiki/COVID-19-Pandemie_in_Deutschland/Statistik').text # since 18/6/2020

datetime_str = time.strftime('%Y%m%d_%H-%M-%S', time.localtime(time.time()))
#for source in files:
#filename = source.split('/')[-1].split('.')
target = 'time_series_covid-19_DEU_Wikipedia_' + datetime_str + '.html'
with open(target, 'w') as t:
    t.write(website_url)
