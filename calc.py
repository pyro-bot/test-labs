def factorial(num):
    if num<1:
        return 1
    buf=1
    for i in range(1,num+1):
        buf*=i
    return buf

def div(a,b):
    return a/b

def minus(a,b):
    return a-b


if __name__=='__main__':
    print(factorial(5))