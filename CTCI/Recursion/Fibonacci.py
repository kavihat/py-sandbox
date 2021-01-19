# def fibonacci(n):
#     if (n==0 or n==1):
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# print(fibonacci(6))

# Fibonacci using Memoization in recursion
def compute_fibonacci(n):
    memo=[0]*(n+1)
    return fib(n,memo)
def fib(n,memo):
    if n==0 or n==1:
        memo[n]=n
        return n
    else:
        if memo[n]==0:
            memo[n]=(fib(n-1,memo)+fib(n-2,memo))
            print(memo)
        return memo[n]
print(compute_fibonacci(8))

