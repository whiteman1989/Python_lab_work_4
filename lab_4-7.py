n = 1 # number in group

def fibonacci(n):
    if(n in (1,2)):
        return 1
    return fibonacci(n - 1) + fibonacci (n - 2)

def fib_sum(n):
    return fibonacci(n+2) - 1

print("Сума чисел в послідовності фібоначі до порядку n",n+10," = ", fib_sum(n+10), sep='')