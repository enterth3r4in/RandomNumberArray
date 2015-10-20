import random

random_numbers = []

for i in range(20):
    random_numbers.append(random.randint(1, 100))

print(random_numbers)

for x in range(len(random_numbers)):
    print(random_numbers[x])