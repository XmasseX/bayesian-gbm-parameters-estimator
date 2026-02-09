import numpy as np
import numpy.typing as npt
import typing


Vector1D: typing.TypeAlias = npt.NDArray[np.float64]
Matrix2D: typing.TypeAlias = npt.NDArray[np.float64]


class StateOfSystem(typing.Protocol):
    state_variables: Vector1D
    covariance_matrix: Matrix2D
