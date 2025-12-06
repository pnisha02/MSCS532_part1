import numpy as np
import time
import random

def time_func(func, *args):
    """Measure execution time of a function."""
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return end - start, result

# --- 1D Access Functions ---
def sequential_sum_1d(arr):
    s = 0
    for i in range(arr.shape[0]):
        s += arr[i]
    return s

def random_sum_1d(arr, idx):
    s = 0
    for i in idx:
        s += arr[i]
    return s

# --- 2D Access Functions ---
def row_major_sum_2d(a):
    s = 0
    rows, cols = a.shape
    for i in range(rows):
        for j in range(cols):
            s += a[i, j]
    return s

def col_major_sum_2d(a):
    s = 0
    rows, cols = a.shape
    for j in range(cols):
        for i in range(rows):
            s += a[i, j]
    return s

# --- List-of-Lists Function ---
def list_of_lists_row_sum(a):
    s = 0
    for row in a:
        for val in row:
            s += val
    return s

# --- Benchmark Runner ---
def run_benchmarks():
    results = []

    # --- 1D Benchmark ---
    N = 2_000_000
    arr = np.arange(N, dtype=np.int64)

    t_seq, _ = time_func(sequential_sum_1d, arr)
    idx = list(range(N))
    random.shuffle(idx)
    t_rand, _ = time_func(random_sum_1d, arr, idx)

    results.append(("1D sequential", N, t_seq))
    results.append(("1D random", N, t_rand))

    # --- 2D Benchmark ---
    rows, cols = 2000, 1000
    a_row = np.arange(rows * cols).reshape(rows, cols)

    t_row, _ = time_func(row_major_sum_2d, a_row)
    t_col, _ = time_func(col_major_sum_2d, a_row)

    results.append(("2D row-major", rows*cols, t_row))
    results.append(("2D col-major", rows*cols, t_col))

    # --- List-of-Lists Benchmark ---
    ll = [list(range(i*cols, (i+1)*cols)) for i in range(rows)]
    t_ll, _ = time_func(list_of_lists_row_sum, ll)

    results.append(("List-of-lists", rows*cols, t_ll))

    return results

# --- Write Results to File ---
def save_results(results, filename="results.txt"):
    with open(filename, "w") as f:
        f.write("Data Locality Benchmark Results\n")
        f.write("="*40 + "\n")
        for name, size, t in results:
            line = f"{name}: elements={size:,}, time={t:.6f} seconds\n"
            print(line.strip())
            f.write(line)

if __name__ == "__main__":
    benchmark_results = run_benchmarks()
    save_results(benchmark_results)
