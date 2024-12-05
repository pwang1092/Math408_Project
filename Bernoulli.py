import numpy as np
import matplotlib.pyplot as plt
import math
import time

# Parameters
n_trials = 5000
n = 100
p = 0.8

def doBernouli():
    bern_samples = np.random.binomial(1, p, (n, n_trials))
    binomial_samples = np.sum(bern_samples, axis=0)

    plt.hist(binomial_samples, bins=range(n + 2), density=True, color='b', edgecolor='black')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('Histogram of Binomial(n=100, p=0.8) via Bernoulli')
    plt.grid(True)
    plt.show()

    prob_empirical = np.mean(np.array(binomial_samples) <= 70)
    prob_theoretical = sum([math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(71)])
    print("Empirical probability:", prob_empirical)
    print("Theoretical probability:", prob_theoretical)
    return binomial_samples

def generateBinomialInverse():
    binomial_samples = []
    cdf = [math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(n + 1)]
    cdf = np.cumsum(cdf)  # Compute cumulative distribution function (CDF)
    for _ in range(n_trials):
        u = np.random.uniform(0, 1)  # Uniform random variable
        # Find the smallest k such that CDF[k] >= u
        k = np.searchsorted(cdf, u)
        binomial_samples.append(k)

    # Plot histogram
    plt.hist(binomial_samples, bins=range(n + 2), density=True, alpha=0.75, color='r', edgecolor='black')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('Histogram of Binomial(n=100, p=0.8) via Inverse Transform')
    plt.grid(True)
    plt.show()

    # Empirical probability of Binomial <= 70
    prob_empirical = np.mean(np.array(binomial_samples) <= 70)

    # Theoretical probability of Binomial <= 70
    prob_theoretical = sum([math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(71)])

    print("Empirical probability (Binomial <= 70):", prob_empirical)
    print("Theoretical probability (Binomial <= 70):", prob_theoretical)
    return binomial_samples

def compare_methods():
    # Timing and generating samples for Bernoulli method
    start = time.time()
    samples_bernoulli = doBernouli()
    time_bernoulli = time.time() - start

    # Timing and generating samples for Inverse Transform method
    start = time.time()
    samples_inverse = generateBinomialInverse()
    time_inverse = time.time() - start

    # Compare times
    print("\nTime taken for Bernoulli method: {:.4f} seconds".format(time_bernoulli))
    print("Time taken for Inverse Transform method: {:.4f} seconds".format(time_inverse))

    # Overlaid histogram for comparison
    plt.hist(samples_bernoulli, bins=range(n + 2), density=True, color='b', label='Bernoulli Method', edgecolor='black')
    plt.hist(samples_inverse, bins=range(n + 2), density=True, color='r', label='Inverse Transform', edgecolor='black')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('Comparison of Binomial Histograms')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run all parts
compare_methods()
