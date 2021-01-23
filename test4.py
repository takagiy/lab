import check
import ctor

for D1 in range(2, 3 + 129):
    D2 = 2 * D1
    for N in range(5 * D1, 3 * D2):
        ists = ctor.makeists(N, D1, D2)
        print(f'====TEST CR({N}, {D1}, {D2})====')
        check.do_check(N, D1, D2, ists)
        print('')
