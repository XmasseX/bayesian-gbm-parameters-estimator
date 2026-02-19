import matplotlib.pyplot as plt


from structure_types import StateOfSystem


def print_list_of_states_2d(list_of_states: list[StateOfSystem]):
    if list_of_states[0].get_state().size != 2:
        raise ValueError(f'Function supports only 2-dimensional states')

    plt.figure(figsize=(10, 8))

    for state in list_of_states:
        x, y = state.get_state()
        plt.scatter(x, y, marker='+', c='violet')

    plt.grid()
    plt.show()
