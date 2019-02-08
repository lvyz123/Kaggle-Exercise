def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    round_num = round(num,2)
    return round_num

q1.check()

round(23.14159,-1)

def to_smash(total_candies, num_friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % num_friends

q3.check()

round_to_two_places(9.9999)

x = -10
y = 5
# Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x), abs(y))

def f(x):
    y = abs(x)
    return y

print(f(5))

# Importing the function 'time' from the module of the same name. 
# (We'll discuss imports in more depth later)
from time import time
t = time()
print(t, "seconds since the Epoch")

from time import sleep
duration = 5
print("Getting sleepy. See you in", duration, "seconds")
sleep(duration)
print("I'm back. What did I miss?")

def time_call(fn, arg):
    """Return the amount of time the given function takes (in seconds) when called with the given argument.
    """
    start_time=time()
    fn(arg)
    end_time=time()
    call_time=end_time-start_time
    return call_time

def slowest_call(fn, arg1, arg2, arg3):
    """Return the amount of time taken by the slowest of the following function
    calls: fn(arg1), fn(arg2), fn(arg3)
    """
    t1=time_call(fn,arg1)
    t2=time_call(fn,arg2)
    t3=time_call(fn,arg3)
    t_max=max(t1,t2,t3)
    return t_max
