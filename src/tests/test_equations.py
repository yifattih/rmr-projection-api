def test_mifflinstjeor_rmr_valid(
    equations, valid_input_data, valid_time_projection
) -> None:
    """Test the mifflinstjeor_rmr method with valid input data"""
    result = equations.mifflinstjeor_rmr(
        valid_input_data["sex"],
        valid_input_data["units"],
        valid_input_data["age"],
        valid_input_data["weight"],
        valid_input_data["height"],
        valid_input_data["weight_loss_rate"],
        valid_time_projection,
    )
    assert result["exit_code"] == 0
    assert "result" in result
    assert isinstance(result["result"], dict)


def test_mifflinstjeor_rmr_invalid_sex(
    equations, valid_time_projection
) -> None:
    """Test the mifflinstjeor_rmr method with invalid sex input"""
    result = equations.mifflinstjeor_rmr(
        "other", "si", 30, 70, 1.75, 0.5, valid_time_projection
    )
    assert result["exit_code"] == 1
    assert "Invalid combination of sex and units" in result["error"]


def test_mifflinstjeor_rmr_invalid_units(
    equations, valid_time_projection
) -> None:
    """Test the mifflinstjeor_rmr method with invalid units input"""
    result = equations.mifflinstjeor_rmr(
        "male", "metric", 30, 70, 1.75, 0.5, valid_time_projection
    )
    assert result["exit_code"] == 1
    assert "Invalid combination of sex and units" in result["error"]


def test_mifflinstjeor_rmr_invalid_time_projection(equations) -> None:
    """Test the mifflinstjeor_rmr method with invalid time projection input"""
    result = equations.mifflinstjeor_rmr(
        "male", "si", 30, 70, 1.75, -0.5, "time_projection"
    )
    assert result["exit_code"] == 1
    assert "error" in result
