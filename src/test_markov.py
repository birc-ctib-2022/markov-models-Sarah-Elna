"""Testing Markov models."""

from markov import *

def test_me() -> None:
    """Test your code."""
    SUNNY = 0
    CLOUDY = 1

    X = [SUNNY, SUNNY, CLOUDY, SUNNY]

    init_probs = [0.1, 0.9]  # it is almost always cloudy
    transitions_from_SUNNY = [0.3, 0.7]
    transitions_from_CLOUDY = [0.4, 0.6]
    transition_probs = [
        transitions_from_SUNNY,
        transitions_from_CLOUDY
    ]
    M = MarkovModel(init_probs, transition_probs)

    x_prob = 0.1 * 0.3 * 0.7 * 0.4

    prob = likelihood(X, M)

    assert x_prob == prob
