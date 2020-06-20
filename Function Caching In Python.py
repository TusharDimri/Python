# Do check the Function Caching tutorial again for better understanding (codewithharry python for beginners video 75 youtube)

import time
from functools import lru_cache  # functools is a built in python module

@lru_cache(maxsize = 3) # this saves 3 previous function calls as cache for function to stop its delay
def work(n):
    time.sleep(n) # assume that this function is taking n seconds to get results
    return n

if __name__ == '__main__':
    work(2)
    print("Done,calling function again")
    work(2)
    print("Done,calling function again")
    work(2)
    print("Done,see how fast we did the task after delay during the first time using it")
    print("Task 2 starting now")
    work(4)
    print("Done")
    work(4)
    print("Done")
    work(4)
    print("Done,see how fast we did the task after delay during the first time using it")