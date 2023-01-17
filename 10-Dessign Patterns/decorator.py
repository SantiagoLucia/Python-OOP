import time

# Sirve para extender la funcionalidad de funciones.

def log_calls(func):
    def wrapper(*args, **kwargs):
        now = time.time()
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        return_value = func(*args, **kwargs)
        print(f"Executed {func.__name__} in {time.time()-now}ms")
        return return_value
    return wrapper

def test1(a, b, c):
    print("\ttest1 called")

@log_calls    
def test2(a, b):
    print("\ttest2 called")
    
test1(1, 2, 3)
test2(1, 2)