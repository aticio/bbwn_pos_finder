from bbwn_pos_finder.domain.result import Result

def test_result_model_init():
    result = Result(
        symbol="BTCUSDT",
        open_position=True
    )

    assert result.symbol == "BTCUSDT"
    assert result.open_position == True
