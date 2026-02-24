import numpy as np


from typing import Iterable
from scipy.stats import rv_continuous
from structure_types import StateOfSystem


class StatePriorProbability:
    state_variables_prior_probabilities: Iterable[rv_continuous]

    def __init__(self, state_variables_prior_probabilities: Iterable[rv_continuous]) -> None:
        self.state_variables_prior_probabilities = state_variables_prior_probabilities

    def calculate_prior_likelihood_sigma(self, state_of_system: StateOfSystem) -> np.float64:
        if state_of_system.get_state().size != 2:
            raise ValueError(f'Number of parameters ({state_of_system.get_state().size}) is not equal to {2}!')

    def calculate_prior_log_likelihood(self, state_of_system: StateOfSystem) -> np.float64:
        ...


if __name__ == '__main__':
    pass
