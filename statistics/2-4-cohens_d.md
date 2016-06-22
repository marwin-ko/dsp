[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)
```
import math, first
def CohensD(group1,group2):
    x1 = group1.mean()
    x2 = group2.mean()
    v1 = group1.var()
    v2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1*v1 + n2*v2)/(n1+n2)
    pooled_std = math.sqrt(pooled_var)
    d = (x1-x2)/(pooled_std)
    return d
live, firsts, others = first.MakeFrames()
D = CohensD(firsts.totalwgt_lb, others.totalwgt_lb)
answer = "The Cohen's D is {0:4.2f} which indicates a small effect size. Essentially, there is no significant difference between the two groups: first babies and other babies."
print answer.format(D)
```

#### ANSWER
The Cohen's D is -0.09 which indicates a small effect size. Essentially, there is no significant difference between the two groups: first babies and other babies.

#### NOTES
The larger the Cohen's D is, the stronger effect size there is and vice versa (smaller D, weaker effect size). A strong effect
indicates some significant difference between two or more groups.

small/weak: d=0.2

medium:d=0.5

large/strong: d=0.8
