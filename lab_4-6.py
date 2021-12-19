n = 1 #number in group

def fibonacci(n):
    if(n in (1,2)):
        return 1
    return fibonacci(n - 1) + fibonacci (n - 2)

print("Число фібоначі порядку n=", n+10,": ", fibonacci(n+10), sep='')