import pytest
import math

def calculate_log(numbers):
    return [math.log(abs(num)) for num in numbers]

def test_calculate_log():
    numbers = [1, -2, 3, -4, 5]
    expected_result = [math.log(1), math.log(2), math.log(3), math.log(4), math.log(5)]
    assert calculate_log(numbers) == expected_result

def test_calculate_log_with_zero():
    numbers = [0, -2, 3, -4, 5]
    with pytest.raises(ValueError):
        calculate_log(numbers)

def test_calculate_log_with_empty_list():
    numbers = []
    assert calculate_log(numbers) == []
