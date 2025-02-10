def test_missing_keys(rmr_model):
    input_data = {"sex": "male", "age": 25}  # Missing required keys
    result = rmr_model.process(input_data)
    assert "error" in result
    assert result["exit_code"] == 1


def test_invalid_age(rmr_model):
    input_data = {
        "sex": "male",
        "units": "si",
        "age": 18,
        "weight": 70,
        "height": 175,
        "weight_loss_rate": 0.5,
        "duration": 10,
    }
    result = rmr_model.process(input_data)
    assert "Invalid age" in result["error"]
    assert result["exit_code"] == 1


def test_invalid_weight(rmr_model):
    input_data = {
        "sex": "male",
        "units": "si",
        "age": 30,
        "weight": 0,
        "height": 175,
        "weight_loss_rate": 0.5,
        "duration": 10,
    }
    result = rmr_model.process(input_data)
    assert "Invalid weight" in result["error"]
    assert result["exit_code"] == 1


def test_invalid_height(rmr_model):
    input_data = {
        "sex": "male",
        "units": "si",
        "age": 30,
        "weight": 70,
        "height": 0,
        "weight_loss_rate": 0.5,
        "duration": 10,
    }
    result = rmr_model.process(input_data)
    assert "Invalid height" in result["error"]
    assert result["exit_code"] == 1


def test_invalid_weight_loss_rate(rmr_model):
    input_data = {
        "sex": "male",
        "units": "si",
        "age": 30,
        "weight": 70,
        "height": 175,
        "weight_loss_rate": -1,
        "duration": 10,
    }
    result = rmr_model.process(input_data)
    assert "Invalid weight loss rate" in result["error"]
    assert result["exit_code"] == 1


def test_invalid_duration(rmr_model):
    input_data = {
        "sex": "male",
        "units": "si",
        "age": 30,
        "weight": 70,
        "height": 175,
        "weight_loss_rate": 0.5,
        "duration": -1,
    }
    result = rmr_model.process(input_data)
    assert "Invalid duration" in result["error"]
    assert result["exit_code"] == 1


def test_valid_input(rmr_model):
    input_data = {
        "sex": "male",
        "units": "si",
        "age": 30,
        "weight": 70,
        "height": 175,
        "weight_loss_rate": 0.5,
        "duration": 10,
    }
    result = rmr_model.process(input_data)
    assert "output" in result
    assert "rmr" in result["output"]
    assert "time_projection" in result["output"]
    assert result["exit_code"] == 0


def test_exception_handling(rmr_model, monkeypatch):
    def mock_calculate(*args, **kwargs):
        raise ValueError("Unexpected error during calculation")

    monkeypatch.setattr(
        rmr_model.time_projection_helper, "calculate", mock_calculate
    )

    input_data = {
        "sex": "male",
        "units": "si",
        "age": 30,
        "weight": 70.0,
        "height": 175.0,
        "weight_loss_rate": 0.5,
        "duration": 10,
    }
    result = rmr_model.process(input_data)
    assert result["exit_code"] == 1
    assert "Unexpected error during calculation" in result["error"]
