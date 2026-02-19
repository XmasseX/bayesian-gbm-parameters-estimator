import numpy as np
import numpy.typing as npt
import typing


Vector1D: typing.TypeAlias = npt.NDArray[np.float64]
Matrix2D: typing.TypeAlias = npt.NDArray[np.float64]


class StateOfSystem:
    state_variables: Vector1D
    covariance_matrix: Matrix2D

    def __init__(self, state_variables: Vector1D, covariance_matrix: Matrix2D) -> None:
        self.state_variables = state_variables
        self.covariance_matrix = covariance_matrix

    def get_state(self) -> Vector1D:
        return self.state_variables

    def get_covariance_matrix(self) -> Matrix2D:
        return self.covariance_matrix

    def add_increment(self, increment_state: Vector1D) -> 'StateOfSystem':
        if increment_state.size != self.state_variables.size:
            raise ValueError(f'Size of increment ({increment_state.size}) must '
                             f'be the same as state variable ({self.state_variables.size})')
        return StateOfSystem(
            state_variables=self.state_variables + increment_state,
            covariance_matrix=self.covariance_matrix
        )

    def get_state_dimension(self) -> int:
        return self.state_variables.size
