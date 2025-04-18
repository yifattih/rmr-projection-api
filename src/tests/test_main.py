import pytest


def test_root_endpoint(client) -> None:
    """Test for root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "Welcome to the RMR API" in response.json()["message"]


def test_invalid_endpoint(client) -> None:
    """Test for invalid endpoint"""
    response = client.get("/invalid")
    assert response.status_code == 404


@pytest.mark.parametrize(
    "input_data, expected_status, type",
    [
        # Valid input
        (
            {
                "sex": "male",
                "units": "si",
                "age": 30,
                "weight": 70.0,
                "height": 1.75,
                "weight_loss_rate": 0.5,
                "duration": 12,
            },
            200,
            "valid input",
        ),
        # Invalid age (too low)
        (
            {
                "sex": "male",
                "units": "si",
                "age": 19,
                "weight": 70.0,
                "height": 1.75,
                "weight_loss_rate": 0.5,
                "duration": 12,
            },
            422,
            "invalid age",
        ),
        # Invalid weight (zero)
        (
            {
                "sex": "male",
                "units": "si",
                "age": 30,
                "weight": 0.0,
                "height": 1.75,
                "weight_loss_rate": 0.5,
                "duration": 12,
            },
            422,
            "invalid weight",
        ),
        # Invalid height (negative value)
        (
            {
                "sex": "male",
                "units": "si",
                "age": 30,
                "weight": 70.0,
                "height": -1.75,
                "weight_loss_rate": 0.5,
                "duration": 12,
            },
            422,
            "invalid height",
        ),
        # Invalid weight_loss_rate (negative value)
        (
            {
                "sex": "male",
                "units": "si",
                "age": 30,
                "weight": 70.0,
                "height": 1.75,
                "weight_loss_rate": -0.5,
                "duration": 12,
            },
            422,
            "invalid weight_loss_rate",
        ),
        # Missing required field (sex)
        (
            {
                "units": "si",
                "age": 30,
                "weight": 70.0,
                "height": 1.75,
                "weight_loss_rate": 0.5,
                "duration": 12,
            },
            422,
            "missing field sex",
        ),
        # Invalid units
        (
            {
                "sex": "male",
                "units": "metric",
                "age": 30,
                "weight": 70.0,
                "height": 1.75,
                "weight_loss_rate": 0.5,
                "duration": 12,
            },
            422,
            "invalid units",
        ),
    ],
)
def test_calculate_rmr(input_data, expected_status, type, client) -> None:
    f"""Test for /projections endpoint with ${type}"""
    response = client.post("/projections", json=input_data)
    assert response.status_code == expected_status
    if expected_status == 200:
        data = response.json()
        assert "rmr" in data
        assert "time_projection" in data


def test_health_check(client) -> None:
    """Test for /health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
