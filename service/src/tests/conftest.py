import numpy as np

import pytest

from ..models.activity_factor import MIFFLINSTJEOR_ACTIVITYFACTOR
from ..models.coefficients import MIFFLINSTJEOR
from ..models.equations import Equations
from ..models.model import RMRModel
from ..models.time_projection import TimeProjection


@pytest.fixture
def equations()-> Equations:
    return Equations()

@pytest.fixture
def valid_time_projection() -> np.ndarray:
    return np.arange(0, 10)

@pytest.fixture
def invalid_time_projection() -> np.ndarray:
    return np.arange(-10, 0)

@pytest.fixture(params=[
    {"sex": "male", "units": "si", "age": 30, "weight": 70, "height": 1.75, "weight_loss_rate": 0.5},
    {"sex": "female", "units": "imperial", "age": 25, "weight": 150, "height": 65, "weight_loss_rate": 0.3},
])
def valid_input_data(request):
    return request.param


@pytest.fixture
def coefficients_fixture():
    """
    Fixture providing MIFFLINSTJEOR coefficients for testing.

    Returns
    -------
    dict
        A dictionary containing coefficients for the Mifflin-St Jeor equations.
    """
    return MIFFLINSTJEOR


@pytest.fixture
def activity_factors_fixture():
    """
    Fixture providing activity factors for testing.

    Returns
    -------
    dict
        A dictionary containing activity factors based on activity levels.
    """
    return MIFFLINSTJEOR_ACTIVITYFACTOR


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
def rmr_model() -> RMRModel:
    """
    Fixture providing an instance of the RMRModel class.

    Returns
    -------
    RMRModel
        An instance of the RMRModel class.
    """
    return RMRModel()


@pytest.fixture
def edge_case_input_data():
    """
    Fixture providing edge case input data for RMRModel.

    Returns
    -------
    dict
        Input data containing edge case values for testing.
    """
    return {
        "sex": "female",
        "units": "imperial",
        "age": 20,
        "weight": 1.0,
        "height": 1.0,
        "weight_loss_rate": 0.0,
        "duration": 0,
    }
