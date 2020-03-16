## Analysis and projections for the spread of the SARS-CoV-2 coronavirus

> * For plots and results, scroll down to the sections with these titles.
> * [The analogous study for Germany and its federal states on the 15th March 2020 in German language.](https://github.com/Melykuti/COVID-19/blob/master/Deutschland.md)

13 March 2020, Freiburg i. Br., Germany. -- As I am writing this analysis and documentation, I'm constantly surprised by the stream of unprecedented news and by the escalation of response to the COVID-19 coronavirus disease. Things that were unthinkable yesterday have become a reality today.

The WHO releases [daily situation reports](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports) with the numbers of diagnosed COVID-19 cases for each country. We can see the total number of confirmed cases and the total deaths since the beginning of the outbreak. We also get the changes from the last report, that is, these two figures for the last day only.

Thinking in terms of the classical SIR model of epidemiology, the population comprises three groups: **S**usceptibles, **I**nfected and **R**emoved. _Removed_ are those who have recovered from or died of the disease and thereby are no longer infectious and can no longer catch the disease. (I assume that recovery gives immunity. There have been reports that suggested that this is not a certainty in this pandemic. So the situation might be worse than what I'll show here.) _Infected_ are the current patients who are also all infectious. _Susceptibles_ are everybody else: people who have not been infected yet (and hopefully will never be).

In the initial stage of an epidemic, we expect that most contacts by infected people will be with a susceptible person. This provides a fertile ground for the disease to spread. The number of infected people is rising exponentially (in the mathematical, not in the vague and overused marketing sense) until there are so many of them that it is becoming harder for the disease to find susceptibles.

**Unfortunately, in many European countries we currently observe exponential growth of case numbers.**

This means that from one day to the next, the total number of infected people increases not by a fixed number but by a fixed multiple. In any one hospital, the number of new patients per day is not the same as the number of new patients was yesterday. Instead, it is increasing by the same factor every day. For example, today the hospital gets 11 new patients, tomorrow 13, the day after 16, on day 4 already 19, on day 5 23. The stream doesn't stop, on day 10 it is 57 new patients, and so on. Each patient spends a week or two hospitalised, and the people being removed from the hospital are the lower numbers that arrived one or two weeks ago. If you are medical personnel and had a hard day at work, you can be sure that tomorrow will be even harder, the day after still harder. There is no system capable of meeting this demand.

**Our intuition is also caught off guard. The risk of contracting the disease is increasing by the same factor every day. It's silently, imperceptibly creeping up until the disease is everywhere around us.**

### So then...

_What is the probability of coming into contact with the disease if I leave my home?_ While I cannot answer that, I try to give a proxy, which is the number of currently infected people.

Some of the infected people will be in hospital, some at home, but some will be around us on the streets, in the shops, on public transport. I assume that the ratio between infected people in isolation (in hospital or at their home) and those among us is independent of how many people are infected in total. With the growth of the infected population, the count of infected people on the street grows proportionally. **From day to day, your chance of encountering an infected person in the street is growing by a fixed factor as long as the disease is spreading exponentially.**

### Data

The Center for Systems Science and Engineering at the Johns Hopkins University is kindly providing [the time series data with daily sampling frequency in tabular format](https://github.com/CSSEGISandData).

### Program files

* **countries_download.py** is a script to download the three csv data tables: the number of confirmed cases, the number of deaths due to the disease, and the number of recovered patients, broken down to countries. The script automatically inserts the timestamp of download into the file names so that later downloads do not overwrite downloaded data.

* **country_plot.py** contains the data selection, preprocessing, analysis and plotting functionalities for a single country. It searches for the most recent download of `countries_download.py` in the current directory based on the timestamp in the file name.

* **joint_analysis.py** calls `country_plot.py` repeatedly on a list of countries.

### Analysis

I compute the number of currently infectious people as the number of total cases minus the number of deaths minus the number of recovered patients for all days where there is data:

`no. of currently infected = no. of cases - no. of deaths - no. of recovered.`

The analysis is founded on the assumption that the growth of this number is exponential. Then I take the base 2 logarithm of this time series for a selected country, and fit a straight line to the last 14 days of data with _ordinary least squares (OLS)_. (If there is a day in this period when the number of patients was zero, then the program crashes.) If the growth is exponential or thereabouts, then this should fit quite well and the slope of this line will tell us the rate of growth.

From this slope I compute:

1. The growth factor per day, which I express in percentage terms. (What percentage more infectious people do we expect tomorrow than we had today.)

2. How many days it takes for the number of infectious people to double.

3. I make a crude estimate of what I guess the total number of infected people might currently be.

This is only my guesswork and it will be controversial. The idea is that in the case of a SARS-CoV-2 infection, it takes on average 5-6 days to develop symptoms (fever, dry cough and others). This incubation time varies between 1 to 14 days. The people who were infected today will present symptoms and will be tested perhaps 5 days from now. They will enter the figure in the situation report only then. But they are likely to be already infectious sooner than that and that is what I want to estimate.

So I project from my linear regression the number of infected three, respectively, five days from the latest data point, and that is the estimate for the _currently infected_ people. This might be too conservative and might only be an underestimate.

The exponential curve is not always a good fit (a straight line is not always a good fit to the logarithm of the current case number). It seems that in several European countries, countermeasures do slow the spread from the uncontrolled exponential growth, although not much yet. To screen for this, I compute:

4. The [R^2 or coefficient of determination](https://en.wikipedia.org/wiki/Coefficient_of_determination) of the linear regression fit (which I can't explain here). The closer it is to 1, the better the match between data and my linear regression.

5. I also compute the difference between the value of the fitted straight line for the last day when we have data and the real observation (in the logarithmic space) for that last day. If the spread is slowing relative to the exponential rate, then this number will be high and the projection is definitely unreliable. If this difference is small, then the projection might well be good. When the difference is negative, it will be an underestimate! You can interpret this number as a factor between the linear approximation and the data (because it is a difference between the logarithms).

If the R^2 is lower than 0.95 or this difference is greater than 0.5, then I do not show projections for the number of infected 3-to-5 days from now, which as I said is what I guess to be the real number of infected cases today.

### Plots

The plots for each individual country present the observed total number of infected on the left panel, and the same data on logarithmic scale on the right panel. These lines are in blue. In orange is the fit of an exponential curve, which is the same as the fit of a straight line on logarithmic scale.

For Italy, the last day's data has not been entered into the table and this is the reason why the last two days share the same value.

![Italy until 12 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Italy_20200313_22-34-57.png)

Denmark is the special case where the situation is more dire than what my exponential fit for the last 14 days suggests.

![Denmark on 13 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Denmark_20200313_22-34-57.png)

Germany is a case where the exponential approximation is fortunately no longer a good fit.

![Germany on 13 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Germany_20200313_22-34-57.png)

Similarly to Italy, data for the last day is missing (it is identical to the previous day) for Japan.

![Japan until 12 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Japan_20200313_22-34-57.png)

Austria is showing a faint good sign on the last day.

![Austria on 13 March 2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Austria_20200313_22-34-57.png)

### Results

The columns have the following meaning:

* The number of currently infected people increases daily by this percentage

* Time it takes for the number of currently infected people to double

* Latest reported number of infectious cases

* My estimate for number of infectious cases at present. (I describe at the end of the Analysis why it is missing in certain cases.)

* R^2 of linear regression fit

* Difference between linear fit and real data in logarithmic space for the last data point

I focus on countries with a large number of cases. China and South Korea are examples where the preventative measures have slowed down the epidemic spread massively below exponential growth.

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