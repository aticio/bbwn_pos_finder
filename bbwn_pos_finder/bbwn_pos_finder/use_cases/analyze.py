from legitindicators import bollinger_bands_width_normalized, super_smoother
from bbwn_pos_finder.domain.result import Result


def analyze(repo, symbol, interval, bbwn_length, bbwn_std, ssf_length_1, ssf_length_2):
    data = repo.get_data(symbol, interval)

    bbwn = bollinger_bands_width_normalized(data, bbwn_length, bbwn_std)
    ssf_1 = super_smoother(data, ssf_length_1)
    ssf_2 = super_smoother(data, ssf_length_2)

    if bbwn[-1] > 0 and bbwn[-2] == 0 and ssf_1[-1] > ssf_2[-1]:
        result = Result(
            symbol=symbol,
            open_position=True,
            bbwn_length=bbwn_length,
            bbwn_std=bbwn_std,
            ssf_length_1=ssf_length_1,
            ssf_length_2=ssf_length_2
        )
    else:
        result = Result(
            symbol=symbol,
            open_position=False,
            bbwn_length=bbwn_length,
            bbwn_std=bbwn_std,
            ssf_length_1=ssf_length_1,
            ssf_length_2=ssf_length_2
        )

    return result
