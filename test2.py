import check
import ctor

D1 = 2
D2 = 2 * D1
for N in range(3 * D2, 3 * D2 + 129):
    ists = ctor.makeists(N, D1, D2)
    print(f'====TEST CR({N}, {D1}, {D2})====')
    check.do_check(N, D1, D2, ists)
    print('')
