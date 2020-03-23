## The race to squash the SARS-CoV-2 coronavirus pandemic

22 March 2020, Freiburg i. Br., Germany -- There are different visualisations of the coronavirus pandemic mushrooming on the internet. Many of them are more alarmist than insightful. My goal on this page is to present another innovation how to look at the problem.

### Background

[On my landing page](https://github.com/Melykuti/COVID-19/blob/master/README.md) I analyse and try to estimate the number of currently infected and thereby infectious people for you to understand the danger to your health. Many dashboards report cumulative numbers of all detected cases, which is informative about the extent of the problem but it is alarmist because it is ever less meaningful as many patients recover and some die. There are dashboards reporting the number of deaths caused by this disease. While the victims deserve our thoughts and every one of them should inspire us to step up our efforts, this information is not actionable. It's too late to help them.

In the exponential growth phase, it is beyond our comprehension to digest a significantly larger number each day than the day before. It is more useful to present the growth rate from one day to the next. This number is rather sensitive to random effects, to the timing of data reporting and so on. For this reason I proposed to look at the problem in logarithmic space, so take the logarithm of the case numbers. To flatten out random noise, I fit a linear regression to this curve in the logarithmic space over four to fourteen data points (days). From this fit, from the slope of the straght line, I compute the **daily increase rate** of the number of infected people and the **doubling time** of the same quantity. These quantities are both easy to comprehend and insightful. Moreover, their being time series, they enable the tracking of the success or inadequacy of control measures.

### Innovation

On this page, I build on these developments and demonstrate a way to compare where different countries are in their fight to contain and to hopefully stop the spread of the pandemic. One can find plots where people compare countries by translating the time series of their individual case numbers, using logarithmic scale on the y-axis, so that each start when the country reached, say, the 50th or the 100th case. The x-axis represents days since this time point. Countries belonging to intervals of growth rates form sectors on this plot (they are in angular domains) because of the logarithmic scale on the y-axis.

I introduce three innovations into this view.

1. Instead of case numbers as a function of time, I look at the growth rate over time.
2. Instead of measuring progress by time, I measure it by cumulative case numbers. Time still flows from left to right in my plots, but not at a constant pace.
3. In addition to total numbers, I also consider case numbers per 100,000 people. Fortunately, this view has started appearing in the community. When Italy passes the number of cases that China has had, it is vital that we do not forget that the population of Italy is much smaller, therefore their problem is that much greater.

To justify Point 1, I argue that this is a better way to assess the success of measures introduced in a jurisdiction. The independent variable, the scale of the problem is the cumulative number of infections. Countries introduce increasingly strict measures as a response to _this_ variable, not as a response to time. The measures can be described qualitatively only and not quantitatively, and their aim is to reduce the transmission rate of the disease, R_0. However, their effect can be quantified by the daily growth rate of infections. The measures achieve perfect success if the growth rate drops to zero. Therefore a good indicator of the success of measures is the mapping from cumulative case numbers to daily growth rates.

By using linear regression, I have quite stable estimates for the daily growth rate. Their disadvantage is that they respond to changes in the growth rate slower than the pairwise ratios between days do. However, by shortening the window size, they follow the trends in an ever more agile fashion. Remember that the mean 5-7 day incubation time of the coronavirus disease itself already introduces a significant delay between introducing constraints on social life and seeing a drop in the increase rate of cumulative cases.

Point 2 allows me to compare different countries' efforts. The sooner in terms of case numbers they can drive down the growth rate, the more lives their response saves. The timing is of secondary importance here, it enters the picture by the limit in the capacity to provide medical care to severe patients.

Point 3 is part a sanity check, part an enrichment of our study. Even Point 2 allows me to compare countries, but it will be informative to see the success of response not only as a function of patients but as a function of patients per 100,000 people.

### Plots

#### Countries with the largest case numbers

Let us start with the countries with the largest number of cases and see how they compare to the first country to encounter the disease, China. In the first plot, we used automatic window size selection for linear regression. This finds the window size which provides the best fit but this window size tends not to be short and often misses the most recent trend from the last day or two. In exchange, it provides quite smooth curves.

What is clear is that China has managed to drive down its curve to zero, where there are essentially no new cases. This is where each country should be trying to head. We know that Italy and Spain are in a particularly difficult situation. Any other country must try to be below their curves. **Worryingly, Germany has had a period when it is anything but below.** In Freiburg, where I live, there is a curfew in place since yesterday (21 March). The states of Bavaria and Saarland introduced similar measures, a day later Rhineland-Palatinate. I expect these drastic measures to start showing results in the data about a week from now.

![Joint daily increase factor, 21/3/2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Joint_DIF_2020-03-21_0_-1.png)

For comparison, a window size of four data points captures the most recent changes better but its behaviour for lower case numbers is more hectic. A window size of three is too noisy.

![Joint daily increase factor, 21/3/2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Joint_DIF_2020-03-21_0_4.png)

Next is the normalised case with automatic window size selection. For the normalisation with the population sizes, in the case of China I used the population of Hubei province and not of the entire country. This choice presents their effort in a more critical light (it suggests that they succeeded after more people had caught the disease). In general, China being the first country to face the epidemic, I think it is unfair to criticise them harshly. All other countries, which have seen the Chinese example, are fair targets.

**Switzerland is on a particularly concerning path.** My place of residence, Freiburg is close to the Swiss border and also to the heavily affected Region Grand Est of France. These aspects were used to justify imposing a curfew in Freiburg. These plots unequivocally support the urgency of aggressive countermeasures.

![Joint daily increase factor, 21/3/2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Joint_DIF_2020-03-21_1_-1.png)

In this set the last plot was made with a fixed window size of 4. The lines bounce around rather strongly but this plot is supposed to capture the trends of the last days more accurately. As far as I know, the French army has flown out patients from Region Grand Est to other parts of the country. On top of that, the German cities of Freiburg, Karlsruhe, Mannheim and Heidelberg offered to treat French patients from the same region. I do not criticise generosity but my plots show that Germany is in a way already in a more difficult situation than France. I hope that I won't be right but it is possible that in the next few days these German hospitals will be surprised by an onslaught of patients whose condition is turning worse just now.

![Joint daily increase factor, 21/3/2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Joint_DIF_2020-03-21_1_4.png)

#### Germany and its federal states

I switched the language of plots to German.

![Joint daily increase factor, 21/3/2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Deutschland_DIF_2020-03-21_0_-1.png)

My state, Baden-Württemberg is doing very poorly. It currently leads the country in the number of reported cases. It has overtaken the 62% more populous North Rhine-Westphalia where there is a well-known outbreak around Heinsberg. I suspect this is down to a delay in reporting from NRW, whose cumulative number increased by three only in the last day. Bremen is the very volatile one.

![Joint daily increase factor, 21/3/2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Deutschland_DIF_2020-03-21_1_-1.png)

#### The Visegrád Group (Poland, Czech Republic, Slovakia, Hungary) and some small countries

In this block there are East European countries. There is Iceland, which has a rather high infection rate. This might be more due to broad testing than to a comparatively bad situation. San Marino, being in Italy, is a proxy for the North Italian situation as its case numbers are from a small, concentrated region. The trajectories of Italy and Spain are included for comparison.

![Joint daily increase factor, 21/3/2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Visegrad_DIF_2020-03-21_0_-1.png)

Both **San Marino**, which is an enclave microstate inside Italy, **and Iceland already carry a high burden of the coronavirus disease relative to their population sizes**. In the case of San Marino, there are some 34,000 inhabitants. Iceland has got about 350,000.
![Joint daily increase factor, 21/3/2020](https://github.com/Melykuti/COVID-19/blob/master/plots/Visegrad_DIF_2020-03-21_1_-1.png)

It is quite quiet in Hungary currently. But I have a nagging feeling that this does not reflect the complete truth as much as it is due to low testing. Romania has apparently been subjected to the return of a wave of its citizens who work in Western Europe, including Italy. There are concerns that they have brought and will spread the disease in their home country. It will be interesting to monitor these countries over the coming days.

### Data

The international data is [time series data with daily sampling frequency](https://github.com/CSSEGISandData) that I source from the repository maintained by the Center for Systems Science and Engineering at the Johns Hopkins University (JHU).

The data for Germany is sourced from the [German Wikipedia page](https://de.wikipedia.org/wiki/COVID-19-Pandemie_in_Deutschland#Infektionsf%C3%A4lle_nach_Bundesl%C3%A4ndern), which collects the official data provided by the [Robert Koch Institute (RKI)](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html) and presents it in time series format. The RKI tends to lag behind the JHU in its reporting. At the same time, it is not quite transparent where exactly the JHU CSSE effort sources its data for Germany.

For the case numbers per 100,000 citizens, I need to know the population of countries. I use the [CIA World Factbook](https://www.cia.gov/library/publications/the-world-factbook/fields/335rank.html) for international figures, and the German Statistical Office for the [population sizes of the German federal states](https://www.statistikportal.de/de/bevoelkerung/flaeche-und-bevoelkerung).

### Please donate if you can

If you can afford to support my work, then please consider donating to my [Ocean Plastic Detector](https://www.gofundme.com/OceanPlasticDetector) project.

Find me on [Twitter (@BMelykuti)](https://www.twitter.com/BMelykuti), on my website/blog: [Melykuti.me](https://melykuti.me), or follow me on [Facebook](https://www.facebook.com/bence.melykuti) for my public posts.

I work as a data science freelancer. You can contact me with your project proposal.