## Analysis of the spread of the SARS-CoV-2 coronavirus

> * Recall that on this page I examine the number of currently infected patients and not the cumulative number of all who have been infected and might have recovered or died.
> * If you already know my methodology, just skip down to the Plots and the Results sections.

13 March 2020 (updated on 4 March 2021), Freiburg i. Br., Germany – The WHO releases [weekly situation reports](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports) with the numbers of diagnosed COVID-19 cases for each country. We can see the total number of confirmed cases and the total deaths since the beginning of the outbreak. We also get the changes from the last report, that is, these two figures for the last day only.

Thinking in terms of the classical SIR model of epidemiology, the population comprises three groups: **S**usceptibles, **I**nfected and **R**emoved. _Removed_ are those who have recovered from or died of the disease and thereby are no longer infectious and can no longer catch the disease. _Infected_ are the current patients who are also all infectious. _Susceptibles_ are everybody else: people who have not been infected yet (and hopefully will never be).

### Data

The Center for Systems Science and Engineering at the Johns Hopkins University is kindly providing [the time series data with daily sampling frequency in tabular format](https://github.com/CSSEGISandData).

Remember that the true number of cases is probably multiple times higher than the number of confirmed cases. For an extreme example, on the 27th March 2020, Scotland’s Chief Medical Officer Catherine Calderwood [estimated that more than 65,000 people in Scotland had the virus](https://www.bbc.com/news/live/world-52058788) when confirmed cases stood at 1059. On the 26th November, [according to the claims of Prof Béla Merkely, the head of Semmelweis University, Budapest](https://hvg.hu/itthon/20201126_Merkely_Bela_felepult_es_ujra_gyogyit), we can put the ratio of infected people to the number of registered infections in Hungary to eight.

### Program files

* **download_JHU_CSSE.py** is a script to download three csv data tables: the number of confirmed cases, the number of deaths due to the disease, and the number of recovered patients, broken down to countries. The script automatically inserts the timestamp of download into the file names so that later downloads do not overwrite downloaded data.

* **utils.py** contains the universal data selection, preprocessing, analysis and plotting functionalities. It searches for the most recent download of `download_JHU_CSSE.py` in the current directory based on the timestamp in the file name. If you want to select a particular one, then modify the variable `timestamp` in `open_csvs()`.

* **analysis_single.py** runs the analysis and plots or saves a graph for a single country.

* **analysis_joint.py** calls the analysis and optionally saves plots repeatedly on a list of countries.

### Analysis

I compute the number of currently infectious people as the number of total confirmed cases minus the number of deaths minus the number of recovered patients for all days where there is data:

`no. of currently infected = no. of cases - no. of deaths - no. of recovered.`

It has to be said that the number of recoveries is the least reliable time series for each country. For some, it is clearly so inaccurate that I had to omit the country from this analysis.

(On 24 March 2020, I reported the total number of confirmed cases for each country because the number of recoveries was not included in the JHU CSSE dataset.)

#### Exponential and linear growth models for cumulative case numbers

Originally, my analysis was founded on the assumption that the growth of this number is exponential. In this case, I took the base&nbsp;2 logarithm of this time series for a selected country, and fitted a straight line to the last 4-14 days of data with _ordinary least squares (OLS)_. If the growth is exponential or thereabouts, then this should fit quite well and the slope of this line will tell us the growth rate. The length of this time window is optimised to provide the best linear fit.

As long as I was fitting exponential models, the interpretation could only be that growth was exponential. Towards the end of March and beginning of April, this no longer held for many countries. Once the daily new case number starts to stabilise, it is natural to fit a linear model. The procedure is the same but I fit to the case numbers and not to their logarithms.

The first dataset is the 30 March 2020 where I tried fitting linear models in addition to the exponentials as well. I had originally presented exponential fits exclusively. Upon the switchover to the new methodology, I also showed the fits where I selected the best of exponential and linear fits for comparison. The last column in the table now displays `e` for the case when the exponential model is a better fit, `l` when the linear model.

Since 9 May 2020, I have been using 7-14-day windows instead of 4-14 days. I decided that it was better to dampen the effect of weekends on visits to the doctor, on laboratory testing and on reporting daily increments by choosing longer time windows.

#### Exponential and linear model fits for daily new case numbers

The COVID-19 pandemic has been a forced learning process for all of us. I learnt to appreciate that fitting curves to the daily new cases is much preferable to fitting to cumulative numbers. The cumulative numbers exhibit strong dependency (autocorrelation) and any fit will appear much better than it really is. By moving to fitting to daily changes, I get more meaningful uncertainties for my fits. Here are [two](https://thelancet.com/journals/lancet/article/PIIS0140-6736(03)13335-1/fulltext) [publications](https://royalsocietypublishing.org/doi/full/10.1098/rspb.2015.0347) that explain this. My new code was ready for the 1 May 2020 but for comparison, I ran it also for the last report done with the old one on 23 April.

From this fit I compute:

1. The daily change in the number of cases. It would be easy to report the change of cumulative numbers between the last and the penultimate days but I derive this value from my fit. You can interpret the fitting process as a smoothing over the last several days.

2. How many days it takes for the number of infectious people to double, i.e. starting today to produce the current cumulative number of cases once more. This is also computed from the fit by an integral. It is to note that even if the current growth rate is positive, the fit might be such that it is dropping sufficiently fast that under the projection implied by the fit, the new cases will never reach the current cumulative case number. In this case, the doubling time is reported as infinity.

3. The growth factor per day, which I express in percentage terms. (What percentage more infectious people we expect tomorrow than we had today.) This is computed from the doubling time, if it is finite, by assuming uniform geometric progression. Here, like for the daily change in the number of cases, I use the fit and not the trivial operation from the raw data as the latter is bound to be very noisy. If the doubling time is estimated to be infinity, then I divide the daily change in the number of cases (as computed in Point&nbsp;1.) by the arithmetic mean of the last two cumulative case numbers.

4. I make a crude estimate of what I guess the total number of infected people might currently be.

The third one is only my guesswork. The idea is that in the case of a SARS-CoV-2 infection, it takes on average 5-6 days to develop symptoms (fever, a usually dry cough, loss of smell or taste, and others). This incubation time varies between 1 to 14 days. The people who were infected today will present symptoms and will be tested perhaps 4-6 days from now. They will enter the figure in the situation report only thereafter. Also, they are likely to be already infectious sooner than that and that is what worries us as ordinary people.

So I project from my curve fit the number of infected four, respectively, six days from the latest data point, and that is the estimate for the current total case number. This is probably too conservative and may be a low estimate not only because many cases never get tested and recorded but also because from developing symptoms, one still needs perhaps 1-5 days to get tested and for the test result to enter the international statistical tables. There are also wide differences between how much testing different countries do; low testing intensity is bound to bias the confirmed case number downwards.


There are two columns of the table that I use to compare the exponential and linear models and to compare different window lengths:

5. The [R^2 or coefficient of determination](https://en.wikipedia.org/wiki/Coefficient_of_determination) of the linear regression fit (which I can't explain here). The closer it is to 1, the better the match is between the data and my linear regression. This is straightforward for both the exponential and the linear models, it is just so that for the exponential model, the linear fit happens for the logarithm of the time series. Very clearly, this value dropped by a great amount at the switch to fitting to daily increments from fitting to cumulative numbers on 1 May 2020. See the comparison for the data on 23 April.

6. I also compute the difference between the change in cumulative numbers over the time window implied by the model fit and the real change in the data over the same time window, normalised by the latter, the real change in the data.  
You can also see it as the ratio of the change in cumulative numbers over the time window from the model fit and of the change in cumulative numbers over the time window from the real data, minus&nbsp;1.  
If the total number is increasing, then this number is positive if the fit overestimates the actual increase and negative, if the fit underestimates it.  
If we study active cases and their number is decreasing, then the denominator is negative. In this case, if the fit overestimates the absolute rate of decrease (it is a negative number which is smaller than the real data), then this indicator is positive. If the fit underestimates the absolute rate of decrease, then this number is negative.  
For example, if the spread of the disease is slowing relative to the fitted curve, then this number will be great and the projection in Point&nbsp;4. is definitely unreliable. If this difference is small, then the projection might well be good. When the difference is negative, then the projection will be an underestimate of the true case number!

The automatic selection of the window length minimises the l_2 norm of the two-dimensional vector  
`(10 * (1-R^2), normalised difference between projected and realised changes in cases over the time window).`  
So I minimise both 1-R^2 and the normalised difference between change for the fitted line and change in the real data (over the selected time window). The factor of 10 is there to weigh one relative to the other. So R^2=0.99 gives first coordinate 10*0.01 = 0.1, and to get the same second coordinate of 0.1, you'd have a difference of 10% between curve fit and actual data for the change over the time window. This is how the two errors trade off in my window length selection.

To choose between the exponential and the linear models, once I have selected the optimal window size independently for each, I choose the model where this l_2 norm is smaller.

Even when the daily increments have stabilised and the spread of the COVID-19 pandemic is clearly only linear, it can happen that both the exponential and the linear models fit well in the time window and the optimisation selects the exponential as the slightly better one. Therefore one should not attribute too much importance to preference for the exponential model over the linear one.

I show projections for the number of infected 4-to-6 days from now (which, as I said, is what I guess to be the real number of cumulative coronavirus cases today) only if (the R^2 is greater than or equal to 0.75 and the above normalised difference is not greater than 0.5) or if the normalised difference is in [-0.3;&nbsp; 0.3]. (Before switching the fit to the daily new cases from cumulative numbers, the condition was: (the R^2 was greater than or equal to 0.95 and an earlier difference was not greater than 0.5) or if the earlier difference was in [-0.2;&nbsp; 0.1]).) Since 15 April 2020, I have omitted the projections also when active case numbers are decreasing.

### Plots

Since 1 May 2020, when I started fitting curves to daily changes instead of cumulative numbers, I have been displaying the daily change for each individual country on the left panel, together with the fitted curve.

On the right panel, the plots present the observed total number of currently infected. These lines are in blue.

If the linear model fits better, then pink is the linear fit, which is the same as the fit of a straight line on natural scale on the left panel. If the exponential model fits better, then orange is the fit of the exponential curve, which is the same as the fit of a straight line on logarithmic y-scale (not actually shown) for the data on the left panel.

![Italy](https://github.com/Melykuti/COVID-19/blob/master/plots/Italy_2021-03-03.png)

![Russia](https://github.com/Melykuti/COVID-19/blob/master/plots/Russia_2021-03-03.png)

![Switzerland](https://github.com/Melykuti/COVID-19/blob/master/plots/Switzerland_2021-03-03.png)

![Iran](https://github.com/Melykuti/COVID-19/blob/master/plots/Iran_2021-03-03.png)

![India](https://github.com/Melykuti/COVID-19/blob/master/plots/India_2021-03-03.png)

![Czechia](https://github.com/Melykuti/COVID-19/blob/master/plots/Czechia_2021-03-03.png)

![Argentina](https://github.com/Melykuti/COVID-19/blob/master/plots/Argentina_2021-03-03.png)

![Germany](https://github.com/Melykuti/COVID-19/blob/master/plots/Germany_2021-03-03.png)

![Hungary](https://github.com/Melykuti/COVID-19/blob/master/plots/Hungary_2021-03-03.png)

![Portugal](https://github.com/Melykuti/COVID-19/blob/master/plots/Portugal_2021-03-03.png)

![Peru](https://github.com/Melykuti/COVID-19/blob/master/plots/Peru_2021-03-03.png)

![Israel](https://github.com/Melykuti/COVID-19/blob/master/plots/Israel_2021-03-03.png)

![Bulgaria](https://github.com/Melykuti/COVID-19/blob/master/plots/Bulgaria_2021-03-03.png)

![Chile](https://github.com/Melykuti/COVID-19/blob/master/plots/Chile_2021-03-03.png)

![Austria](https://github.com/Melykuti/COVID-19/blob/master/plots/Austria_2021-03-03.png)

![Japan](https://github.com/Melykuti/COVID-19/blob/master/plots/Japan_2021-03-03.png)

![Belarus](https://github.com/Melykuti/COVID-19/blob/master/plots/Belarus_2021-03-03.png)

![South Korea](https://github.com/Melykuti/COVID-19/blob/master/plots/Korea__South_2021-03-03.png)

![Denmark](https://github.com/Melykuti/COVID-19/blob/master/plots/Denmark_2021-03-03.png)

![Australia](https://github.com/Melykuti/COVID-19/blob/master/plots/Australia_2021-03-03.png)

![Saudi Arabia](https://github.com/Melykuti/COVID-19/blob/master/plots/Saudi_Arabia_2021-03-03.png)

![China](https://github.com/Melykuti/COVID-19/blob/master/plots/China_2021-03-03.png)

![Singapore](https://github.com/Melykuti/COVID-19/blob/master/plots/Singapore_2021-03-03.png)

![New Zealand](https://github.com/Melykuti/COVID-19/blob/master/plots/New_Zealand_2021-03-03.png)



### Results

The columns have the following meaning:

* (Since 15 April 2020) The number of currently infected people changes daily by this number right now. This is computed from the model fit and not from the last two data points.

* (Since 15 April 2020) The number of currently infected people per 100,000 population changes daily by this number right now. This is computed from the model fit and not from the last two data points.

* The number of currently infected people increases daily by this percentage

* Time it takes for the number of currently infected people to double

* Latest reported total number of currently infected cases

* (Since 30 March 2020) Latest reported total number of currently infected cases per 100,000 population

* My estimate for total number of currently infected cases at present. (Since 30 March 2020, per 100,000 population. I describe at the end of the Analysis why it is missing in certain cases.)

* R^2 of linear regression fit

* Normalised difference between change in active cases over the selected time window between curve fit and real data

* (Since 18 March 2020) The number of days in the time window in which I fit the linear regression. It is automatically optimised to minimise the vector (10 * (1-R^2), normalised difference) in l_2.

* (Since 11 April 2020) e if the exponential model, l if the linear model provides the better fit and yielded the entries in the specific row of the table.

I focus on countries with a large number of cases and on those to which I have got some personal connection. China and South Korea are examples where the preventative measures have slowed down the epidemic spread massively. The USA, the United Kingdom, the Netherlands, Belgium and Sweden do not currently report the number of recovered patients. For this reason, when I noticed this, I stopped including them in the analysis. Spain also seems to have stopped recording and incrementing the number of recovered patients. (Which means that I expect the real number of active cases in those countries to be much lower than what the numbers below show.)

&nbsp;

    Country              Increment Incr. Growth   Doubling  Active     per      Estimate   R^2  Diff. Win- Exp/Lin
                                    per   rate      time     Cases   100,000                          dow
                                  100,000                                                             size

4 March 2021

    Italy                     8458   14   2.9%    24.5 days  437421    701     [765, 804] 0.54 -0.15  14  l
    Russia                   -4278 -3.0  -1.3%     nan days  334479    236                0.17 -0.08  10  l
    Switzerland               1313   16   1.2%    56.1 days  232231   2763   [2835, 2879] 0.06  0.02   7  l
    Iran                      1677  2.0   1.7%    40.2 days  182629    215     [224, 230] 0.56 -0.02   7  l
    India                     1831  0.1   1.1%     inf days  173413     13       [13, 13] 0.35  0.07   8  l
    Czechia                   2417   23   1.6%     inf days  154580   1444   [1496, 1497] 0.29  0.08   8  l
    Argentina                 -310 -0.7  -0.2%     nan days  152489    335                0.08  0.20   9  l
    Germany                  -3614 -4.5  -3.2%     nan days  114900    143                0.14 -0.93   7  l
    Hungary                   2801   29   3.8%    18.7 days   98361   1007   [1143, 1227] 0.40 -0.07  10  l
    Portugal                 -1238  -12  -1.9%     nan days   64797    629                0.27  0.02  14  l
    Peru                     -2531 -7.9  -5.0%     nan days   47374    148                0.18 -1.61  14  l
    Israel                    1587   18   6.1%    11.8 days   42741    493                0.41  0.59  14  l
    Bulgaria                   342  4.9   1.0%     inf days   33770    485     [495, 495] 0.16  0.06  10  l
    Chile                     -281 -1.5  -1.2%     nan days   24320    134                0.38  0.37   7  l
    Austria                    206  2.3   1.0%     inf days   21028    237     [240, 240] 0.25  0.17   7  l
    Japan                     -337 -0.3  -2.5%     nan days   13698     11                0.38  0.04  14  l
    Belarus                     64  0.7   3.8%    18.7 days    7679     81                0.18  0.30   8  l
    Korea, South                58  0.1   3.0%    23.4 days    7459     14                0.53  0.47  10  l
    Denmark                     87  1.5   1.2%     inf days    6995    119     [124, 125] 0.47 -0.01   7  e
    Australia                  7.4  0.0   0.7%   101.2 days    5178     20       [20, 21] 0.36 -0.22   9  l
    Saudi Arabia               -23 -0.1  -0.9%     nan days    2546    7.5                0.46  3.84   8  l
    China                      7.6  0.0   7.9%     9.1 days     449   0.03                0.44  0.86   8  l
    Singapore                   11  0.2  14.4%     5.1 days     101    1.6                0.64 -0.94   7  l
    New Zealand              -0.36 -0.0  -0.6%     nan days      68    1.4                0.12  0.10  11  l

5 February 2021

    Russia                   -6780 -4.8  -1.5%     nan days  448105    316                0.09  0.06   7  l
    Italy                    -5321 -8.5  -1.2%     nan days  430277    690                0.08  0.01   7  l
    Switzerland               1308   16   0.6%     inf days  203133   2417   [2469, 2487] 0.08  0.15  11  l
    Germany                 -34890  -44 -18.7%     nan days  184599    230                0.40 -3.34   8  l
    Portugal                 -6769  -66  -4.2%     nan days  161442   1567                0.54 -0.54   9  l
    Argentina                  657  1.4   3.0%    23.2 days  158230    348     [363, 378] 0.28 -0.05   7  l
    Iran                       546  0.6   1.8%    39.7 days  151489    178     [183, 186] 0.37  0.20   7  l
    India                    -4589 -0.3  -3.0%     nan days  151460     11                0.47 -0.06   7  l
    Czechia                    543  5.1   3.3%    21.4 days   94519    883     [930, 974] 0.18  0.22  14  l
    Hungary                  -1199  -12  -1.4%     nan days   84848    868                0.31  0.15   7  l
    Israel                    3977   46   7.3%     9.8 days   81129    935                0.28 -0.40   9  l
    Peru                      -832 -2.6  -1.7%     nan days   47670    149                0.09  2.62   8  l
    Japan                    -2031 -1.6  -4.5%     nan days   44144     35                0.05  0.20  10  l
    Chile                    -1142 -6.3  -4.9%     nan days   23258    128                0.45 -0.34   8  l
    Bulgaria                  -287 -4.1  -1.4%     nan days   20545    295                0.44 -0.02   7  l
    Austria                     78  0.9   3.7%    19.2 days   13955    158     [167, 177] 0.41  0.18   7  l
    Belarus                    -93 -1.0  -0.9%     nan days   10508    111                0.20  0.13   9  l
    Korea, South               8.8  0.0   3.8%    18.8 days    8555     17       [17, 18] 0.54  0.06   7  l
    Denmark                   -282 -4.8  -3.6%     nan days    7602    130                0.51  0.06  10  l
    Saudi Arabia                12  0.0   2.3%    31.1 days    2162    6.3                0.14 -1.61   7  l
    China                     -168 -0.0  -8.2%     nan days    1987   0.14                0.73 -0.19  13  l
    Australia                  2.9  0.0   1.2%    58.7 days    1853    7.3                0.45  1.25  10  l
    Singapore                 -8.1 -0.1  -3.2%     nan days     247    4.0                0.17  2.16  12  l
    New Zealand               -2.7 -0.1  -4.5%     nan days      62    1.3                0.16 -0.61  10  l

28 January 2021

    Russia                   -7466 -5.3  -1.5%     nan days  495351    350                0.37 -0.08  11  l
    Italy                    -4326 -6.9  -0.9%     nan days  477969    766                0.23  0.07   9  l
    Switzerland               1504   18   0.8%     inf days  190845   2271   [2328, 2346] 0.10  0.14  10  l
    India                    -1727 -0.1  -1.0%     nan days  173740     13                0.22  0.15  10  l
    Portugal                  1107   11   0.7%     inf days  172893   1678   [1684, 1684] 0.43  0.11   8  l
    Argentina                  713  1.6   2.9%    24.2 days  166055    365     [380, 395] 0.18 -0.02   7  l
    Iran                       278  0.3   1.9%    37.5 days  151200    178     [181, 184] 0.86  0.19   7  l
    Hungary                  -1068  -11  -1.0%     nan days  103087   1055                0.24 -0.06   8  l
    Czechia                  -1223  -11  -1.2%     nan days   98846    924                0.80  0.15   9  l
    Germany                 -69976  -87 -45.2%     nan days   81408    102                0.42 -0.16   8  l
    Israel                     619  7.1   4.9%    14.6 days   74870    863    [948, 1034] 0.08  0.15   7  l
    Japan                    -3241 -2.6  -5.0%     nan days   63086     50                0.42 -0.25  14  l
    Peru                     -3363  -11  -8.1%     nan days   39012    122                0.13 -1.29   8  l
    Bulgaria                  1470   21  11.1%     6.6 days   26448    380     [553, 706] 0.78  0.38  10  l
    Chile                    -1173 -6.4  -4.6%     nan days   25049    138                0.79 -3.42   7  l
    Austria                    -46 -0.5  -0.3%     nan days   14866    168                0.30  0.13  13  l
    Belarus                   -125 -1.3  -1.0%     nan days   12387    131                0.13  0.09   8  l
    Denmark                   -340 -5.8  -3.0%     nan days   10843    185                0.57  0.17   9  l
    Korea, South              -377 -0.7  -4.0%     nan days    9524     18                0.02 -0.03  12  l
    China                      -23 -0.0  -0.8%     nan days    2768   0.20                0.43  0.22   8  l
    Saudi Arabia               -11 -0.0  -0.5%     nan days    2115    6.2                0.50  0.33   9  l
    Australia                 -7.6 -0.0  -0.4%     nan days    1854    7.3                0.66 -0.30  13  l
    Singapore                   10  0.2   6.4%    11.2 days     258    4.2                0.21 -1.55  11  l
    New Zealand               -3.1 -0.1  -4.6%     nan days      69    1.4                0.12 -1.93  14  l

17 January 2021

    Italy                    -4128 -6.6  -0.7%     nan days  557717    894                0.25 -0.26  10  l
    Russia                   -4600 -3.2  -0.9%     nan days  537095    379                0.75 -0.27  14  l
    Germany                   5256  6.6   5.7%    12.4 days  311702    389                0.61  1.60   7  l
    India                     -575 -0.0  -0.3%     nan days  208826     16                0.16  0.46  13  l
    Argentina                 -515 -1.1  -0.3%     nan days  173580    382                0.52  0.14  12  l
    Switzerland                872   10   0.5%     inf days  168953   2010   [2022, 2022] 0.33  0.19  13  l
    Iran                      1031  1.2   3.1%    22.8 days  154454    182     [191, 200] 0.79  0.34  11  l
    Czechia                  -3204  -30  -2.2%     nan days  149847   1400                0.31  0.24  10  l
    Hungary                  -2311  -24  -2.1%     nan days  111998   1146                0.38 -0.02   7  l
    Israel                    2929   34   4.4%    15.9 days   83842    966   [1128, 1230] 0.05 -0.24   7  l
    Japan                     1567  1.2   2.1%     inf days   76864     61       [65, 67] 0.86  0.03  10  e
    Bulgaria                 -3286  -47  -7.0%     nan days   46936    674                0.23 -0.04  14  l
    Peru                      3813   12  10.0%     7.3 days   39297    123                0.15 -0.31  14  l
    Chile                      329  1.8   1.3%     inf days   25737    142     [144, 144] 0.23  0.09  10  l
    Denmark                   -743  -13  -3.7%     nan days   20085    342                0.12  0.05   7  l
    Austria                   -744 -8.4  -4.1%     nan days   17673    199                0.44 -0.23  11  l
    Belarus                   -321 -3.4  -2.1%     nan days   15288    161                0.21 -0.55  14  l
    Korea, South               -89 -0.2  -0.7%     nan days   12838     25                0.56  0.42   7  l
    Saudi Arabia              -2.8 -0.0  -0.1%     nan days    1894    5.5                0.57  0.13  14  l
    Australia                -0.07 -0.0  -0.0%     nan days    1886    7.4                0.33  0.30  10  l
    China                      114  0.0   6.9%    10.4 days    1820   0.13         [0, 0] 0.88 -0.13  12  l
    Singapore                   12  0.2   6.2%    11.5 days     270    4.3         [5, 6] 0.20 -0.16   8  l
    New Zealand                5.4  0.1   9.7%     7.5 days      82    1.7         [2, 3] 0.13  0.20   7  l

7 January 2021

    Italy                    -3480 -5.6  -0.6%     nan days  568712    911                0.57 -4.13   7  l
    Russia                    2894  2.0   1.7%    42.2 days  557484    393                0.16 -0.34   8  l
    Germany                 -12270  -15  -4.0%     nan days  307211    383                0.10 -0.47   8  l
    India                    -3610 -0.3  -1.6%     nan days  228083     17                0.05  0.09  10  l
    Iran                     -3485 -4.1  -2.1%     nan days  165552    195                0.12  0.07   7  l
    Argentina                 4629   10   4.5%    15.8 days  158147    348                0.09 -0.62  12  l
    Switzerland               5189   62   4.9%    14.5 days  145080   1726   [2037, 2239] 0.16  0.06   7  l
    Hungary                  -2100  -21  -1.5%     nan days  142029   1453                0.28 -0.02   7  l
    Czechia                   1102   10   0.9%     inf days  126348   1181   [1188, 1188] 0.16  0.23   8  l
    Bulgaria                 -1225  -18  -1.7%     nan days   69642   1000                0.66 -0.11   7  l
    Israel                    3804   44   6.3%    11.3 days   61551    709    [911, 1032] 0.25 -0.13  11  l
    Japan                     1836  1.5   4.1%    17.2 days   49029     39       [46, 50] 0.26 -0.06  11  l
    Denmark                   -579 -9.9  -2.0%     nan days   28690    489                0.54  0.15   7  l
    Peru                     -1572 -4.9  -7.4%     nan days   21527     67                0.16 -0.99   7  l
    Austria                    288  3.2   4.3%    16.4 days   20691    234     [257, 277] 0.25  0.27  12  l
    Korea, South               -97 -0.2  -0.5%     nan days   17991     35                0.30  0.20  14  l
    Chile                       45  0.2   0.3%     inf days   17586     97       [97, 97] 0.22  0.21   8  l
    Belarus                    655  6.9   8.4%     8.6 days   17084    180                0.61  1.67   7  l
    Saudi Arabia               -79 -0.2  -3.6%     nan days    2206    6.5                0.27 -0.06  14  l
    Australia                  2.4  0.0   0.1%     inf days    1827    7.2         [7, 7] 0.83 -0.02   7  e
    China                      4.8  0.0   3.5%    20.4 days    1210   0.09         [0, 0] 0.32  0.17   9  l
    Singapore                   16  0.3   8.3%     8.7 days     210    3.4         [5, 5] 0.30 -0.14  13  l
    New Zealand               -1.9 -0.0  -3.1%     nan days      62    1.3                0.10  0.62   8  l

20 December 2020

    Italy                   -11264  -18  -1.8%     nan days  620166    994                0.14 -0.03   9  l
    Russia                    -147 -0.1  -0.0%     nan days  509811    360                0.47  0.30   7  l
    Germany                  14486   18   6.1%    11.6 days  375232    468     [571, 645] 0.41 -0.15   7  l
    India                    -5567 -0.4  -1.8%     nan days  305344     23                0.14 -0.07   7  l
    Iran                     -4409 -5.2  -2.0%     nan days  222681    262                0.48 -0.08  14  l
    Hungary                    -39 -0.4  -0.0%     nan days  198785   2034                0.81  0.11  10  l
    Argentina                 2498  5.5   3.4%    20.9 days  132789    292                0.60 -0.69  14  l
    Bulgaria                 -1028  -15  -1.2%     nan days   86452   1241                0.16 -0.13  12  l
    Switzerland               4061   48   7.2%    10.0 days   85887   1022   [1301, 1505] 0.22 -0.14   7  l
    Czechia                   3736   35   6.5%    11.1 days   76943    719    [902, 1026] 0.47 -0.01   7  l
    Denmark                   2257   38   5.8%    12.4 days   41017    699     [872, 975] 0.44 -0.07  14  e
    Austria                  -1112  -13  -3.5%     nan days   31389    354                0.52 -0.04   7  l
    Japan                      242  0.2   0.8%     inf days   30914     25       [25, 25] 0.18  0.15  11  l
    Israel                    1593   18   7.7%     9.3 days   24222    279     [372, 434] 0.34 -0.21   7  l
    Peru                     -2386 -7.5 -10.2%     nan days   22189     70                0.16 -0.14   7  l
    Belarus                     44  0.5   1.8%    38.6 days   20910    221                0.07  1.36  11  l
    Korea, South               787  1.5   7.3%     9.8 days   14269     28       [35, 41] 0.55 -0.10  13  e
    Chile                      538  3.0   5.7%    12.5 days   12921     71       [86, 97] 0.16 -0.12   8  l
    Saudi Arabia               -12 -0.0  -0.4%     nan days    3014    8.8                0.64  0.10  10  l
    Australia                   34  0.1   4.0%    17.7 days    1556    6.1         [7, 7] 0.81 -0.09   7  l
    China                      -14 -0.0  -0.9%     nan days    1524   0.11                0.29  1.40  14  l
    Singapore                  6.0  0.1   8.6%     8.4 days     100    1.6                0.19 -0.34   7  l
    New Zealand                3.4  0.1  10.1%     7.2 days      55    1.1         [2, 2] 0.16 -0.14   7  l

5 December 2020

    US                      142256   43   3.8%    18.6 days 8618141   2591   [2805, 2953] 0.77 -0.05   7  e
    France                    8280   12   0.4%     inf days 2067279   3047   [3092, 3112] 0.07  0.04  10  l
    Italy                    -9001  -14  -1.2%     nan days  757702   1214                0.28 -0.47  14  l
    Russia                   -1897 -1.3  -0.4%     nan days  468068    330                0.28 -0.20   7  l
    India                   -10361 -0.8  -2.5%     nan days  409689     31                0.70 -0.25  11  l
    Germany                  -3678 -4.6  -1.2%     nan days  307002    383                0.21 -1.95  10  l
    Iran                      2681  3.2   1.0%     inf days  259034    305     [315, 317] 0.57  0.04  11  l
    Hungary                   3963   41   3.0%    23.5 days  164018   1678   [1862, 1969] 0.07 -0.09   9  l
    Argentina                 1048  2.3   2.6%    27.1 days  133164    293     [307, 318] 0.33  0.15  14  l
    Bulgaria                  1087   16   2.3%    31.0 days   94480   1356   [1433, 1483] 0.43 -0.01   7  l
    Switzerland               1293   15   6.5%    11.1 days   78604    935   [1097, 1253] 0.08 -0.14   7  l
    Czechia                   1020  9.5   8.6%     8.4 days   59674    558                0.35  1.33   7  l
    Austria                  -1494  -17  -2.9%     nan days   49819    562                0.36  0.06   7  l
    Peru                     -3222  -10 -11.0%     nan days   27041     85                0.45 -0.64   8  l
    Japan                      900  0.7   5.9%    12.0 days   25157     20       [24, 27] 0.03 -0.02   7  l
    Belarus                     92  1.0   0.4%     inf days   21622    228     [230, 230] 0.08  0.21  12  l
    Denmark                    295  5.0   2.4%    29.8 days   17244    294     [317, 330] 0.14 -0.05  10  l
    Israel                     377  4.3   3.7%    19.1 days   12043    139     [159, 170] 0.18 -0.09  14  l
    Chile                      253  1.4   5.2%    13.8 days   10034     55                0.14  1.63   7  l
    Korea, South               307  0.6   4.1%    17.4 days    7458     14       [17, 18] 0.27 -0.03   8  e
    Saudi Arabia              -106 -0.3  -2.5%     nan days    4158     12                0.60  0.04  14  l
    Australia                  5.1  0.0   1.6%    44.8 days    1414    5.6                0.21 -0.85   9  l
    China                       73  0.0   4.3%    16.3 days    1398   0.10         [0, 0] 0.17 -0.04  14  e
    Singapore                  2.2  0.0   7.4%     9.7 days      61   0.98                0.24  0.35  10  l
    New Zealand               -5.1 -0.1  -8.5%     nan days      59    1.2                0.66 -0.87   9  l


23 November 2020

    US                      139814   42   2.9%    24.3 days 7463554   2244   [2433, 2545] 0.49 -0.05   7  e
    France                   15979   24   0.8%     inf days 1962709   2893   [2971, 2997] 0.27  0.04  12  l
    Italy                    11821   19   1.5%     inf days  805947   1292   [1353, 1373] 0.35  0.03  12  l
    Russia                    -482 -0.3  -0.1%     nan days  453252    320                0.23  0.28  14  l
    India                     3531  0.3   3.9%    18.2 days  443486     33       [36, 38] 0.86  0.42   8  l
    Germany                  -1702 -2.1  -0.5%     nan days  306581    382                0.38  0.36  13  l
    Iran                      5607  6.6   2.8%     inf days  206114    243     [267, 278] 0.41  0.00   7  e
    Argentina                -2613 -5.7  -1.9%     nan days  137872    303                0.18  0.51   7  l
    Hungary                   1660   17   1.3%     inf days  127903   1309   [1338, 1338] 0.79  0.05   7  l
    Switzerland              -1785  -21  -1.7%     nan days  105845   1259                0.01 -0.96  10  l
    Czechia                  -1648  -15  -1.9%     nan days   86966    813                0.92  0.10   7  l
    Bulgaria                   657  9.4   0.8%     inf days   82416   1183   [1204, 1208] 0.60 -0.07   7  e
    Austria                  -1365  -15  -1.8%     nan days   75540    853                0.51  0.17  12  l
    Peru                     -1427 -4.5  -4.0%     nan days   33093    104                0.05 -0.34  12  l
    Japan                     2967  2.4  19.2%     3.9 days   20818     17                0.38 -1.57   7  l
    Belarus                    -49 -0.5  -0.3%     nan days   19055    201                0.75  0.34   7  l
    Denmark                    202  3.4   2.8%    25.1 days   14427    246                0.42 -0.40  12  l
    Chile                      101  0.6   4.0%    17.8 days    9450     52       [56, 60] 0.10  0.16   7  l
    Israel                    -136 -1.6  -1.6%     nan days    8232     95                0.87  0.69   7  l
    Saudi Arabia              -278 -0.8  -4.4%     nan days    6107     18                0.92 -0.08   7  l
    Korea, South               268  0.5   6.8%    10.6 days    3956    7.6       [10, 11] 0.84 -0.09  14  l
    Australia                   13  0.1   2.7%    25.7 days    1400    5.5                0.33 -0.54   7  l
    China                       52  0.0  12.3%     6.0 days     582   0.04         [0, 0] 0.92 -0.42   7  l
    Singapore                  4.0  0.1  10.0%     7.2 days      65    1.0                0.54  1.89   9  l
    New Zealand                3.0  0.1  10.5%     7.0 days      52    1.1                0.06 -0.43   7  l

15 November 2020

    US                      127346   38   3.5%    20.3 days 6509848   1957   [2138, 2252] 0.69 -0.04   7  e
    France                  -16157  -24  -0.9%     nan days 1712489   2524                0.46  1.39   7  l
    Italy                    25312   41   4.1%    17.1 days  688435   1103   [1283, 1388] 0.20  0.01   7  e
    India                    -2096 -0.2  -0.4%     nan days  479216     36                0.33  0.23  13  l
    Russia                    1401  1.0   0.3%     inf days  440087    311     [311, 311] 0.52  0.14   7  l
    Germany                   5240  6.5   1.8%     inf days  288226    360     [379, 384] 0.07  0.07  13  l
    Iran                      5966  7.0   4.5%    15.6 days  155744    183     [215, 234] 0.75 -0.04  11  e
    Czechia                  -7859  -73  -6.0%     nan days  129788   1213                0.09 -0.11  11  l
    Switzerland              -3001  -36  -2.7%     nan days  112784   1342                0.09  0.24  13  l
    Hungary                   3368   34   3.3%     inf days  102607   1050   [1183, 1245] 0.06  0.02   9  l
    Austria                   1509   17   2.0%     inf days   77130    871     [926, 945] 0.22 -0.09  11  e
    Bulgaria                  5369   77  17.2%     4.4 days   66539    955                0.30 -0.32   7  e
    Belarus                    683  7.2   7.9%     9.2 days   17494    185     [228, 267] 0.23 -0.25   7  e
    Japan                     1041  0.8   7.9%     9.1 days   14086     11                0.35 -0.35  14  l
    Denmark                   -195 -3.3  -1.4%     nan days   13547    231                0.66  0.17  14  l
    Israel                      19  0.2   3.5%    20.1 days    7993     92      [96, 101] 0.06  0.20  11  l
    Saudi Arabia               -60 -0.2  -0.8%     nan days    7362     22                0.12 -0.04  12  l
    Korea, South               115  0.2   6.7%    10.7 days    2362    4.6         [6, 7] 0.50  0.03   7  l
    Australia                   11  0.0   2.2%    32.2 days    1337    5.3                0.53  1.79  14  l
    China                     -8.7 -0.0  -1.6%     nan days     543   0.04                0.64 -1.43   7  l
    Singapore                  2.7  0.0   6.3%    11.3 days      69    1.1                0.08 -1.30  10  l
    New Zealand                4.9  0.1  11.2%     6.5 days      58    1.2                0.29  0.52  11  l

27 October 2020

    US                       46794   14   2.2%    32.5 days 5018031   1509   [1573, 1611] 0.19 -0.11   8  e
    France                   58448   86   6.8%    10.6 days 1046547   1542   [1978, 2264] 0.16 -0.07   7  l
    India                   -21203 -1.6  -3.3%     nan days  625857     47                0.30 -0.04  12  l
    Russia                    8058  5.7   3.1%    22.9 days  354375    250     [276, 292] 0.44  0.00   7  l
    Italy                    19354   31   9.1%     8.0 days  236684    379     [532, 635] 0.88 -0.06  14  e
    Germany                   6719  8.4   5.2%    13.6 days  115115    144     [180, 200] 0.06 -0.04  14  l
    Iran                      1845  2.2   3.2%    21.8 days   82653     97     [108, 114] 0.57 -0.10   9  l
    Switzerland               5932   71  10.0%     7.3 days   57282    682   [1014, 1219] 0.17 -0.10  10  l
    Hungary                   2431   25   7.9%     9.1 days   43600    446     [578, 677] 0.78 -0.10  14  e
    Austria                   2139   24  13.6%     5.4 days   23239    262     [422, 577] 0.78 -0.14   8  e
    Bulgaria                  1249   18   5.6%    12.6 days   20346    292     [370, 414] 0.27 -0.02  14  l
    Israel                    -658 -7.6  -4.7%     nan days   13544    156                0.67  0.17   7  l
    Belarus                    284  3.0   2.9%    24.3 days    8998     95     [108, 114] 0.19 -0.03  14  l
    Denmark                    744   13   9.9%     7.3 days    8467    144     [210, 255] 0.93 -0.11   7  l
    Saudi Arabia               -40 -0.1  -0.5%     nan days    8228     24                0.04 -0.15   8  l
    Japan                      168  0.1   5.5%    12.8 days    6751    5.4                0.37 -1.57   8  l
    Korea, South                42  0.1   4.0%    17.8 days    1602    3.1                0.19 -0.52  14  l
    Australia                 -2.4 -0.0  -0.2%     nan days    1422    5.6                0.21  2.24   7  l
    China                      6.2  0.0   4.4%    16.0 days     418   0.03                0.29 -1.96   7  l
    New Zealand               -5.2 -0.1  -7.3%     nan days      68    1.4                0.58  1.50   7  l
    Singapore                  -12 -0.2 -15.8%     nan days      66    1.1                0.70 -0.79   7  l

29 September 2020

    US                        9313  2.8   0.2%     inf days 4148365   1247   [1256, 1260] 0.20 -0.12  12  e
    India                    -9259 -0.7  -1.0%     nan days  947576     71                0.14 -0.18  14  l
    France                   14156   21   3.5%    20.1 days  443437    654     [746, 800] 0.04 -0.10  10  l
    Brazil                   -6776 -3.2  -1.6%     nan days  406034    192                0.05 -0.13  13  l
    Russia                    7744  5.5  18.1%     4.2 days  191381    135     [255, 644] 0.83 -0.26   7  e
    Israel                     456  5.3   0.7%     inf days   66567    767     [770, 770] 0.09 -0.23   7  l
    Italy                      982  1.6   4.0%    17.8 days   50323     81       [88, 94] 0.52 -0.09   7  e
    Iran                       937  1.1   2.0%     inf days   47650     56       [60, 61] 0.57  0.02   7  l
    Germany                    640  0.8   3.6%    19.6 days   26470     33       [37, 39] 0.27 -0.09   8  l
    Hungary                    827  8.5   4.8%    14.8 days   18815    193     [230, 252] 0.24 -0.07   7  e
    Saudi Arabia              -289 -0.8  -2.6%     nan days   11090     32                0.71  0.04   8  l
    Austria                    -34 -0.4  -0.4%     nan days    8590     97                0.55  0.09  14  l
    Switzerland                580  6.9  11.2%     6.5 days    7881     94                0.38 -0.97   7  l
    Denmark                    165  2.8   2.6%     inf days    6481    110     [120, 124] 0.42  0.03  12  e
    Japan                      -12 -0.0  -0.2%     nan days    6428    5.1                0.07  0.56  13  l
    Bulgaria                    98  1.4   2.6%    26.7 days    5125     74       [80, 84] 0.31 -0.04  14  l
    Belarus                    264  2.8   9.6%     7.6 days    2957     31       [45, 54] 0.82 -0.05   7  l
    Korea, South               -33 -0.1  -1.7%     nan days    1822    3.5                0.24  0.22  14  l
    Australia                  -14 -0.1  -0.9%     nan days    1494    5.9                0.42  0.30   7  l
    China                      4.7  0.0   4.6%    15.5 days     368   0.03         [0, 0] 0.38 -0.14   7  l
    Singapore                  5.3  0.1   6.9%    10.4 days     295    4.8         [6, 7] 0.64  0.09  14  l
    New Zealand               -2.4 -0.0  -4.3%     nan days      55    1.1                0.14 -0.27   7  l

17 September 2020

    US                        8447  2.5   0.2%     inf days 3907715   1175   [1182, 1183] 0.58 -0.05   7  e
    India                      945  0.1   0.1%     inf days  995933     75       [75, 75] 0.79  0.12   8  l
    Brazil                   -1641 -0.8  -0.4%     nan days  439513    208                0.04  0.08  11  l
    France                   10101   15   3.4%    21.0 days  315056    464     [529, 566] 0.05 -0.08  12  l
    Russia                    1375  1.0   2.5%    28.3 days  169175    119                0.30 -0.77   9  l
    Israel                    2833   33   8.2%     8.8 days   46081    531     [702, 827] 0.40 -0.18  13  e
    Italy                      711  1.1   1.8%     inf days   40532     65       [69, 71] 0.48  0.02  14  l
    Iran                       605  0.7   2.5%    28.4 days   34683     41       [44, 46] 0.51 -0.06  14  l
    Germany                    521  0.6   3.8%    18.4 days   20873     26       [29, 31] 0.34 -0.23   9  l
    Saudi Arabia              -549 -1.6  -3.2%     nan days   17178     50                0.69 -0.15   9  l
    Hungary                    710  7.3   6.9%    10.4 days    9653     99     [131, 150] 0.41 -0.07  14  e
    Japan                       55  0.0   4.5%    15.9 days    7406    5.9                0.24  0.53  13  l
    Austria                    460  5.2   6.9%    10.4 days    6660     75      [99, 113] 0.57 -0.06  14  l
    Switzerland                 29  0.3   0.5%     inf days    6326     75                0.08  0.33   7  l
    Bulgaria                  -7.8 -0.1  -0.2%     nan days    4410     63                0.30 -0.06   7  l
    Denmark                    122  2.1   3.6%     inf days    3381     58       [62, 63] 0.39  0.03   7  l
    Korea, South              -236 -0.5  -8.5%     nan days    2742    5.3                0.29 -0.04  14  l
    Australia                  -64 -0.3  -2.8%     nan days    2191    8.6                0.14  0.07  14  l
    Belarus                    138  1.5  12.5%     5.9 days    1186     13       [20, 25] 0.39 -0.18   7  l
    Singapore                  -46 -0.7  -8.3%     nan days     532    8.6                0.48 -0.46   8  l
    China                     -1.6 -0.0  -0.5%     nan days     362   0.03                0.35  0.08  13  l
    New Zealand               -8.3 -0.2 -10.6%     nan days      77    1.6                0.38 -0.18  12  l

28 August 2020

    US                       14246  4.3   0.4%     inf days 3585635   1078   [1091, 1095] 0.14  0.10   7  l
    India                    11148  0.8   2.5%    28.4 days  742023     56       [60, 62] 0.25 -0.09  12  l
    Brazil                   -7388 -3.5  -1.4%     nan days  519896    246                0.09 -0.18   8  l
    Spain                    10141   20   4.8%    14.7 days  250135    500     [596, 655] 0.09  0.02   7  l
    France                    2750  4.1   1.6%     inf days  177729    262                0.21  0.38   7  l
    Russia                   -1346 -1.0  -0.8%     nan days  165585    117                0.09  0.12   7  l
    Belgium                    386  3.3   0.7%     inf days   55256    471     [483, 487] 0.15  0.01   9  l
    Iran                       222  0.3   0.7%     inf days   30021     35       [36, 36] 0.28  0.05  10  l
    Italy                     1049  1.7   5.1%    13.9 days   21932     35       [43, 47] 0.79 -0.05  14  l
    Saudi Arabia               -42 -0.1  -0.2%     nan days   21815     64                0.15  0.81  10  l
    Israel                     331  3.8   5.7%    12.5 days   21793    251                0.29  5.34   7  l
    Germany                     92  0.1   0.5%     inf days   18372     23       [23, 23] 0.19  0.19   9  l
    Japan                     -410 -0.3  -3.4%     nan days   11870    9.5                0.65 -0.23   9  l
    Australia                  246  1.0  13.6%     5.4 days    4500     18                0.43  1.23   8  l
    Bulgaria                   8.0  0.1   2.3%    30.8 days    4270     61                0.12  0.67  14  l
    Korea, South               307  0.6   6.4%    11.2 days    4210    8.1       [11, 12] 0.34 -0.06  14  e
    Switzerland                216  2.6   6.4%    11.2 days    4203     50       [63, 71] 0.16 -0.24   8  l
    Austria                     64  0.7   2.0%     inf days    3311     37       [39, 39] 0.34  0.06  10  l
    Singapore                  -95 -1.5  -6.5%     nan days    1406     23                0.51  0.17   7  l
    Denmark                    -98 -1.7  -7.7%     nan days    1240     21                0.45 -0.32  14  l
    Hungary                     44  0.4   4.6%    15.5 days    1008     10       [12, 14] 0.33 -0.04  14  l
    Belarus                    -24 -0.3  -2.7%     nan days     853    9.0                0.35  0.13   9  l
    China                      -45 -0.0  -5.6%     nan days     764   0.05                0.30  0.12   9  l
    New Zealand               0.69  0.0   0.5%     inf days     131    2.7         [3, 3] 0.41  0.12  13  l

8 August 2020

    US                       24231  7.3   0.8%     inf days 3156538    949     [975, 986] 0.14  0.04  14  l
    India                    10933  0.8   2.8%    25.3 days  619088     47       [51, 53] 0.23 -0.10   7  l
    Brazil                   12098  5.7   3.4%    20.7 days  590571    279                0.13 -0.65  14  l
    Russia                   -2362 -1.7  -1.3%     nan days  178402    126                0.14  0.24   7  l
    Spain                     4861  9.7   4.0%    17.5 days  135483    271     [315, 341] 0.19 -0.04  11  l
    France                    2913  4.3   4.3%    16.5 days  120508    178     [201, 217] 0.43 -0.14   7  l
    Belgium                    670  5.7   2.1%    33.4 days   45190    386     [411, 426] 0.23  0.02   7  l
    Saudi Arabia                36  0.1   4.3%    16.6 days   33752     99                0.46  0.55   8  l
    Israel                    -488 -5.6  -1.9%     nan days   25097    289                0.49 -0.45   8  l
    Iran                      -7.2 -0.0  -0.0%     nan days   24711     29                0.59  0.22  11  l
    Japan                      291  0.2   2.0%     inf days   14481     12       [12, 12] 0.47  0.14   7  l
    Italy                      161  0.3   2.9%    24.6 days   12924     21       [22, 23] 0.51 -0.08   7  l
    Germany                    559  0.7   7.0%    10.3 days   11066     14       [18, 20] 0.44 -0.16   7  l
    Australia                  120  0.5   1.4%     inf days    8860     35       [35, 35] 0.29  0.17  10  l
    Singapore                   64  1.0   1.0%     inf days    6458    104     [106, 106] 0.13  0.09  14  l
    Belarus                   -257 -2.7  -6.4%     nan days    3831     40                0.53 -0.04   7  l
    Switzerland                198  2.4   9.5%     7.6 days    2683     32       [45, 55] 0.78 -0.17   7  l
    China                      -90 -0.0  -4.2%     nan days    2111   0.15                0.92  0.33  12  l
    Austria                    -40 -0.5  -2.8%     nan days    1427     16                0.15 -0.58  14  l
    Denmark                     96  1.6  10.4%     7.0 days     985     17       [25, 31] 0.58 -0.10   8  l
    Korea, South               -47 -0.1  -7.2%     nan days     629    1.2                0.54 -0.16   7  l
    Hungary                    8.1  0.1   4.1%    17.4 days     555    5.7                0.20 -0.91   7  l
    New Zealand              -0.92 -0.0  -4.0%     nan days      23   0.47                0.12  1.62   8  l

2 August 2020

    US                       38902   12   1.5%    47.6 days 3004112    903     [952, 979] 0.19  0.00   7  l
    Brazil                   21538   10   6.5%    11.0 days  576332    272                0.53 -1.53   9  l
    India                     7950  0.6   1.4%     inf days  567730     43       [45, 45] 0.19 -0.08   7  e
    Russia                   -4651 -3.3  -2.5%     nan days  184540    130                0.57 -0.30   7  l
    France                    1151  1.7   1.7%    40.8 days  111370    164     [172, 176] 0.06 -0.05  10  l
    Spain                     1701  3.4   1.6%     inf days  109701    219     [230, 233] 0.04 -0.14   7  l
    Belgium                    649  5.5   2.2%    32.2 days   41984    358     [383, 398] 0.63 -0.07  14  l
    Saudi Arabia             -1597 -4.7  -4.3%     nan days   37043    108                0.39 -0.12   9  l
    Israel                   -1941  -22  -7.3%     nan days   26590    306                0.16 -0.48  13  l
    Iran                        77  0.1   0.3%     inf days   23940     28       [28, 28] 0.41 -0.17   7  e
    Italy                      -25 -0.0  -0.2%     nan days   12457     20                0.04  0.41  11  l
    Japan                      791  0.6   6.7%    10.7 days   11445    9.1       [12, 14] 0.39 -0.10  13  l
    Germany                    348  0.4   4.0%    17.6 days    9215     11       [13, 15] 0.17 -0.04  14  l
    Australia                   90  0.4   1.3%     inf days    6864     27       [27, 27] 0.15  0.07   8  l
    Singapore                   65  1.1   1.1%     inf days    5745     93       [93, 93] 0.70  0.11   8  l
    Belarus                   -306 -3.2  -6.4%     nan days    4697     50                0.11 -0.09  13  l
    China                       64  0.0   2.9%     inf days    2253   0.16         [0, 0] 0.55 -0.06   7  e
    Switzerland                160  1.9  10.2%     7.1 days    2131     25                0.37 -0.34   7  l
    Austria                    -18 -0.2  -1.1%     nan days    1583     18                0.41  0.40  10  l
    Korea, South               -34 -0.1  -4.3%     nan days     806    1.6                0.22 -0.58   9  l
    Denmark                    9.5  0.2   1.6%     inf days     596     10       [11, 11] 0.11  0.14  13  l
    Hungary                     14  0.1   3.8%    18.6 days     565    5.8         [7, 7] 0.52 -0.13  13  l
    New Zealand                1.8  0.0   9.7%     7.5 days      25   0.51                0.30 -1.61  11  l

27 July 2020

    US                       38089   11   1.4%     inf days 2789125    838     [881, 899] 0.37  0.04  11  l
    Brazil                   -9597 -4.5  -1.8%     nan days  519174    245                0.08 -0.84  13  l
    India                    15971  1.2   3.5%    20.1 days  485277     37       [42, 45] 0.36 -0.02   7  l
    Russia                   -1911 -1.3  -1.0%     nan days  198652    140                0.06 -0.35   8  l
    France                     -68 -0.1  -0.1%     nan days  104687    154                0.68  0.45   7  l
    Spain                       70  0.1   0.1%     inf days   93613    187                0.56  0.38   7  l
    Saudi Arabia               301  0.9   5.2%    13.7 days   43885    128                0.67  0.59   7  l
    Belgium                    370  3.2   1.6%    43.8 days   38767    331     [345, 353] 0.43 -0.07  14  l
    Israel                     606  7.0   1.8%     inf days   34461    397     [418, 424] 0.18  0.04  14  l
    Iran                       262  0.3   3.4%    20.9 days   22259     26                0.62  1.06  11  l
    Italy                      121  0.2   2.7%    26.0 days   12565     20                0.46  0.54  13  l
    Japan                      722  0.6  10.3%     7.1 days    7944    6.3        [9, 11] 0.73 -0.18   7  l
    Germany                    330  0.4   6.0%    11.9 days    7488    9.3       [11, 13] 0.48 -0.20   7  l
    Belarus                   -142 -1.5  -2.3%     nan days    6173     65                0.28  0.07  12  l
    Australia                  330  1.3   5.5%    13.0 days    5600     22       [28, 31] 0.29 -0.04  10  l
    Singapore                  306  4.9   7.9%     9.1 days    4821     78     [104, 121] 0.70 -0.16   9  l
    Switzerland                111  1.3   9.2%     7.9 days    1735     21                0.19 -0.76   8  l
    Austria                     52  0.6   5.1%    13.8 days    1551     18       [21, 23] 0.40 -0.26   9  l
    China                      138  0.0   9.3%     7.8 days    1459   0.10         [0, 0] 0.64 -0.10  12  l
    Korea, South                25  0.0   4.3%    16.5 days     971    1.9                0.38 -1.46  14  l
    Hungary                     10  0.1   5.0%    14.1 days     510    5.2                0.60  2.43   7  l
    Denmark                   -5.8 -0.1  -1.2%     nan days     485    8.3                0.91  0.33   7  l
    New Zealand               -1.3 -0.0  -6.0%     nan days      21   0.43                0.17 -1.00  10  l

19 July 2020

    US                       52380   16   2.0%    34.2 days 2448574    736     [802, 837] 0.28 -0.01  14  l
    Brazil                    7771  3.7   2.6%    27.3 days  548680    259                0.18 -0.37  14  l
    India                    15256  1.2   5.7%    12.5 days  373542     28       [34, 38] 0.89 -0.05  12  e
    Russia                   -3140 -2.2  -1.5%     nan days  206078    145                0.35 -0.43   7  l
    France                     525  0.8   0.9%    75.7 days   99600    147     [150, 152] 0.03 -0.04  12  l
    Spain                      997  2.0   1.8%    39.6 days   81459    163     [172, 177] 0.09 -0.05  12  l
    Saudi Arabia             -2182 -6.4  -4.2%     nan days   51751    151                0.22 -0.11  10  l
    Belgium                    219  1.9   1.3%    53.1 days   36617    312     [321, 326] 0.40 -0.05  13  l
    Israel                    1479   17   5.1%    14.0 days   27616    318     [392, 434] 0.35 -0.05  14  e
    Iran                      -249 -0.3  -1.1%     nan days   22327     26                0.27  0.11  10  l
    Italy                      -33 -0.1  -0.3%     nan days   12368     20                0.26  0.15  12  l
    Belarus                   -195 -2.1  -2.5%     nan days    7602     80                0.35  0.05  12  l
    Germany                     50  0.1   3.1%    22.9 days    6135    7.7                0.11  0.50  14  l
    Japan                      424  0.3   9.7%     7.5 days    4749    3.8         [5, 7] 0.15 -0.11   7  l
    Singapore                   44  0.7   3.5%    20.0 days    3795     61       [66, 70] 0.37  0.25  14  l
    Australia                  312  1.2  11.9%     6.2 days    3406     13       [20, 26] 0.33 -0.20   9  e
    Switzerland                110  1.3   9.1%     8.0 days    1623     19       [27, 32] 0.31 -0.24   7  l
    Austria                    9.2  0.1   0.7%     inf days    1361     15       [15, 15] 0.24  0.17  14  l
    Korea, South               -15 -0.0  -1.7%     nan days     894    1.7                0.07 -0.27   8  l
    China                       15  0.0   2.7%    25.6 days     652   0.05         [0, 0] 0.02 -0.06  14  l
    Hungary                   -5.9 -0.1  -1.2%     nan days     497    5.1                0.37  0.13   9  l
    Denmark                     25  0.4   8.6%     8.4 days     353    6.0                0.47 -0.73  12  l
    New Zealand              -0.03 -0.0  -0.1%     nan days      25   0.51                0.01  0.24  14  l

4 July 2020

    US                       13623  4.1   0.7%     inf days 1874315    563     [576, 580] 0.12 -0.17   8  e
    Brazil                  -24151  -11  -5.0%     nan days  492582    233                0.20 -0.96   8  l
    India                     2780  0.2   1.2%     inf days  235433     18       [18, 19] 0.15 -0.11   8  e
    Russia                    -588 -0.4  -0.3%     nan days  219942    155                0.10  0.20  11  l
    France                     505  0.7   1.5%    46.1 days   93911    138     [142, 145] 0.08 -0.24  10  l
    Spain                      396  0.8   1.1%    62.6 days   71784    144     [147, 149] 0.12 -0.07  12  e
    Saudi Arabia              -8.4 -0.0  -0.0%     nan days   59385    174                0.33  0.28   7  l
    Belgium                     37  0.3   0.1%     inf days   34889    298                0.13  0.30  11  l
    Iran                       -38 -0.0  -0.1%     nan days   27723     33                0.73  0.14   7  l
    Italy                     -180 -0.3  -1.2%     nan days   14884     24                0.41  0.12  11  l
    Belarus                   -918 -9.7  -7.0%     nan days   12676    134                0.17 -0.04  13  l
    Germany                   -272 -0.3  -3.6%     nan days    7470    9.3                0.45 -0.62   8  l
    Singapore                 -285 -4.6  -6.0%     nan days    4684     75                0.47 -0.12   8  l
    Japan                      109  0.1   7.8%     9.3 days    1487    1.2         [2, 2] 0.34 -0.21  11  l
    Switzerland                134  1.6  15.5%     4.8 days     936     11       [20, 26] 0.54 -0.20   7  l
    Korea, South                16  0.0   6.9%    10.4 days     936    1.8                0.49  0.56   9  l
    Australia                   12  0.0   1.5%     inf days     837    3.3         [3, 3] 0.58 -0.07   7  e
    Hungary                    -15 -0.2  -1.8%     nan days     832    8.5                0.22 -0.02   7  l
    Austria                     61  0.7   8.0%     9.0 days     787    8.9       [12, 14] 0.47 -0.09  13  l
    China                     -6.3 -0.0  -1.2%     nan days     517   0.04                0.67  0.19  14  l
    Denmark                    -43 -0.7 -10.1%     nan days     409    7.0                0.60 -0.14   7  l
    New Zealand               -1.7 -0.0  -9.3%     nan days      18   0.37                0.42  0.75   8  l

23 June 2020

    US                       22424  6.7   3.5%    20.1 days 1551702    466     [500, 523] 0.27 -0.15   8  e
    Brazil                    9284  4.4   2.1%     inf days  453463    214     [228, 232] 0.03  0.14   7  l
    Russia                    1592  1.1   3.1%    22.4 days  239422    169     [178, 186] 0.54  0.20   7  l
    India                     6352  0.5  10.4%     7.0 days  178014     13                0.33 -0.31   8  e
    France                     297  0.4   1.5%    45.9 days   91110    134                0.37 -0.51   7  l
    Spain                       88  0.2   0.1%     inf days   67804    136     [136, 136] 0.08  0.07  12  l
    Saudi Arabia                42  0.1   0.1%     inf days   54523    160     [160, 160] 0.79  0.11   7  l
    Belgium                     25  0.2   0.1%     inf days   34083    291     [291, 292] 0.28  0.03  14  l
    Iran                      -194 -0.2  -0.6%     nan days   31356     37                0.79  0.33   7  l
    Belarus                   -245 -2.6  -1.2%     nan days   20749    219                0.15 -0.09   7  l
    Italy                     -416 -0.7  -2.0%     nan days   20637     33                0.48  0.07  14  l
    Germany                    330  0.4   6.0%    11.9 days    7726    9.6                0.23 -0.87  13  l
    Singapore                 -451 -7.3  -6.5%     nan days    6697    108                0.59  0.04   7  l
    Korea, South                13  0.0   1.0%     inf days    1295    2.5         [3, 3] 0.18 -0.15   7  e
    Hungary                    8.7  0.1   4.7%    15.1 days     940    9.6       [11, 11] 0.94  0.35   7  l
    Japan                       23  0.0   5.4%    13.3 days     908   0.72                0.23  1.01  11  l
    Denmark                     34  0.6   8.9%     8.1 days     578    9.8       [13, 16] 0.48 -0.18   7  l
    Australia                   18  0.1   5.3%    13.4 days     475    1.9                0.50 -0.35  14  l
    Austria                   -2.2 -0.0  -0.5%     nan days     449    5.1                0.41  0.15   8  l
    China                       21  0.0   5.1%     inf days     438   0.03         [0, 0] 0.21  0.09  10  l
    Switzerland               -6.0 -0.1  -1.7%     nan days     354    4.2                0.14 -0.02   7  l
    New Zealand                1.7  0.0  15.3%     4.9 days      10   0.20         [0, 0] 0.47 -0.07  14  l

13 June 2020

    US                       16901  5.1   1.9%    37.1 days 1386931    417     [440, 453] 0.29 -0.13  13  l
    Brazil                    -759 -0.4  -0.2%     nan days  341859    161                0.04  0.19  14  l
    Russia                    -552 -0.4  -0.2%     nan days  235194    166                0.10  0.66  13  l
    India                     2060  0.2   1.5%     inf days  141842     11       [11, 11] 0.22  0.04  10  l
    France                     607  0.9   2.8%    25.5 days   90025    133                0.29 -5.47   9  l
    Spain                      429  0.9   1.4%    49.1 days   65697    131     [135, 138] 0.48  0.01   7  l
    Saudi Arabia              2646  7.7   7.4%     9.8 days   38020    111     [148, 171] 0.77 -0.09  14  l
    Belgium                     77  0.7   0.7%    94.1 days   33675    287     [290, 292] 0.28 -0.05  10  l
    Iran                      -196 -0.2  -0.7%     nan days   29217     34                0.54  0.10  12  l
    Italy                    -1479 -2.4  -5.0%     nan days   28997     46                0.25 -0.01   7  l
    Belarus                   -214 -2.3  -0.9%     nan days   24462    258                0.35  0.22  14  l
    Singapore                 -346 -5.6  -2.9%     nan days   11785    190                0.85 -0.24  10  l
    Germany                   -251 -0.3  -3.6%     nan days    6908    8.6                0.22 -0.17   7  l
    Korea, South                14  0.0   1.3%     inf days    1083    2.1         [2, 2] 0.07 -0.16   9  e
    Hungary                    -39 -0.4  -3.6%     nan days    1051     11                0.47 -0.02   7  l
    Japan                      -47 -0.0  -4.7%     nan days     964   0.77                0.20 -0.32   7  l
    Denmark                   -8.9 -0.2  -1.8%     nan days     512    8.7                0.09  0.02   7  l
    Austria                    -14 -0.2  -3.5%     nan days     404    4.6                0.36 -0.51   8  l
    Australia                  -18 -0.1  -4.4%     nan days     389    1.5                0.60 -0.12   8  l
    Switzerland                7.0  0.1   6.6%    10.9 days     325    3.9                0.14  0.31  14  l
    China                      1.7  0.0   4.1%    17.1 days     118   0.01                0.07 -0.86   7  l
    New Zealand               0.07  0.0   inf%     0.0 days    0.00   0.00         [0, 0] 0.17 -0.14   7  l

7 June 2020

    US                       17764  5.3   2.9%    23.9 days 1309410    394     [422, 442] 0.54 -0.25   7  l
    Brazil                   17066  8.1   5.2%    13.7 days  359767    170     [207, 230] 0.58 -0.03   7  l
    Russia                   -1178 -0.8  -0.5%     nan days  231450    163                0.33  1.71   7  l
    India                     5070  0.4   4.4%    16.2 days  120981    9.1       [11, 12] 0.45 -0.03   8  e
    France                    -499 -0.7  -0.6%     nan days   89698    132                0.07 -0.15  11  l
    Spain                       86  0.2   0.1%     inf days   63799    128                0.42  0.34  10  l
    Italy                     -785 -1.3  -2.2%     nan days   35877     57                0.54  0.04  12  l
    Belgium                     24  0.2   0.1%     inf days   33302    284     [285, 285] 0.17  0.08  14  l
    Iran                       776  0.9   3.1%    22.9 days   29178     34       [38, 41] 0.17 -0.07  13  l
    Saudi Arabia              1782  5.2   9.8%     7.4 days   26402     77     [109, 134] 0.80 -0.50   7  l
    Belarus                   -178 -1.9  -0.7%     nan days   24473    258                0.61  0.30   7  l
    Singapore                  186  3.0   5.0%    14.3 days   12943    208     [233, 255] 0.80  0.19  10  l
    Germany                   -143 -0.2  -1.8%     nan days    7819    9.8                0.16  0.07   8  l
    Hungary                    -20 -0.2  -1.7%     nan days    1166     12                0.39 -0.19   7  l
    Japan                      -15 -0.0  -1.3%     nan days    1158   0.92                0.54  0.06  14  l
    Korea, South                32  0.1   4.2%    17.0 days     951    1.8         [2, 2] 0.51 -0.09   9  l
    Denmark                   -6.5 -0.1  -1.0%     nan days     616     10                0.17  0.24   8  l
    Australia                  -13 -0.1  -2.8%     nan days     454    1.8                0.31 -0.33   7  l
    Austria                     24  0.3  11.6%     6.3 days     437    4.9                0.49  1.96   8  l
    Switzerland                -13 -0.2  -3.5%     nan days     335    4.0                0.08  0.26   8  l
    China                    -0.46 -0.0  -0.4%     nan days     124   0.01                0.14  2.43   7  l
    New Zealand               0.00  0.0   0.0%     inf days     1.0   0.02                1.00  0.00   7  l

31 May 2020

    US                       20104  6.0   3.1%    22.4 days 1249928    376                0.39 -0.38   9  l
    Brazil                   18983  9.0  10.0%     7.3 days  268714    127     [178, 219] 0.91 -0.08   7  e
    Russia                   -1504 -1.1  -0.7%     nan days  224551    158                0.42  0.32  14  l
    France                    1233  1.8   3.4%    20.5 days   90845    134     [145, 153] 0.30 -0.22   7  l
    India                     1112  0.1   1.3%     inf days   89706    6.8         [7, 7] 0.14  0.08   8  l
    Spain                     1317  2.6   3.4%    21.0 days   61727    123                0.27 -0.43  13  l
    Italy                    -2551 -4.1  -5.7%     nan days   43691     70                0.45 -0.03   8  l
    Belgium                    6.6  0.1   0.0%     inf days   32964    281     [281, 281] 0.49  0.26   8  l
    Sweden                     676  6.6   3.3%    21.6 days   27747    272     [303, 322] 0.86 -0.05   8  l
    Iran                       521  0.6   3.5%    20.4 days   24389     29       [32, 34] 0.36 -0.12   8  l
    Saudi Arabia             -1105 -3.2  -4.6%     nan days   24021     70                0.47 -0.25  11  l
    Belarus                    169  1.8   0.7%     inf days   23465    248     [253, 254] 0.23  0.05  14  l
    Singapore                 -621 -10.0  -4.5%     nan days   13616    219                0.61 -0.04  13  l
    Germany                   -216 -0.3  -2.2%     nan days    9751     12                0.23  0.07  11  l
    Japan                      -59 -0.0  -3.7%     nan days    1555    1.2                0.74  0.09   9  l
    Hungary                    -77 -0.8  -6.2%     nan days    1201     12                0.39 -0.09  14  l
    Korea, South                33  0.1   6.5%    11.1 days     793    1.5         [2, 2] 0.53  0.15  13  l
    Denmark                    -18 -0.3  -2.4%     nan days     735     13                0.15  0.05  14  l
    Switzerland                -11 -0.1  -2.0%     nan days     526    6.3                0.20  0.12   8  l
    Austria                    -88 -1.0 -15.5%     nan days     497    5.6                0.58 -0.16   8  l
    Australia                  1.1  0.0   2.7%    25.7 days     475    1.9         [2, 2] 0.21  0.13  14  l
    China                     0.11  0.0   2.9%    24.6 days     104   0.01                0.05  0.40   9  l
    New Zealand               -4.2 -0.1 -418.2%     nan days     1.0   0.02                0.04 -0.03  10  l

25 May 2020

    US                        2963  0.9   0.3%     inf days 1178790    354     [355, 355] 0.13  0.13  11  l
    Russia                    1113  0.8   0.5%     inf days  227641    161     [162, 162] 0.60  0.05  14  l
    Brazil                   10511  5.0   7.0%    10.3 days  190634     90     [115, 131] 0.35 -0.12   8  e
    France                      10  0.0   1.3%    53.2 days   88581    131     [131, 132] 0.29  0.07  13  l
    India                     3865  0.3   5.4%    13.2 days   76820    5.8         [7, 8] 0.83 -0.05  10  l
    Spain                      776  1.6   3.6%    19.5 days   56644    113     [123, 130] 0.47  0.16  13  l
    Italy                    -1135 -1.8  -2.0%     nan days   56594     91                0.41  0.15  10  l
    Belgium                    166  1.4   1.1%    62.8 days   32540    278     [284, 288] 0.20 -0.14  12  l
    Saudi Arabia              -124 -0.4  -0.4%     nan days   28650     84                0.14  1.41   9  l
    Sweden                     368  3.6   1.5%     inf days   24490    240     [254, 260] 0.12 -0.03  13  e
    Iran                       207  0.2   0.9%     inf days   22483     26       [27, 27] 0.61  0.18   7  l
    Belarus                    164  1.7   0.8%     inf days   21844    230     [233, 233] 0.43  0.08   8  l
    Singapore                 -397 -6.4  -2.3%     nan days   16717    269                0.38 -0.05   7  l
    Germany                   -220 -0.3  -1.8%     nan days   11764     15                0.29  0.08  13  l
    Japan                     -224 -0.2  -9.3%     nan days    2317    1.8                0.07  0.16  11  l
    Hungary                    -34 -0.3  -2.1%     nan days    1565     16                0.57 -0.20   8  l
    Denmark                    -15 -0.3  -1.7%     nan days     898     15                0.62  0.10  11  l
    Austria                   -9.0 -0.1  -1.1%     nan days     800    9.0                0.10 -0.05   7  l
    Switzerland                -33 -0.4  -4.3%     nan days     730    8.7                0.34  0.27   9  l
    Korea, South               7.9  0.0   6.8%    10.5 days     713    1.4         [2, 2] 0.44 -0.03   7  l
    Australia                 -7.2 -0.0  -1.5%     nan days     481    1.9                0.11  0.05  14  l
    China                      6.2  0.0   9.0%     8.1 days     114   0.01                0.71  0.38  14  l
    New Zealand              -0.06 -0.0  -0.2%     nan days      27   0.55                0.46  0.15  14  l

21 May 2020

    US                       18224  5.5   4.2%    16.8 days 1164102    350     [379, 400] 0.18 -0.27  10  e
    Russia                    2630  1.9   1.2%     inf days  220341    155     [160, 161] 0.61  0.05  14  l
    Brazil                    9180  4.3   7.0%    10.2 days  156037     74      [95, 109] 0.30 -0.14  11  e
    France                      28  0.0   1.9%    37.1 days   89272    132     [133, 135] 0.34  0.28   8  l
    India                     2412  0.2   3.9%    17.9 days   63172    4.8         [6, 6] 0.28 -0.02   9  l
    Italy                    -1741 -2.8  -2.7%     nan days   62752    101                0.19  0.03   8  l
    Spain                     -111 -0.2  -0.2%     nan days   54291    109                0.20  0.22   7  l
    Belgium                     54  0.5   0.2%     inf days   31986    273     [274, 274] 0.34  0.08  14  l
    Saudi Arabia               424  1.2   3.3%    21.4 days   28728     84                0.12 -0.53   9  l
    Sweden                     391  3.8   1.7%     inf days   22721    223     [237, 243] 0.11 -0.02   9  e
    Iran                       763  0.9   4.7%    15.1 days   20958     25       [29, 31] 0.46 -0.09  14  e
    Belarus                    276  2.9   1.3%     inf days   20832    220     [230, 234] 0.18 -0.08  11  e
    Singapore                 -525 -8.5  -2.9%     nan days   18135    292                0.60 -0.65  14  l
    Germany                   -279 -0.3  -2.0%     nan days   13363     17                0.27  0.08   9  l
    Japan                     -6.4 -0.0  -0.2%     nan days    4035    3.2                0.39  0.36   7  l
    Hungary                     16  0.2   4.6%    15.4 days    1674     17                0.61  0.34   8  l
    Denmark                    -34 -0.6  -3.3%     nan days    1027     17                0.72  0.11   7  l
    Switzerland               -115 -1.4 -11.5%     nan days     966     11                0.12 -0.22   7  l
    Austria                    -81 -0.9  -8.8%     nan days     838    9.5                0.27  0.05   7  l
    Korea, South               -56 -0.1  -7.5%     nan days     723    1.4                0.44 -0.13  11  l
    Australia                  -22 -0.1  -4.1%     nan days     511    2.0                0.43 -0.06   7  l
    China                      5.3  0.0  10.5%     7.0 days     115   0.01         [0, 0] 0.86  0.34  10  l
    New Zealand               -2.7 -0.1  -8.4%     nan days      30   0.61                0.31  0.07  14  l

17 May 2020

    US                       11416  3.4   1.0%     inf days 1110690    334     [346, 350] 0.12  0.02  12  l
    Russia                    4633  3.3   2.3%     inf days  206340    146     [157, 161] 0.74  0.02  14  l
    Brazil                   10908  5.2  12.9%     5.7 days  128177     61      [94, 127] 0.69 -0.15   7  e
    France                    -797 -1.2  -0.9%     nan days   90582    134                0.32 -0.69  11  l
    Italy                    -3053 -4.9  -4.3%     nan days   70187    112                0.34 -0.04   7  l
    Spain                    -1489 -3.0  -2.6%     nan days   56689    113                0.10  0.14   7  l
    India                     1082  0.1   2.0%     inf days   53553    4.0         [4, 4] 0.57  0.05   7  e
    Belgium                     54  0.5   0.2%     inf days   31524    269     [269, 269] 0.47  0.09  10  l
    Saudi Arabia               -16 -0.0  -0.1%     nan days   28048     82                0.26  0.13  14  l
    Sweden                     902  8.8   5.6%    12.7 days   21032    206                0.26 -0.57  13  l
    Belarus                    243  2.6   1.3%     inf days   19023    201     [205, 205] 0.52  0.04   7  l
    Singapore                 -675  -11  -3.5%     nan days   18992    306                0.91 -0.50   8  l
    Iran                       684  0.8   4.2%    17.0 days   18308     22       [25, 27] 0.58 -0.10  14  l
    Germany                  -1013 -1.3  -6.5%     nan days   15214     19                0.22 -0.26   9  l
    Japan                      -23 -0.0  -0.4%     nan days    5174    4.1                0.28  0.84   7  l
    Hungary                    -68 -0.7  -4.1%     nan days    1654     17                0.46 -0.19   7  l
    Switzerland                -23 -0.3  -1.7%     nan days    1293     15                0.32  0.27  13  l
    Denmark                    -95 -1.6  -7.6%     nan days    1208     21                0.20 -0.08  14  l
    Austria                   -4.6 -0.1  -0.4%     nan days    1048     12                0.31  0.13  12  l
    Korea, South               -31 -0.1  -3.4%     nan days     900    1.7                0.37 -0.23   7  l
    Australia                 -3.1 -0.0  -0.5%     nan days     582    2.3                0.45  0.17  12  l
    China                     -7.1 -0.0  -6.1%     nan days     113   0.01                0.70  0.04   7  l
    New Zealand               -3.8 -0.1  -8.0%     nan days      45   0.91                0.49  0.13  13  l

13 May 2020

    US                        6269  1.9   0.6%     inf days 1056733    318     [323, 324] 0.20 -0.16   8  e
    Russia                    6574  4.6   3.6%     inf days  186615    132     [149, 156] 0.46  0.02  10  l
    Brazil                    2884  1.4   3.1%     inf days   93156     44       [48, 49] 0.65  0.06   7  e
    France                    -687 -1.0  -0.7%     nan days   92639    137                0.42 -1.83   7  l
    Italy                     -375 -0.6  -0.5%     nan days   81266    130                0.51  0.44   7  l
    Spain                     -329 -0.7  -0.5%     nan days   62130    124                0.27  0.24  11  l
    India                     2214  0.2   4.6%    15.5 days   47457    3.6         [4, 5] 0.32 -0.06  14  e
    Belgium                    343  2.9   2.5%    27.9 days   31286    267                0.27 -0.33   7  l
    Saudi Arabia               155  0.5   0.6%     inf days   27404     80       [81, 81] 0.56  0.05  14  l
    Singapore                  129  2.1   0.6%     inf days   20799    335     [336, 336] 0.72  0.11   7  l
    Sweden                     932  9.1   7.6%     9.5 days   18988    186                0.32 -0.90   9  l
    Germany                   -507 -0.6  -2.7%     nan days   18233     23                0.18  0.04  13  l
    Belarus                    697  7.4   7.0%    10.2 days   17757    187     [228, 261] 0.63 -0.10   7  e
    Iran                       548  0.6   4.8%    14.8 days   15677     18       [22, 24] 0.79 -0.26  14  l
    Japan                     -654 -0.5  -9.5%     nan days    6780    5.4                0.13 -0.09  13  l
    Hungary                    -34 -0.3  -1.8%     nan days    1881     19                0.36 -0.98  12  l
    Switzerland                -30 -0.4  -1.8%     nan days    1713     20                0.49  0.34   9  l
    Denmark                   -105 -1.8  -6.7%     nan days    1484     25                0.32 -0.11  10  l
    Austria                    -15 -0.2  -1.3%     nan days    1190     13                0.35  0.15   8  l
    Korea, South                14  0.0   6.6%    10.9 days    1008    1.9                0.73  0.42   7  l
    Australia                  -22 -0.1  -3.4%     nan days     612    2.4                0.12  0.15   8  l
    China                      -21 -0.0 -12.7%     nan days     159   0.01                0.39  0.07  10  l
    New Zealand               -5.4 -0.1  -7.1%     nan days      74    1.5                0.47  0.16   9  l



As the United Kingdom and the Netherlands have not been releasing the _number of recovered patients_, the data presented for these two countries in the tables below is the `no. of confirmed cases - no. of deaths`.

9 May 2020

    US                       21868  6.6   2.5%    28.5 days 1007756    303     [332, 348] 0.50 -0.02   7  l
    United Kingdom            4674  7.1   2.5%    28.2 days  180123    274     [304, 320] 0.14 -0.00   7  l
    Russia                    9141  6.4   5.1%    13.9 days  159528    113     [140, 156] 0.67 -0.02  14  l
    France                     491  0.7   2.1%    34.0 days   93356    138                0.15 -1.60   9  l
    Italy                    -3210 -5.1  -3.6%     nan days   87961    141                0.23 -0.08   8  l
    Spain                    -1002 -2.0  -1.5%     nan days   65410    131                0.22  0.20  10  l
    Netherlands                221  1.3   0.6%     inf days   36734    213     [217, 218] 0.30  0.06   9  l
    Belgium                     50  0.4   0.2%     inf days   30289    258     [259, 259] 0.21  0.13  14  l
    Saudi Arabia               375  1.1   1.4%     inf days   26083     76       [78, 78] 0.64  0.07   7  l
    Germany                   -652 -0.8  -3.1%     nan days   21378     27                0.15  0.11   8  l
    Singapore                  521  8.4   2.7%     inf days   19647    316     [348, 362] 0.13  0.04  13  l
    Sweden                    -158 -1.6  -0.9%     nan days   17119    168                0.07  0.18  14  l
    Belarus                    282  3.0   1.8%     inf days   15496    163     [169, 169] 0.52  0.07   7  l
    Iran                       492  0.6   5.8%    12.2 days   14313     17       [20, 23] 0.87 -0.55   9  l
    Japan                     -248 -0.2  -2.5%     nan days    9839    7.8                0.14 -0.25  14  l
    Switzerland               -131 -1.6  -5.6%     nan days    2284     27                0.37  0.15   9  l
    Hungary                    -49 -0.5  -2.5%     nan days    1921     20                0.62 -0.86   7  l
    Denmark                    -79 -1.3  -4.3%     nan days    1769     30                0.27 -0.19  14  l
    Austria                    -64 -0.7  -4.6%     nan days    1324     15                0.12  0.07  11  l
    Korea, South               -73 -0.1  -6.9%     nan days    1016    2.0                0.51 -0.10   9  l
    Australia                  1.3  0.0   5.6%    12.6 days     699    2.7                0.36  0.31  14  l
    China                      -42 -0.0 -12.0%     nan days     346   0.02                0.09 -0.11   7  l
    New Zealand                -19 -0.4 -17.0%     nan days     103    2.1                0.35 -0.04   9  l

5 May 2020

    US                       14847  4.5   1.6%     inf days  924273    278     [292, 297] 0.59  0.07   4  e
    United Kingdom            3640  5.5   2.3%     inf days  161850    246     [264, 271] 0.88  0.04   5  e
    Russia                    9581  6.8   8.2%     8.8 days  125817     89     [122, 143] 0.96 -0.08   6  l
    Italy                      244  0.4   3.9%    18.0 days   99980    160                0.58  1.38   5  l
    France                     803  1.2   4.7%    15.1 days   92280    136                0.58  2.35   6  l
    Spain                    -1023 -2.0  -1.4%     nan days   71240    142                0.29  0.30   6  l
    Netherlands                194  1.1   0.5%     inf days   35688    207     [208, 208] 0.96  0.09   5  l
    Belgium                    235  2.0   6.3%    11.3 days   29965    256     [273, 294] 0.87 -0.16   4  e
    Germany                  -1240 -1.5  -4.5%     nan days   26459     33                0.24  0.21   4  l
    Saudi Arabia              1303  3.8   5.8%    12.2 days   23989     70       [88, 99] 0.92 -0.05   4  l
    Singapore                  463  7.5   2.7%     inf days   17303    279     [303, 312] 0.54  0.04  14  l
    Sweden                   -1856  -18 -10.8%     nan days   15878    156                0.63 -0.39   4  l
    Belarus                    860  9.1  10.6%     6.9 days   14127    149     [208, 264] 0.60 -0.15   4  e
    Iran                      0.90  0.0   3.7%    19.1 days   12991     15       [16, 17] 0.83  0.14  13  l
    Japan                     -322 -0.3  -3.1%     nan days   10386    8.3                0.43  0.36  13  l
    Switzerland               -477 -5.7 -14.4%     nan days    2997     36                0.22  0.03   4  l
    Denmark                     21  0.4   5.5%    12.8 days    2089     36                0.66  0.57   6  l
    Hungary                     32  0.3   1.5%     inf days    2054     21       [22, 22] 0.66  0.05   4  l
    Austria                    -29 -0.3  -1.7%     nan days    1705     19                0.67  0.12   7  l
    Korea, South               -59 -0.1  -4.5%     nan days    1267    2.4                0.49 -0.18   5  l
    Australia                  -13 -0.0  -1.5%     nan days     864    3.4                0.81  0.09   4  l
    China                     -103 -0.0 -17.5%     nan days     537   0.04                0.60 -0.08   4  l
    New Zealand                -22 -0.4 -12.3%     nan days     164    3.3                0.68 -0.13   4  l

1 May 2020

    US                        3882  1.2   0.5%     inf days  852481    256     [236, 249] 0.63  0.19   6  l
    United Kingdom            4578  7.0   4.1%    17.3 days  144482    220     [253, 273] 0.30  0.00   4  l
    Italy                    -2256 -3.6  -2.2%     nan days  101551    163                0.72 -0.24   5  l
    Russia                    5327  3.8   4.5%    15.6 days   93806     66       [82, 90] 0.17 -0.03  14  e
    France                   -2730 -4.0  -3.0%     nan days   91912    135                0.48 -0.77   4  l
    Spain                    -3328 -6.7  -4.3%     nan days   76842    154                0.46 -0.10   6  l
    Netherlands                230  1.3   0.7%     inf days   34521    200     [201, 202] 0.82  0.06  14  l
    Germany                  -2352 -2.9  -7.0%     nan days   32886     41                0.56 -0.31   6  l
    Belgium                     95  0.8   0.3%     inf days   29349    250                0.56  0.31   7  l
    Saudi Arabia              1154  3.4   4.8%    14.7 days   19428     57       [71, 78] 0.64 -0.02  14  l
    Sweden                     716  7.0   6.1%    11.7 days   17501    172     [210, 237] 0.68 -0.17   4  l
    Singapore                  452  7.3   3.1%     inf days   14910    240     [260, 262] 0.79  0.07  11  l
    Iran                      -261 -0.3  -1.9%     nan days   13509     16                0.74  0.12   9  l
    Belarus                    762  8.0   6.9%    10.4 days   11552    122     [159, 182] 0.41 -0.06  10  e
    Japan                     -222 -0.2  -2.0%     nan days   11198    8.9                0.45  0.78   8  l
    Switzerland               -210 -2.5  -4.4%     nan days    4449     53                0.18  0.07  11  l
    Denmark                    -79 -1.3  -3.6%     nan days    2160     37                0.60 -0.49   6  l
    Austria                    -66 -0.7  -3.3%     nan days    1961     22                0.55  0.08  10  l
    Hungary                    4.6  0.0   0.2%     inf days    1882     19                0.71  0.35   4  l
    Korea, South               -32 -0.1  -2.2%     nan days    1454    2.8                0.40  0.24   8  l
    Australia                  7.0  0.0  10.7%     6.8 days     931    3.7         [5, 7] 0.79  0.44   6  l
    China                      -27 -0.0  -3.3%     nan days     796   0.06                0.65  0.20   5  l
    New Zealand               -3.4 -0.1  -1.6%     nan days     208    4.2                0.89  0.32   5  l

23 April 2020

    US                       23716  7.1   3.6%    19.6 days  715726    215     [247, 265] 0.84 -0.04   4  l
    United Kingdom            3343  5.1   2.9%     inf days  115395    175     [189, 191] 0.78  0.10   4  l
    Italy                     -312 -0.5  -0.3%     nan days  107699    173                0.84  0.16  12  l
    Spain                     -341 -0.7  -0.3%     nan days  100757    201                0.32  0.75   6  l
    France                   -3445 -5.1  -3.6%     nan days   93863    138                0.91 -1.33   4  l
    Russia                    5943  4.2  11.8%     6.2 days   53066     37       [59, 73] 0.91 -0.06  14  e
    Germany                  -2601 -3.2  -5.5%     nan days   45969     57                0.78 -0.15   5  l
    Netherlands                610  3.5   2.0%     inf days   30788    178     [188, 189] 0.83  0.06   6  l
    Belgium                    349  3.0   1.3%     inf days   26194    223     [230, 231] 0.49 -0.11   4  e
    Iran                     -1075 -1.3  -6.0%     nan days   17492     21                0.48 -0.31   4  l
    Sweden                     399  3.9   3.0%     inf days   13517    132     [146, 151] 0.33  0.06   6  l
    Saudi Arabia              1104  3.2  10.9%     6.7 days   10846     32       [48, 59] 0.88 -0.06  14  e
    Japan                       24  0.0   0.2%     inf days    9875    7.9                0.51  0.60   6  l
    Singapore                 1374   22  16.9%     4.4 days    9233    149     [277, 384] 0.88 -0.10  13  e
    Switzerland               -600 -7.1  -8.5%     nan days    6859     82                0.43 -0.10   7  l
    Belarus                    667  7.0  12.0%     6.1 days    6454     68     [107, 135] 0.10 -0.20   5  l
    Austria                   -143 -1.6  -4.4%     nan days    3087     35                0.60  0.19   7  l
    Denmark                   -234 -4.0  -9.3%     nan days    2441     42                0.66 -0.15  14  l
    Hungary                     64  0.7   6.8%    10.5 days    1648     17       [20, 23] 0.48 -0.12   5  e
    Korea, South               -63 -0.1  -2.8%     nan days    2179    4.2                0.42  0.04   5  l
    China                      -30 -0.0  -2.1%     nan days    1371   0.10                0.36  0.18   6  l


In the following tables, all curve fitting used the cumulative case numbers, not the daily increments.

    Country              Increment Incr. Growth   Doubling  Active     per      Estimate   R^2  Diff. Win- Exp/Lin
                                    per   rate      time     Cases   100,000                          dow
                                  100,000                                                             size

23 April 2020

    US                       23772  7.1   3.4%    20.9 days  715726    215     [246, 263] 1.00  0.00   4  e
    United Kingdom            4300  6.5   3.8%    52.8 days  115395    175     [203, 216] 1.00  0.01  13  l
    Italy                      853  1.4   0.8%   252.5 days  107699    173     [182, 185] 0.87  0.02  14  l
    Spain                     1688  3.4   1.7%   119.2 days  100757    201     [218, 225] 0.90  0.02  11  l
    France                    3672  5.4   3.8%    52.3 days   93863    138                0.77  0.14  14  l
    Russia                    4820  3.4   9.5%    21.1 days   53066     37       [51, 58] 1.00  0.00   6  l
    Germany                  -2253 -2.8  -4.8%     nan days   45969     57                1.00 -0.00   4  l
    Netherlands                855  4.9   2.8%    71.4 days   30788    178     [199, 209] 1.00  0.01  12  l
    Belgium                    701  6.0   2.7%    74.4 days   26194    223     [249, 261] 0.99  0.01  14  l
    Iran                      -536 -0.6  -3.0%     nan days   17492     21                0.99  0.02  12  l
    Sweden                     533  5.2   4.0%    17.6 days   13517    132     [157, 170] 1.00  0.01  14  e
    Saudi Arabia               993  2.9   9.6%    20.9 days   10846     32       [43, 49] 1.00  0.00   4  l
    Japan                      468  0.4   4.8%    41.7 days    9875    7.9       [10, 11] 0.97  0.06  14  l
    Singapore                 1448   23  16.6%     4.5 days    9233    149     [279, 379] 1.00  0.02  13  e
    Switzerland               -524 -6.2  -7.5%     nan days    6859     82                0.99 -0.01   6  l
    Belarus                    692  7.3  11.0%     6.6 days    6454     68     [109, 134] 0.97  0.07  13  e
    Austria                   -368 -4.1 -11.3%     nan days    3087     35                0.98 -0.06  14  l
    Denmark                   -141 -2.4  -5.6%     nan days    2441     42                0.98  0.02   8  e
    Hungary                     60  0.6   3.7%    19.2 days    1648     17       [19, 21] 0.99 -0.00   5  e
    Korea, South               -79 -0.2  -3.6%     nan days    2179    4.2                1.00 -0.01  13  l
    China                      -44 -0.0  -3.2%     nan days    1371   0.10                0.99 -0.01  10  e


18 April 2020

    US                       25014  7.5   4.2%    16.8 days  604388    182     [214, 233] 1.00  0.00   4  e
    Italy                     1381  2.2   1.3%   154.6 days  106962    171     [182, 187] 0.99  0.01  13  l
    Spain                      721  1.4   0.8%   248.1 days   90836    182     [186, 189] 0.88 -0.01  13  l [1 day earlier]
    France                    3795  5.6   4.0%    17.7 days   94868    140     [165, 178] 0.91  0.01   6  e
    United Kingdom            4189  6.4   4.6%    43.8 days   94116    143     [168, 181] 1.00 -0.00   8  l
    Germany                  -2066 -2.6  -3.7%     nan days   53931     67                0.99  0.00   6  l
    Russia                    4059  2.9  14.9%     5.0 days   29145     21       [36, 47] 1.00  0.00   5  e
    Netherlands                933  5.4   3.6%    56.1 days   26740    155     [177, 188] 1.00  0.00  14  l
    Belgium                    704  6.0   3.1%    64.5 days   23014    196     [220, 232] 0.99 -0.00  14  l
    Iran                      -559 -0.7  -2.7%     nan days   20472     24                1.00 -0.00   7  l
    Sweden                     445  4.4   4.1%    17.4 days   11266    110     [129, 140] 1.00 -0.01   9  e
    Switzerland               -440 -5.2  -4.7%     nan days    9351    111                0.95 -0.01   9  l
    Japan                      527  0.4   6.5%    30.8 days    8662    6.9         [8, 9] 0.99 -0.04  11  l
    Saudi Arabia               596  1.7  10.6%     6.9 days    6006     18       [26, 32] 1.00 -0.01   8  e
    Austria                   -601 -6.8 -12.6%     nan days    4460     50                0.98  0.01   4  l
    Singapore                  687   11  17.1%     4.4 days    4331     70     [130, 178] 1.00 -0.01   6  e
    Denmark                   -106 -1.8  -3.1%     nan days    3348     57                0.96  0.01   5  l
    Hungary                     69  0.7   5.1%    39.6 days    1400     14       [18, 19] 0.96  0.03  14  l
    Korea, South               -74 -0.1  -2.8%     nan days    2576    5.0                0.99 -0.00  13  e
    China                      -62 -0.0  -3.8%     nan days    1572   0.11                0.99  0.00   5  l


15 April 2020


    US                       26250  7.9   5.0%    39.9 days  534075    161     [196, 212] 1.00  0.02  14  l
    Italy                     1606  2.6   1.5%    45.2 days  104291    167     [179, 184] 0.99  0.01  10  e
    Spain                     1117  2.2   1.3%   156.2 days   86981    174     [189, 194] 0.86  0.04  14  l
    France                    2539  3.7   2.8%    70.8 days   85719    126     [154, 161] 0.85  0.10  11  l
    United Kingdom            4314  6.6   5.4%    36.9 days   81766    124     [151, 164] 1.00 -0.00   5  l
    Germany                  -1667 -2.1  -2.7%     nan days   59865     75                0.90  0.01   4  l
    Netherlands                937  5.4   3.9%    50.9 days   24224    140     [162, 172] 1.00 -0.00  14  l
    Iran                      -556 -0.7  -2.5%     nan days   22065     26                0.99  0.00   4  l
    Belgium                    664  5.7   3.3%    60.4 days   20094    171     [198, 210] 0.99  0.02  11  l
    Switzerland               -268 -3.2  -2.4%     nan days   11062    132                0.95 -0.00  14  l
    Sweden                     425  4.2   4.3%    16.4 days   10031     98     [117, 127] 1.00  0.00   6  e
    Japan                      762  0.6  11.6%     6.3 days    6703    5.3      [8.7, 11] 0.99  0.07  14  e
    Austria                   -306 -3.5  -4.9%     nan days    6209     70                0.99 -0.02  12  l
    Denmark                    143  2.4   3.8%    52.3 days    3697     63                0.88  0.12  14  l
    Hungary                    105  1.1   8.4%     8.5 days    1268     13       [19, 22] 0.97  0.05  14  e
    Korea, South               -83 -0.2  -2.9%     nan days    2808    5.4                0.99 -0.01  14  e
    China                      -54 -0.0  -3.0%     nan days    1761    0.1                0.87 -0.08  14  e
    


&nbsp;

    Country             Growth rate  Doubling    Active    per       Estimate    R^2  Diff. Win- Exp/Lin
                                                 Cases   100,000                            dow
                                                                                            size

11 April 2020

    US                       6.5%    30.9 days   449159    135      [169, 187]  1.00 -0.00   4  l
    Italy                    1.5%    46.8 days    98273    157      [167, 172]  1.00 -0.00   4  e
    France                   3.9%    50.7 days    86740    127      [148, 158]  0.96  0.00   7  l
    Spain                    0.7%   103.9 days    86524    172      [177, 179]  0.95 -0.00   4  e
    Germany                 -3.2%     nan days    65491     81        [67, 62]  0.71 -0.04   5  l
    United Kingdom           6.1%    32.8 days    64456     98      [118, 130]  0.99 -0.04  11  l
    Iran                    -3.7%     nan days    28495     33        [28, 26]  0.99  0.00   4  l
    Netherlands              4.2%    47.3 days    20336    117      [135, 145]  1.00 -0.02  13  l
    Belgium                  4.5%    15.9 days    18080    154      [183, 200]  1.00  0.00   7  e
    Switzerland             -0.8%     nan days    12449    148      [143, 140]  0.97 -0.00   5  e
    Sweden                   6.4%    11.2 days     8434     82      [106, 120]  0.99  0.01   9  e
    Austria                 -4.0%     nan days     7172     80        [70, 63]  0.97  0.03   8  l
    Japan                   11.6%     6.3 days     4746      3          [5, 6]  0.99 -0.06  12  e
    Denmark                  5.4%    37.1 days     3799     64        [80, 87]  0.99  0.02  10  l
    Hungary                  7.8%     9.3 days     1001     10        [12, 14]  0.98 -0.14  13  e
    Korea, South            -2.8%     nan days     3125      6          [5, 5]  0.99  0.01  14  e
    China                   -2.8%     nan days     1810      0          [0, 0]  1.00  0.00   6  l


30 March 2020

    US                      13.2%    15.2 days   135754     40        [62, 73]  1.00 -0.00   5  l
    Italy                    5.3%    37.8 days    73880    118      [143, 155]  1.00 -0.00  10  l
    Spain                    6.9%    29.1 days    58598    117      [149, 166]  1.00  0.00   4  l
    Germany                  9.0%    22.2 days    52351     65       [89, 101]  1.00  0.01   6  l
    France                  11.7%     6.3 days    30366     44        [72, 90]  0.99  0.05  12  e
    Iran                     9.5%    21.1 days    23278     27        [37, 43]  1.00  0.00   4  l
    United Kingdom          12.9%    15.5 days    18159     27        [41, 49]  1.00  0.00   5  l
    Switzerland              7.0%    28.8 days    12934    153      [203, 225]  0.98  0.05  14  l
    Netherlands              9.6%    20.8 days     9845     56        [79, 90]  1.00  0.01   6  l
    Belgium                 20.2%     3.8 days     9046     77      [161, 233]  1.00  0.01   6  e
    Austria                  8.3%    24.2 days     8223     92      [126, 142]  0.99  0.04  11  l
    Sweden                   9.7%     7.5 days     3574     35        [50, 60]  1.00  0.00  14  e
    Denmark                  8.3%     8.7 days     2322     39        [54, 63]  1.00  0.00   6  e
    Japan                   12.8%     5.7 days     1388      1          [1, 2]  0.98 -0.01   4  e
    Hungary                 18.4%     4.1 days      361      3         [7, 10]  1.00  0.02  13  e
    Korea, South            -4.4%     nan days     4398      8          [7, 6]  0.98 -0.02   6  e
    China                  -11.4%     nan days     3236      0          [0, 0]  1.00 -0.01   9  l

&nbsp;
In the following tables, all curve fitting used the exponential model.

    Country             Growth rate  Doubling ActiveCases per100000  Estimate    R^2  Diff. Window size

30 March 2020

    US                      18.4%     4.1 days   135754     40       [81, 114]  0.99  0.02   4
    Italy                    6.6%    10.9 days    73880    118      [154, 175]  1.00  0.01   7
    Spain                    8.0%     9.0 days    58598    117      [160, 187]  0.99  0.01   4
    Germany                 11.8%     6.2 days    52351     65      [103, 129]  0.99  0.03  10
    France                  11.7%     6.3 days    30366     44        [72, 90]  0.99  0.05  12
    Iran                    11.4%     6.4 days    23278     27        [42, 52]  1.00  0.01   5
    United Kingdom          19.4%     3.9 days    18159     27        [57, 82]  1.00  0.04  10
    Switzerland              8.8%     8.2 days    12934    153      [228, 270]  0.93  0.09   9
    Netherlands             14.3%     5.2 days     9845     56      [101, 132]  1.00  0.06   9
    Belgium                 20.2%     3.8 days     9046     77      [161, 233]  1.00  0.01   6
    Austria                 11.2%     6.5 days     8223     92      [150, 186]  0.96  0.09   7
    Sweden                   9.7%     7.5 days     3574     35        [50, 60]  1.00  0.00  14
    Denmark                  8.3%     8.7 days     2322     39        [54, 63]  1.00  0.00   6
    Japan                   12.8%     5.7 days     1388      1          [1, 2]  0.98 -0.01   4
    Hungary                 18.4%     4.1 days      361      3         [7, 10]  1.00  0.02  13
    Korea, South            -4.4%     nan days     4398      8          [7, 6]  0.98 -0.02   6
    China                   -7.9%     nan days     3236      0          [0, 0]  1.00  0.02  14

&nbsp;

    Country             Growth rate   Doubling  Active cases  Estimate      R^2  Diff. Window size

28 March 2020

    US                      23.5%     3.3 days    99207  [231517, 352961]  1.00  0.01   5
    Italy                    7.2%    10.0 days    66414   [87627, 100681]  1.00 -0.00   4
    Spain                   16.3%     4.6 days    51224   [97340, 131693]  1.00  0.05   9
    Germany                 13.9%     5.3 days    43871    [73559, 95511]  1.00 -0.01   4
    France                  12.1%     6.1 days    25269    [39851, 50080]  1.00 -0.00   4
    Iran                    10.3%     7.1 days    18821    [27653, 33661]  1.00 -0.01   4
    United Kingdom          21.4%     3.6 days    13649    [29127, 42913]  1.00 -0.02   5
    Switzerland             17.3%     4.4 days    11167    [27007, 37131]  0.96  0.36  13
    Netherlands             15.1%     4.9 days     8054    [14147, 18757]  1.00 -0.00   4
    Austria                 19.2%     3.9 days     7374    [16478, 23430]  0.99  0.14  11
    Belgium                 17.4%     4.3 days     6137    [11868, 16351]  0.99  0.03  13
    Sweden                   9.5%     7.7 days     2948      [4233, 5072]  1.00  0.00  13
    Denmark                  8.6%     8.4 days     1993      [2767, 3261]  1.00 -0.00   4
    Japan                    5.2%    13.6 days     1047      [1274, 1412]  0.97 -0.01   8
    Hungary                 18.8%     4.0 days      256        [530, 748]  1.00  0.06  11
    Korea, South            -5.5%     nan days     4665      [3720, 3320]  0.97  0.00   5
    China                   -7.6%     nan days     3881      [2868, 2451]  1.00  0.02  10

&nbsp;

    Country             Growth rate   Doubling  Total cases  Estimate       R^2  Diff. Window size

24 March 2020 (total number of confirmed cases without deaths or recoveries)

    Italy                   13.1%     5.6 days    63927  [108776, 139105]  1.00  0.06   9
    US                      31.8%     2.5 days    43290  [130768, 227080]  1.00  0.00   4
    Spain                   19.9%     3.8 days    35136   [73146, 105158]  1.00  0.01   8
    Germany                 13.4%     5.5 days    29056    [47418, 60965]  0.99 -0.02   4
    Iran                     5.4%    13.1 days    21237    [26165, 29082]  1.00 -0.00   6
    France                  16.6%     4.5 days    19856    [36039, 48984]  1.00 -0.03   8
    Switzerland             18.0%     4.2 days     8795    [17148, 23857]  0.99  0.01   4
    United Kingdom          24.0%     3.2 days     6650    [16810, 25860]  0.99  0.10  11
    Netherlands             19.4%     3.9 days     4749    [10132, 14450]  1.00  0.07   8
    Austria                 23.1%     3.3 days     4474    [10263, 15557]  1.00 -0.00  10
    Belgium                 20.8%     3.7 days     3743     [8359, 12191]  1.00  0.07   9
    Sweden                   9.6%     7.6 days     2046      [3015, 3622]  0.99  0.03   9
    Denmark                  5.0%    14.3 days     1450      [1767, 1947]  0.99  0.01   4
    Japan                    5.2%    13.8 days     1128      [1384, 1530]  0.98  0.01   6
    Hungary                 25.4%     3.1 days      167        [409, 643]  1.00 -0.01   4
    Korea, South             1.2%    56.6 days     8961      [9445, 9680]  0.99  0.01  13
    Hubei                    0.0%     inf days    67800    [67800, 67800]  1.00  0.00   4

&nbsp;

    Country             Growth rate   Doubling  Active cases  Estimate      R^2  Diff. Window size

20 March 2020

    Italy                   12.9%     5.7 days    33190    [53627, 68355]  1.00 -0.01   6
    Spain                   21.5%     3.6 days    16026    [33714, 49788]  0.99 -0.05   7
    Germany                 27.2%     2.9 days    15163    [39618, 64138]  1.00 -0.00   7
    Iran                     7.1%    10.1 days    11413    [15093, 17316]  0.97  0.01   5
    France                  17.9%     4.2 days    10864    [20807, 28939]  1.00 -0.01   4
    Switzerland             26.4%     3.0 days     4019    [10758, 17183]  0.99  0.07  14
    United Kingdom          25.4%     3.1 days     2487     [6940, 10907]  0.99  0.18  14
    Netherlands             20.3%     3.8 days     2453      [5138, 7433]  1.00  0.00   4
    Austria                 25.2%     3.1 days     1998      [4980, 7800]  1.00  0.02   6
    Sweden                   8.3%     8.7 days     1412      [1919, 2252]  0.99 -0.02   5
    Denmark                  5.5%    12.9 days     1077      [1311, 1460]  0.98 -0.03   6
    Japan                    6.0%    11.9 days      745       [999, 1123]  0.97  0.09  14
    Hungary                 23.3%     3.3 days       70        [160, 243]  1.00 -0.01   5
    Korea, South            -2.1%     nan days     6934      [6177, 5917]  0.71 -0.04   6
    China                   -0.0%     nan days    65149    [65130, 65120]  0.93  0.00   4


19 March 2020

    Italy                   11.8%     6.2 days    28710    [45147, 56451]  1.00  0.01   4
    Spain                   20.7%     3.7 days    12206    [26317, 38309]  0.99  0.03   6
    Germany                 27.7%     2.8 days    12194    [31773, 51852]  1.00 -0.03   5
    Iran                    10.2%     7.2 days    10837    [17009, 20640]  0.97  0.09  13
    France                  24.3%     3.2 days     9037    [22983, 35515]  0.99  0.09  13
    Switzerland             26.6%     2.9 days     2985     [8703, 13953]  0.98  0.18  13
    United Kingdom          30.7%     2.6 days     2490     [7189, 12276]  1.00 -0.01   4
    Netherlands             20.8%     3.7 days     2044      [4353, 6356]  1.00 -0.00   6
    Austria                 26.6%     2.9 days     1633      [4266, 6843]  1.00  0.02   6
    Sweden                   7.6%     9.4 days     1268      [1703, 1972]  1.00  0.00   4
    Denmark                  4.9%    14.5 days      995      [1191, 1311]  0.99 -0.02   5
    Japan                    6.3%    11.4 days      716       [969, 1094]  0.97  0.09  13
    Hungary                 22.8%     3.4 days       55        [127, 192]  0.99  0.03   4
    Korea, South            -3.0%     nan days     6789      [5948, 5597]  0.86 -0.02   5
    China                    0.0% 11254.5 days    65157    [65185, 65193]  0.70  0.00  10


18 March 2020

    Italy                   13.5%     5.5 days    26062    [43435, 55945]  1.00  0.01   4
    Spain                   21.3%     3.6 days    10187    [22585, 33222]  0.99  0.04   5
    Iran                    10.5%     7.0 days     9792    [15956, 19475]  0.97  0.13  12
    Germany                 26.4%     3.0 days     9166    [23294, 37194]  1.00 -0.00   4
    France                  24.7%     3.1 days     7647    [19099, 29683]  0.99  0.05  12
    Switzerland             27.3%     2.9 days     2669     [7335, 11896]  0.98  0.06  12
    United Kingdom          26.6%     2.9 days     1843      [4785, 7667]  0.99  0.02  14
    Netherlands             20.4%     3.7 days     1659      [3474, 5037]  1.00 -0.01   5
    Austria                 27.2%     2.9 days     1328      [3473, 5623]  0.99 -0.00   5
    Sweden                   7.3%     9.8 days     1182      [1561, 1797]  1.00 -0.00   4
    Denmark                  4.3%    16.4 days      926      [1099, 1196]  1.00  0.00   4
    Japan                    7.2%    10.0 days      705       [983, 1130]  0.97  0.08  14
    Hungary                 24.3%     3.2 days       47        [111, 171]  0.98 -0.01  10
    Korea, South            -3.5%     nan days     6832      [5938, 5528]  0.84  0.00   4
    China                    0.0% 11854.3 days    65162    [65183, 65190]  0.83  0.00   8


12 March 2020

    Italy            22.3%    3.44 days    10590    [24045, 35971]  0.99   0.31
    France           33.5%    2.40 days     2278     [7271, 12962]  0.98   0.42
    Spain            38.6%    2.12 days     2039     [6980, 13418]  0.99   0.36
    Germany          36.4%    2.23 days     2050                    0.97   0.54
    Switzerland      39.3%    2.09 days      644                    0.97   0.67
    Japan             8.4%    8.59 days      505        [695, 817]  0.98   0.11
    Denmark          58.5%    1.50 days      613      [1630, 4096]  0.95  -0.58
    Netherlands      55.0%    1.58 days      498                    0.93   1.12
    Sweden           43.2%    1.93 days      597      [2191, 4495]  0.98   0.32
    United Kingdom   30.3%    2.62 days      453                    0.98   0.51
    Austria          37.2%    2.19 days      297       [901, 1697]  0.97   0.23
    Korea, South      8.5%    8.52 days     7470                    0.84   0.29
    China             0.2%  365.94 days    65152                    0.79   0.01


### Please donate if you can

If you can afford to support my work, then please consider donating. Thank you!

* Address for bitcoin (BTC): `13veK2ecjhtNenTxhGKJjP83QiMmNd1M7p`
* Address for ether (ETH) and tokens: `0x49fC2a73e1eC76248324E411e699f92adD6565Ff`

Find me on [Twitter (@BMelykuti)](https://www.twitter.com/BMelykuti), on my website/blog: [Melykuti.me](https://melykuti.me), or follow me on [Facebook](https://www.facebook.com/bence.melykuti) for my public posts.

I work as a data science freelancer. You can contact me with your project proposal.
