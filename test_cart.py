import pytest
import time
from cart import ShoppingCart

# 1. Module-scoped fixture (shared setup)
@pytest.fixture(scope="module")
def module_cart():
    cart = ShoppingCart()
    cart.add_item("Laptop", 1000.0, 1)
    cart.add_item("Mouse", 50.0, 2)
    return cart

# 1. Function-scoped fixture (fresh cart)
@pytest.fixture(scope="function")
def fresh_cart():
    return ShoppingCart()

def test_add_item(fresh_cart):
    fresh_cart.add_item("Apple", 1.5, 3)
    assert fresh_cart.total() == 4.5
    fresh_cart.add_item("Apple", 1.5, 2)
    assert fresh_cart.total() == 7.5

def test_remove_item(fresh_cart):
    fresh_cart.add_item("Apple", 1.5, 3)
    fresh_cart.remove_item("Apple")
    assert fresh_cart.total() == 0.0
    fresh_cart.remove_item("NonExistent") # should not raise error

def test_module_cart_total(module_cart):
    # Laptop: 1000, Mouse: 2 * 50 = 100 -> Total: 1100
    assert module_cart.total() == 1100.0

# 2. Parametrize over discount percentages, verify with pytest.approx
@pytest.mark.parametrize("percent, expected_total", [
    (0, 100.0),
    (10, 90.0),
    (25, 75.0),
    (50, 50.0),
    (100, 0.0),
    (33.33, 66.67)
])
def test_apply_discount(fresh_cart, percent, expected_total):
    fresh_cart.add_item("Shirt", 50.0, 2)
    discounted = fresh_cart.apply_discount(percent)
    assert discounted == pytest.approx(expected_total, rel=1e-3)

def test_apply_discount_invalid(fresh_cart):
    with pytest.raises(ValueError):
        fresh_cart.apply_discount(110)

# 3. Custom mark @pytest.mark.slow
@pytest.mark.slow
def test_slow_operation(fresh_cart):
    time.sleep(0.1) # Simulate slow test
    fresh_cart.add_item("Expensive Item", 9999.99, 1)
    assert fresh_cart.total() == 9999.99

# 4. Test for apply_coupon marked skip
@pytest.mark.skip(reason="not implemented")
def test_apply_coupon(fresh_cart):
    fresh_cart.apply_coupon("SAVE20")
