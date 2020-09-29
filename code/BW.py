'''
exec(open('BW.py').read())
15/3-15/4/2020
'''

import os, datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from importlib import reload
import utils

allowed_values = ['Alb-Donau-Kreis', 'Baden-Baden (Stadtkreis)', 'Biberach', 'Böblingen',
       'Bodenseekreis', 'Breisgau-Hochschwarzwald', 'Calw', 'Emmendingen',
       'Enzkreis', 'Esslingen', 'Freiburg im Breisgau (Stadtkreis)',
       'Freudenstadt', 'Göppingen', 'Heidelberg (Stadtkreis)', 'Heidenheim',
       'Heilbronn', 'Heilbronn (Stadtkreis)', 'Hohenlohekreis', 'Karlsruhe',
       'Karlsruhe (Stadtkreis)', 'Konstanz', 'Lörrach', 'Ludwigsburg',
       'Main-Tauber-Kreis', 'Mannheim (Stadtkreis)', 'Neckar-Odenwald-Kreis',
       'Ortenaukreis', 'Ostalbkreis', 'Pforzheim (Stadtkreis)', 'Rastatt',
       'Ravensburg', 'Rems-Murr-Kreis', 'Reutlingen', 'Rhein-Neckar-Kreis',
       'Rottweil', 'Schwäbisch Hall', 'Schwarzwald-Baar-Kreis', 'Sigmaringen',
       'Stuttgart', 'Tübingen', 'Tuttlingen', 'Ulm (Stadtkreis)', 'Waldshut',
       'Zollernalbkreis', 'Baden-Württemberg', 'alle']

#['Freiburg im Breisgau (Stadtkreis)', 'Breisgau-Hochschwarzwald', 'Summe']

### User input ###

selection = 'alle' # Choose one of the elements of allowed_values.
#selection = allowed_values[10] # Alternatively, choose an element index from allowed_values.
#selection = allowed_values[4]
#selection = allowed_values[-2]
§selection = 'Breisgau-Hochschwarzwald'

cases = 'both' # 'confirmed' or 'deaths' or 'both'

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

save_not_show = -1 # if 0, then shows the plot for individual district (Landkreis); if 1, then saves it; otherwise it does neither.

sc_save_not_show = 1 # In the case of 'alle', if 0, then shows the joint scatter plot; if 1, then saves it; otherwise it does neither.

normalise_by = 1e5 # report case numbers per this many people
exp_or_lin = 'both' # Use 'exp' model (fitting linear model on logarithmic scale) or 'lin' model or 'both' for trying both and selecting the better.
max_display_length = 60 #45 # in days; if positive, then it plots the most recent max_display_length days only
panels = 2 # 2 or 3, to plot only two panels or all three, that is, the logarithmically scaled cumulative numbers also

### End of user input ###


def open_data():
    '''
    Finding and opening your most recent data download if timestamp == None.
    Alternatively, specify a substring of requested timestamp to select which file to open.
    '''
    timestamp = None
    #timestamp = '20200331'
    df=dict()
    lists = list()
    with os.scandir() as it:
        for entry in it:
            if (timestamp==None or timestamp in entry.name) and 'BW_Tabelle_Coronavirus-Faelle_' in entry.name and entry.is_file():
                lists.append(entry.name)
    lists.sort()
    figures = dict()
    sheets = ['confirmed', 'deaths']
    header_row = 6
    for i in range(2):
        figures[sheets[i]] = pd.read_excel(lists[-1], sheet_name=i, header=header_row, index_col=0)
        figures[sheets[i]].columns = pd.to_datetime(figures[sheets[i]].columns)
        figures[sheets[i]] = figures[sheets[i]].loc[:'Summe']
        figures[sheets[i]].loc['Baden-Württemberg'] = figures[sheets[i]].loc['Summe']
        figures[sheets[i]].drop('Summe', axis=0, inplace=True)
        figures[sheets[i]] = figures[sheets[i]].T
        figures[sheets[i]].sort_index(ascending=True, inplace=True)
    return figures

# Scatter plot
def scp(sc_save_not_show, case_type='confirmed'):
    lk2kz = {'Alb-Donau-Kreis': 'UL*', 'Baden-Baden (Stadtkreis)': 'BAD', 'Biberach': 'BC', 'Böblingen': 'BB', 'Bodenseekreis': 'FN', 'Breisgau-Hochschwarzwald': 'FR*', 'Calw': 'CW', 'Emmendingen': 'EM', 'Enzkreis': 'PF*', 'Esslingen': 'ES', 'Freiburg im Breisgau (Stadtkreis)': 'FR', 'Freudenstadt': 'FDS', 'Göppingen': 'GP', 'Heidelberg (Stadtkreis)': 'HD', 'Heidenheim': 'HDH', 'Heilbronn (Stadtkreis)': 'HN', 'Heilbronn': 'HN*', 'Hohenlohekreis': 'KÜN', 'Karlsruhe': 'KA*', 'Karlsruhe (Stadtkreis)': 'KA', 'Konstanz': 'KN', 'Lörrach': 'LÖ', 'Ludwigsburg': 'LB', 'Main-Tauber-Kreis': 'TBB', 'Mannheim (Stadtkreis)': 'MA', 'Neckar-Odenwald-Kreis': 'MOS', 'Ortenaukreis': 'OG', 'Ostalbkreis': 'AA/GD', 'Pforzheim (Stadtkreis)': 'PF', 'Rastatt': 'RA', 'Ravensburg': 'RV', 'Rems-Murr-Kreis': 'WN', 'Reutlingen': 'RT', 'Rhein-Neckar-Kreis': 'HD*', 'Rottweil': 'RW', 'Schwäbisch Hall': 'SHA', 'Schwarzwald-Baar-Kreis': 'VS', 'Sigmaringen': 'SIG', 'Stuttgart': 'S', 'Tuttlingen': 'TUT', 'Tübingen': 'TÜ', 'Ulm (Stadtkreis)': 'UL', 'Waldshut': 'WT', 'Zollernalbkreis': 'BL'}
    figures = open_data()
    if case_type=='confirmed':
        fallzahl = 'Fallzahl auf {0} Einwohner'.format(utils.separated(str(int(normalise_by)), lang))
    elif case_type=='deaths':
        fallzahl = 'Todesfälle auf {0} Einwohner'.format(utils.separated(str(int(normalise_by)), lang))
    pop_dens = 'Bevölkerungsdichte (Einwohner/km²)'
    pop = utils.load_population_BW(incl_density=True)
    case_density = normalise_by*figures[case_type].iloc[-1]/pop['Bevölkerung insgesamt']
    df = pop.join(pd.Series(case_density, name=fallzahl))
    print('\nKorrelationskoeffizient zwischen {0} und {1}: {2:.3f}.'.format(pop_dens, fallzahl, np.corrcoef(df['Bevölkerungsdichte EW/km²'], df[fallzahl])[0,1]))
    idx_FR = pd.Series(df.index).apply(lambda x: 'Freiburg' in x).idxmax()
    fig, ax = plt.subplots(1,1, figsize=(12.8, 6.4))
    neither_FR_nor_BW = pd.Series(df.index, index=df.index).apply(
        lambda x: 'Freiburg' not in x and 'Baden-Württemberg' not in x)
    ax.scatter(df[neither_FR_nor_BW].iloc[:,2], df[neither_FR_nor_BW].iloc[:,1], label='Baden-Württembergische Landkreise', color='tab:blue')
    ax.scatter(df.iloc[idx_FR, 2], df.iloc[idx_FR, 1], label=df.index[idx_FR], color='crimson', marker='+')
    ax.scatter(df.iloc[-1, 2], df.iloc[-1, 1], label=df.index[-1], color='gold', edgecolor='k')
    for k in df.index[:-1]:
        if k in lk2kz.keys():
            #print(k)
            ax.annotate(lk2kz[k], (df.loc[k][2], df.loc[k][1]), xytext=(5,5), textcoords='offset pixels', size=8, color='gray')
    ax.legend()
    ax.set_xlabel(fallzahl)
    ax.set_ylabel(pop_dens)
    ax.set_xlim(left=None, right=None)
    if 0==1:
        ax.set_ylim(bottom=0, top=3200)
    else:
        ax.set_ylim(bottom=90, top=4000)
        ax.set_yscale("log")
        ax.set_yticks([100, 200, 300, 400, 500, 1000, 2000, 3000, 4000])
        ax.set_yticklabels([int(tick) for tick in ax.get_yticks()])
    if case_type=='confirmed':
        fig.suptitle('COVID-19-Infizierten in Baden-Württemberg vs Bevölkerungsdichte pro Landkreis\nStand ' + figures[case_type].index[-1].strftime('%d.%m.%Y'))
    elif case_type=='deaths':
        fig.suptitle('COVID-19-Todesfälle in Baden-Württemberg vs Bevölkerungsdichte pro Landkreis\nStand ' + figures[case_type].index[-1].strftime('%d.%m.%Y'))
    #plt.gcf().text(0.905, 0.865, "© Bence Mélykúti, 2020. http://COVID19BW.Melykuti.Be", fontsize=8, color='lightgray', rotation=90)
    plt.gcf().text(0.905, 0.395, "© Bence Mélykúti, 2020. http://COVID19BW.Melykuti.Be", fontsize=8, color='lightgray', rotation=90)
    if sc_save_not_show == 0:
        plt.show()
    else:
        dt = figures[case_type].index[-1].strftime('%Y-%m-%d')
        plt.savefig('BW_population_density_scatter_{0}_{1}.png'.format(case_type, dt))
        plt.close()

if __name__ == '__main__':
    pop_csv = 'BW'
    lang = 'de' # 'de' for German, anything else for English
    #scp(1, 'confirmed')
    #scp(0, 'confirmed')
    #scp(1, 'deaths')
    #scp(0, 'deaths')
    
    if cases!='both':
        cases_list = [cases]
    else:
        cases_list = ['confirmed', 'deaths']

    figures = open_data()

    utils.print_header(normalise_by, pop_csv)

    if selection != 'alle': # single run
    #print(figures['confirmed'])
        for case in cases_list:
            if max_display_length > 0:
                figures[case] = figures[case].iloc[-max_display_length:,:]
            df_ts = figures[case][selection]
            df_ts = utils.rm_early_zeros(df_ts)
            #if max_display_length > 0:
            #    df_ts = df_ts[-max_display_length:]

            results, model, selected_window_length, e_or_l = utils.process_geounit(
                                                                df_ts, window_length, exp_or_lin)
            print()
            utils.print_results(selection, results, normalise_by, pop_csv,
                     selected_window_length, e_or_l, case, lang)

            if save_not_show in [0, 1]:
                country = selection + ' '
                if case=='confirmed':
                    country += 'Fallzahl'
                else:
                    country += 'Todesfälle'
                utils.plotting(df_ts, model, save_not_show, country, selected_window_length, e_or_l,
                                 lang, panels)

    else: # analysis of all counties and complete BW

        results_dict = dict()
        selected_window_length_dict = dict()
        exp_or_lin_dict = dict()
        for case in cases_list:
            if max_display_length > 0:
                figures[case] = figures[case].iloc[-max_display_length:,:]
            #for selection in allowed_values[:3]:
            for selection in allowed_values[:-1]:
                print(selection)
                df_ts = figures[case][selection]
                df_ts = utils.rm_early_zeros(df_ts)
                results, model, selected_window_length, e_or_l = utils.process_geounit(
                                                                        df_ts, window_length, exp_or_lin)

                results_dict[selection] = results
                selected_window_length_dict[selection] = selected_window_length
                exp_or_lin_dict[selection] = e_or_l
                if save_not_show in [0, 1]:
                    country = selection + ' '
                    if case=='confirmed':
                        country += 'Fallzahl'
                    else:
                        country += 'Todesfälle'
                    utils.plotting(df_ts, model, save_not_show, country,
                        selected_window_length, e_or_l, lang, panels)
            print()
            #for selection in allowed_values[:3]:
            for selection in allowed_values[:-1]:
                if selection == 'Baden-Württemberg':
                    print()
                if window_length_all[selection] > 0:
                    utils.print_results(selection, results_dict[selection], normalise_by, pop_csv,
                            window_length_all[selection], exp_or_lin_dict[selection], case, lang)
                else:
                    #print(results)
                    #print(pop[])
                    utils.print_results(selection, results_dict[selection], normalise_by, pop_csv,
                     selected_window_length_dict[selection], exp_or_lin_dict[selection], case, lang)

            if sc_save_not_show in [0, 1]:
                scp(sc_save_not_show, case)
    
