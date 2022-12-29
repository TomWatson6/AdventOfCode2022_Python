
def move(numbers, index, amount):
    i = int(index)
    wrap = lambda t: (t + (1 if amount > 0 else -1)) % len(numbers)

    while i != (index + amount) % len(numbers):
        n = wrap(i)
#        if n == 0 and i == len(numbers) - 1: # Cycled to start, everything needs pushing back one
#            temp = tuple(numbers[i])
#            for x in range(len(numbers) - 1, 0, -1):
#                numbers[x] = tuple(numbers[x - 1])
#            numbers[n] = temp
#        elif n == len(numbers) - 1 and i == 0: # Cycled to end, everything needs forward one
#            temp = tuple(numbers[i])
#            for x in range(len(numbers) - 1):
#                numbers[x] = tuple(numbers[x + 1])
#            numbers[n] = temp
#        else:
        numbers[i], numbers[n] = numbers[n], numbers[i]
#        print(" ->", ", ".join([str(x[1]) for x in numbers]))
        i = wrap(i)

with open("input.txt") as f:
    numbers = [int(x.strip()) for x in f.readlines()]
    numbers = list(enumerate(numbers))

M = len(numbers)
print(numbers)

for i in range(M):
    n = [(index, x) for index, x in enumerate(numbers) if x[0] == i][0]
    amt = (n[1][1] % M) + (n[1][1] // M)
    while amt > len(numbers):
        amt = (amt % M) + (amt // M)
    move(numbers, n[0], amt)
#    print(", ".join([str(x[1]) for x in numbers]))

start_index = [i for i, x in enumerate(numbers) if x[1] == 0][0]
print("0 index at:", start_index)

total = 0

for i in range(start_index + 1000, start_index + 3001, 1000):
    index = i % M
    print(f"Index of Number is {index}, which is {numbers[index][1]}")
    total += numbers[index][1]

print(total)









