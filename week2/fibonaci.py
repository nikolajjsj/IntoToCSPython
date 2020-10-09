def fibo(x):
    """
    Input: x is int larger than or equal to 0
    Output: fibonaci of x
    """
    if x == 0 or x == 1:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)
