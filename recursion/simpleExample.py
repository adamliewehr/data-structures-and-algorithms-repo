

def foo(num):
    if (num == 1):
        return 1
    
    return num + foo(num-1)

print(foo(5))