series(R1, R2, R) :- R is R1 + R2.
parallel(R1, R2, R) :- R is (R1 * R2) / (R1 + R2).
mixed(R1, R2, R3, R) :- parallel(R2, R3, Rp), series(R1, Rp, R).

series_list([], 0).
series_list([H|T], R) :- series_list(T, R1), R is H + R1.

inverse_sum([], 0).
inverse_sum([H|T], S) :- inverse_sum(T, S1), S is 1/H + S1.

parallel_list(L, R) :- inverse_sum(L, S), R is 1/S.

/*
Queries:
1. Two resistors in series (10 and 20 ohms)
series(10, 20, R).
R = 30.

2. Two resistors in parallel (10 and 20 ohms)
parallel(10, 20, R).
R = 6.666666666666667.

3. 10 ohm in series with (20 ohm parallel 30 ohm)
mixed(10, 20, 30, R).
R = 22.

4. Many resistors in series (10, 20, 30 ohms)
series_list([10, 20, 30], R).
R = 60.

5. Many resistors in parallel (10, 10 ohms)
parallel_list([10, 10], R).
R = 5.0.

6. Many resistors in parallel (10, 20, 30 ohms)
parallel_list([10, 20, 30], R).
R = 5.454545454545454 (approximately).
*/