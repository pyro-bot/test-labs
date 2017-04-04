def factorial(num):
    if num<1:
        return 1
    buf=1
    for i in range(1,num+1):
        buf*=i
    return buf

if __name__=='__main__':
    print(factorial(100))