'''
Downloads the Wikipedia html file for the tables at
https://de.wikipedia.org/wiki/COVID-19-F%C3%A4lle_in_Deutschland#Infektionsf%C3%A4lle_deutschlandweit

exec(open('DEU_download.py','r').read())
16/3/2020
'''

import os, time
import requests

website_url = requests.get('https://de.wikipedia.org/wiki/COVID-19-F%C3%A4lle_in_Deutschland').text

datetime_str = time.strftime('%Y%m%d_%H-%M-%S', time.localtime(time.time()))
#for source in files:
#filename = source.split('/')[-1].split('.')
target = 'time_series_covid-19_DEU_Wikipedia_' + datetime_str + '.html'
with open(target, 'w') as t:
    t.write(website_url)
