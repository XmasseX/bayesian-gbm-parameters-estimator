from structure_types import StateOfSystem


class MetropolisHastingsAlgorithm:
    state_of_system: StateOfSystem

    def __init__(self, state_of_system: StateOfSystem) -> None:
        if state_of_system.state_variables.ndim != 1:
            raise ValueError(f'Expected 1-dimensional array, not '
                             f'{state_of_system.state_variables.ndim}-dimensional!')

        if state_of_system.state_variables.ndim != 2:
            raise ValueError(f'Expected 2-dimensional array, not '
                             f'{state_of_system.covariance_matrix.ndim}-dimensional!')

        if not state_of_system.covariance_matrix.shape[0] == state_of_system.covariance_matrix.shape[1]:
            raise ValueError(f'Expected squared covariance matrix,'
                             f' not ({state_of_system.covariance_matrix.shape[0]},'
                             f' {state_of_system.covariance_matrix.shape[1]})-shaped!')

        if state_of_system.covariance_matrix.shape[0] != state_of_system.state_variables.shape[0]:
            raise ValueError(f'Dimension of covariance matrix is not compatible with state dimension!')

        self.state_of_system = state_of_system

    def get_proposal(self) -> StateOfSystem:
        ...


if __name__ == '__main__':
    pass
