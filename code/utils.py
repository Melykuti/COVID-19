import os, math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from sklearn import linear_model
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from importlib import reload

# Constants
#files = ['time_series_19-covid-Confirmed', 'time_series_19-covid-Deaths', 'time_series_19-covid-Recovered']
#labels = ['Confirmed', 'Deaths', 'Recovered']# until 23 March 2020
# Since 24 March 2020
#files = ['time_series_covid19_confirmed_global', 'time_series_covid19_deaths_global']
#labels = ['confirmed', 'deaths']
# Since 28 March 2020
files = ['time_series_covid19_confirmed_global', 'time_series_covid19_deaths_global', 'time_series_covid19_recovered_global']
labels = ['confirmed', 'deaths', 'recovered']


def open_csvs():
    '''
    Finding and opening your most recent data download if timestamp == None.
    Alternatively, specify a substring of requested timestamp to select which files to open.
    '''
    timestamp = None
    #timestamp = '20200330_15-26'
    df=dict()
    lists = list([list(), list(), list()])
    with os.scandir() as it:
        for entry in it:
            for i in range(3):
                if (timestamp==None or timestamp in entry.name) and files[i] in entry.name\
                    and entry.is_file():
                    lists[i].append(entry.name)
    for i in range(3):
        lists[i].sort()
        df[labels[i]] = pd.read_csv(lists[i][-1])
    return df

def data_preparation(df, country, output):
    '''
    This is used for the JHU CSSE dataset.
    output can be 'confirmed', 'deaths', 'recovered', 'active' or 'all'
    'active' returns dft['confirmed']-dft['deaths']-dft['recovered']
    'all' returns all three as columns in a DataFrame as used in death_over_cases.py
    '''
    sets = dict({'EU': ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']})#,
#'China': [['Anhui', 'China'], ['Beijing', 'China'], ['Chongqing', 'China'], ['Fujian', 'China'], ['Gansu', 'China'], ['Guangdong', 'China'], ['Guangxi', 'China'], ['Guizhou', 'China'], ['Hainan', 'China'], ['Hebei', 'China'], ['Heilongjiang', 'China'], ['Henan', 'China'], ['Hong Kong', 'China'], ['Hubei', 'China'], ['Hunan', 'China'], ['Inner Mongolia', 'China'], ['Jiangsu', 'China'], ['Jiangxi', 'China'], ['Jilin', 'China'], ['Liaoning', 'China'], ['Macau', 'China'], ['Ningxia', 'China'], ['Qinghai', 'China'], ['Shaanxi', 'China'], ['Shandong', 'China'], ['Shanghai', 'China'], ['Shanxi', 'China'], ['Sichuan', 'China'], ['Tianjin', 'China'], ['Tibet', 'China'], ['Xinjiang', 'China'], ['Yunnan', 'China'], ['Zhejiang', 'China']]})
    #sets = dict({'EU': ['Croatia', 'Hungary']}) # test only
    l = list()
    if country == 'EU' or country == 'China' or country == 'Australia':
        ''' First, recursive implementation
        l_members = list()
        for member in sets[country]:
            l_members.append(data_preparation(df, member, only_cases))
        dft_members = pd.concat(l_members, axis=1)
        return dft_members.sum(axis=1)
        '''
        M = dict() # these matrices are the booleans of selections for each Province/State, we take their multiple
        for i in range(3):
            k = labels[i]
            M[k] = list()
            if country == 'China' or country == 'Australia':
                M[k].append((df[k]['Province/State'].notna()) & (df[k]['Country/Region']==country))
                l.append(df[k][M[k][0]].iloc[:,4:].sum(axis=0))
            else: # country == 'EU'
                for member in sets[country]:
                    #print(member)
                    if isinstance(member, str):
                        M[k].append((df[k]['Province/State'].isna()) & (df[k]['Country/Region']==member))
                    elif len(member)==2: # if it's a pair of [Province/State, Country/Region]
                        M[k].append((df[k]['Province/State']==member[0])
                                     & (df[k]['Country/Region']==member[1]))
                l.append(df[k][np.sum(np.array(M[k]), axis=0)>=1].iloc[:,4:].sum(axis=0))
        dft = pd.concat(l, ignore_index=True, axis=1)
        #dft.rename(columns={i: labels[i] for i in range(3)}, inplace=True)
    else:
        for i in range(3):
            k = labels[i]
            if isinstance(country, str):
                l.append(df[k][np.logical_and(df[k]['Province/State'].isna(),
                                              df[k]['Country/Region']==country)].iloc[:,4:])
            elif len(country)==2: # if it's a pair of [Province/State, Country/Region]
                l.append(df[k][np.logical_and(df[k]['Province/State']==country[0],
                                              df[k]['Country/Region']==country[1])].iloc[:,4:])
        dft = pd.concat(l, ignore_index=True, axis=0).transpose()
    #print(dft)
    dft.rename(columns={i: labels[i] for i in range(3)}, inplace=True)
    #print(dft)
    if output=='all':
        df_ts = dft
    elif output=='active':
        df_ts = dft['confirmed']-dft['deaths']-dft['recovered'] # On 24 March 2020, recovered is not available; on 28 March 2020 it is there again.
    else:
        df_ts = dft[output]
    #print(df_ts)
    #df_ts.rename(index={df_ts.index[i]: pd.to_datetime(df_ts.index)[i] for i in range(len(df_ts.index))}, inplace=True)
    df_ts.rename(index=pd.Series(df_ts.index, index=df_ts.index).apply(lambda x: pd.to_datetime(x)), inplace=True)
    #print(df_ts)
    return df_ts

def rm_early_zeros(ts):
    '''
    Removes early zeros and NaNs from a pandas time series. It finds last (most recent) zero or NaN in
    time series and omits all elements before and including this last zero or NaN. Returns the remaining
    time series which is free of zeros and NaN.
    pd.Series([0,0,0,0,1,2,0,0,3,6]) -> pd.Series([3,6])
    '''
    zeroindices = ts[(ts==0) | ts.isna()].index
    if len(zeroindices)==0:
        return ts
    else:
        successor = np.nonzero((ts.index==zeroindices.max()))[0][0] + 1
        return ts[successor:]

def rm_consecutive_early_zeros(ts, keep=1):
    '''
    Removes first consecutive subsequence of early zeros from a pandas time series
    except for the last keep if there are that many.
    rm_consecutive_early_zeros(pd.Series([0,0,0,0,1,2,3,6]), 2) -> pd.Series([0,0,1,2,3,6])
    '''
    zeroindices = ts[ts==0].index
    if len(zeroindices)==0:
        return ts
    else:
        first_pos_index = np.nonzero((ts.index==ts[ts>0].index[0]))[0][0]
        if first_pos_index <= keep:
            return ts
        else:
            return ts[first_pos_index-keep:]

def separated(s, lang='en', k=3):
    '''
    Input must be a string. Puts a comma between blocks of k=3 digits:
    '1000000' -> '1,000,000'
    '''
    if lang == 'de':
        chr = '.'
    else:
        chr = ','
    if len(s)>=5:
        l=list()
        for i in range(len(s)//k):
            l.insert(0, s[len(s)-(i+1)*k:len(s)-i*k])
        if len(s) % k !=0:
            l.insert(0, s[:len(s)-(i+1)*k])
        return chr.join(l)
    else:
        return s

def x2str(x, width):
    '''
    Rounds a number to tenths. If width is greater than its length, then it pads it with space.
    If width<0, then it does no padding.
    '''
    #if x<0.1 and x>-0.1 and width>=6:
    #    s = '{:.3f}'.format(x) #str(round(x*1000)/1000)
    if x<1 and x>-1 and width>=5:
        s = '{:.2f}'.format(x) #str(round(x*100)/100)
    elif x<10 and x>-10 and width>=4:
        s = '{:.1f}'.format(x) #str(round(x*10)/10)
    else:
        s = '{:.0f}'.format(x) #str(int(round(x)))
    if width > len(s):
        return s.rjust(width)
    else:
        return s

def analysis(df_ts, window_length, exp_or_lin, extent='full'):
    '''
    df_ts: pd.Series, it is a time series, can be totals or no. per e.g. 100,000 ppl
    window_length: int
    exp_or_lin in ['exp', 'lin']
    For 'exp', because of log2, this requires all entries in df_ts to be positive.
    For 'lin', because of log2, this requires last entry in df_ts to be positive.
    extent in ['full', 'minimal']
    'minimal' doesn't compute predictions.
    output: results = [
      daily increment in natural units (units of df_ts): float,
      daily growth rate in percentage: float,
      doubling time in days: float or 0 for 'minimal',
      current cases (df_ts.iloc[-1]),
      projection_lower: type(df_ts.dtype) or 0 for 'minimal',
      projection_upper: type(df_ts.dtype) or 0 for 'minimal',
      model_score=R^2: float,
      difference of model fit on last date and last data point in log space: float
      ]
            model: sklearn.linear_model
            #failure: 0 or 1; 1 if it failed due to nonpositive number in exponential fit or too short time series
    '''

    i_ts = (df_ts - df_ts.shift(1))[1:] # i for increments
    if len(i_ts)<window_length:# or (exp_or_lin=='exp' and (i_ts.iloc[-window_length:]<=0).sum()>=5):
        results = 8 * [0]
        results[-1] = 100
        return results, None
    intl_lo_days = 4
    intl_hi_days = 6
    results = [None] * 8
    results[3] = df_ts.iloc[-1]
    model = linear_model.LinearRegression(fit_intercept=True)
    if exp_or_lin=='exp':
        i_ts_orig = i_ts.copy()
        i_ts.iloc[-window_length:][i_ts<=0] = 1
        y = i_ts.iloc[-window_length:].values
        ylog = np.log(y)
        model.fit(np.arange(-window_length+1, 1).reshape(-1, 1), ylog)
        results[0] = math.exp(model.intercept_)
        # For doubling, the area of the increments is equal to df_ts[-1]
        # cf. https://www.wolframalpha.com/input/?i=integrate+%28exp%28a+t+%2Bb%29+dt%29+from+t%3D0+to+x
        if model.coef_[0]!=0:
            temp2 = math.exp(model.intercept_)/model.coef_[0]
            temp = model.coef_[0]*df_ts.iloc[-1]/math.exp(model.intercept_) + 1
            if temp>0:
                results[2] = math.log(temp)/model.coef_[0]
            else:
                results[2] = np.inf
        else:
            results[2] = df_ts.iloc[-1]/math.exp(model.intercept_)
        if extent == 'full':
            if model.coef_[0]!=0:
                results[4] = (math.exp(model.coef_[0]*intl_lo_days)-1)*temp2 + df_ts.iloc[-1]
                results[5] = (math.exp(model.coef_[0]*intl_hi_days)-1)*temp2 + df_ts.iloc[-1]
            else:
                results[4] = math.exp(model.intercept_)*intl_lo_days + df_ts.iloc[-1]
                results[5] = math.exp(model.intercept_)*intl_hi_days + df_ts.iloc[-1]

        if (i_ts_orig.iloc[-window_length:]>0).all():
            results[6] = model.score(np.arange(-window_length+1, 1).reshape(-1, 1), ylog)
        else:
            results[6] = 0
        if df_ts.iloc[-1]==df_ts.iloc[-window_length]:
            results[7] = 100
        else:
            if model.coef_[0]!=0:
                results[7] = temp2*(1-math.exp(model.coef_[0]*(-window_length+1)))/(df_ts.iloc[-1]-df_ts.iloc[-window_length])-1
            else:
                results[7] = math.exp(model.intercept_)*(-window_length+1)/(df_ts.iloc[-1]-df_ts.iloc[-window_length])-1
    else: # 'lin'
        y = i_ts.iloc[-window_length:].values
        model.fit(np.arange(-window_length+1, 1).reshape(-1, 1), y)
        results[0] = model.intercept_
        if model.coef_[0]!=0:
            if 2*model.coef_[0]*df_ts.iloc[-1] >= - model.intercept_*model.intercept_:
                results[2] = (-model.intercept_ + math.sqrt(model.intercept_*model.intercept_ + 2*model.coef_[0]*df_ts.iloc[-1]))/model.coef_[0]
            else:
                results[2] = np.inf
        else:
            if model.intercept_!=0:
                results[2] = df_ts.iloc[-1]/model.intercept_
            else:
                if df_ts.iloc[-1]!=0:
                    results[2] = np.inf
                else:
                    results[2] = 0 # model.coef_[0]==model.intercept_==0
        if extent == 'full':
            if model.coef_[0]*model.intercept_<0 and\
            ((model.coef_[0]>0 and -model.intercept_<intl_lo_days*model.coef_)\
            or (model.coef_[0]<0 and -model.intercept_>intl_lo_days*model.coef_)):
            # there is a zero-crossing until intl_lo_days
                results[4] = -model.intercept_*model.intercept_/(2*model.coef_[0]) + df_ts.iloc[-1]
                results[5] = results[4]
            elif model.coef_[0]*model.intercept_<0 and\
            ((model.coef_[0]>0 and -model.intercept_<intl_hi_days*model.coef_)\
            or (model.coef_[0]<0 and -model.intercept_>intl_hi_days*model.coef_)):
            # there is a zero-crossing after intl_lo_days, before intl_hi_days
                results[5] = -model.intercept_*model.intercept_/(2*model.coef_[0]) + df_ts.iloc[-1]
            if results[4] is None:
                results[4] = (model.coef_[0]*intl_lo_days/2+model.intercept_)*intl_lo_days + df_ts.iloc[-1]
            if results[5] is None:
                results[5] = (model.coef_[0]*intl_hi_days/2+model.intercept_)*intl_hi_days + df_ts.iloc[-1]
        results[6] = model.score(np.arange(-window_length+1, 1).reshape(-1, 1), y)
        if df_ts.iloc[-1]==df_ts.iloc[-window_length]:
            if model.coef_[0]==0 and model.intercept_==0:
                results[7] = 0
            else:
                results[7] = 100
        else:
            #print(model.coef_[0], model.intercept_, '\n', df_ts.iloc[-window_length:])
            #print(-(model.coef_[0]*(-window_length+1)/2+model.intercept_)*(-window_length+1))
            #print(df_ts.iloc[-1]-df_ts.iloc[-window_length])
            results[7] = -(model.coef_[0]*(-window_length+1)/2+model.intercept_)*(-window_length+1)/(df_ts.iloc[-1]-df_ts.iloc[-window_length])-1 # From the integral
            #print(window_length*(2*model.intercept_+model.coef_[0]*(-window_length+1))/(2*(df_ts.iloc[-1]-df_ts.iloc[-window_length]))-1) # From summing
            #print((-model.coef_[0]*(-window_length+1)*(-window_length+1)/2+(model.coef_[0]/2-model.intercept_)*(-window_length+1)+model.intercept_)/(df_ts.iloc[-1]-df_ts.iloc[-window_length])-1) # From summing
            #results[7] = np.sum(model.coef_[0]*np.arange(-window_length+1, 1)+model.intercept_)/(df_ts.iloc[-1]-df_ts.iloc[-window_length])-1 # From summing
            #print(results[7])
    if results[2]!=np.inf and results[2]!=0 and results[0]>0:
        #print(window_length, df_ts.iloc[-window_length-1:], y, model.coef_[0], model.intercept_, results, 1/results[2])
        results[1] = (math.pow(2, 1/results[2])-1)*100
    else:
        #y_last = (df_ts.iloc[-1]+df_ts.iloc[-2]+df_ts.iloc[-3])/3 # smoothening to lessen the impact of penultimate data point
        y_last = (df_ts.iloc[-1]+df_ts.iloc[-2])/2 # smoothening to lessen the impact of penultimate data point
        if y_last!=0:
            results[1] = results[0]*100 / y_last
        elif model.coef_[0]==0 and model.intercept_==0:
            results[1] = 0
        else:
            results[1] = np.inf

    if extent == 'minimal':
        #results[2] = 0
        results[4] = 0
        results[5] = 0
    #print(window_length, results)
    return results, model

'''
def analysis(df_ts, window_length, exp_or_lin, extent='full'):
    
    df_ts: pd.Series, it is a time series, can be totals or no. per e.g. 100,000 ppl
    window_length: int
    exp_or_lin in ['exp', 'lin']
    For 'exp', because of log2, this requires all entries in df_ts to be positive.
    For 'lin', because of log2, this requires last entry in df_ts to be positive.
    extent in ['full', 'minimal']
    'minimal' doesn't compute predictions.
    output: results = [
      daily increment in natural units (units of df_ts): float,
      daily growth rate in percentage: float,
      doubling time in days: float or 0 for 'minimal',
      current cases (df_ts.iloc[-1]),
      projection_lower: type(df_ts.dtype) or 0 for 'minimal',
      projection_upper: type(df_ts.dtype) or 0 for 'minimal',
      model_score=R^2: float,
      difference of model fit on last date and last data point in log space: float
      ]
            model: sklearn.linear_model
    
    if len(df_ts)<window_length:
        results = 8 * [0]
        results[-1] = 100
        return results, None
    intl_lo_days = 4
    intl_hi_days = 6
    results = [None] * 8
    results[3] = df_ts.iloc[-1]
    if exp_or_lin=='exp':
        ylog2 = np.log2(df_ts.iloc[-window_length:].values)
        model = linear_model.LinearRegression(fit_intercept=True)
        model.fit(np.arange(len(ylog2)).reshape(-1, 1), ylog2)
        y_last = (ylog2[-1]+ylog2[-2])/2 # smoothening to lessen the impact of last data point
        results[0] = (math.pow(2, model.coef_[0])-1) * math.pow(2, y_last)
        results[1] = (math.pow(2, model.coef_[0])-1)*100
        if extent == 'full':
            results[2] = 1/model.coef_[0]
            results[4] = math.pow(2, model.predict(np.array(len(ylog2)-1+intl_lo_days).reshape(1,-1)))
            results[5] = math.pow(2, model.predict(np.array(len(ylog2)-1+intl_hi_days).reshape(1,-1)))
        results[6] = model.score(np.arange(len(ylog2)).reshape(-1, 1), ylog2)
        results[7] = model.predict(np.array(len(ylog2)-1).reshape(-1, 1))[0]-ylog2[-1]
    else: # 'lin'
        y = df_ts.iloc[-window_length:].values
        model = linear_model.LinearRegression(fit_intercept=True)
        model.fit(np.arange(len(y)).reshape(-1, 1), y)
        results[0] = model.coef_[0]
        y_last = (y[-1]+y[-2])/2 # smoothening to lessen the impact of last data point
        results[1] = model.coef_[0]/y_last*100
        if extent == 'full':
            results[2] = 2*y_last/model.coef_[0]
            results[4] = model.predict(np.array(len(y)-1+intl_lo_days).reshape(1,-1))
            results[5] = model.predict(np.array(len(y)-1+intl_hi_days).reshape(1,-1))
        results[6] = model.score(np.arange(len(y)).reshape(-1, 1), y)
        results[7] = model.predict(np.array(len(y)-1).reshape(-1, 1))[0]/y[-1]-1
    if extent == 'minimal':
        results[2] = 0
        results[4] = 0
        results[5] = 0
    return results, model
'''

def select_window_length(R, round_output):
    '''
    This selects the window length that is good on two aspects: R^2 and matching last value
    round_output: boolean. If True, then it returns current and two projected case numbers as int.
    '''
    nr_col = R.shape[1]
    if nr_col==8: # If we're calling this from pick_exp_vs_lin() with window_selection, then we already have this so no need to compute it again and add it as new column.
        # We take l_2 norm of 10*(1-R^2) and distance column:
        R.insert(nr_col, nr_col, R[6].apply(lambda x: (10*(1-x))**2)
                                 + R[7].apply(lambda x: x**2))
    # Sort and return the row (corresponding to a window_length) with lowest l_2 norm:
    #return R.sort_values(7, axis=0, ascending=True).iloc[0:1,:]
    if R.shape[0]>1:
        R = R.sort_values(8, axis=0, ascending=True)
        #print(R)
    output = list()
    if round_output==True:
        for i in range(R.shape[1]):
            output.append(int(round(R.iloc[0,i])) if i in [3, 4, 5] else R.iloc[0,i])
    else:
        output = [R.iloc[0,i] for i in range(R.shape[1])]
    return output, R.index[0]
    #return [R.iloc[0,i] for i in range(nr_col+1)], R.index[0] # This maintains integer elements as integers, R.iloc[0,:] would cast them as float bc it creates a pd.Series with a shared type.

def pick_exp_vs_lin(r_exp, m_exp, r_lin, m_lin):
    r_exp = pd.DataFrame(r_exp).T
    r_exp, _ = select_window_length(r_exp, round_output=False)
    r_lin = pd.DataFrame(r_lin).T
    r_lin, _ = select_window_length(r_lin, round_output=False)
    if r_exp[-1] < r_lin[-1]:
        return r_exp[:-1], m_exp, 'exp'
    else:
        return r_lin[:-1], m_lin, 'lin'

#TODO this should have a switch that it should compute in densities when population size is available
def process_geounit(df_ts, window_length, exp_or_lin='both', running_extent='full'):
    '''
    This processes one geographical unit.
    df_ts is the time series.
    '''
    #df_ts = rm_early_zeros(df_ts)
    if window_length > 0:
        selected_window_length = window_length
        if exp_or_lin=='both':
            results_e, model_e = analysis(df_ts, window_length, 'exp', running_extent)
            results_l, model_l = analysis(df_ts, window_length, 'lin', running_extent)
            results, model, exp_or_lin = pick_exp_vs_lin(results_e, model_e, results_l, model_l)
            #print(results_e)
            #print(results_l)
        elif exp_or_lin=='exp':
            results, model = analysis(df_ts, window_length, 'exp', running_extent)
        else:
            results, model = analysis(df_ts, window_length, 'lin', running_extent)
    else: # do a search over window_lengths for best possible fit
        # minimum and maximum allowed window lengths; we test all in this closed interval
        wl_lo = 4
        wl_hi = 15 # this end point is not included
        # Rule out zeros because we take logarithm; rule out windows longer than the time series df_ts.
        #wl_hi = min(wl_hi, 1+len(df_ts[df_ts[df_ts>0].idxmin():]), 1+len(df_ts))
        wl_hi = min(wl_hi, 1+len(df_ts))
        if wl_hi <= wl_lo: # then abort
            #print(df_ts)
            results, model = analysis(pd.Series([]), 1, 'exp', running_extent)
            return results, model, window_length, exp_or_lin
        '''
        R = pd.DataFrame(np.zeros((wl_hi-wl_lo, 7)), index=range(wl_lo, wl_hi))
        models = dict()
        for wl in range(wl_lo, wl_hi): # last wl_hi-1 points must be available and positive <==
            result_wl, model = analysis_exp(df_ts, wl) # last wl points must be available and positive
            R.iloc[wl-wl_lo, :] = result_wl
            models[wl] = model
        R = R.astype({2: int, 3: int, 4: int})
        results, selected_window_length = select_window_length(R)
        model = models[selected_window_length]
        '''
        if exp_or_lin in ['exp', 'both']:
            R_e = pd.DataFrame(np.zeros((wl_hi-wl_lo, 8)), index=range(wl_lo, wl_hi))
            models_e = dict()
        if exp_or_lin in ['lin', 'both']:
            R_l = pd.DataFrame(np.zeros((wl_hi-wl_lo, 8)), index=range(wl_lo, wl_hi))
            models_l = dict()
        for wl in range(wl_lo, wl_hi): # last wl_hi-1 points must be available and positive <==
            if exp_or_lin in ['exp', 'both']:
                result_wl, model = analysis(df_ts, wl, 'exp', running_extent) # last wl points must be available and positive
                R_e.iloc[wl-wl_lo, :] = result_wl
                models_e[wl] = model
            if exp_or_lin in ['lin', 'both']:
                result_wl, model = analysis(df_ts, wl, 'lin', running_extent)
                R_l.iloc[wl-wl_lo, :] = result_wl
                models_l[wl] = model
        if exp_or_lin in ['exp', 'both']:
            results_e, selected_window_length_e = select_window_length(R_e, round_output=False)
            model_e = models_e[selected_window_length_e]
        if exp_or_lin in ['lin', 'both']:
            results_l, selected_window_length_l = select_window_length(R_l, round_output=False)
            model_l = models_l[selected_window_length_l]
        if exp_or_lin == 'exp':
            results, model, selected_window_length = results_e[:-1], model_e, selected_window_length_e
        if exp_or_lin == 'lin':
            results, model, selected_window_length = results_l[:-1], model_l, selected_window_length_l
        if exp_or_lin == 'both':
            results, model, exp_or_lin = pick_exp_vs_lin(results_e, model_e, results_l, model_l)
            selected_window_length = selected_window_length_e if exp_or_lin=='exp'\
                                     else selected_window_length_l
    return results, model, selected_window_length, exp_or_lin

def print_header(normalise_by, population_csv=None):
    print('The number of cases increases daily by /')
    if population_csv is not None:
        print('The number of cases per {} people increases daily by /'.format(separated(str(int(normalise_by)))))
    print('The number of cases increases daily by (%)/')
    print('Time it takes for the number of cases to double /')
    print('Latest reported number of cases /')
    if population_csv is not None:
        print('Latest reported number of cases per {} people /'.format(separated(str(int(normalise_by)))))
        print('My estimation for number of cases per {} people at present /'.format(separated(str(int(normalise_by)))))
    else:
        print('My estimation for number of cases at present /')
    print('R^2 /')
    print('Tail difference /')
    print('Window length /')
    print('Exponential (e) or linear (l) approximation\n')

def print_results(country, results, normalise_by, population_csv, wl, exp_or_lin, frmt='normal', lang='en'):
    '''
    frmt (format) can be 'deaths' or other. For 'deaths', there is one more decimal digit displayed for
    cases per 100,000 and estimate interval is not displayed.
    '''
    country_width = 23 if frmt!='deaths' else 24
    interval_width = 14
    #if country in ['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen',
    #'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
    #'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen',
    #'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen',
    #'Deutschland']:
    if population_csv=='DEU':
        pop = load_population_DEU()
    elif population_csv=='world':
        pop = load_population_world()
    elif population_csv=='BW':
        pop = load_population_BW()
    else:
        pop = normalise_by # We don't normalise.
    if not isinstance(country, str): # If it's a province or state of a country or region.
        country = country[0]

    if frmt!='active': # If input is a cumulative number, then don't display negative estimates.
        if results[0]<0:
            results[0]=0
        if results[1]<0:
            results[1]=0
    if population_csv is not None:
        incr_per_ppl = x2str(normalise_by*results[0]/pop[country], 4 if frmt!='deaths' else 6)
    else:
        incr_per_ppl = ' ' * 4 if frmt!='deaths' else ' ' * 6
    #if ((results[6]>=0.95 and results[7]<=0.5) or (results[7]>=-0.2 and results[7]<=0.1)) and\
    #    results[0]>0 and frmt!='deaths':
    if ((results[6]>=0.75 and results[7]<=0.5) or (results[7]>=-0.3 and results[7]<=0.3)) and\
        results[0]>0 and frmt!='deaths':
        #print('{0} {1:4.1f}% {2:7.1f} {3}  {4}  {5}  {6:4.2f} {7:5.2f}  {8}'.format(
         #country.ljust(country_width), results[0], results[1] if results[1]>=0 else np.NaN, 'Tage' if lang=='de' else 'days',
         #str(results[2]).rjust(7), ('[' + str(results[3]) +', '+ str(results[4]) + ']').rjust(interval_width), results[5], results[6], str(wl).rjust(2)).replace('.', ',' if lang=='de' else '.'))
        if population_csv is not None:
            nr_cases_per_ppl = x2str(normalise_by*results[3]/pop[country], int(math.log10(normalise_by))+1)
            est_lo_per_ppl = normalise_by*results[4]/pop[country]
            est_hi_per_ppl = normalise_by*results[5]/pop[country]
        else:
            nr_cases_per_ppl = ' ' * int(math.log10(normalise_by))
            est_lo_per_ppl = results[4]
            est_hi_per_ppl = results[5]
        #interval = ('[' + x2str(est_lo_per_ppl, -1) +', '\
        #         + x2str(est_hi_per_ppl, -1) + ']').rjust(interval_width)
        est_per_ppl_min = min(est_lo_per_ppl, est_hi_per_ppl)
        est_per_ppl_max = max(est_lo_per_ppl, est_hi_per_ppl)
        interval = ('[' + x2str(est_per_ppl_min, -1) +', '\
                 + x2str(est_per_ppl_max, -1) + ']').rjust(interval_width)
    else:
        if population_csv is not None:
            nr_cases_per_ppl = x2str(normalise_by*results[3]/pop[country], int(math.log10(normalise_by))+1)
        else:
            nr_cases_per_ppl = ' ' * int(math.log10(normalise_by))
        if frmt!='deaths':
            interval = ' ' * interval_width
        else:
            interval = '  '

    print('{0} {1} {2} {3:5.1f}% {4:7.1f} {5} {6} {7} {8} {9:4.2f} {10:5.2f}  {11}  {12}'.format(
        country[:country_width].ljust(country_width),
        x2str(results[0], 6),
        incr_per_ppl,
        results[1],
        results[2] if results[0]>=0 else np.NaN, # if results[1]>=0 else np.NaN,
        'Tage' if lang=='de' else 'days',
        x2str(results[3], 7),
        nr_cases_per_ppl,
        interval,
        results[6],
        results[7],
        str(wl).rjust(2),
        'e' if exp_or_lin=='exp' else 'l').replace('.', ',' if lang=='de' else '.'))

def plotting(df_ts, model, save_not_show, country, window_length, exp_or_lin, lang='en'):
    if not isinstance(country, str): # If it's a province or state of a country or region.
        country = country[0]
    #fig, (ax1, ax2) = plt.subplots(1,2, figsize=(9.6, 4.8))
    fig, (ax0, ax1, ax2) = plt.subplots(1,3, figsize=(14.4, 4.8))
    if lang=='de':
        line0 = 'Beobachtungen'
        line1 = 'Exponentielle Annäherung' if exp_or_lin=='exp' else 'Lineare Annäherung'
        fig.suptitle(country + ', Stand ' + df_ts.index[-1].strftime('%d.%m.%Y'))
        plt.gcf().text(0.905, 0.86, "© Bence Mélykúti, 2020. http://COVID19de.Melykuti.Be", fontsize=8, color='lightgray', rotation=90)
    else:
        line0 = 'Observations'
        line1 = 'Exponential approximation' if exp_or_lin=='exp' else 'Linear approximation'
        fig.suptitle(country + ', ' + df_ts.index[-1].strftime('%d %B %Y'))
        plt.gcf().text(0.905, 0.862, "© Bence Mélykúti, 2020. http://COVID19.Melykuti.Be", fontsize=8, color='lightgray', rotation=90)
    #fig.tight_layout()
    fig.subplots_adjust(bottom=0.2)
    #ax1.plot(df_ts[df_ts>0], label=line0)
    #ax1.plot(df_ts[df_ts>0].iloc[-window_length:].index, np.power(2, np.arange(0, window_length)*model.coef_ + model.intercept_), label=line1)
    plot_x = df_ts.iloc[-window_length:].index
    i_ts = (df_ts - df_ts.shift(1))[1:] # i for increments
    ax0.bar(df_ts[1:].index, i_ts[-len(df_ts)+1:], color='tab:blue')
    #df_ts_no0 = rm_consecutive_early_zeros(df_ts)
    #df_ts_no0 = df_ts
    if exp_or_lin=='exp':
        #print(df_ts_no0[1:].index)
        #print(i_ts[-len(df_ts_no0)+1:])
        #print(i_ts)
        if model is not None:
            ax0.plot(plot_x, np.exp(model.coef_[0]*np.arange(-window_length+1, 1) + model.intercept_), color='tab:orange', linewidth=3)
        #plot_y = np.power(2, np.arange(0, window_length)*model.coef_ + model.intercept_)
        #temp2 = math.pow(2, model.intercept_)/(math.log(2)*model.coef_[0])
            if model.coef_[0]!=0:
                temp2 = math.exp(model.intercept_)/model.coef_[0]
            #plot_y = (np.power(2, model.coef_[0]*np.arange(-window_length+1, 1))-1)*temp2 + df_ts.iloc[-1]
            #plot_y = (np.power(2, model.coef_[0]*np.arange(-window_length+1, 1))-1)*temp2 + df_ts.iloc[-window_length]
                plot_y = (np.exp(model.coef_[0]*np.arange(-window_length+1, 1)) - math.exp(model.coef_[0] * (-window_length+1)))*temp2 + df_ts.iloc[-window_length]
            else:
                plot_y = math.exp(model.intercept_)*(np.arange(-window_length+1, 1) - (-window_length+1)) + df_ts.iloc[-window_length]
            ax1.plot(plot_x, plot_y, label=line1, color='tab:orange', linewidth=3)
            ax2.plot(plot_x, plot_y, label=line1, color='tab:orange', linewidth=3)
    else:
        #print(df_ts_no0[1:].index)
        #print(i_ts[-len(df_ts_no0)+1:])
        #ax0.bar(df_ts[1:].index, i_ts[-len(df_ts)+1:], color='tab:blue')
        ax0.plot(plot_x, model.coef_[0]*np.arange(-window_length+1, 1) + model.intercept_, color='tab:pink', linewidth=3)
        #plot_y = np.arange(0, window_length)*model.coef_ + model.intercept_
        #plot_y = (model.coef_[0]*np.arange(-window_length+1, 1)/2+model.intercept_)*np.arange(-window_length+1, 1) + df_ts.iloc[-1]
#        plot_y = (model.coef_[0]*np.arange(0, window_length)/2+model.intercept_)*np.arange(0, window_length) + df_ts.iloc[-window_length]
        plot_y = (model.coef_[0]*np.arange(-window_length+1, 1)/2+model.intercept_)*np.arange(-window_length+1, 1) - (model.coef_[0]*(-window_length+1)/2+model.intercept_)*(-window_length+1) + df_ts.iloc[-window_length]
        ax1.plot(plot_x, plot_y, label=line1, color='tab:pink', linewidth=3)
        ax2.plot(plot_x, plot_y, label=line1, color='tab:pink', linewidth=3)

    ax1.plot(df_ts, label=line0, color='tab:blue')
    ax2.plot(df_ts, label=line0, color='tab:blue')

    ax2.set_yscale("log")
    for tick in ax0.get_xticklabels():
        tick.set_rotation(80)
    for tick in ax1.get_xticklabels():
        tick.set_rotation(80)
    for tick in ax2.get_xticklabels():
        tick.set_rotation(80)
    handles, labs = ax1.get_legend_handles_labels()
    if model is not None:
        ax1.legend((handles[1], handles[0]), (labs[1], labs[0]))
    else:
        ax1.legend([handles[0]], [labs[0]])
    if save_not_show==0:
        plt.show()
    elif save_not_show==1:
        imgfile = country.replace(',', '_').replace(' ', '_').replace('(', '_').replace(')', '_')\
                  + '_' + df_ts.index[-1].strftime('%Y-%m-%d') + '.png'
        plt.savefig(imgfile)
        plt.close(fig)

def load_population_world():
    pop = pd.read_csv('population_world.csv', sep='\t')
    pop_ser=pd.Series(pop.Population.apply(lambda x: int(x.replace(',', ''))).values, index=pop.Country)
    countries = dict()
    for country in pop_ser.index:
        country_new = country.strip()
        countries[country_new] = pop_ser.loc[country]
    return countries

def load_population_DEU():
    pop = pd.read_csv('population_DEU.csv', sep='\t')
    pop_ser=pd.Series(pop.insgesamt.values, index=pop.Bundesland)
    countries = dict()
    for country in pop_ser.index:
        country_new = country.strip()
        countries[country_new] = pop_ser.loc[country]
    return countries

def load_population_BW(incl_density=False):
    pop = pd.read_csv('population_BW.csv', sep=',')
    pop_ser=pd.Series(pop['Bevölkerung insgesamt'].values, index=pop.Regionalname)
    countries = dict()
    for country in pop_ser.index:
        countries[country] = pop_ser.loc[country]
    if incl_density:
        pop.rename(index=pop.Regionalname, inplace=True)
        return pop.drop('Regionalname', axis=1, inplace=False)
    else:
        return countries
