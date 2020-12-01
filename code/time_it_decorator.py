import time
def time_it(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Function "{func.__name__}" took {end - start} seconds to complete.')
    return inner

@time_it
def find_nemo(array):
    for element in array:
        if element == 'nemo':
            print('Found!')

if __name__ =='__main__':
    find_nemo(['nemo'])
