from bbwn_pos_finder.repository.binance.binancerepo import BinanceRepo
from unittest import mock
import os


@mock.patch.dict(os.environ, {"BINANCE_KLINE_URL": "https://api.binance.com/api/v3/klines"})
def test_repo_get_data_with_parameters():
    symbol = "BTCUSDT"
    interval = "1d"

    binance_repo = BinanceRepo()
    data = binance_repo.get_data(symbol, interval)

    assert isinstance(data, list) is True


@mock.patch.dict(os.environ, {"BINANCE_EXCHANGE_INFO": "https://api.binance.com/api/v3/exchangeInfo"})
def test_repo_list_pairs():
    binance_repo = BinanceRepo()
    pairs = binance_repo.list_pairs()

    assert isinstance(pairs, list) is True
