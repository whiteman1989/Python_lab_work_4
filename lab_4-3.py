n = 1 #number in group

lambdas = [lambda x: x+n, lambda x: x ** 3, lambda x: x -1, lambda x: x ** 5]


for l in lambdas:
    x = n+2
    print("X = ", x, ". Результат: f(x) = ", l(x))