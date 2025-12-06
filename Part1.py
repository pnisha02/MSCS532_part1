import numpy as np
import time

# Naive Matrix Multiplication

def matmul_naive(A, B):
    n = A.shape[0]
    C = np.zeros((n, n), dtype=np.float64)
    for i in range(n):
        for j in range(n):
            s = 0.0
            for k in range(n):
                s += A[i, k] * B[k, j]
            C[i, j] = s
    return C

# Optimized Matrix Multiplication (Tiled)

def matmul_tiled(A, B, block_size):
    n = A.shape[0]
    C = np.zeros((n, n), dtype=np.float64)

    for ii in range(0, n, block_size):
        for jj in range(0, n, block_size):
            for kk in range(0, n, block_size):

                i_max = min(ii + block_size, n)
                j_max = min(jj + block_size, n)
                k_max = min(kk + block_size, n)

                for i in range(ii, i_max):
                    for k in range(kk, k_max):
                        a_val = A[i, k]
                        for j in range(jj, j_max):
                            C[i, j] += a_val * B[k, j]

    return C

# Benchmarking Function

def benchmark(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return end - start, result

# Main Program

if __name__ == "__main__":
    n = 200
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    print("Running matrix multiplication benchmarks...\n")

    # Naive method
    t_naive, _ = benchmark(matmul_naive, A, B)
    print(f"Naive version:  {t_naive:.6f} seconds")

    # Tiled method (fixed)
    t_tiled, _ = benchmark(matmul_tiled, A, B, 32)
    print(f"Tiled version:  {t_tiled:.6f} seconds")

    print(f"\nSpeedup: {t_naive / t_tiled:.2f}x faster")
