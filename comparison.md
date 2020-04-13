## The race to squash the SARS-CoV-2 coronavirus pandemic

22 March 2020 (updated on 13 April 2020), Freiburg i. Br., Germany -- There are different visualisations of the spread of the coronavirus pandemic mushrooming on the internet. Many of them are more alarmist than insightful. My goal on this page is to present an innovation in how to look at the problem.

### Background

[On my first analysis page](https://github.com/Melykuti/COVID-19/blob/master/global.md) I analyse and try to estimate the number of currently infected and thereby infectious people for you to understand the danger to your health. Many dashboards report cumulative numbers of all detected cases. This is informative about the extent of the problem but it is alarmist because it is ever less meaningful as many patients recover and some die. There are dashboards reporting the number of deaths caused by this disease. While the victims deserve our thoughts and every one of them should inspire us to step up our efforts, this information is not actionable. It's too late to help them.

In the exponential growth phase, it is beyond comprehension to digest number each day which is a significantly larger than the day before. It is more useful to present the growth rate from one day to the next. This number is rather sensitive to random effects, to the timing of data reporting and so on. For this reason I proposed to look at the problem in logarithmic space, so I take the logarithm of the case numbers. To flatten out random noise, I fit a linear regression to this curve in the logarithmic space over four to fourteen data points (days). From this fit, from the slope of the straght line, I compute the **daily increase rate** of the cumulative number of infected people and the **doubling time** of the same quantity. These quantities are both easy to comprehend and insightful. Moreover, their being time series, they enable the tracking of the success or inadequacy of pandemic control measures.

### Innovation

On this page, I build on these developments and demonstrate a way to compare where different countries are in their fight to contain and to hopefully stop the spread of the COVID-19 pandemic. One can find plots where people compare countries by translating the time series of their individual case numbers, using logarithmic scale on the _y_-axis, so that each starts when the country reached, say, the 50th or the 100th case. The _x_-axis represents days since this time point. Countries with similar growth rates form sectors on this plot (they are in angular domains) because of the logarithmic scale on the _y_-axis.

I introduce three innovations into this view.

1. Instead of case numbers as a function of time, I look at the growth rate over time.
2. Instead of measuring progress by time, I measure it by cumulative case numbers. Time still flows from left to right in my plots, but not at a constant pace.
3. In addition to total numbers, I also consider case numbers per 100,000 people. Fortunately, this view has started appearing in the community. When Italy passes the number of cases that China has had, it is vital that we do not forget that the population of Italy is much smaller, therefore their problem is that much greater.

To justify Point 1, I argue that this is a better way to assess the success of measures introduced in a jurisdiction. The independent variable, the scale of the problem, is the cumulative number of infections. Countries introduce increasingly strict measures as a response to _this_ variable, not as a response to time. The measures can be described qualitatively only and not quantitatively, and their aim is to reduce the transmission rate of the disease, _R_\_0. However, their effect can be quantified by the daily growth rate of infections. The measures achieve perfect success if the growth rate drops to zero. Therefore a good indicator of the success of measures is the mapping from cumulative case numbers to daily growth rates.

By using linear regression, I have quite stable estimates for the daily growth rate. Their disadvantage is that they respond to changes in the growth rate slower than the pairwise ratios between days do. However, by shortening the window size, they follow the trends in an ever more agile fashion. Recall that the mean 5-7 day incubation time of the coronavirus disease itself already introduces a significant delay between introducing constraints on social life and seeing a drop in the growth rate of the cumulative case number. Therefore any inaccuracy by using linear regression is not going to be meaningful.

Point 2 allows me to compare different countries' efforts. The sooner in terms of case numbers they can drive down the growth rate, the more lives their response saves. China has basically hit zero growth rate. The timing is of secondary importance here, it enters the picture by the capacity limit to provide medical care to severe patients. The effect of timing on the overspill over capacity is important for how many people will succumb to the disease but I would rather we did not get infected in the first place. For me, this justifies why dropping the time aspect from the plot is defensible.

Point 3 is part a sanity check, part an enrichment of our study. Even Point 2 allows me to compare countries but it will be informative to see the success of response not only as a function of patients but as a function of patients per 100,000 people.

### Plots

#### Countries with the largest case numbers

Let us start with the countries with the largest number of cases and see how they compare to the first country to encounter the disease, China. In the first plot, I used automatic window size selection for linear regression. This finds the window size which provides the best fit but this window size tends not to be short and often misses the most recent trend from the last day or two. In exchange, it provides quite smooth curves.

What is clear is that China has managed to drive down its curve to zero, where there are essentially no new cases. This is where each country should be trying to head. We know that Italy and Spain, and more recently the USA are in a particularly difficult situation. Any other country must try to be below their curves. Worryingly, Germany has had a period when it was anything but below Italy and Spain. In Freiburg, where I live, there is a lockdown in place since Saturday, 21 March. The states of Bavaria and Saarland introduced similar measures, a day later Rhineland-Palatinate. As I expected, these drastic measures have started showing results in the data by now. On 24 March, the WHO warned that the USA might become a new epicentre for the coronavirus disease, and so it did. Due to its population size, I chose to compare it with the whole European Union and China.

![Joint daily growth rate, absolute numbers](https://github.com/Melykuti/COVID-19/blob/master/plots/Joint_DGR_2020-04-12_0_-1.png)

For comparison, a window size of four data points captures the most recent changes better but its behaviour for lower case numbers is more volatile (see Appendix at the bottom). A window size of three is too noisy.

Next is the normalised case with automatic window size selection. For the normalisation with the population sizes, in the case of China I had used the population of Hubei province and not of the entire country for plots created until 24th March 2020. This choice used to present their effort in a more critical light (it suggested that they succeeded only after more people had caught the disease). In general, China being the first country to face the epidemic, I think it is unfair to criticise them harshly. All other countries, which have seen the Chinese example, had a warning to prepare and had the opportunity to learn from the effect of Chinese measures on the pandemic spread. They are fair targets.

Switzerland was on a particularly concerning path but the country has seen a significant slowdown in the spread over the past few days. (The case numbers still grow, but at a lower pace.) My place of residence, Freiburg is close to the Swiss border and also to the heavily affected Region Grand Est of France. These aspects were used to justify imposing a lockdown in Freiburg. These plots unequivocally support the urgency of aggressive countermeasures.

![Joint daily growth rate, relative numbers](https://github.com/Melykuti/COVID-19/blob/master/plots/Joint_DGR_2020-04-12_1_-1.png)

The French army has flown out patients from Region Grand Est to other parts of the country. A few days later they asked the German armed forces, the Bundeswehr, to contribute helicopters to this effort. On 28 March I heard that Paris hospitals are desperate to send severe patients for treatement to other parts of France. Some days before that, the German cities of Freiburg, Karlsruhe, Mannheim and Heidelberg had offered to treat French patients from Region Grand Est. Leipzig received patients from Italy on request of Italy. Germany was in a way already in a more difficult situation than France. But it seems that the high number of hospital and especially intensive care unit beds relative to population size gave enough buffer to manage this generosity.

I moved the analogous plots for Germany and its federal states [to the page that focuses on Germany (in German).](https://github.com/Melykuti/COVID-19/blob/master/Deutschland.md)

#### A comparison of the great powers China, European Union and the United States of America

![Daily growth rates for China, EU, USA, absolute numbers](https://github.com/Melykuti/COVID-19/blob/master/plots/great_powers_DGR_2020-04-12_0_-1.png)

![Daily growth rates for China, EU, USA, relative numbers](https://github.com/Melykuti/COVID-19/blob/master/plots/great_powers_DGR_2020-04-12_1_-1.png)


#### The Visegrád Group (Poland, Czech Republic, Slovakia, Hungary) and some small countries

In this block there are East European countries. There is Iceland, which has a rather high infection rate. This is more due to broad testing than to a comparatively bad situation. As far as I know, Iceland tests even random selected members of the population who do not show any symptoms to get a clearer idea of the extent of infections. San Marino, being in Italy, is a proxy for the North Italian situation as its case numbers are from a small, concentrated region. The trajectories of Italy and Spain are included for comparison.

![Daily growth rates for East Europe, absolute numbers](https://github.com/Melykuti/COVID-19/blob/master/plots/Visegrad_DGR_2020-04-12_0_-1.png)

Both **San Marino**, which is an enclave microstate inside Italy, **and Iceland already carry a high burden of the coronavirus disease relative to their population sizes**. In the case of San Marino, there are some 34,000 inhabitants. Iceland has got about 350,000.

![Daily growth rates for East Europe, relative numbers](https://github.com/Melykuti/COVID-19/blob/master/plots/Visegrad_DGR_2020-04-12_1_-1.png)

The situation in Hungary deteriorated a lot by a spike in cases in a retirement home in Budapest. I also have a nagging feeling that any calm does not reflect the complete truth as much as it is due to low testing. Romania was apparently subjected in mid-March to the return of a wave of its citizens who work in Western Europe, including Italy. There were concerns that they brought and would spread the disease in their home country and the plots are concordant with this earlier projection.

### Data

The international data is time series data with daily sampling frequency that I source from the [repository](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series) maintained by the Center for Systems Science and Engineering at the Johns Hopkins University (JHU).

For the case numbers per 100,000 citizens, I retrieved the populations of countries from the [CIA World Factbook](https://www.cia.gov/library/publications/the-world-factbook/fields/335rank.html).

### Program files

* **download_JHU_CSSE.py** is a script to download three csv data tables: the number of confirmed cases, the number of deaths due to the disease, and the number of recovered patients, broken down to countries. The script automatically inserts the timestamp of download into the file names so that later downloads do not overwrite downloaded data.

* **comparison_joint.py** contains the data processing and plotting functionalities that are specific to these joint plots.

* **utils.py** contains the universal data selection, preprocessing, analysis and plotting functionalities. It searches for the most recent download of `download_JHU_CSSE.py` in the current directory based on the timestamp in the file name. If you want to select a particular one, then modify the variable `timestamp` in `open_csvs()`.


### Please donate if you can

If you can afford to support my work, then please consider donating to my [Ocean Plastic Detector](https://www.gofundme.com/OceanPlasticDetector) project.

Find me on [Twitter (@BMelykuti)](https://www.twitter.com/BMelykuti), on my website/blog: [Melykuti.me](https://melykuti.me), or follow me on [Facebook](https://www.facebook.com/bence.melykuti) for my public posts.

I work as a data science freelancer. You can contact me with your project proposal.

### Appendix

#### Countries with the largest case numbers, window size 4

![Joint daily growth rate, absolute numbers](https://github.com/Melykuti/COVID-19/blob/master/plots/Joint_DGR_2020-04-12_0_4.png)

This plot about relative infection numbers was made with a fixed window size of 4. The lines bounce around rather strongly but this plot captures the trends of the last days more accurately.

![Joint daily growth rate, relative numbers](https://github.com/Melykuti/COVID-19/blob/master/plots/Joint_DGR_2020-04-12_1_4.png)
