"""
exercise 11
"""
import time
from math import sqrt
from multiprocessing import Pool, cpu_count


def is_prime(n):
    is_prime_num = True
    if n < 2:
        is_prime_num = False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            is_prime_num = False
    return is_prime_num


def primes_less_than(limit):
    result_list = [n for n in range(2, limit) if is_prime(n)]
    return result_list


def part_a():
    start_time = time.time()
    primes = primes_less_than(1_000_000)
    end_time = time.time()
    print(f"part A: found {len(primes)} primes less than 1 million in {end_time - start_time:.2f} seconds.")
    return end_time - start_time


def part_b():
    start_time = time.time()
    primes = primes_less_than(10_000_000)
    end_time = time.time()
    print(f"part B: found {len(primes)} primes less than 10 million in {end_time - start_time:.2f} seconds.")
    return end_time - start_time


def compare_execution_times():
    time_a = part_a()
    time_b = part_b()
    print(f"Comparison: Part B took {time_b / time_a:.2f} times longer than Part A.")


def chunk_processor(start, end):
    return [n for n in range(start, end) if is_prime(n)]


def parallel_primes(limit):
    """
    writing multiprocessing code as python lacks true parallel process with threading.
    """    
    num_workers = cpu_count()
    step = limit // num_workers
    ranges = [(i * step, (i + 1) * step) for i in range(num_workers)]

    start_time = time.time()
    with Pool(num_workers) as pool:
        results = pool.starmap(chunk_processor, ranges)
    primes = [p for sublist in results for p in sublist]
    end_time = time.time()

    print(f"parallel: {len(primes)} primes less than {limit} in {end_time - start_time:.2f} seconds.")


if __name__ == "__main__":
    # BEWARE: parb_b takes a LONG time.
    compare_execution_times()
    parallel_primes(1_000_000)
    # my results:
    # part A: found 78498 primes less than 1 million in 29.59 seconds.
    # part B: found 664579 primes less than 10 million in 922.71 seconds.
    # Comparison: Part B took 31.18 times longer than Part A.
    # parallel: 78498 primes less than 1000000 in 4.90 seconds.
