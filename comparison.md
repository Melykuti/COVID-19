## The race to squash the SARS-CoV-2 coronavirus pandemic

> * On this page I examine the cumulative number of all confirmed coronavirus patients – who may be ill or may have recovered or died by now.

22 March 2020 (updated on 30 January 2021), Freiburg i. Br., Germany – There are different visualisations of the spread of the coronavirus pandemic. Many of them are more alarmist than insightful. My goal on this page is to present an innovation in how to look at the problem.

### Background

[On my first analysis page](https://github.com/Melykuti/COVID-19/blob/master/global.md) I analyse and try to estimate the number of currently infected and thereby infectious people for you to understand the danger to your health. Many dashboards report cumulative numbers of all detected cases. This is informative about the extent of the problem but it is alarmist because it is ever less meaningful as many patients recover and some die. There are dashboards reporting the number of deaths caused by this disease. While the victims deserve our thoughts and every one of them should inspire us to step up our efforts, this information is not actionable. It's too late to help them.

In the exponential growth phase, it is beyond comprehension to digest a number each day which is significantly larger than the day before. It is more useful to present the growth rate from one day to the next. This number is rather sensitive to random effects, to the timing of data reporting and so on. For this reason I proposed to look at the problem in logarithmic space, so I took the logarithm of the case numbers. To flatten out random noise, I fitted a linear regression to this curve in the logarithmic space over four to fourteen data points (days). From this fit, from the slope of the straght line, I computed the _daily increase rate_ of the cumulative number of infected people and the _doubling time_ of the same quantity. These quantities are both easy to comprehend and insightful. Moreover, their being time series, they enable the tracking of the success or inadequacy of pandemic control measures.

On 1 May 2020, I introduced a technical refinement. I no longer fit curves to the cumulative numbers of COVID-19 cases but to the daily increments, that is, to the daily new cases. Because this is the raw data, it is preferable but it is also noisier. As the daily increment has stabilised in most countries due to the countermeasures, mainly the lockdowns or shelter-in-place orders, I fit linear regressions to the numbers directly and not to their logarithms.

From this fit, I compute **the daily number of new cases**. It would be easy to use the change of cumulative numbers between the last and the penultimate days but I derive this value from my fit. You can interpret the fitting process as a smoothing over the last several days. From the fit I also compute the _doubling time_ and use that to infer a **daily growth rate** by imposing a uniform geometric progression over the time interval from present until the time when doubling has been achieved. This is again a smoothing procedure to deal with noisy data.

### Innovation

On this page, I build on these developments and demonstrate a way to compare where different countries are in their fight to contain and to hopefully stop the spread of the COVID-19 pandemic. One can find plots where people compare countries by translating the time series of their individual case numbers, using logarithmic scale on the _y_-axis, so that each starts when the country reached, say, the 50th or the 100th case. The _x_-axis represents days since this time point. Countries with similar growth rates form sectors on this plot (they are in angular domains) because of the logarithmic scale on the _y_-axis.

I introduce four innovations into this view.

1. Instead of case numbers as a function of time, I look at the growth rate over time.
2. Instead of measuring progress by time, I measure it by cumulative case numbers. Time still flows from left to right in my plots, but not at a constant pace.
3. In addition to total numbers, I also consider case numbers per 100,000 people. Fortunately, this view has started appearing in the community. When Italy passed the number of cases that China had had, it was vital not to forget that the population of Italy is much smaller, therefore their problem was that much greater.
4. (Since 16 April 2020) In addition to growth rate, I express daily growth also in terms of persons per 100,000 population.

To justify Points&nbsp;1 and&nbsp;2, I argue that this is a better way to assess the success of countermeasures against the coronavirus introduced in a jurisdiction. The independent variable, the scale of the problem, is the cumulative number of infections. Countries introduce increasingly strict measures as a response to _this_ variable, not as a response to time. The measures can be described qualitatively only and not quantitatively, and their aim is to reduce the transmission rate of the disease, _R_\_0. However, their effect can be quantified by the daily growth rate of infections. The measures achieve perfect success if the growth rate drops to zero. Therefore a good indicator of the success of measures is the mapping from cumulative case numbers to daily growth rates.

By using linear regression, I have quite stable estimates for the daily growth rate. Their disadvantage is that they respond to changes in the growth rate slower than the pairwise ratios between days do. However, by shortening the window size, they follow the trends in an ever more agile fashion. Recall that the mean 5-7 day incubation time of the coronavirus disease itself already introduces a significant delay between introducing constraints on social life and seeing a drop in the growth rate of the cumulative case number. Therefore any inaccuracy by using linear regression is not going to be meaningful.

Point 2 allows me to compare different countries' efforts. The sooner in terms of case numbers they can drive down the growth rate, the more lives their response saves. The timing is of secondary importance here, it enters the picture by the capacity limit to provide medical care to severe patients. The effect of timing on the overspill over capacity is important for how many people will succumb to the disease but I would rather we did not get infected in the first place. For me, this justifies why dropping the time aspect from the plot is defensible.

Point 3 is part a sanity check, part an enrichment of our study. Even Point 2 allows me to compare countries but it will be informative to see the success of response not only as a function of patients but as a function of patients per 100,000 people.

Point 4 allows us to track a country over time as the base, the cumulative number of infections, keeps growing: even if the number of new infections per day only stabilises, the growth rate relative to the growing base starts falling. If I look at increment per 100,000 people, then I remove this distortion. It also gives a way to compare the current situation in countries that have significantly different cumulative case numbers per 100,000 people.

### Plots

#### Countries with the largest case numbers

Let us start with the European countries which experienced the first outbreaks and the largest number of cases and see how they compare to the first country to encounter the disease, China. In all plots, I used automatic window size selection for linear regression. This finds the window size which provides the best fit but this window size may not be short and often misses the most recent trend from the last day or two. In exchange, it provides somewhat smoother curves.

First, a plot of daily increments of coronavirus cases per 100,000 population indexed simply by time.

![Joint relative increments through time](https://github.com/Melykuti/COVID-19/blob/master/plots/Joint_DGR_2021-01-29_xy_-1_lin_date_incr_confirmed.png)

Next is the case where I measure progress in terms of cumulative case numbers and not time. For the normalisation with the population sizes, in the case of China I had used the population of Hubei province and not of the entire country for plots created until 24th March 2020. This choice used to present their effort in a more critical light (it suggested that they succeeded only after more people had caught the disease). In general, China being the first country to face the epidemic, I think it is unfair to criticise them harshly. All other countries, which have seen the Chinese example, had a warning to prepare and had the opportunity to learn from the effect of Chinese measures on the pandemic. They are fair targets.

![Joint relative increments against relative numbers](https://github.com/Melykuti/COVID-19/blob/master/plots/Joint_DGR_2021-01-29_xy_-1_lin_cases_incr_confirmed.png)

![Joint daily growth rates against relative numbers](https://github.com/Melykuti/COVID-19/blob/master/plots/Joint_DGR_2021-01-29_xy_-1_lin_cases_rate_confirmed.png)

I moved the analogous plots for Germany and its federal states [to the page that focuses on Germany (in German).](https://github.com/Melykuti/COVID-19/blob/master/Deutschland.md)

#### A comparison of the great powers China, the European Union and the United States of America

On 18 May 2020, I added Russia, Brazil and India due to the increasing case numbers they are confronted with in the COVID-19 pandemic.

![Daily relative increments for China, EU, USA, Russia, Brazil and India through time](https://github.com/Melykuti/COVID-19/blob/master/plots/great_powers_DGR_2021-01-29_xy_-1_lin_date_incr_confirmed.png)

![Daily relative increments for China, EU, USA, Russia, Brazil and India against relative numbers](https://github.com/Melykuti/COVID-19/blob/master/plots/great_powers_DGR_2021-01-29_xy_-1_lin_cases_incr_confirmed.png)

![Daily growth rates for China, EU, USA, Russia, Brazil and India against relative numbers](https://github.com/Melykuti/COVID-19/blob/master/plots/great_powers_DGR_2021-01-29_xy_-1_lin_cases_rate_confirmed.png)


#### The Visegrád Group (Poland, Czech Republic, Slovakia, Hungary) and some small countries

In this block there are East European countries. There is Iceland, which has a rather high infection rate. This is more due to broad testing than to a comparatively bad situation. As far as I know, from very early on Iceland tested even randomly selected members of the population who did not show any symptoms to get a clearer idea of the extent of infections. San Marino, being in Italy, is a proxy for the North Italian situation as its case numbers are from a small, concentrated region. The trajectories of Italy and Spain are included for comparison.

![Daily relative increments for East Europe through time](https://github.com/Melykuti/COVID-19/blob/master/plots/Visegrad_DGR_2021-01-29_xy_-1_lin_date_incr_confirmed.png)

In San Marino, there are some 34,000 inhabitants. Iceland has got about 350,000.

![Daily relative increments for East Europe against relative numbers](https://github.com/Melykuti/COVID-19/blob/master/plots/Visegrad_DGR_2021-01-29_xy_-1_lin_cases_incr_confirmed.png)

![Daily growth rates for East Europe against relative numbers](https://github.com/Melykuti/COVID-19/blob/master/plots/Visegrad_DGR_2021-01-29_xy_-1_lin_cases_rate_confirmed.png)

### Data

The international data is time series data with daily sampling frequency that I source from the [repository](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series) maintained by the Center for Systems Science and Engineering at the Johns Hopkins University (JHU).

For the case numbers per 100,000 citizens, I retrieved the populations of countries from the [CIA World Factbook](https://www.cia.gov/library/publications/the-world-factbook/fields/335rank.html).

### Program files

* **download_JHU_CSSE.py** is a script to download three csv data tables: the number of confirmed cases, the number of deaths due to the disease, and the number of recovered patients, broken down to countries. The script automatically inserts the timestamp of download into the file names so that later downloads do not overwrite downloaded data.

* **comparison_joint.py** contains the data processing and plotting functionalities that are specific to these joint plots.

* **utils.py** contains the universal data selection, preprocessing, analysis and plotting functionalities. It searches for the most recent download of `download_JHU_CSSE.py` in the current directory based on the timestamp in the file name. If you want to select a particular one, then modify the variable `timestamp` in `open_csvs()`.


### Please donate if you can

If you can afford to support my work, then please consider donating. Thank you!

* Address for bitcoin (BTC): `13veK2ecjhtNenTxhGKJjP83QiMmNd1M7p`
* Address for ether (ETH) and tokens: `0x49fC2a73e1eC76248324E411e699f92adD6565Ff`

Find me on [Twitter (@BMelykuti)](https://twitter.com/BMelykuti), on my website/blog: [Melykuti.me](https://melykuti.me), or follow me on [Facebook](https://www.facebook.com/bence.melykuti) for my public posts.

I work as a data science freelancer. You can contact me with your project proposal.