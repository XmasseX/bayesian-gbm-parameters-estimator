import numpy as np

from src.structure_types import StateOfSystem
from src.mcmc_core import MetropolisHastingsAlgorithm
from src.printer import print_list_of_states_2d


def common_likelihood(state: StateOfSystem) -> float:
    likelihood = 0
    mu, sigma = state.get_state()

    if not sigma > 0:
        return -np.inf

    sample = np.random.normal(loc=5, scale=2.0, size=10)

    for el in sample:
        likelihood += - 1 / 2 / sigma ** 2 * (el - mu) ** 2 - np.log(np.sqrt(2 * np.pi) * sigma)

    return likelihood


if __name__ == '__main__':
    metropolis_hastings_algorithm = MetropolisHastingsAlgorithm()

    initial_state = StateOfSystem(
        state_variables=np.asarray(np.zeros(2), dtype=np.float64),
        covariance_matrix=np.asarray(np.diag([0.1, 0.1]), dtype=np.float64)
    )
    print(f'state: {initial_state.state_variables.shape}')
    print(f'state: {initial_state.covariance_matrix.shape}')

    list_of_states = metropolis_hastings_algorithm.get_list_of_states(initial_state, common_likelihood)
    print_list_of_states_2d(list_of_states)
