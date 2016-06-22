[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

```
import thinkstats2
x1 = thinkstats2.EvalNormalCdf(177.8,mu=178,sigma=7.7)
x2 = thinkstats2.EvalNormalCdf(185.42,mu=178,sigma=7.7)
percentage = (x2-x1)*100
print 'Approximately {0:4.2f}% of the US male population is between 5\'10\" and 6\'1\". Therefore, 34.27% of males in the US are eligible to join the blue man group.'.format(percentage)
```

## ANSWER
Approximately 34.27% of the US male population is between 5'10" and 6'1". Therefore, 34.27% of males in the US are eligible to join the blue man group.

## NOTES
I computed the CDF at 5'10"(177.8cm) and 6'1"(185.42cm). Afterwards, I took the difference the two CDFS which yields the proportion of men in the US between 5'10" and 6'1".
