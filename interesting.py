# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 23:45:00 2018

@author: Daniel
"""


import numpy as np
import math
import line_profiler
from matplotlib import pyplot as plt

DEFAULT_K = 2
DEFAULT_LAMBDA = 0.1
DEFAULT_EPSILON = 0.01
DEFAULT_Q = 0.1

def main():
    dist = np.random.randint(10, size=(100,))
    vary_lambda_tests(dist)
    
def basic_test(dist=None):
    if dist is None: dist = np.random.randint(10, size=(100,))
    run_tests(dist)

def vary_q_tests(dist=None):
    if dist is None: dist = np.arange(100) % 10 + 1
    for q in [0.05, 0.01, 0.1, 0.25, 0.5, 1, 2, 4]:    
        run_tests(dist, "vary_q_tests", q=q)

def vary_k_tests(dist=None):
    if dist is None: dist = np.arange(100) % 10 + 1
    ks = [i for i in range(2, 10)]
    for k in ks:
        run_tests(dist, "vary_k_tests", k=k)
        
def vary_epsilon_tests(dist=None):
    if dist is None: dist = np.arange(100) % 10 + 1
    for eps in [10**(-i) for i in range(1,6)]:
        run_tests(dist, "vary_epsilon_tests", _epsilon=eps)
        
def vary_lambda_tests(dist=None):
    if dist is None: dist = np.arange(100) % 10 + 1
    for lam in [0.2, 0.1, 0.05, 0.01]:
        run_tests(dist, "interesting", _lambda=lam)

def run_tests(dist, prefix=None, k=DEFAULT_K, _lambda=DEFAULT_LAMBDA, _epsilon=DEFAULT_EPSILON, q=DEFAULT_Q):
    n = 10
    m = 100
        
    estimates = test(dist, 100, n, k, _lambda, _epsilon, q)
    fig = plt.figure()
    norm = true_lp_norm(dist,k)
    lower_bound = (1-_lambda)*norm
    upper_bound = (1+_lambda)*norm
    
    fig = plt.figure()
    plt.hist(estimates, bins = 20)
    mean = np.mean(estimates)
    
    plt.axvline(mean, color='green')
    plt.axvline(norm, color='black')
    plt.axvline(lower_bound, color='red')
    plt.axvline(upper_bound, color='red')
    
    plt.title("k={}, lambda={}, epsilon={}, q={}".format(k, _lambda, _epsilon, q))
    plt.xlabel("Estimates")
    plt.ylabel("Number of estimates")
    if prefix: fig.savefig("{}/F{}_n={}_m={}_lambda={}_epsilon={}_q={}.png".format(prefix, k, n, m, _lambda, _epsilon, q), format="png")
    
def test(dist, num_test, n, k, _lambda, _epsilon, q):
    print("Beginning tests...")
    estimates = []
    for _ in range(num_test):
        estimate = lp_norm_sketch(dist, k, n, _lambda, _epsilon, q)
        estimates.append(estimate)
        print("Test {} estimate: {}".format(_, estimate))
    return estimates
    

def lp_norm_sketch(A, k, n, _lambda, _epsilon, q):
    # compute the number of counters we need
    s1 = math.ceil(q*k*n**(1-1/k)/(_lambda**2))
    # C = ((1/2 - 1/q)**2)*(2/q)
    s2 = math.ceil(2*math.log(1/_epsilon))
    print("(s1, s2) = {}. The product is {}".format((s1, s2), s1*s2))
    
    X = np.zeros((s2, s1), dtype=int)  # the random element we care about
    r = np.zeros((s2, s1))  # stores the frequency count
    
    m = 0
    for cnt, a in enumerate(A):
        # since we don't know m in advance, we
        # update X and r as we go
        # when we encounter the m-th element, we update w.p. 1/m
        to_change = np.random.rand(s2, s1) < 1/(cnt+1)
        X[to_change] = a
        r[to_change] = 0  # reset counter as needed
        r[X == a] += 1
        m += 1
        
    return np.median(np.mean((m)*(r**k - (r-1)**k), axis=1), axis=0)

def true_lp_norm(dist, k):
    uniq, cnts = np.unique(dist, return_counts=True)
    return np.sum(cnts**k)

if __name__ == "__main__":
    main()