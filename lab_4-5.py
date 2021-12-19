from functools import reduce

n = 1 # number in group

a = [12, 34, 45, 66, n]
print("Послідовність A: ", a)

print("Сума елементів послідовності А:   ", reduce(lambda x, y: x+y, a))
print("Добуток елементів послідовності А:", reduce(lambda x, y: x*y, a))