import numpy as np
import numpy.typing as npt
import typing


Vector1D: typing.TypeAlias = npt.NDArray[np.float64]
Matrix2D: typing.TypeAlias = npt.NDArray[np.float64]


class StateOfSystem:
    state_variables: Vector1D
    covariance_matrix: Matrix2D

    def __init__(self, state_variables: Vector1D, covariance_matrix: Matrix2D) -> None:
        ...

    def get_state_dimension(self) -> int:
        return self.state_variables.size
