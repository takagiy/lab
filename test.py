import check
import ctor

for D1 in range(3, 65):
    D2 = 2 * D1
    for N in range(3 * D2, 3 * D2 + 65):
        ists = ctor.makeists(N, D1, D2)
        print(f'====TEST CR({N}, {D1}, {D2})====')
        check.do_check(N, D1, D2, ists)
        print('')
