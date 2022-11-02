"""Markov models."""


import numpy as np


class MarkovModel:
    """Representation of a Markov model."""

    init_probs: list[float]
    trans: list[list[float]]

    def __init__(self,
                 init_probs: list[float],
                 trans: list[list[float]]):
        """Create model from initial and transition probabilities."""
        # Sanity check...
        k = len(init_probs)
        assert k == len(trans)
        for row in trans:
            assert k == len(row)

        self.init_probs = init_probs
        self.trans = trans


def likelihood(x: list[int], mm: MarkovModel) -> float:
    """
    Compute the likelihood of mm given x.

    This is the same as the probability of x given mm,
    i.e., P(x ; mm).
    """

    for i in range(0, len(x)):
        if i == 0: # base case, probability of starting at state x[0]
            prob = mm.init_probs[x[0]]
        else: # probability of transisioning from state x[i-1] to x[i]
            prob = prob * mm.trans[x[i-1]][x[i]]
    return prob
