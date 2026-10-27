% Facts
like(mary, food).
like(mary, wine).
like(mary, john).
like(joseph, joseph).

% Every fact is also a "likes"
likes(X, Y) :- like(X, Y).

% Rule 1: john likes anything that mary likes
likes(john, X) :- like(mary, X).

% Rule 2: john likes everyone who likes wine
likes(john, X) :- like(X, wine).

% Rule 3: john likes anyone who likes themselves
likes(john, X) :- like(X, X).