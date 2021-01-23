import totex
import check
import ctor

N = 46
D1 = 6
D2 = 12

ists = ctor.makeists(N, D1, D2)
totex.compile(f'cr{N}_{D1}_{D2}_alt.tex', N, ists)
check.do_check(N, D1, D2, ists)
