## Analysis and projections for the spread of the SARS-CoV-2 coronavirus

> * For plots and results, scroll down to the sections with these titles.
> * [The analogous study for Germany and its federal states in German language.](https://github.com/Melykuti/COVID-19/blob/master/Deutschland.md)
> * [NEW! A comparison of countries how well they are tackling the pandemic in terms of innovative visualisations.](https://github.com/Melykuti/COVID-19/blob/master/comparison.md)

13 March 2020 (updated on 24 March 2020), Freiburg i. Br., Germany, where a lockdown is in force from 21 March 2020. -- The WHO releases [daily situation reports](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports) with the numbers of diagnosed COVID-19 cases for each country. We can see the total number of confirmed cases and the total deaths since the beginning of the outbreak. We also get the changes from the last report, that is, these two figures for the last day only.

Thinking in terms of the classical SIR model of epidemiology, the population comprises three groups: **S**usceptibles, **I**nfected and **R**emoved. _Removed_ are those who have recovered from or died of the disease and thereby are no longer infectious and can no longer catch the disease. _Infected_ are the current patients who are also all infectious. _Susceptibles_ are everybody else: people who have not been infected yet (and hopefully will never be).

In the initial stage of an epidemic, we expect that most contacts by infected people will be with a susceptible person. This provides a fertile ground for the disease to spread. The number of infected people is rising exponentially (in the mathematical, not in the vague and overused marketing sense) until there are so many of them that it is becoming harder for the disease to find susceptibles.

**Unfortunately, in many European countries we still observe exponential growth of case numbers. With lockdowns in force, I expect the growth to subside in a few days.**

This means that from one day to the next, the total number of infected people increases not by a fixed number but by a fixed multiple. In any one hospital, the number of new patients per day is not the same as the number of new patients was yesterday. Instead, it is increasing by the same factor every day. For example, today the hospital gets 11 new patients, tomorrow 13, the day after 16, on day 4 already 19, on day 5 23. The stream doesn't stop, on day 10 it is 57 new patients, and so on. Each patient spends one to three weeks hospitalised, and the people being removed from the hospital are the lower numbers that arrived one to three weeks ago. If you are medical personnel and had a hard day at work, you can be sure that tomorrow will be even harder, the day after still harder. There is no system capable of meeting this demand.

**Our intuition is also caught off guard. The risk of contracting the disease is not constant; it is increasing by the same factor every day. It's silently, imperceptibly creeping up until the disease is everywhere around us.**

### How shall I think about the danger which I'm exposed to?...

_What is the probability of coming into contact with the disease if I leave my home?_ While I cannot answer that, a good proxy is the number of currently infected people.

Some of the infected people will be in hospital, some at home, but some will be around us on the streets, in the grocery shops, on public transport. I assume that the ratio between infected people in isolation (in hospital or at their home) and those among us is independent of how many people are infected in total. With the growth of the infected population, the count of infected people on the street and in grocery shops grows proportionally (unless social distancing takes hold or a lockdown is introduced and people start avoiding public spaces).

**From day to day, your chance of encountering an infected person in the street is growing by a fixed factor as long as the disease is spreading exponentially (and people don't vanish from the streets). The daily growth rate of cases across several countries has been about 15-30% without extreme control measures, such as a lockdown.**


### Data

The Center for Systems Science and Engineering at the Johns Hopkins University is kindly providing [the time series data with daily sampling frequency in tabular format](https://github.com/CSSEGISandData).

### Program files

* **download_JHU_CSSE.py** is a script to download two csv data tables: the number of confirmed cases and the number of deaths due to the disease (before 24 March 2020 also the number of recovered patients), broken down to countries. The script automatically inserts the timestamp of download into the file names so that later downloads do not overwrite downloaded data.

* **utils.py** contains the universal data selection, preprocessing, analysis and plotting functionalities. It searches for the most recent download of `download_JHU_CSSE.py` in the current directory based on the timestamp in the file name. If you want to select a particular one, then modify the variable `timestamp` in `open_csvs()`.

* **analysis_single.py** runs the analysis and plots or saves a graph for a single country.

* **analysis_joint.py** calls the analysis and optionally saves plots repeatedly on a list of countries.

### Analysis

**Since 24 March 2020, I report the total number of confirmed cases for each country only.** Originally, I was computing the number of currently infectious people as the number of total cases minus the number of deaths minus the number of recovered patients for all days where there is data: `no. of currently infected = no. of cases - no. of deaths - no. of recovered`. But the number of recoveries is no longer included in my dataset.

The analysis is founded on the assumption that the growth of this number is exponential. Then I take the base 2 logarithm of this time series for a selected country, and fit a straight line to the last 4-14 days of data with _ordinary least squares (OLS)_. If the growth is exponential or thereabouts, then this should fit quite well and the slope of this line will tell us the growth rate. The length of this time window is optimised to provide the best linear fit.

From this slope I compute:

1. The growth factor per day, which I express in percentage terms. (What percentage more infected people we expect tomorrow than we had today.)

2. How many days it takes for the number of infected people to double.

3. I make a crude estimate of what I guess the total number of infected people might currently be.

This is only my guesswork and it will be controversial. The idea is that in the case of a SARS-CoV-2 infection, it takes on average 5-6 days to develop symptoms (fever, a usually dry cough and others). This incubation time varies between 1 to 14 days. The people who were infected today will present symptoms and will be tested perhaps 4-6 days from now. They will enter the figure in the situation report only then. Also, they are likely to be already infectious sooner than that and that is what worries us as common people.

So I project from my linear regression the number of infected four, respectively, six days from the latest data point, and that is the estimate for the current total case number. This is probably too conservative and may be a low estimate as many cases never get tested and recorded. There are also wide differences between how much testing different countries do.

The exponential curve is not always a good fit (a straight line is not always a good fit to the logarithm of the current case number). It seems that in several European countries, countermeasures do slow the spread from the uncontrolled exponential growth, although not much yet. To screen for this, I compute:

4. The [R^2 or coefficient of determination](https://en.wikipedia.org/wiki/Coefficient_of_determination) of the linear regression fit (which I can't explain here). The closer it is to 1, the better the match is between the data and my linear regression.

5. I also compute the difference between the value of the fitted straight line for the last day when we have data and the real observation (in the logarithmic space) for that last day. If the spread is slowing relative to the exponential rate, then this number will be high and the projection is definitely unreliable. If this difference is small, then the projection might well be good. When the difference is negative, then the projection will be an underestimate! You can interpret this number as a factor between the linear approximation and the data (because it is a difference between the logarithms).

The automatic selection of the window length minimises the l_2 norm of the two-dimensional vector  
`(10 * (1-R^2), difference between projection and last data point in base 2 logarithmic space).`

I show projections for the number of infected 4-to-6 days from now (which, as I said, is what I guess to be the real number of cumulative coronavirus cases today) only if (the R^2 is greater than or equal to 0.95 and the above difference is not greater than 0.5) or if the difference is in [-0,2;&nbsp; 0,1].

### Plots

The plots for each individual country present the observed total number of infected on the left panel, and the same data on logarithmic scale on the right panel. These lines are in blue. In orange is the fit of an exponential curve, which is the same as the fit of a straight line on logarithmic scale.

23 March 2020

![Italy until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Italy_2020-03-23.png)

![US until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/US_2020-03-23.png)

![Spain until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Spain_2020-03-23.png)

![Germany until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Germany_2020-03-23.png)

![Iran until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Iran_2020-03-23.png)

![France until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/France_2020-03-23.png)

![Switzerland until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Switzerland_2020-03-23.png)

![United Kingdom until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/United_Kingdom_2020-03-23.png)

![Netherlands until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Netherlands_2020-03-23.png)

![Austria until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Austria_2020-03-23.png)

![Belgium until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Belgium_2020-03-23.png)

![Sweden until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Sweden_2020-03-23.png)

![Denmark until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Denmark_2020-03-23.png)

![Japan until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Japan_2020-03-23.png)

![Hungary until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Hungary_2020-03-23.png)

![South Korea until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Korea__South_2020-03-23.png)

![Hubei province in China until 23 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Hubei_2020-03-23.png)


### Results

The columns have the following meaning:

* The number of currently infected people increases daily by this percentage

* Time it takes for the number of currently infected people to double

* Latest reported number of total cases

* My estimate for number of total cases at present. (I describe at the end of the Analysis why it is missing in certain cases.)

* R^2 of linear regression fit

* Difference between linear fit and real data in logarithmic space for the last data point

* (Since 18 March 2020) The number of days in the time window in which I fit the linear regression. It is automatically optimised to minimise the vector (10 * (1-R^2), difference) in l_2.

I focus on countries with a large number of cases and on those where I have got some personal connection. China and South Korea are examples where the preventative measures have slowed down the epidemic spread massively.

&nbsp;

    Country             Growth rate   Doubling  Total cases  Estimate       R^2  Diff. Window size

24 March 2020

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



### Requirements

The following Python&nbsp;3 packages are required. The version numbers are what I have got installed but they are not strict requirements. `beautifulsoup4` is used to parse Wikipedia tables for Germany (Deutschland.md).

`python3==3.7.6`  
`matplotlib==3.0.3`  
`numpy==1.16.4`  
`pandas==0.25.3`  
`scikit-learn==0.21.3`  
`beautifulsoup4==4.8.2`

### Please donate if you can

If you can afford to support my work, then please consider donating to my [Ocean Plastic Detector](https://www.gofundme.com/OceanPlasticDetector) project.

Find me on [Twitter (@BMelykuti)](https://www.twitter.com/BMelykuti), on my website/blog: [Melykuti.me](https://melykuti.me), or follow me on [Facebook](https://www.facebook.com/bence.melykuti) for my public posts.

I work as a data science freelancer. You can contact me with your project proposal.