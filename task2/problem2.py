from itertools import combinations

input_numbers = input("Введите числа через пробел: ")
n = int(input("Введите число n: "))

numbers = list(map(int, input_numbers.split()))

pairs = [(a, b) for a, b in combinations(numbers, 2) if a + b == n]

print(pairs)