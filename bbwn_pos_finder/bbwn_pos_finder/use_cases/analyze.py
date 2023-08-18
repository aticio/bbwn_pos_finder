from legitindicators import bollinger_bands_width_normalized, super_smoother
from bbwn_pos_finder.domain.result import Result
from bbwn_pos_finder.responses import (
    ResponseSuccess,
    ResponseFailure,
    ResponseTypes,
    build_response_from_invalid_request,
)


def analyze(repo, request):
    if not request:
        return build_response_from_invalid_request(request)

    try:
        symbol = request.parameters["symbol"]
        interval = request.parameters["interval"]
        bbwn_length = request.parameters["bbwn_length"]
        bbwn_std = request.parameters["bbwn_std"]
        ssf_length_1 = request.parameters["ssf_length_1"]
        ssf_length_2 = request.parameters["ssf_length_2"]

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

        return ResponseSuccess(result)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
