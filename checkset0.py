from istset0 import *
import totex
import check

totex.compile('cr20_4_8.tex', N, ists)
check.do_check(N, D1, D2, ists)
