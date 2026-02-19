import numpy as np

from src.structure_types import StateOfSystem
from src.mcmc_core import MetropolisHastingsAlgorithm
from src.printer import print_list_of_states_2d


if __name__ == '__main__':
    metropolis_hastings_algorithm = MetropolisHastingsAlgorithm()

    initial_state = StateOfSystem(
        state_variables=np.asarray(np.zeros(2), dtype=np.float64),
        covariance_matrix=np.asarray(np.diag([1.0, 1.0]), dtype=np.float64)
    )
    print(f'state: {initial_state.state_variables.shape}')
    print(f'state: {initial_state.covariance_matrix.shape}')

    list_of_states = metropolis_hastings_algorithm.get_list_of_states(initial_state)
    print_list_of_states_2d(list_of_states)
