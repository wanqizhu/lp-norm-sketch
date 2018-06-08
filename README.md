# Overview

Over a large data stream of elements with many repetitions, we often want to know certain statistics about the distribution of unique elements. The *L_p norm* over a frequency vector is defined as the p-th root of the sum of p-th powers of the frequencies. We can obtain this statistic exactly by storing all unique elements as well as their count, but doing so require space linear in the size of the data stream (times log of the largest element). It is of interest to estimate Lp norm in sublinear space, without keeping track of the exact frequency vector and seen elements. 


Here we present an analysis and implementation of the generic Lp-norm-sketch streaming algorithm as outlined in [Alon, Matias, and Szegedy: The Space Complexity of Approximating the Frequency Moments](https://www.tau.ac.il/~nogaa/PDFS/amsz4.pdf), using sublinear space for a fixed p and epsilon-lambda error bounds.

See the [iPython notebook](lp_sketch.ipynb) for a detailed walkthrough of implementation and usage.




### Details

[project.py](project.py) shows the code used to generate the various graphs, which show the error distribution of LP-norm estimation under varying parameters (k, lambda, epsilon, etc.)

[Powerpoint slides for CS166 presentation](CS166_Final_Presentation.pdf)

[Final paper, largely modeled off ](Final_Paper.pdf)


## Interesting tidbits

- The original paper's math intuition is quite unscrutible
- The bound on *Var[X]* is not tight at all, and tightening it will definitely give practical speedups on the constant factors
- Likewise, the choice of constant factors *8* and *2* are pretty unoptimized. In practice, choosing better constants (see [paper](Final_Paper.pdf) for details) will lead to significant speedup and reduction in space usage.
- There are also more optimal solutions for estimating a specific p, with common ones being L-0 and L-2 norm. These are sketched in the original paper. What is impressive about this approach is it works for any *p*, and the techniques used here (taking the mean to reduce variance, then taking the median to bound error rate) is common among approximation algorithms and has a lot of potential applications.