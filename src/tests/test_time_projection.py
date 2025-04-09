import numpy as np


def test_calculate_valid(time_projection) -> None:
    """Test the calculate method with valid input"""
    result = time_projection.calculate(5)
    assert result["exit_code"] == 0
    assert np.array_equal(result["result"], np.array([0, 1, 2, 3, 4, 5]))


def test_calculate_zero(time_projection) -> None:
    """Test the calculate method with zero input"""
    result = time_projection.calculate(0)
    assert result["exit_code"] == 0
    assert np.array_equal(result["result"], np.array([0]))


def test_calculate_negative(time_projection) -> None:
    """Test the calculate method with negative input"""
    result = time_projection.calculate(-1)
    assert result["exit_code"] == 1
    assert "Duration must be non-negative" in result["error"]


def test_calculate_large_number(time_projection) -> None:
    """Test the calculate method with large input"""
    result = time_projection.calculate(10000)
    assert result["exit_code"] == 0
    assert result["result"].shape == (10001,)
    assert result["result"][0] == 0
    assert result["result"][-1] == 10000


def test_calculate_type_error(time_projection) -> None:
    """Test the calculate method with invalid input type"""
    result = time_projection.calculate("ten")
    assert result["exit_code"] == 1
    assert (
        "'<' not supported between instances of 'str' and 'int'"
        in result["error"]
    )
