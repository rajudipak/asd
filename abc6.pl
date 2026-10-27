female(catherine).
female(sophia).
female(elizabeth).

male(X) :- \+ female(X).

parent(james1, charles1).
parent(james1, elizabeth).
parent(charles1, catherine).
parent(charles1, james2).
parent(charles1, charles2).
parent(elizabeth, sophia).
parent(sophia, george).

mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).

sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.

aunt(X, Y) :- parent(P, Y), sibling(X, P), female(X).
uncle(X, Y) :- parent(P, Y), sibling(X, P), male(X).

grandparent(X, Y) :- parent(X, P), parent(P, Y).

cousin(X, Y) :- parent(P1, X), parent(P2, Y), sibling(P1, P2).

/*
Queries:
1. Find the mother of Catherine.
mother(X, catherine).

2. Find who is the aunt or uncle of George.
aunt(X, george).
uncle(X, george).

3. Find all grandparents of George.
grandparent(X, george).

Extra queries:
father(X, catherine).
mother(X, sophia).
sibling(catherine, X).
cousin(sophia, X).
*/