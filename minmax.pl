% max(X, Y, Max): Max is the bigger of X and Y
max(X, Y, X) :- X >= Y.
max(X, Y, Y) :- X < Y.

% min(X, Y, Min): Min is the smaller of X and Y
min(X, Y, X) :- X =< Y.
min(X, Y, Y) :- X > Y.