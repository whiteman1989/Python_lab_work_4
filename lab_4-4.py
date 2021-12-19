n = 1 # number in grpup

a = [ i for i in range(-15, 16)]
print("Послідовність А:              ", a)

b = list(filter(lambda x: x < n, a))
print("Відфільтрована послідовність: ", b)