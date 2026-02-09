import numpy as np


from structure_types import StateOfSystem


class StateGBM(StateOfSystem):
    def __init__(self, mu: float, sigma: float) -> None:
        self.state_variables = np.array([mu, sigma])
        self.covariance_matrix = np.eye(2)
