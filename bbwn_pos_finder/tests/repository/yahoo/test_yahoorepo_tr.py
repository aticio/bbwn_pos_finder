from bbwn_pos_finder.repository.yahoo.yahoorepo_tr import YahooRepoTR


def test_repo_get_data_with_parameters():
    symbol = "ISCTR.IS"
    interval = "1d"

    yahoo_repo = YahooRepoTR()
    data = yahoo_repo.get_data(symbol, interval)

    assert isinstance(data, list) is True


def test_repo_list_pairs():
    yahoo_repo = YahooRepoTR()
    pairs = yahoo_repo.list_pairs()

    assert isinstance(pairs, list) is True