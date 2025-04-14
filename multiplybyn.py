def multiply_once(a, b):
    return a * b

def multiply_by_iteration(a, b):
    result = 0
    for _ in range(a):
        result += b
    return result

# Input from user
a = int(input("Enter 'a' for a*b : "))
b = int(input("Enter 'b' for a*b : "))

# One iteration (direct multiplication)
result_once = multiply_once(a, b)
print("\n1 iteration: ", result_once)

# N iterations (repeated addition)
result_n = multiply_by_iteration(a, b)
print("N iteration: ", result_n)
