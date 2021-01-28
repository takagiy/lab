import check
import ctor

for N in  range(10, 128 + 1):
    for D1 in range(2, N // 5 + 1):
        D2 = 2 * D1
        ists = ctor.makeists(N, D1, D2)
        print(f'====TEST CR({N}, {D1}, {D2})====')
        check.do_check(N, D1, D2, ists)
        print('')
