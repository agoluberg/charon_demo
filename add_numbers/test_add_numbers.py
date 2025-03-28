import pytest
import add_numbers


def test_add_1_and_2():
    assert add_numbers.add_numbers(1, 2) == 3
