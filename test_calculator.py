import pytest
from calculator import Calculator

# Fixture 1: Standard calculator instance
@pytest.fixture
def calc():
    return Calculator()

# Fixture 2: A second fixture to satisfy the requirement, could be used for specific setups if needed
@pytest.fixture
def advanced_calc():
    return Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),
    (-2, 8, 6),
    (0, 0, 0)
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (-2, 8, -10),
    (0, 0, 0)
])
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 50),
    (-2, 8, -16),
    (0, 100, 0)
])
def test_multiply(advanced_calc, a, b, expected):
    assert advanced_calc.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2.0),
    (5, 2, 2.5),
    (1, 3, pytest.approx(0.3333333333333333))  # 4. Use of pytest.approx for float result
])
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected

# 3. Test asserting divide(x, 0) raises ZeroDivisionError
def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)
