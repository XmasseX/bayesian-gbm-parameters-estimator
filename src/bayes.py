import numpy as np


from typing import Iterable
from scipy.stats import rv_continuous
from structure_types import StateOfSystem


class StatePriorProbability:
    state_variables_prior_probabilities: Iterable[rv_continuous]

    def __init__(self, state_variables_prior_probabilities: Iterable[rv_continuous]) -> None:
        self.state_variables_prior_probabilities = state_variables_prior_probabilities

    def calculate_prior_likelihood(self, state_of_system: StateOfSystem) -> np.float64:
        ...

    def calculate_prior_log_likelihood(self, state_of_system: StateOfSystem) -> np.float64:
        ...


if __name__ == '__main__':
    pass
