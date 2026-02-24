import numpy as np


from typing import Callable
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

    @staticmethod
    def get_list_of_states(
            initial_state: StateOfSystem,
            log_likelihood: Callable[[StateOfSystem], float],
            number_of_simulations: int = 1000
    ) -> list[StateOfSystem]:
        current_state = initial_state
        list_of_states = [current_state]
        for i in range(number_of_simulations):
            likelihood_current_state = log_likelihood(current_state)
            proposal = MetropolisHastingsAlgorithm.get_proposal(current_state)
            likelihood_proposal = log_likelihood(proposal)

            alpha = np.random.rand()
            if likelihood_proposal - likelihood_current_state > np.log(alpha):
                current_state = proposal
            else:
                pass
            print(alpha)
            # current_state = proposal
            # print(proposal.state_variables.shape, proposal.covariance_matrix.shape)
            list_of_states.append(current_state)

        return list_of_states


if __name__ == '__main__':
    initial_state_of_system = StateOfSystem(
        state_variables=np.zeros(2),
        covariance_matrix=np.eye(2, 2)
    )

    metropolis_hastings_process = MetropolisHastingsAlgorithm()
    print(metropolis_hastings_process.get_proposal(initial_state_of_system))
    list_of_states_of_system = metropolis_hastings_process.get_list_of_states(initial_state_of_system)

    # print_list_of_states_2d(metropolis_hastings_process.get_list_of_states(initial_state_of_system))
