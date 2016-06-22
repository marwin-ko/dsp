[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)
```
import math, thinkstats2, thinkplot, chap01soln

def BiasedPmf(pmf,label):
    new_pmf = pmf.Copy(label=label)
    for x,p in pmf.Items():
        new_pmf.Mult(x,x)
    new_pmf.Normalize()
    return new_pmf

resp = chap01soln.ReadFemResp()
actual_pmf = thinkstats2.Pmf(resp.numkdhh,label='actual')
biased_pmf = BiasedPmf(actual_pmf,label='observed')
thinkplot.PrePlot(2)
thinkplot.Pmfs([actual_pmf,biased_pmf])
thinkplot.Show(xlabel='# of childen (less than 18 yrs old)',ylabel='PMF')
print 'Actual PMF Mean = ', actual_pmf.Mean()   # actual_mean=1.02
print 'Biased PMF Mean = ', biased_pmf.Mean()   # biased_mean=2.40
```

## ANSWER
Actual PMF Mean = 1.02

Biased PMF Mean = 2.40
![alt text](https://github.com/marwin-ko/dsp/blob/master/statistics/METIS_3-1-actualVSbiased.png "Logo Title Text 1")

## NOTES
The data consists of number of children under 18 in a household. Households with no children would shift the mean towards zero which would not accurately illustrate the distribution of number of children in a household. As a result, the biased PMF also referred to as observed PMF, is a better statistical representation of the number of children under 18 in a household since the biased PMF omits holdholds with zero children.


