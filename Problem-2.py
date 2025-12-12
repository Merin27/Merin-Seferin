# Problem-2: Generate a series of odd numbers based on input 'a'

a = int(input("Enter a number: "))

output = []
for i in range(1, a * 2, 2):
    output.append(i)


print(*output, sep=", ")
