[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

```
import random, thinkstats2, thinkplot

rand_nums = [random.random() for i in range(1000)]
PMF = thinkstats2.Pmf(rand_nums,label='PMF')
CDF = thinkstats2.Cdf(rand_nums,label='CDF')

thinkplot.PrePlot(2)
thinkplot.Pmf(PMF)
thinkplot.Cdf(CDF)
thinkplot.Show(xlabel='# of childen (less than 18 yrs old)',ylabel='PMF')
```

## ANSWER
Yes, the distribution is uniform.
![alt text](https://github.com/marwin-ko/dsp/blob/master/statistics/METIS_4-2-random_distribution_PMF_CDF.png)
