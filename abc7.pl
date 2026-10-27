food(burger).
food(sandwich).
food(pizza).

lunch(sandwich).
dinner(pizza).

meal(X) :- food(X).

/*
Queries:
1. List all items that are food.
food(X).

2. Check whether burger is a meal.
meal(burger).

3. Check whether pizza is a meal.
meal(pizza).

4. Find all items that can be considered meals.
meal(X).
*/