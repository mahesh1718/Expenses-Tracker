import pytest
from unittest.mock import patch, mock_open
from datetime import date
from project import expensetype, expenditure, get_budget, set_budget, saving, Date  # Import the project module
import project

# Mock input function for testing expensetype
@pytest.mark.parametrize("input_value, expected_output", [
    ("medical", "medical"),
    ("rental", "rental"),
    ("school fee", "school fee"),
    ("college fee", "college fee"),
    ("other", "other"),
])
def test_expensetype(input_value, expected_output):
    with patch('builtins.input', return_value=input_value):
        assert expensetype() == expected_output


# Test for expenditure function
@pytest.mark.parametrize("expense_type, amount, expected_output", [
    ("medical", 1000, 1000),
    ("rental", 1500, 1500),
    ("school fee", 2000, 2000),
    ("college fee", 2500, 2500),
    ("other", 500, 500),
])
def test_expenditure(expense_type, amount, expected_output):
    with patch('builtins.input', return_value=str(amount)):
        assert expenditure(expense_type) == expected_output


# Test for get_budget function
def test_get_budget():
    # Test case where file exists with valid content
    mock_open_function = mock_open(read_data="10000")
    with patch('builtins.open', mock_open_function):
        assert get_budget() == 10000

    # Test case where file doesn't exist or is empty
    mock_open_function = mock_open(read_data="")
    with patch('builtins.open', mock_open_function):
        assert get_budget() is None


# Test for set_budget function
def test_set_budget():
    # Mocking the open function to simulate file writing
    mock_open_function = mock_open()
    with patch('builtins.open', mock_open_function):
        set_budget(20000)
        mock_open_function.assert_called_once_with("budget.txt", "w")
        mock_open_function().write.assert_called_once_with("20000")


# Test for saving function
def test_saving():
    assert saving(10000, 2000) == 8000
    assert saving(5000, 1000) == 4000


# Test for Date function (testing today's date)
def test_date():
    today = Date()
    assert today == date.today()
