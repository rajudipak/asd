def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0
    if x <= b:
        return (x - a) / (b - a)
    return (c - x) / (c - b)
 
dirt = float(input("Enter Dirt Level (0-100): "))
grease = float(input("Enter Grease Level (0-100): "))
d = [triangular(dirt, *p) for p in
     [(0,25,50), (25,50,75), (50,75,100)]]
g = [triangular(grease, *p) for p in
     [(0,25,50), (25,50,75), (50,75,100)]]
 
print("\nDirt:", [round(x,2) for x in d])
print("Grease:", [round(x,2) for x in g])
rules = [min(d[i], g[j]) for i, j in
         [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]]
strengths = [rules[0], max(rules[1],rules[3]),
             max(rules[2],rules[4],rules[6]),
             max(rules[5],rules[7]), rules[8]]
times = [10,20,30,40,50]
total = sum(strengths)
if total:
    wash_time = sum(s*t for s,t in zip(strengths,times)) / total
else:
    wash_time = 0
print("Rule Strengths:", [round(x,2) for x in strengths])
print("Estimated Wash Time =", round(wash_time,2), "minutes")
if wash_time < 15:
    print("Recommendation: Very Short Wash")
elif wash_time < 25:
    print("Recommendation: Short Wash")
elif wash_time < 35:
    print("Recommendation: Medium Wash")
elif wash_time < 45:
    print("Recommendation: Long Wash")
else:
    print("Recommendation: Very Long Wash")