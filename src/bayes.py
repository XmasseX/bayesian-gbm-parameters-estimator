import typing


def uniform_distribution_probability(value: float, left_border: float, right_border: float) -> float:
    if left_border >= right_border:
        raise ValueError('Левый край должен быть строго меньше правого!')

    if left_border <= value <= right_border:
        return 1.0 / (right_border - left_border)
    else:
        return 0.0


class PriorDistribution(typing.Protocol):
    def pdf(self, *args, **kwargs) -> float:
        ...
