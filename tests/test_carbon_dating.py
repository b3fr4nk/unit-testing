import pytest
import math
from carbon_dating import get_age_carbon_14_dating

# Write a unit test which feed 0.35 to the function.
# The result should be '8680.34'. Does the function handles
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle
# every possible input properly. Then write a unit test againt
# this special case.


def test_get_age_carbon_14_dating():
    # Test with value of 0.35
    result = get_age_carbon_14_dating(0.35)
    assert math.isclose(result, 8680.34, rel_tol=1e-2)


def test_get_age_carbon_14_dating_zero():
    # Test with value of zero, expecting value error
    with pytest.raises(ValueError):
        get_age_carbon_14_dating(0)


def test_get_age_carbon_14_dating_negative():
    # Test with value of -1, expecting ValueError
    with pytest.raises(ValueError):
        get_age_carbon_14_dating(-1)


def test_get_age_carbon_14_dating_string():
    # Test with value of 'hello world', expecting TypeError
    with pytest.raises(TypeError):
        get_age_carbon_14_dating('hello world')


def test_get_age_carbon_14_dating_greater_than_one():
    # Test with value of 3.14, expecting a ValueError
    with pytest.raises(ValueError):
        get_age_carbon_14_dating(1.14)
