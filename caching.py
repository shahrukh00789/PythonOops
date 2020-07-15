import time
from functools import lru_cache
@lru_cache(3)
def some_work(n):
    print(f"some task taking {n}  seconds")
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Now running some work")
    print(some_work(3))
    print("done")
    print(some_work(3))
    print("done")
    print(some_work(5))
    print("Done")
    print(some_work(5))
    print("Done")
