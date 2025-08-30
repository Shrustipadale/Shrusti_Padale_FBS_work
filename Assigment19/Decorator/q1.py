def memoize(func):
    cache={}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result=func(*args)
        cache[args]=result
        return result
    return wrapper
 
def fibonacci(n):
    if(n<=1):
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))     