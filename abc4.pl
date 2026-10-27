studies(amol, physics).
studies(omkar, physics).
studies(javed, chemistry).
studies(ashwin, mathematics).

teaches(karthik, physics).
teaches(chahal, chemistry).
teaches(jasprit, mathematics).
teaches(chahel, biology).

professor_of(X, Y) :- teaches(X, Y).
student_of(X, Y) :- studies(X, Z), teaches(Y, Z).

/*
Queries:
1. Which subjects does amol study?
studies(amol, X).
X = physics.

2. Which subjects are taught by professor Chahal?
teaches(chahal, X).
X = chemistry.

3. Who are the students of Professor Karthik?
student_of(X, karthik).
X = amol ;
X = omkar.

Extra checks:
professor_of(karthik, physics).
true.

student_of(javed, chahal).
true.
*/