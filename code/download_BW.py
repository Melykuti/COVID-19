'''
Downloads the xlsx file
»Tabelle „Coronavirus in Baden-Württemberg: Anzahl der Infizierten und der Todesfälle in Stadt-/Landkreisen“ (XLSX)«
https://sozialministerium.baden-wuerttemberg.de/de/gesundheit-pflege/gesundheitsschutz/infektionsschutz-hygiene/informationen-zu-coronavirus/lage-in-baden-wuerttemberg/

exec(open('download_BW.py','r').read())
14/4/2020
'''

import os, time
import urllib.request

source = 'https://sozialministerium.baden-wuerttemberg.de/fileadmin/redaktion/m-sm/intern/downloads/Downloads_Gesundheitsschutz/Tabelle_Coronavirus-Faelle-BW.xlsx'

datetime_str = time.strftime('%Y%m%d_%H-%M-%S', time.localtime(time.time()))
#for source in files:
#filename = source.split('/')[-1].split('.')
target = 'BW_Tabelle_Coronavirus-Faelle_' + datetime_str + '.xlsx'
with open(target, 'bw') as t:
    with urllib.request.urlopen(source) as response:
        source=response.read()
    t.write(source)

