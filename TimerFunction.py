import time
def my_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + " mil sec")
        return result
    return wrapper

@my_timer
def func1():
   time.sleep(1); # delay of 1 second
   print('func1 is executing!')

@my_timer
def func2():
    time.sleep(2); # delay of 2 seconds
    print('func2 is executing!')

def test_timer () :
   print("Output: my_time()")
   func1()
   func2()
