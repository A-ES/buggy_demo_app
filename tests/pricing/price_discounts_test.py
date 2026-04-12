import pytest

from src.pricing.price_discounts import calculate_discount

def test_calculate_discount_with_zero_quantity_no_division_by_zero_error():
    assert calculate_discount(100, 0) == 'Quantity cannot be zero'

def test_calculate_discount_with_positive_quantity_no_error():
    assert calculate_discount(100, 10) == 90.0

def test_calculate_discount_with_large_positive_quantity():
    assert round(calculate_discount(250, 50), 2) == 125.0

def test_calculate_discount_with_quantity_greater_than_100():
    assert round(calculate_discount(150, 120), 2) == -30.0
