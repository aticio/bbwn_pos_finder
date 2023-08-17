import dataclasses


@dataclasses.dataclass
class Result:
    symbol: str
    open_position: bool
    bbwn_length: int
    bbwn_std: int
    ssf_length_1: int
    ssf_length_2: int
