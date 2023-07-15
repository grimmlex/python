def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Время выполнения {end-start}')
        return result
    return wrapper



@benchmark
def dtf(url):
    import requests
    webpage = requests.get(url)
    return webpage.text

result = dtf('https://dtf.ru/')
print(result)