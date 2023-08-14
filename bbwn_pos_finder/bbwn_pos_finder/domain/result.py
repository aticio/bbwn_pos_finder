import dataclasses

@dataclasses.dataclass
class Result:
    symbol: str
    open_position: bool
