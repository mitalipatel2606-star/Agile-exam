import pytest
from library import calculate_fine

@pytest.mark.parametrize("days, expected", [
    (0, 0),
    (3, 6),
    (5, 10),
    (6, 30),
    (10, 50),
    (11, 110)
])
def test_fine(days, expected):
    assert calculate_fine(days) == expected

def test_invalid():
    with pytest.raises(ValueError):
        calculate_fine(-1)