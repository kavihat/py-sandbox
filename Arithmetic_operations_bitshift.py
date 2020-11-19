# # Multiplication without using *
def multiply(num1,num2):
    result=0
    for i in range(num2):
        result+=num1;
    return result


m=8
n=1
output=multiply(m,n)
print(output)

# Multiplication using bit shifting

def multiply(m,n):
    result=0
    count=0
    while m:
        if m % 2==1:
            result+=n<<count


        count+=1
        m=int(m/2)
    return result
m=12
n=12
print(multiply(m,n))



#division
def divide(dividend, divisor):

    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    while (dividend >= divisor):
        dividend -= divisor
        quotient += 1

    return sign * quotient

a = 10
b = -3
print(divide(a, b))





#Addition using Bitshift operators

def add(a,b):
    while b:
        carry=a&b
        a=a^b
        b=carry<<1
    return a

a=2
b=5
print(add(a,b))

#

def subtract(a,b):
    if b>a:
        a,b=b,a
    while b:
        borrow=(~a)&b
        a=a^b
        b=borrow<<1
    return a

a=122
b=544444
print(subtract(a,b))






