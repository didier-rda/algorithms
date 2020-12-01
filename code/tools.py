import time
def time_it(func):

    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Function "{func.__name__}" took {end - start} seconds to complete.')
    return inner

