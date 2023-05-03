#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambdas function
print((lambda x:x**2+5*x+4) (-4))

#lambdas in named function
def polynomial_1(f,x):
    return f(x)

print(polynomial_1((lambda x:x**2 + 5*x + 4),-4))

nums = [1,2,3]
print(list(map(lambda x:x+1,nums)))

#filter
print(list(filter(lambda x:x%2==0,nums)))

