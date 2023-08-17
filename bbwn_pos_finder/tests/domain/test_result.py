from bbwn_pos_finder.domain.result import Result


def test_result_model_init():
    result = Result(
        symbol="BTCUSDT",
        open_position=True,
        bbwn_length=20,
        bbwn_std=2,
        ssf_length_1=15,
        ssf_length_2=30
    )

    assert result.symbol == "BTCUSDT"
    assert result.open_position is True
    assert result.bbwn_length == 20
    assert result.bbwn_std == 2
    assert result.ssf_length_1 == 15
    assert result.ssf_length_2 == 30
