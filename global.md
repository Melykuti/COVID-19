## Analysis of the spread of the SARS-CoV-2 coronavirus

> * Recall that on this page I examine the number of currently infected patients and not the cumulative number of all who have been infected and might have recovered or died.
> * If you already know my methodology, just skip down to the Plots and the Results sections.

13 March 2020 (updated on 23 April 2020), Freiburg i. Br., Germany, where a lockdown has been in force since 21 March 2020. -- The WHO releases [daily situation reports](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports) with the numbers of diagnosed COVID-19 cases for each country. We can see the total number of confirmed cases and the total deaths since the beginning of the outbreak. We also get the changes from the last report, that is, these two figures for the last day only.

Thinking in terms of the classical SIR model of epidemiology, the population comprises three groups: **S**usceptibles, **I**nfected and **R**emoved. _Removed_ are those who have recovered from or died of the disease and thereby are no longer infectious and can no longer catch the disease. _Infected_ are the current patients who are also all infectious. _Susceptibles_ are everybody else: people who have not been infected yet (and hopefully will never be).

In the initial stage of an epidemic, we expect that most contacts by infected people will be with a susceptible person. This provides a fertile ground for the disease to spread. The number of infected people is rising exponentially (in the mathematical, not in the vague and overused marketing sense) until there are so many of them that it is becoming harder for the disease to find susceptibles.

**Unfortunately, most countries saw exponential growth of case numbers without introducing lockdowns. (As far as I know, Singapore, South Korea, Taiwan are a few which have avoided this.) With lockdowns in force for three weeks now, a deceleration of growth is seen in Italy, Spain, Germany, France.**

Exponential growth means that from one day to the next, the total number of infected people increases not by a fixed number but by a fixed multiple. In any one hospital, the number of new patients per day is not the same as the number of new patients was yesterday. Instead, it is increasing by the same factor every day. For example, today the hospital gets 11 new patients, tomorrow 13, the day after 16, on day&nbsp;4 already 19, on day&nbsp;5 23. If the stream doesn't stop, then on day&nbsp;10 it will be 57 new patients, and so on. Each patient spends one to three weeks hospitalised, and the people being removed from the hospital are the lower numbers that arrived one to three weeks ago. If you are medical personnel and had a hard day at work, you can be sure that tomorrow will be even harder, the day after still harder. There is no system capable of meeting this demand.

**Our intuition is also caught off guard. The risk of contracting the disease is not constant; it is increasing by the same factor every day. It's silently, imperceptibly creeping up until the disease is everywhere around us unless we stop it.**

### How shall I think about the danger which I'm exposed to?...

_What is the probability of coming into contact with the disease if I leave my home?_ While I cannot answer that, a good proxy is the number of currently infected people.

Some of the infected people will be in hospital, some at home, but some will be around us on the streets, in the grocery shops, on public transport. I assume that the ratio between infected people in isolation (in hospital or at their home) and those among us is independent of how many people are infected in total. With the growth of the infected population, the count of infected people on the street and in grocery shops grows proportionally (unless social distancing takes hold or a lockdown is introduced and people start avoiding public spaces).

**From day to day, your chance of encountering an infected person on the street is growing by a fixed factor as long as the disease is spreading exponentially (and people don't vanish from the streets). The daily growth rate of cases across several countries was about 15-30% without extreme control measures, such as a lockdown.**


### Data

The Center for Systems Science and Engineering at the Johns Hopkins University is kindly providing [the time series data with daily sampling frequency in tabular format](https://github.com/CSSEGISandData).

Remember that the true number of cases is probably multiple times higher than the number of confirmed cases. For an extreme example, on the 27th March, Scotland’s Chief Medical Officer Catherine Calderwood [estimated that more than 65,000 people in Scotland had the virus](https://www.bbc.com/news/live/world-52058788) when confirmed cases stood at 1059.

### Program files

* **download_JHU_CSSE.py** is a script to download three csv data tables: the number of confirmed cases, the number of deaths due to the disease, and the number of recovered patients, broken down to countries. The script automatically inserts the timestamp of download into the file names so that later downloads do not overwrite downloaded data.

* **utils.py** contains the universal data selection, preprocessing, analysis and plotting functionalities. It searches for the most recent download of `download_JHU_CSSE.py` in the current directory based on the timestamp in the file name. If you want to select a particular one, then modify the variable `timestamp` in `open_csvs()`.

* **analysis_single.py** runs the analysis and plots or saves a graph for a single country.

* **analysis_joint.py** calls the analysis and optionally saves plots repeatedly on a list of countries.

### Analysis

I compute the number of currently infectious people as the number of total confirmed cases minus the number of deaths minus the number of recovered patients for all days where there is data:

`no. of currently infected = no. of cases - no. of deaths - no. of recovered.`

(On 24 March 2020, I reported the total number of confirmed cases for each country because the number of recoveries was not included in the JHU CSSE dataset.)

#### Exponential growth model

Originally, my analysis was founded on the assumption that the growth of this number is exponential. In this case, I take the base&nbsp;2 logarithm of this time series for a selected country, and fit a straight line to the last 4-14 days of data with _ordinary least squares (OLS)_. If the growth is exponential or thereabouts, then this should fit quite well and the slope of this line will tell us the growth rate. The length of this time window is optimised to provide the best linear fit.

From this slope I compute:

1. The growth factor per day, which I express in percentage terms. (What percentage more infectious people we expect tomorrow than we had today.)

2. How many days it takes for the number of infectious people to double.

3. I make a crude estimate of what I guess the total number of infected people might currently be.

The third one is only my guesswork. The idea is that in the case of a SARS-CoV-2 infection, it takes on average 5-6 days to develop symptoms (fever, a usually dry cough and others). This incubation time varies between 1 to 14 days. The people who were infected today will present symptoms and will be tested perhaps 4-6 days from now. They will enter the figure in the situation report only thereafter. Also, they are likely to be already infectious sooner than that and that is what worries us as common people.

So I project from my linear regression the number of infected four, respectively, six days from the latest data point, and that is the estimate for the current total case number. This is probably too conservative and may be a low estimate not only because many cases never get tested and recorded but also because from developing symptoms, one still needs perhaps 1-3 days to get tested and for the test result to enter the international statistical tables. There are also wide differences between how much testing different countries do; low testing intensity is bound to bias the confirmed case number downwards.

The exponential curve is not always a good fit (a straight line is not always a good fit to the logarithm of the current case number). Especially after the introduction of draconian countermeasures, such as a lockdown, the growth slowed substantially.

#### Linear growth model

As long as I was fitting exponential models, the interpretation could only be that growth was exponential. Towards the end of March and beginning of April, this no longer held for many countries. Once the daily new case number starts to stabilise, it is natural to fit a linear model. The procedure is the same but I fit to the case numbers and not to their logarithms.

The first dataset is the 30 March 2020 where I tried fitting linear models in addition to the exponentials as well. I had originally presented exponential fits exclusively. Upon the switchover to the new methodology, I also show the fits where I selected the best of exponential and linear fits for comparison. The last column in the table now displays `e` for the case when the exponential model is a better fit, `l` when the linear model.

The _doubling time_ is by nature a notion best suited for exponential growth. I compute it for linear growth, too, although it is less meaningful. In exponential growth, after twice the doubling time, there will be four times the original case number. After `n` times the doubling time, you have got `2^n` times the original count. In linear growth, after twice the doubling time, you have got only three times the original count. After `n` times the doubling time, you have got `n+1` times the original count.

The next columns of the table are used to compare the two models and to compare different window lengths:

4. The [R^2 or coefficient of determination](https://en.wikipedia.org/wiki/Coefficient_of_determination) of the linear regression fit (which I can't explain here). The closer it is to 1, the better the match is between the data and my linear regression. This is straightforward for both the exponential and the linear models, it is just so that for the exponential model, the linear fit happens for the logarithm of the time series.

5. I also compute the difference between the value of the fitted straight line for the last day when we have data and the real observation _in the logarithmic space_ for that last day.  
For the _exponential model_, this is indeed a difference. You can interpret this number as a ratio between the linear approximation and the data because it is a difference between the logarithms. For the _linear model_, this is the ratio of the fitted line on the last available day and the real observation for the last available day, minus 1.  
If the spread is slowing relative to the exponential rate, then this number will be great and the projection is definitely unreliable. If this difference is small, then the projection might well be good. When the difference is negative, then the projection will be an underestimate of the true case number!

The automatic selection of the window length minimises the l_2 norm of the two-dimensional vector  
`(10 * (1-R^2), difference between projection and last data point in base 2 logarithmic space).`  
So I minimise both 1-R^2 and the difference between the fitted line and the true data point (only for the most recent date). The factor of 10 is there to weigh one relative to the other. Note that the difference is in log2 space so it is a factor in linear space. So R^2=0.99 gives first coordinate 10*0.01 = 0.1, and to get the same second coordinate of 0.1, you'd have a ratio of 2^0.1 = 1.072 between linear fit and actual data for the last available data point. This is how the two errors trade off in my window length selection.

To choose between the exponential and the linear models, once I have selected the optimal window size independently for each, I choose the model where this l_2 norm is smaller.

Even when the daily increments have stabilised and the growth is clearly only linear, it can happen that both the exponential and the linear models fit well in the time window and the optimisation selects the exponential as the slightly better one. Therefore one should not attribute too much importance to preference for the exponential model over the linear one.

I show projections for the number of infected 4-to-6 days from now (which, as I said, is what I guess to be the real number of cumulative coronavirus cases today) only if (the R^2 is greater than or equal to 0.95 and the above difference is not greater than 0.5) or if the difference is in [-0,2;&nbsp; 0,1]. Since 15 April 2020, I have omitted the projections also when active case numbers are decreasing.

### Plots

The plots for each individual country present the observed total number of infected on the left panel, and the same data on logarithmic scale on the right panel. These lines are in blue.

If the exponential model fits better, then orange is the fit of the exponential curve, which is the same as the fit of a straight line on logarithmic scale (on the right panel). If the linear model fits better, then pink is the linear fit, which is the same as the fit of a straight line on natural scale (on the left panel).

![US](https://github.com/Melykuti/COVID-19/blob/master/plots/US_2020-04-22.png)

![United Kingdom](https://github.com/Melykuti/COVID-19/blob/master/plots/United_Kingdom_2020-04-22.png)

![Italy](https://github.com/Melykuti/COVID-19/blob/master/plots/Italy_2020-04-22.png)

![Spain](https://github.com/Melykuti/COVID-19/blob/master/plots/Spain_2020-04-22.png)

![France](https://github.com/Melykuti/COVID-19/blob/master/plots/France_2020-04-22.png)

![Russia](https://github.com/Melykuti/COVID-19/blob/master/plots/Russia_2020-04-22.png)

![Germany](https://github.com/Melykuti/COVID-19/blob/master/plots/Germany_2020-04-22.png)

![Netherlands](https://github.com/Melykuti/COVID-19/blob/master/plots/Netherlands_2020-04-22.png)

![Belgium](https://github.com/Melykuti/COVID-19/blob/master/plots/Belgium_2020-04-22.png)

![Iran](https://github.com/Melykuti/COVID-19/blob/master/plots/Iran_2020-04-22.png)

![Sweden](https://github.com/Melykuti/COVID-19/blob/master/plots/Sweden_2020-04-22.png)

![Saudi Arabia](https://github.com/Melykuti/COVID-19/blob/master/plots/Saudi_Arabia_2020-04-22.png)

![Japan](https://github.com/Melykuti/COVID-19/blob/master/plots/Japan_2020-04-22.png)

![Singapore](https://github.com/Melykuti/COVID-19/blob/master/plots/Singapore_2020-04-22.png)

Switzerland added 1399 recovered patients on 27 March (cumulative number went from 131 to 1530). This is why the currently infected cases dropped substantially on that date.

![Switzerland](https://github.com/Melykuti/COVID-19/blob/master/plots/Switzerland_2020-04-22.png)

![Belarus](https://github.com/Melykuti/COVID-19/blob/master/plots/Belarus_2020-04-22.png)

![Austria](https://github.com/Melykuti/COVID-19/blob/master/plots/Austria_2020-04-22.png)

Denmark added 893 recovered patients on 1 April (cumulative number went from 1 to 894). This is why the currently infected cases dropped so much on that date.

![Denmark](https://github.com/Melykuti/COVID-19/blob/master/plots/Denmark_2020-04-22.png)

![Hungary](https://github.com/Melykuti/COVID-19/blob/master/plots/Hungary_2020-04-22.png)

![South Korea](https://github.com/Melykuti/COVID-19/blob/master/plots/Korea__South_2020-04-22.png)

![China](https://github.com/Melykuti/COVID-19/blob/master/plots/China_2020-04-22.png)


### Results

The columns have the following meaning:

* (Since 15 April 2020) The number of currently infected people changes daily by this number right now

* (Since 15 April 2020) The number of currently infected people per 100,000 population changes daily by this number right now

* The number of currently infected people increases daily by this percentage

* Time it takes for the number of currently infected people to double

* Latest reported total number of currently infected cases

* (Since 30 March 2020) Latest reported total number of currently infected cases per 100,000 population

* My estimate for total number of currently infected cases at present. (Since 30 March 2020, per 100,000 population. I describe at the end of the Analysis why it is missing in certain cases.)

* R^2 of linear regression fit

* Difference between linear fit and real data in logarithmic space for the last data point

* (Since 18 March 2020) The number of days in the time window in which I fit the linear regression. It is automatically optimised to minimise the vector (10 * (1-R^2), difference) in l_2.

* (Since 11 April 2020) e if the exponential model, l if the linear model provides the better fit and yielded the entries in the specific row of the table.

I focus on countries with a large number of cases and on those to which I have got some personal connection. China and South Korea are examples where the preventative measures have slowed down the epidemic spread massively.
&nbsp;

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

If you can afford to support my work, then please consider donating to my [Ocean Plastic Detector](https://www.gofundme.com/OceanPlasticDetector) project.

Find me on [Twitter (@BMelykuti)](https://www.twitter.com/BMelykuti), on my website/blog: [Melykuti.me](https://melykuti.me), or follow me on [Facebook](https://www.facebook.com/bence.melykuti) for my public posts.

I work as a data science freelancer. You can contact me with your project proposal.