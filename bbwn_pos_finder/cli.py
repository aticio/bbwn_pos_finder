#!/usr/bin/env python

from bbwn_pos_finder.repository.memrepo import MemRepo
from bbwn_pos_finder.use_cases.analyze import analyze

repo = MemRepo()
result = analyze(repo, "BTCUSDT", "1d", 20, 2, 15, 30)

print(result)
