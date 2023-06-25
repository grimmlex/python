import time
def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time()-t))
        return res

    return tmp

def pause(f):
    def tmp(*args, **kwargs):
        time.sleep(1)
        return f(*args, **kwargs)

    return tmp

@timer


def func(x, y):
    return x + y * x -x**y

print(func(103, 1231))
print(func(10, 1231))
print(func(103, 121))
print(func(10, 31))