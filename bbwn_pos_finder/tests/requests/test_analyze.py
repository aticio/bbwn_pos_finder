from bbwn_pos_finder.requests.analyze import build_analyze_request


def test_build_analyze_request_without_parameters():
    request = build_analyze_request()

    assert request.has_errors()
    assert bool(request) is False


def test_build_analyze_request_missing_parameters():
    request = build_analyze_request({"symbol": "BTCUSDT", "interval": "1d"})

    assert request.has_errors()
    assert bool(request) is False


def test_build_analyze_request_with_invalid_keys():
    request = build_analyze_request({"sybol": "BTCUSDT", "interval": "1d", "bbwn_length": 20, "bbwn_std": 2, "ssf_length_1": 15, "ssf_length_2": 30})

    assert request.has_errors()
    assert bool(request) is False


def test_build_analyze_request_with_invalid_parameters():
    request = build_analyze_request("test")

    assert request.has_errors()
    assert bool(request) is False


def test_build_analyze_request_with_valid_parameters():
    request = build_analyze_request({"symbol": "BTCUSDT", "interval": "1d", "bbwn_length": 20, "bbwn_std": 2, "ssf_length_1": 15, "ssf_length_2": 30})

    assert bool(request) is True
