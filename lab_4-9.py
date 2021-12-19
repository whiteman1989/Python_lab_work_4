n = 1 #number in group

lambdas = [lambda x: x*n, lambda x: x ** 6, lambda x: x -2, lambda x: x ** 2]


for l in lambdas:
    x = n+3
    print("X = ", x, ". Результат: f(x) = ", l(x))