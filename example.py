import check
import totex
import ctor

for D1 in range(2, 2 + 8):
    D2 = 2 * D1
    for N in range(5 * D1, 5 * D1 + 30, 10):
        ists = ctor.makeists(N, D1, D2)
        print(f'====TEST CR({N}, {D1}, {D2})====')
        check.do_check(N, D1, D2, ists)
        if N < 47:
            totex.compile(f'examples/ex_cr{N}_{D1}_{D2}.tex', N, ists)
        print('')
