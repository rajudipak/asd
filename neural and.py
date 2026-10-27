x1 = float(input("Enter x1 and x2: "))
x2 = float(input())
total = x1 + x2 - 1.5
output = 0
if total >= 0:
    output = 1
print("Sum = %.2f" % total)
print("Output =", output)