# Problem-3: Generate a series of odd numbers based on input 'a'
# Rule:
# - If 'a' is odd → print odd numbers up to 'a'
# - If 'a' is even → print odd numbers up to (a - 1)

a = int(input("Enter a number: "))
limit = a if a % 2 != 0 else a - 1
output = []

for i in range(1, limit * 2, 2):
    output.append(i)

print(*output, sep=", ")
