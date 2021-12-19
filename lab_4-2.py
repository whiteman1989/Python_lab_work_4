n = 1 # number in group

a = [5, 6, 7, 8, 9]
b = [3, 4, 5, 8, n]

print("Масив A:   ", a)
print("Масив B:   ", b)

c = list(map(pow, a, b))

print("Результат: ", c)