from istset4 import *
import totex
import check

totex.compile('cr29_4_8.tex', N, ists)
check.do_check(N, D1, D2, ists)