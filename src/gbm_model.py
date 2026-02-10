from structure_types import StateOfSystem


class StateGBM:
    state_of_system: StateOfSystem

    def __init__(self, state_of_system: StateOfSystem) -> None:
        self.state_of_system = state_of_system
