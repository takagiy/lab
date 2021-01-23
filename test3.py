import check
import ctor
import totex

for D1 in range(2, 12):
    D2 = D1 * 2
    for N in [D1 * 5 - 1, D1 * 5]:
        print(f'CR({N}, {D1}, {D2})')
        ists = ctor.makeists(N, D1, D2)
        check.do_check(N, D1, D2, ists)
        print('')
