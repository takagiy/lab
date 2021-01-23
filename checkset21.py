from istset21 import *
import totex
import check

totex.compile(f'cr{N}_{D1}_{D2}_alt.tex', N, ists)
check.do_check(N, D1, D2, ists)
