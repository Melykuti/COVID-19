'''
Compares the daily increase factor as a function of case number across countries
using the JHU CSSE dataset:
https://github.com/CSSEGISandData

exec(open('comparison_joint.py').read())
12/3/2020-2/1/2021
'''

import os, math, time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import utils
from importlib import reload

class PlotSpecs():
    def __init__(self):
        self.cases = 'confirmed' # 'confirmed' or 'deaths' or 'active' or 'recovered'
        self.incr_or_rate = 'rate' # Which to display: 'incr' for daily increment, 'rate' for daily growth rate
        self.normalise = 'xy' # 'xy' or 'y' if you want to normalise by population size ('xy' normalises both x and y values (unless xaxis = 'date'), 'y' normalises only y values), o.w. None; 'y' alone can be normalised only if incr_or_rate=='incr' & xaxis=='cases'
        self.xaxis = 'cases' # What to use for x-axis: 'date' for date or 'cases' for number of cases
        self.left_bound=0.8
        self.right_bound=None
        self.bottom_bound=-10.
        self.top_bound=100.
        self.cycle_linestyle = 0 # if 0, then all lines are solid; if 1, then it cycles through solid, dotted, dashed, dash-dotted
        self.exp_or_lin = 'lin' # Use 'exp' model (fitting linear model on logarithmic scale) or 'lin' model or 'both' for trying both and selecting the better.
        self.lang = 'en' # 'de' for German, anything else for English
        self.max_display_length = 100 #45 # in days; if positive, then it plots the most recent max_display_length days only
        self.normalise_by = int(1e5) # display case numbers per this many people
        self.save_not_show = 1 # if 0, then shows the plot; if 1, then saves it; o.w. it does neither
        self.time_start = pd.Timestamp.date(pd.Timestamp('today'))-self.max_display_length*pd.DateOffset()
        self.window_length = -1 # from latest data point back into past if positive; if nonpositive, then it searches for optimum for model fitting (recommended)
        #self.window_length = 7

### User input ###

intl0 = PlotSpecs()
intl0.countries = ['United Kingdom', 'Spain', 'Sweden', 'Belgium', 'Italy', 'France', 'Germany', 'Ireland', 'Netherlands', 'Switzerland', 'Korea, South', 'Japan', 'China']; intl0.left_bound=4.; intl0.right_bound=None; intl0.bottom_bound=0.; intl0.top_bound=30.; intl0.normalise = 'xy'; intl0.filename = 'Joint'; intl0.cycle_linestyle = 1; intl0.incr_or_rate = 'rate'; intl0.xaxis = 'cases'; intl0.exp_or_lin = 'lin' #'Turkey', 
intl1 = PlotSpecs()
intl1.countries = ['United Kingdom', 'Spain', 'Sweden', 'Belgium', 'Italy', 'France', 'Germany', 'Ireland', 'Netherlands', 'Switzerland', 'Korea, South', 'Japan', 'China']; intl1.left_bound=3.; intl1.right_bound=None; intl1.bottom_bound=0.; intl1.top_bound=None; intl1.normalise = 'xy'; intl1.filename = 'Joint'; intl1.cycle_linestyle = 1; intl1.incr_or_rate = 'incr'; intl1.xaxis = 'cases'; intl1.exp_or_lin = 'lin' #'Turkey', 
intl2 = PlotSpecs()
intl2.countries = ['United Kingdom', 'Spain', 'Sweden', 'Belgium', 'Italy', 'France', 'Germany', 'Ireland', 'Netherlands', 'Switzerland', 'Korea, South', 'Japan', 'China']; intl2.left_bound=intl2.time_start; intl2.right_bound=None; intl2.bottom_bound=0.; intl2.top_bound=None; intl2.normalise = 'xy'; intl2.filename = 'Joint'; intl2.cycle_linestyle = 1; intl2.incr_or_rate = 'incr'; intl2.xaxis = 'date'; intl2.exp_or_lin = 'lin' #'Turkey', 

gp0 = PlotSpecs()
gp0.countries = ['China', 'EU', 'US', 'Russia', 'Brazil', 'India']; gp0.left_bound=0.1; gp0.right_bound=None; gp0.bottom_bound=0.; gp0.top_bound=25.; gp0.normalise = 'xy'; gp0.filename = 'great_powers'; gp0.lang = 'en'; gp0.cycle_linestyle = 0; gp0.incr_or_rate = 'rate'; gp0.xaxis = 'cases'; gp0.exp_or_lin = 'lin'
gp1 = PlotSpecs()
gp1.countries = ['China', 'EU', 'US', 'Russia', 'Brazil', 'India']; gp1.left_bound=0.1; gp1.right_bound=None; gp1.bottom_bound=0.; gp1.top_bound=None; gp1.normalise = 'xy'; gp1.filename = 'great_powers'; gp1.lang = 'en'; gp1.cycle_linestyle = 0; gp1.incr_or_rate = 'incr'; gp1.xaxis = 'cases'; gp1.exp_or_lin = 'lin'
gp2 = PlotSpecs()
gp2.countries = ['China', 'EU', 'US', 'Russia', 'Brazil', 'India']; gp2.left_bound=gp2.time_start; gp2.right_bound=None; gp2.bottom_bound=0.; gp2.top_bound=None; gp2.normalise = 'xy'; gp2.filename = 'great_powers'; gp2.lang = 'en'; gp2.cycle_linestyle = 0; gp2.incr_or_rate = 'incr'; gp2.xaxis = 'date'; gp2.exp_or_lin = 'lin'

vis0 = PlotSpecs()
vis0.countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; vis0.left_bound=2; vis0.right_bound=None; vis0.bottom_bound=0.; vis0.top_bound=35.; vis0.normalise = 'xy'; vis0.filename = 'Visegrad'; vis0.cycle_linestyle = 1; vis0.incr_or_rate = 'rate'; vis0.xaxis = 'cases'; vis0.exp_or_lin = 'lin'
vis1 = PlotSpecs()
vis1.countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; vis1.left_bound=2; vis1.right_bound=None; vis1.bottom_bound=0.; vis1.top_bound=None; vis1.normalise = 'xy'; vis1.filename = 'Visegrad'; vis1.cycle_linestyle = 1; vis1.incr_or_rate = 'incr'; vis1.xaxis = 'cases'; vis1.exp_or_lin = 'lin'
vis2 = PlotSpecs()
vis2.countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; vis2.left_bound=vis2.time_start; vis2.right_bound=None; vis2.bottom_bound=0.; vis2.top_bound=None; vis2.normalise = 'xy'; vis2.filename = 'Visegrad'; vis2.cycle_linestyle = 1; vis2.incr_or_rate = 'incr'; vis2.xaxis = 'date'; vis2.exp_or_lin = 'lin'

deu0 = PlotSpecs()
deu0.countries = 'Deutschland'; deu0.left_bound=9; deu0.right_bound=None; deu0.bottom_bound=0.; deu0.top_bound=27.5; deu0.normalise = 'xy'; deu0.filename = 'Deutschland'; deu0.lang = 'de'; deu0.cycle_linestyle = 1; deu0.incr_or_rate = 'rate'; deu0.xaxis = 'cases'; deu0.exp_or_lin = 'lin'
deu1 = PlotSpecs()
deu1.countries = 'Deutschland'; deu1.left_bound=9; deu1.right_bound=None; deu1.bottom_bound=0.; deu1.top_bound=None; deu1.normalise = 'xy'; deu1.filename = 'Deutschland'; deu1.lang = 'de'; deu1.cycle_linestyle = 1; deu1.incr_or_rate = 'incr'; deu1.xaxis = 'cases'; deu1.exp_or_lin = 'lin'
deu2 = PlotSpecs()
deu2.countries = 'Deutschland'; deu2.left_bound=pd.to_datetime('2020-10-01'); deu2.right_bound=None; deu2.bottom_bound=0.; deu2.top_bound=None; deu2.normalise = 'xy'; deu2.filename = 'Deutschland'; deu2.lang = 'de'; deu2.cycle_linestyle = 1; deu2.incr_or_rate = 'incr'; deu2.xaxis = 'date'; deu2.exp_or_lin = 'lin' #deu2.left_bound=deu2.time_start; pd.to_datetime('2020-03-01');
deu3 = PlotSpecs()
deu3.countries = 'Deutschland'; deu3.left_bound=pd.to_datetime('2020-10-01'); deu3.right_bound=None; deu3.bottom_bound=0.; deu3.top_bound=None; deu3.normalise = 'xy'; deu3.filename = 'Deutschland'; deu3.lang = 'de'; deu3.cycle_linestyle = 1; deu3.incr_or_rate = 'incr'; deu3.xaxis = 'date'; deu3.exp_or_lin = 'lin'; deu3.cases = 'deaths'; # deu3.left_bound=pd.to_datetime('2020-03-01');

# Nordic countries
nordic0 = PlotSpecs()
nordic0.countries = ['Norway', 'Sweden', 'Finland', 'Denmark', 'Iceland']; nordic0.left_bound=2; nordic0.right_bound=None; nordic0.bottom_bound=0.; nordic0.top_bound=None; nordic0.normalise = 'xy'; nordic0.filename = 'Nordic'; nordic0.cycle_linestyle = 1; nordic0.incr_or_rate = 'rate'; nordic0.xaxis = 'cases'; nordic0.exp_or_lin = 'lin'
nordic1 = PlotSpecs()
nordic1.countries = ['Norway', 'Sweden', 'Finland', 'Denmark', 'Iceland']; nordic1.left_bound=2; nordic1.right_bound=None; nordic1.bottom_bound=0.; nordic1.top_bound=None; nordic1.normalise = 'xy'; nordic1.filename = 'Nordic'; nordic1.cycle_linestyle = 1; nordic1.incr_or_rate = 'incr'; nordic1.xaxis = 'cases'; nordic1.exp_or_lin = 'lin'
nordic2 = PlotSpecs()
nordic2.countries = ['Norway', 'Sweden', 'Finland', 'Denmark', 'Iceland']; nordic2.left_bound=nordic2.time_start; nordic2.right_bound=None; nordic2.bottom_bound=0.; nordic2.top_bound=None; nordic2.normalise = 'xy'; nordic2.filename = 'Nordic'; nordic2.cycle_linestyle = 1; nordic2.incr_or_rate = 'incr'; nordic2.xaxis = 'date'; nordic2.exp_or_lin = 'lin'

# DACH
dach0 = PlotSpecs()
dach0.countries = ['Germany', 'Switzerland', 'Liechtenstein', 'Austria']; dach0.left_bound=2; dach0.right_bound=None; dach0.bottom_bound=0.; dach0.top_bound=80.; dach0.normalise = 'xy'; dach0.filename = 'DACH'; dach0.cycle_linestyle = 1; dach0.incr_or_rate = 'rate'; dach0.xaxis = 'cases'; dach0.exp_or_lin = 'lin'
dach1 = PlotSpecs()
dach1.countries = ['Germany', 'Switzerland', 'Liechtenstein', 'Austria']; dach1.left_bound=2; dach1.right_bound=None; dach1.bottom_bound=0.; dach1.top_bound=None; dach1.normalise = 'xy'; dach1.filename = 'DACH'; dach1.cycle_linestyle = 1; dach1.incr_or_rate = 'incr'; dach1.xaxis = 'cases'; dach1.exp_or_lin = 'lin'
dach2 = PlotSpecs()
dach2.countries = ['Germany', 'Switzerland', 'Liechtenstein', 'Austria']; dach2.left_bound=dach2.time_start; dach2.right_bound=None; dach2.bottom_bound=0.; dach2.top_bound=None; dach2.normalise = 'xy'; dach2.filename = 'DACH'; dach2.cycle_linestyle = 1; dach2.incr_or_rate = 'incr'; dach2.xaxis = 'date'; dach2.exp_or_lin = 'lin'

#countries = ['United Kingdom', 'Spain', 'Sweden', 'Denmark', 'Italy', 'France', 'Germany', 'Netherlands', 'Belgium']; left_bound=time_start; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'WesternEurope'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'lin'

# Confirmed
#countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia']; left_bound=2; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'CentralEurope'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'cases'; exp_or_lin = 'lin'
#countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia']; left_bound=time_start; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'CentralEurope'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'lin'


# Death toll
intl0d = PlotSpecs()
intl0d.cases = 'deaths'; intl0d.countries = ['US', 'Brazil', 'United Kingdom', 'Spain', 'Sweden', 'Belarus', 'Italy', 'France', 'Belgium', 'Germany']; intl0d.left_bound=1; intl0d.right_bound=None; intl0d.bottom_bound=0.; intl0d.top_bound=None; intl0d.normalise = 'xy'; intl0d.filename = 'Joint'; intl0d.cycle_linestyle = 1; intl0d.incr_or_rate = 'incr'; intl0d.xaxis = 'cases'; intl0d.exp_or_lin = 'lin'
intl1d = PlotSpecs()
intl1d.cases = 'deaths'; intl1d.countries = ['US', 'Brazil', 'United Kingdom', 'Spain', 'Sweden', 'Belarus', 'Italy', 'France', 'Belgium', 'Germany']; intl1d.left_bound=intl1d.time_start; intl1d.right_bound=None; intl1d.bottom_bound=0.; intl1d.top_bound=None; intl1d.normalise = 'xy'; intl1d.filename = 'Joint'; intl1d.cycle_linestyle = 1; intl1d.incr_or_rate = 'incr'; intl1d.xaxis = 'date'; intl1d.exp_or_lin = 'lin'

west0d = PlotSpecs()
west0d.cases = 'deaths'; west0d.countries = ['United Kingdom', 'Spain', 'Sweden', 'Denmark', 'Italy', 'France', 'Germany', 'Netherlands', 'Belgium']; west0d.left_bound=1; west0d.right_bound=None; west0d.bottom_bound=0.; west0d.top_bound=None; west0d.normalise = 'xy'; west0d.filename = 'WesternEurope'; west0d.cycle_linestyle = 1; west0d.incr_or_rate = 'incr'; west0d.xaxis = 'cases'; west0d.exp_or_lin = 'lin'
west1d = PlotSpecs()
west1d.cases = 'deaths'; west1d.countries = ['United Kingdom', 'Spain', 'Sweden', 'Denmark', 'Italy', 'France', 'Germany', 'Netherlands', 'Belgium']; west1d.left_bound=west1d.time_start; west1d.right_bound=None; west1d.bottom_bound=0.; west1d.top_bound=None; west1d.normalise = 'xy'; west1d.filename = 'WesternEurope'; west1d.cycle_linestyle = 1; west1d.incr_or_rate = 'incr'; west1d.xaxis = 'date'; west1d.exp_or_lin = 'lin'

west2_0d = PlotSpecs()
west2_0d.cases = 'deaths'; west2_0d.countries = ['Italy', 'Spain', 'US', 'United Kingdom', 'France', 'Netherlands', 'Belgium', 'Sweden', 'Germany']; west2_0d.left_bound=0.1; west2_0d.right_bound=None; west2_0d.bottom_bound=0.; west2_0d.top_bound=3.; west2_0d.normalise = 'xy'; west2_0d.filename = 'deathtoll'; west2_0d.cycle_linestyle = 1; west2_0d.incr_or_rate = 'incr'; west2_0d.xaxis = 'cases'; west2_0d.exp_or_lin = 'lin'
west2_1d = PlotSpecs()
west2_1d.cases = 'deaths'; west2_1d.countries = ['Italy', 'Spain', 'US', 'United Kingdom', 'France', 'Netherlands', 'Belgium', 'Sweden', 'Germany']; west2_1d.left_bound=pd.to_datetime('2020-03-01'); west2_1d.right_bound=None; west2_1d.bottom_bound=0.; west2_1d.top_bound=3.; west2_1d.normalise = 'xy'; west2_1d.filename = 'deathtoll'; west2_1d.cycle_linestyle = 1; west2_1d.incr_or_rate = 'incr'; west2_1d.xaxis = 'date'; west2_1d.exp_or_lin = 'lin' # left_bound=time_start?

gp0d = PlotSpecs()
gp0d.cases = 'deaths'; gp0d.countries = ['China', 'EU', 'US', 'Russia', 'Brazil', 'India']; gp0d.left_bound=0.01; gp0d.right_bound=None; gp0d.bottom_bound=0.; gp0d.top_bound=None; gp0d.normalise = 'xy'; gp0d.filename = 'great_powers'; gp0d.lang = 'en'; gp0d.cycle_linestyle = 0; gp0d.incr_or_rate = 'incr'; gp0d.xaxis = 'cases'; gp0d.exp_or_lin = 'lin'
gp1d = PlotSpecs()
gp1d.cases = 'deaths'; gp1d.countries = ['China', 'EU', 'US', 'Russia', 'Brazil', 'India']; gp1d.left_bound=gp1d.time_start; gp1d.right_bound=None; gp1d.bottom_bound=0.; gp1d.top_bound=None; gp1d.normalise = 'xy'; gp1d.filename = 'great_powers'; gp1d.lang = 'en'; gp1d.cycle_linestyle = 0; gp1d.incr_or_rate = 'incr'; gp1d.xaxis = 'date'; gp1d.exp_or_lin = 'lin'

vis0d = PlotSpecs()
vis0d.cases = 'deaths'; vis0d.countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia']; vis0d.left_bound=0.01; vis0d.right_bound=None; vis0d.bottom_bound=0.; vis0d.top_bound=None; vis0d.normalise = 'xy'; vis0d.filename = 'Visegrad'; vis0d.cycle_linestyle = 1; vis0d.incr_or_rate = 'incr'; vis0d.xaxis = 'cases'; vis0d.exp_or_lin = 'lin'
vis1d = PlotSpecs()
vis1d.cases = 'deaths'; vis1d.countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia']; vis1d.left_bound=vis1d.time_start; vis1d.right_bound=None; vis1d.bottom_bound=0.; vis1d.top_bound=None; vis1d.normalise = 'xy'; vis1d.filename = 'Visegrad'; vis1d.cycle_linestyle = 1; vis1d.incr_or_rate = 'incr'; vis1d.xaxis = 'date'; vis1d.exp_or_lin = 'lin'
# countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia']; left_bound=0.01; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'CentralEurope'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'cases'; exp_or_lin = 'lin'
#cases = 'deaths'; countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia']; left_bound=time_start; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'CentralEurope'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'lin'

vis2.countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; vis2.left_bound=vis2.time_start; vis2.right_bound=None; vis2.bottom_bound=0.; vis2.top_bound=None; vis2.normalise = 'xy'; vis2.filename = 'Visegrad'; vis2.cycle_linestyle = 1; vis2.incr_or_rate = 'incr'; vis2.xaxis = 'date'; vis2.exp_or_lin = 'lin'


nordic0d = PlotSpecs()
nordic0d.cases = 'deaths'; nordic0d.countries = ['Norway', 'Sweden', 'Finland', 'Denmark', 'Iceland']; nordic0d.left_bound=0.01; nordic0d.right_bound=None; nordic0d.bottom_bound=0.; nordic0d.top_bound=None; nordic0d.normalise = 'xy'; nordic0d.filename = 'Nordic'; nordic0d.cycle_linestyle = 1; nordic0d.incr_or_rate = 'incr'; nordic0d.xaxis = 'cases'; nordic0d.exp_or_lin = 'lin'
nordic1d = PlotSpecs()
nordic1d.cases = 'deaths'; nordic1d.countries = ['Norway', 'Sweden', 'Finland', 'Denmark', 'Iceland']; nordic1d.left_bound=nordic1d.time_start; nordic1d.right_bound=None; nordic1d.bottom_bound=0.; nordic1d.top_bound=None; nordic1d.normalise = 'xy'; nordic1d.filename = 'Nordic'; nordic1d.cycle_linestyle = 1; nordic1d.incr_or_rate = 'incr'; nordic1d.xaxis = 'date'; nordic1d.exp_or_lin = 'lin'

USAGER1d = PlotSpecs()
USAGER1d.cases = 'deaths'; USAGER1d.countries = ['US', 'Germany']; USAGER1d.left_bound=USAGER1d.time_start; USAGER1d.right_bound=None; USAGER1d.bottom_bound=0.; USAGER1d.top_bound=None; USAGER1d.normalise = 'xy'; USAGER1d.filename = 'USA_GER'; USAGER1d.cycle_linestyle = 0; USAGER1d.incr_or_rate = 'incr'; USAGER1d.xaxis = 'date'; USAGER1d.exp_or_lin = 'lin'; USAGER1d.save_not_show = 0

# Testing

#countries = ['China', 'EU', 'US']; left_bound=1000; right_bound=None; bottom_bound=0.; top_bound=None; normalise = None; filename = 'great_powers'; lang = 'en'; cycle_linestyle = 0
#countries = ['China', 'EU', 'US']; left_bound=pd.to_datetime('2020-03-01'); right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'y'; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'exp'; filename = 'great_powers'; lang = 'en'; cycle_linestyle = 0

#countries = ['Japan', 'Korea, South', 'China']; left_bound=None; right_bound=None; bottom_bound=0.; top_bound=80.; normalise = 'xy'; filename = 'Joint'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'lin'

#countries = 'Deutschland'; left_bound=1; right_bound=None; bottom_bound=0.; top_bound=60.; normalise = 'xy'; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'exp'; cases = 'deaths'
#countries = 'Deutschland'; left_bound=1; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'cases'; exp_or_lin = 'exp'; cases = 'deaths'
#countries = 'Deutschland'; left_bound=time_start; right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'exp'; cases = 'deaths'

#countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; left_bound=pd.to_datetime('2020-03-01'); right_bound=None; bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Visegrad'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'exp'
#countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; left_bound=pd.to_datetime('2020-03-15'); right_bound=pd.to_datetime('2020-04-02'); bottom_bound=0.; top_bound=None; normalise = 'xy'; filename = 'Visegrad'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'exp'

#countries = 'Deutschland'; left_bound=200; right_bound=None; bottom_bound=0.; top_bound=60.; normalise = None; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'exp'
#countries = 'Deutschland'; left_bound=9; right_bound=None; bottom_bound=0.; top_bound=60.; normalise = 'xy'; filename = 'Deutschland'; lang = 'de'; cycle_linestyle = 1; incr_or_rate = 'rate'; xaxis = 'cases'; exp_or_lin = 'exp'

#countries = ['US', 'Italy', 'China', 'Spain', 'Germany', 'Iran', 'France', 'Korea, South', 'Switzerland', 'United Kingdom', 'Netherlands', 'Japan']; left_bound=1000; right_bound=None; bottom_bound=0.; top_bound=60.; normalise = None; filename = 'Joint'; cycle_linestyle = 1
#countries = ['US', 'Italy', 'China', 'Spain', 'Germany', 'Iran', 'France', 'Korea, South', 'Switzerland', 'United Kingdom', 'Netherlands', 'Japan']; left_bound=1.; right_bound=None; bottom_bound=0.; top_bound=80.; normalise = 'y'; filename = 'Joint'; cycle_linestyle = 1

#countries = ['Switzerland', 'United Kingdom']; left_bound=10.; right_bound=None; bottom_bound=0.; top_bound=80.; normalise = 'y'; filename = 'test';
#countries = ['Italy', 'Spain', 'France', 'Germany', 'Switzerland', ['United Kingdom', 'United Kingdom'], 'Netherlands', 'Austria', 'Sweden', 'Denmark', 'Japan', 'Hungary', 'Korea, South', 'China']
#countries = ['Hungary']; left_bound=50*normalise_by/10e6; right_bound=None; normalise = 'y'; filename = 'Visegrad'
#countries = ['Iceland']; left_bound=None; right_bound=None; normalise = None; filename = 'Iceland'
#countries = ['Iceland']; left_bound=0.8; right_bound=None; normalise = 'y'; filename = 'Iceland'
#countries = ['Czechia']; left_bound=time_start; right_bound=None; bottom_bound=0.; top_bound=30.; normalise = 'xy'; filename = 'Czechia'; cycle_linestyle = 1; incr_or_rate = 'incr'; xaxis = 'date'; exp_or_lin = 'lin'

#, 'Netherlands', 'Austria', 'Sweden', 'Denmark', 'Japan', 'Hungary', 'Korea, South', ]
#countries = [ 'Japan']; left_bound=400; right_bound=None
#countries = ['Italy']
#countries = ['Italy', 'Japan', 'Denmark', 'France', 'Germany', 'Spain', 'Switzerland']
#country = 'France' #'Switzerland' #'Netherlands' #'Denmark' # Denmark, Spain, France, Germany, Sweden
#country = 'Korea, South'
#country = ['United Kingdom', 'United Kingdom']

p = PlotSpecs()
p.countries = ['Poland', 'Czechia', 'Slovakia', 'Hungary', 'Romania', 'Serbia', 'Croatia', 'Slovenia', 'Iceland', 'San Marino', 'Italy', 'Spain']; p.left_bound=2; p.right_bound=None; p.bottom_bound=0.; p.top_bound=35.; p.normalise = 'xy'; p.filename = 'Visegrad'; p.cycle_linestyle = 1; p.incr_or_rate = 'rate'; p.xaxis = 'cases'; p.exp_or_lin = 'lin'

p = PlotSpecs()
#p.countries = ['Poland', 'Czechia']; p.left_bound=200; p.right_bound=None; p.bottom_bound=0.; p.top_bound=35.; p.normalise = 'xy'; p.filename = 'Visegrad'; p.cycle_linestyle = 1; p.incr_or_rate = 'rate'; p.xaxis = 'cases'; p.exp_or_lin = 'lin'

p.countries = 'Deutschland'; p.left_bound=900; p.right_bound=None; p.bottom_bound=0.; p.top_bound=27.5; p.normalise = 'xy'; p.filename = 'Deutschland'; p.lang = 'de'; p.cycle_linestyle = 1; p.incr_or_rate = 'rate'; p.xaxis = 'cases'; p.exp_or_lin = 'lin'


#specs_list = [intl0, intl1, intl2, gp0, gp1, gp2, vis0, vis1, vis2]
#specs_list = [deu0, deu1, deu2, deu3]
#specs_list = [dach0, dach1, dach2]
#specs_list = [vis0, vis1, vis2]
#specs_list = [nordic0, nordic1, nordic2]
#specs_list = [intl0d, intl1d, west0d, west1d]
#specs_list = [west2_0d, west2_1d]
#specs_list = [gp0d, gp1d]
#specs_list = [nordic0d, nordic1d]
#specs_list = [vis0d, vis1d]
#specs_list = [intl0, gp0, vis0]
specs_list = [USAGER1d]

### End of user input ###

def call_process_geounit_minimal(df_ts, latest_date, p):
    '''
    This processes one geographical unit.
    df_ts is the time series.
    '''
    case_no = list()
    dif_optim = list() # list of daily increase factors
    #latest_date = None
    df_ts = utils.rm_consecutive_early_zeros(df_ts, 0) #window_length_for_cutoffs-2)
    #print(df_ts)
    if isinstance(p.left_bound, int) or isinstance(p.left_bound, float):
        df_ts = df_ts[(df_ts>p.left_bound).idxmax()-wl_hi*pd.DateOffset():]
    elif p.left_bound is not None:
        df_ts = df_ts[p.left_bound-wl_hi*pd.DateOffset():]
    #print(df_ts)
    if latest_date==None or latest_date<df_ts.index[-1]:
        latest_date = df_ts.index[-1]

    for i in range(window_length_for_cutoffs-len(df_ts), 1):
        #results, model, selected_window_length, e_or_l = process_geounit_minimal(
        #                                        df_ts[:len(df_ts)+i], window_length, exp_or_lin)
        results, model = utils.process_geounit(
                                            df_ts[:len(df_ts)+i], p.window_length, p.exp_or_lin, 'minimal')
        #print(results)
        if p.incr_or_rate == 'incr':
            dif_optim.append(results.iloc[0,0])
        else: # 'rate'
            dif_optim.append(results.iloc[0,1])
        if p.xaxis == 'cases':
            case_no.append(results.iloc[0,3])
        #else: # 'date'
        #    case_no.append(df_ts.index[len(df_ts)+i-1])
    if p.xaxis == 'date':
        case_no = df_ts.index[window_length_for_cutoffs-1:]

    return df_ts, dif_optim, case_no, latest_date, results.iloc[0,9]

def plotting_countries(dif_all, latest_date, p):
    fig, ax1 = plt.subplots(1,1, figsize=(12., 8.))
    #fig, ax1 = plt.subplots(1,1, figsize=(9.6, 6.4))
    space_below = 0.2 # in the case of dates which are rotated
    if p.lang=='de':
        if p.cases=='confirmed':
            case_txt_0 = 'bestätigten COVID-19-Fallzahlen'
            case_txt_0sh = 'Fallzahlen'
            case_txt_0zl = 'den täglichen Zuwachs der Fallzahlen'
            case_txt_0ze = 'den Logarithmus des täglichen Zuwachses der Fallzahlen'
            case_txt_1 = 'Fallzahl'
        elif p.cases=='deaths':
            case_txt_0 = 'COVID-19-Todesfälle'
            case_txt_0sh = 'Todesfälle'
            case_txt_0zl = 'die täglichen neuen Todesfälle'
            case_txt_0ze = 'den Logarithmus der täglichen neuen Todesfälle'
            case_txt_1 = 'Todesfälle'
        '''
        if p.window_length<0:
            ax1.set_title('Lineare Regression auf {0} mit optimaler Fenstergröße.'.format(case_txt_0ze if p.exp_or_lin=='exp' else case_txt_0zl))
        else:
            ax1.set_title('Lineare Regression auf {0} mit Fenstergröße von {1} Datenpunkten.'.format(case_txt_0ze if p.exp_or_lin=='exp' else case_txt_0zl, p.window_length))
        '''
        if p.xaxis == 'cases':
            if p.normalise=='xy':
                ax1.set_xlabel('{0} auf {1} Einwohner'.format(case_txt_1, utils.separated(str(p.normalise_by), p.lang)) if p.normalise=='xy' else case_txt_1)
            else:
                ax1.set_xlabel(case_txt_1)
            '''
            if cases=='confirmed':
                ax1.set_xlabel('{0} auf {1} Einwohner'.format(case_txt_1, utils.separated(str(normalise_by), lang)) if normalise=='xy' else 'Fallzahl')
            elif cases=='deaths':
                ax1.set_xlabel('{0} auf {1} Einwohner'.format(case_txt_1, utils.separated(str(normalise_by), lang)) if normalise=='xy' else 'Todesfälle')
            '''
        #else:
        #    fig.subplots_adjust(bottom=space_below)

        if p.incr_or_rate == 'rate':
            ax1.set_ylabel('Wachstumsrate der {}'.format(case_txt_0sh))
            #fig.suptitle('Tägliche Wachstumsrate der {}, Stand '.format(case_txt_0) + latest_date.strftime('%d.%m.%Y'))
            ax1.set_title('Tägliche Wachstumsrate der {}, Stand '.format(case_txt_0) + latest_date.strftime('%d.%m.%Y'))
        else:
            if p.normalise is None:
                ax1.set_ylabel('Täglicher Zuwachs')
                #fig.suptitle('Täglicher Zuwachs der {}, Stand '.format(case_txt_0) + latest_date.strftime('%d.%m.%Y'))
                ax1.set_title('Täglicher Zuwachs der {}, Stand '.format(case_txt_0) + latest_date.strftime('%d.%m.%Y'))
            else:
                ax1.set_ylabel('Täglicher Zuwachs auf {} Einwohner'.format( utils.separated(str(p.normalise_by), p.lang)))
                #fig.suptitle('Täglicher Zuwachs der {0} auf {1} Einwohner, Stand {2}'.format(case_txt_0, utils.separated(str(p.normalise_by), p.lang), latest_date.strftime('%d.%m.%Y')))
                ax1.set_title('Täglicher Zuwachs der {0} auf {1} Einwohner, Stand {2}'.format(case_txt_0, utils.separated(str(p.normalise_by), p.lang), latest_date.strftime('%d.%m.%Y')))

    else: # i.e. 'en'
        if p.cases=='confirmed':
            case_txt_0 = 'confirmed COVID-19 cases'
            case_txt_0zl = 'daily new cases'
            case_txt_0ze = 'logarithm of daily new cases'
            case_txt_1 = 'cases'
        elif p.cases=='deaths':
            case_txt_0 = 'COVID-19-related deaths'
            case_txt_0zl = 'daily numbers of deaths'
            case_txt_0ze = 'logarithm of daily numbers of deaths'
            case_txt_1 = 'deaths'
        '''
        if p.window_length<0:
            ax1.set_title('Linear regression for the {0} with optimised window length.'.format(case_txt_0ze if p.exp_or_lin=='exp' else case_txt_0zl))
        else:
            ax1.set_title('Linear regression for the {0}. Window length: {1} data points.'.format(case_txt_0ze if p.exp_or_lin=='exp' else case_txt_0zl, p.window_length))
        '''
        if p.xaxis == 'cases':
            if p.cases=='confirmed':
                ax1.set_xlabel('Number of {0} per {1} people'.format(case_txt_1, utils.separated(str(p.normalise_by), p.lang)) if p.normalise=='xy' else 'Number of cases')
            elif p.cases=='deaths':
                ax1.set_xlabel('Number of {0} per {1} people'.format(case_txt_1, utils.separated(str(p.normalise_by), p.lang)) if p.normalise=='xy' else 'Number of deaths')
        #else:
        #    fig.subplots_adjust(bottom=space_below)

        if p.incr_or_rate == 'rate':
            ax1.set_ylabel('Daily growth rate')
            #fig.suptitle('Daily growth rate of number of {} ('.format(case_txt_1) +\
            # latest_date.strftime('%d %B %Y').lstrip('0')+')')
            ax1.set_title('Daily growth rate of the number of {} ('.format(case_txt_0) +\
             latest_date.strftime('%d %B %Y').lstrip('0')+')')
        else:
            if p.normalise is None:
                ax1.set_ylabel('Daily increment')
                #fig.suptitle('Daily increment of number of {} ('.format(case_txt_1) +\
                # latest_date.strftime('%d %B %Y').lstrip('0')+')')
                ax1.set_title('Daily increment of the number of {} ('.format(case_txt_0) +\
                 latest_date.strftime('%d %B %Y').lstrip('0')+')')
            else:
                ax1.set_ylabel('Daily increment per {} people'.format(utils.separated(str(p.normalise_by), p.lang)))
                #fig.suptitle('Daily increment of number of {0} per {1} people ({2})'.format(case_txt_1, utils.separated(str(p.normalise_by), p.lang), latest_date.strftime('%d %B %Y').lstrip('0')))
                ax1.set_title('Daily increment of the number of {0} per {1} people ({2})'.format(case_txt_0, utils.separated(str(p.normalise_by), p.lang), latest_date.strftime('%d %B %Y').lstrip('0')))
    #fig.tight_layout()

    geounit_list = list(dif_all.keys())
    for i in range(len(geounit_list)):
        if p.cycle_linestyle==1:
            ax1.plot(dif_all[geounit_list[i]], label=geounit_list[i], linestyle=['solid', 'dotted', 'dashed', 'dashdot'][i % 4])
        elif p.filename == 'great_powers':
            #ax1.plot(dif_all[geounit_list[i]], label=geounit_list[i], color=['tab:red', 'tab:blue', 'tab:gray'][i % 3])
            ax1.plot(dif_all[geounit_list[i]], label=geounit_list[i], color=['tab:orange', 'tab:blue', 'tab:gray', 'tab:purple', 'tab:green', 'tab:olive'][i % 6])
        else:
            ax1.plot(dif_all[geounit_list[i]], label=geounit_list[i])

    #for tick in ax1.get_yticklabels():
    #    tick = str(tick) + '%'
    if p.xaxis == 'cases':
        #ax1.set_xscale("log")
        ax1.set_xlim(left=p.left_bound, right=p.right_bound)
        ax1.set_xticklabels([float(tick) if float(tick)<1 else utils.separated(str(int(tick)), p.lang) for tick in ax1.get_xticks()])
    else:
        fig.subplots_adjust(bottom=space_below)
        ax1.set_xlim(left=p.left_bound, right=p.right_bound)
        for tick in ax1.get_xticklabels():
            tick.set_rotation(80)

    ax1.set_ylim(bottom=p.bottom_bound, top=p.top_bound)
    if p.incr_or_rate == 'rate':
        ax1.set_yticklabels([str(int(tick)) + '%' for tick in ax1.get_yticks()])
    ax1.legend()
    ax1.grid(True, axis='y')
    #plt.gcf().text(0.905, 0.87, "© Bence Mélykúti, Melykuti.me, 2020", fontsize=8, color='lightgray', rotation=90) # 0.905, 0.37
    #plt.gcf().text(0.905, 0.87, "© Bence Mélykúti, 2020. http://COVID19.Melykuti.Be", fontsize=8, color='lightgray', rotation=90)
    if p.lang=='de':
        plt.gcf().text(0.905, 0.498, "© Bence Mélykúti, 2021. http://COVID19de.Melykuti.Be", fontsize=8, color='lightgray', rotation=90)
    else: # i.e. 'en'
        plt.gcf().text(0.905, 0.515, "© Bence Mélykúti, 2021. http://COVID19.Melykuti.Be", fontsize=8, color='lightgray', rotation=90)
    if p.save_not_show==0:
        plt.show()
    elif p.save_not_show==1:
        imgfile = p.filename + '_DGR_'\
                  + latest_date.strftime('%Y-%m-%d') + '_' \
                  + (p.normalise if p.normalise is not None else '0') + '_' \
                  + str(p.window_length) + '_' + p.exp_or_lin + '_' + p.xaxis + '_' \
                  + p.incr_or_rate + '_' + p.cases + '.png'
        plt.savefig(imgfile)
        plt.close(fig)

if __name__ == '__main__':
    start_time = time.time()
    for p in specs_list:
        if p.window_length > 0: # we'll omit from time series the early part that is not plotted to save computation
            wl_hi = p.window_length
        else:
            wl_hi = 15
        fixed_positive_window_length = 2
        if p.window_length < fixed_positive_window_length:
            if p.window_length <= 0: # run rm_consecutive_early_zeros w. 0, for i in range from wl_lo=4
                window_length_for_cutoffs = 4 #fixed_positive_window_length
            else: # run rm_consecutive_early_zeros w. 0, for i in range from fixed_positive_window_length=2
                p.window_length = fixed_positive_window_length
                window_length_for_cutoffs = fixed_positive_window_length
        else: # run rm_consecutive_early_zeros w. 0, for i in range from window_length
            window_length_for_cutoffs = p.window_length

        dif_all = dict()
        latest_date = None

        if p.countries != 'Deutschland':
            if p.normalise=='xy' or p.normalise=='y':
                pop_world = utils.load_population_world()
            df = utils.open_csvs()
            for country in p.countries:
                print(country)
                #case_no = list()
                #dif_optim = list() # list of daily increase factors
                df_ts = utils.data_preparation(df, country, p.cases)
                #print(df_ts)
                if not isinstance(country, str): # If it's a province or state of a country or region.
                    country = country[0]
                if p.normalise=='xy':
                    if country=='Hubei': #'China':
                        df_ts = p.normalise_by*df_ts/58500000 # Population of Hubei province
                    else:
                        df_ts = p.normalise_by*df_ts/pop_world[country]
                #print(df_ts)
                df_ts, dif_optim, case_no, latest_date, e_or_l = call_process_geounit_minimal(
                    df_ts, latest_date, p)
                dif_all[country] = pd.Series(dif_optim, index=case_no)
                if p.normalise == 'y' and p.incr_or_rate=='incr':
                    dif_all[country] = p.normalise_by*dif_all[country]/pop_world[country]
                #print(dif_optim)
                #dif_all[country] = pd.Series(dif_optim, index=case_no, name=country)
                #dif_all[country] = pd.Series(dif_optim, index=case_no)

        else:
            #lang = 'de'
            from DEU import data_preparation_DEU
            if p.normalise=='xy' or p.normalise=='y':
                pop_DEU = utils.load_population_DEU()
            allowed_values = \
                ['Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen',
                'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen',
                'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen',
                'Sachsen-Anhalt', 'Schleswig-Holstein', 'Thüringen',
                'Deutschland',
                'alle']
            figures_diff = data_preparation_DEU(p.cases)
            if p.normalise=='xy':
                for j in figures_diff.columns:
                    figures_diff[j] = p.normalise_by*figures_diff[j]/pop_DEU[j]
            # For sensitivity analysis, enter fake values here
            #figures_diff['Baden-Württemberg'][-2] = 2800 # test
            #figures_diff['Baden-Württemberg'][-1] = 3000 # test
            for j in range(0, figures_diff.shape[1]):
            #for j in [0, 1, 2, 16]:
                print(allowed_values[j])
                #case_no = list()
                #dif_optim = list() # list of daily increase factors
                df_ts = figures_diff.iloc[:,j]
                df_ts, dif_optim, case_no, latest_date, e_or_l = call_process_geounit_minimal(
                    df_ts, latest_date, p)
                dif_all[allowed_values[j]] = pd.Series(dif_optim, index=case_no)
                if p.normalise == 'y' and p.incr_or_rate=='incr':
                    dif_all[allowed_values[j]] = normalise_by*dif_all[allowed_values[j]]/pop_DEU[j]
        
        #print(df_ts)
        #print(dif_ts)
        print(dif_all)

        if p.save_not_show in [0, 1]:
            plotting_countries(dif_all, latest_date, p)
    print('Time elapsed: {:.2f} sec'.format(time.time() - start_time))
