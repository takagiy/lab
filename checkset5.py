from istset5 import *
import totex
import check

totex.compile('cr30_4_8.tex', N, ists)
check.do_check(N, D1, D2, ists)
