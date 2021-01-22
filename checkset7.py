from istset7 import *
import totex
import check

totex.compile('cr32_4_8.tex', N, ists)
check.do_check(N, D1, D2, ists)
