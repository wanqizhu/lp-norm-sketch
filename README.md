# Overview

Over a large data stream of elements with many repetitions, we often want to know certain statistics about the distribution of unique elements. The *L_p norm* over a frequency vector is defined as the p-th root of the sum of p-th powers of the frequencies. We can obtain this statistic exactly by storing all unique elements as well as their count, but doing so require space linear in the size of the data stream (times log of the largest element). It is of interest to estimate Lp norm in sublinear space, without keeping track of the exact frequency vector and seen elements. 


Here we present an analysis and implementation of the generic Lp-norm-sketch streaming algorithm as outlined in [Alon, Matias, and Szegedy: The Space Complexity of Approximating the Frequency Moments](https://www.tau.ac.il/~nogaa/PDFS/amsz4.pdf), using sublinear space for a fixed p and epsilon-lambda error bounds.

See the [iPython notebook](lp_sketch.ipynb) for a detailed walkthrough of implementation and usage.




### Details

[project.py](project.py) shows the code used to generate the various graphs, which show the error distribution of LP-norm estimation under varying parameters (k, lambda, epsilon, etc.)

[Powerpoint slides for CS166 presentation](CS166_Final_Presentation.pdf)

[Final paper, largely modeled off ](Final_Paper.pdf)