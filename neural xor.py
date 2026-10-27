def activation(total):
    if total >= 0:
        return 1
    return 0
 
x1 = int(input("Enter x1 and x2 (0 or 1): "))
x2 = int(input())
h1 = activation(x1 + x2 - 0.5)
h2 = activation(-x1 - x2 + 1.5)
output = activation(h1 + h2 - 1.5)
print("Hidden layer h1 (OR) =", h1)
print("Hidden layer h2 (NAND) =", h2)
print("XOR Output =", output)