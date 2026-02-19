import numpy as np


from numpy.random import multivariate_normal
from structure_types import StateOfSystem
# from printer import print_list_of_states_2d


class MetropolisHastingsAlgorithm:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_proposal(state: StateOfSystem) -> StateOfSystem:
        representative = multivariate_normal(
            mean=np.zeros(state.get_state().shape[0]),
            cov=state.covariance_matrix,
            size=1
        )
        return state.add_increment(np.array(representative).flatten())

    def get_list_of_states(self, initial_state: StateOfSystem) -> list[StateOfSystem]:
        current_state = initial_state
        list_of_states = [current_state]
        for i in range(100):
            proposal = MetropolisHastingsAlgorithm.get_proposal(current_state)
            current_state = proposal
            # print(proposal.state_variables.shape, proposal.covariance_matrix.shape)
            list_of_states.append(proposal)

        return list_of_states


if __name__ == '__main__':
    initial_state_of_system = StateOfSystem(
        state_variables=np.zeros(2),
        covariance_matrix=np.eye(2, 2)
    )

    metropolis_hastings_process = MetropolisHastingsAlgorithm()
    print(metropolis_hastings_process.get_proposal(initial_state_of_system))
    list_of_states = get_list_of_states(initial_state_of_system)

    # print_list_of_states_2d(metropolis_hastings_process.get_list_of_states(initial_state_of_system))
