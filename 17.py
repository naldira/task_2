"""
exercise 17
"""
from functools import reduce
from multiprocessing import Pool, cpu_count


def multi(x, y):
    return x * y


def partial_factorial(start, end):
    return reduce(multi, range(start, end + 1))


def factorial_map_parallel(n):
    num_workers = cpu_count()
    chunk_size = n // num_workers
    ranges = [(i * chunk_size + 1, (i + 1) * chunk_size) for i in range(num_workers)]
    ranges[-1] = (ranges[-1][0], n)

    with Pool(num_workers) as pool:
        partial_results = pool.starmap(partial_factorial, ranges)

    return reduce(multi, partial_results)


if __name__ == "__main__":
    import time
    n = 10_000_000
    start_time = time.time()
    result = factorial_map_parallel(n)
    end_time = time.time()
    print(f"{n}! calculated using multiprocessing in {end_time - start_time:.2f} seconds.")
