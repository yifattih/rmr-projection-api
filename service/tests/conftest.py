import numpy as np
import pytest

from ..main import app
from fastapi.testclient import TestClient
from ..models.model import Equations
from ..models.model import RMRModel
from ..models.time_projection import TimeProjection


@pytest.fixture
def client() -> TestClient:
    client = TestClient(app)
    return client


@pytest.fixture
def equations() -> Equations:
    return Equations()


@pytest.fixture
def valid_time_projection() -> np.ndarray:
    return np.arange(0, 10)


@pytest.fixture(
    params=[
        {
            "sex": "male",
            "units": "si",
            "age": 30,
            "weight": 70,
            "height": 1.75,
            "weight_loss_rate": 0.5,
        },
        {
            "sex": "female",
            "units": "imperial",
            "age": 25,
            "weight": 150,
            "height": 65,
            "weight_loss_rate": 0.3,
        },
    ]
)
def valid_input_data(request):
    return request.param


@pytest.fixture
def time_projection() -> TimeProjection:
    """
    Fixture providing an instance of the TimeProjection helper class.

    Returns
    -------
    TimeProjection
        An instance of the TimeProjection helper.
    """
    return TimeProjection()


@pytest.fixture
def rmr_model():
    """
    Fixture providing an instance of the RMRModel class.

    Returns
    -------
    TimeProjection
        An instance of the RMRModel.
    """
    return RMRModel()
