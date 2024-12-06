import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Parameters
n = 100
m = 1000
mu = 0  # Mean of normal distribution
sigma = np.sqrt(2)  # Standard deviation of normal


# Function to compute the confidence interval and histogram
def estimate_expectation_and_ci():
    # random variable samples
    samples = np.random.normal(mu, sigma, n)
    transformed_samples = 95 * np.exp(0.3 * samples + (0.05 - (0.3**2 / 2))*2)

    # Estimate expected value
    sample_mean = np.mean(transformed_samples)
    sample_std = np.std(transformed_samples, ddof=1)  # Unbiased sample std

    # 95% Confidence Interval
    t_critical = t.ppf(0.975, df=n - 1)
    margin_of_error = t_critical * (sample_std / np.sqrt(n))
    ci_lower = sample_mean - margin_of_error
    ci_upper = sample_mean + margin_of_error

    print(f"Sample Mean: {sample_mean}")
    print(f"95% Confidence Interval: ({ci_lower}, {ci_upper})")

    # Simulate sample means for the histogram
    sample_means = []
    for _ in range(m):
        simulated_samples = np.random.normal(mu, sigma, n)
        transformed = 95 * np.exp(0.3 * simulated_samples + (0.05 - (0.3**2 / 2))*2)
        sample_means.append(np.mean(transformed))

    # Plot histogram of sample means
    plt.hist(sample_means, bins=20, density=True, color='blue', edgecolor='black')
    plt.xlabel('Sample Mean')
    plt.ylabel('Probability')
    plt.title('Histogram of Sample Means')
    plt.grid(True)
    plt.show()


# Run the estimation and plot
estimate_expectation_and_ci()
