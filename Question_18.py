"""
18. Implement a decorator function called ‘timer’ that measures the execution time of a function. The ‘timer’ decorator should print the time taken by the decorated function to execute. Use the ‘time’ module in Python to calculate the execution time.

Example:

import time

@timer
def my_function():
    # Function code goes here
    time.sleep(2)

my_function()

"""
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")
        return result
    return wrapper

@timer
def my_function():
    # Function code goes here
    time.sleep(2)

my_function()
