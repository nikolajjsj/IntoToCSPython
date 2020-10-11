def efficient_fib(n, d):
    if n in d:
        return d[n]
    else:
        ans = efficient_fib(n-1, d) + efficient_fib(n-2, d)
        d[n] = ans
        return ans

d = {1: 1, 2:2}