import pymc as pm
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    true_mu = 5.0
    true_sigma = 2.0

    sample = np.random.normal(true_mu, true_sigma, size=10)

    with pm.Model() as model:
        mu = pm.Normal('mu', mu=0, sigma=10)
        sigma = pm.HalfNormal('sigma', sigma=5)
        likelihood = pm.Normal('likelihood', mu=mu, sigma=sigma, observed=sample)

        trace = pm.sample(draws=500, discard_tuned_samples=False, return_inferencedata=True)

        mu_samples = trace.posterior['mu'].values
        sigma_samples = trace.posterior['sigma'].values

        plt.figure(figsize=(10, 8))
        plt.scatter(mu_samples, sigma_samples, marker='+', c='purple')
        plt.grid()
        plt.show()
