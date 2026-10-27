series(R1, R2, R) :- R is R1 + R2.
parallel(R1, R2, R) :- R is (R1 * R2) / (R1 + R2).
mixed(R1, R2, R3, R) :- parallel(R2, R3, Rp), series(R1, Rp, R).

/*
Queries:
1. Two resistors in series (10 and 20 ohms)
series(10, 20, R).
R = 30.

2. Two resistors in parallel (10 and 20 ohms)
parallel(10, 20, R).
R = 6.666666666666667.

3. Two equal resistors in parallel (10 and 10 ohms)
parallel(10, 10, R).
R = 5.

4. R1 = 10 in series with (R2 = 20 parallel R3 = 30)
mixed(10, 20, 30, R).
R = 22.
*/