# MSCS532_part1
# Data Locality Optimization in High-Performance Computing

This repository demonstrates the impact of **data locality** on memory performance in high-performance computing (HPC). The project benchmarks different memory access patterns to show how contiguous and sequential memory access significantly improves performance.

---

## Project Overview

Data locality refers to accessing memory that is **close together in space or recently used in time**. Optimizing data locality improves cache utilization, reduces memory latency, and increases computational performance.

This project benchmarks:

- **1D Arrays:** Sequential vs random access  
- **2D Arrays:** Row-major vs column-major traversal  
- **Nested Data Structures:** Python list-of-lists vs NumPy arrays  

Results show that **contiguous and sequential access is much faster** than random or scattered access.

---

## Files in This Repository

| File | Description |
|------|-------------|
| `Part1.py` | Python script |
| `DataLocality.py` | Main Python script containing the benchmark code |
| `Part-1_mscs532.docx` | Full report with background, benchmarks, and discussion |

---

## Requirements

- Python 3.8 or higher  
- NumPy library  

Install NumPy using pip:

```bash
pip install numpy
```

# Running the Benchmark

## Clone the repository:

git clone <your-repo-url>
cd <repo-folder>

## Run the benchmark script:

python DataLocality.py


## Results will be printed in the console and saved to results.txt:

- 1D sequential: elements=2,000,000, time=0.25 seconds
- 1D random:     elements=2,000,000, time=1.84 seconds
- 2D row-major:  2,000,000 elements, time=0.40 seconds
- 2D col-major:  2,000,000 elements, time=2.31 seconds
- List-of-lists: 2,000,000 elements, time=3.21 seconds

## Key Observations

Sequential access is 7–9× faster than random access.

Row-major traversal is 5–6× faster than column-major in 2D arrays.

NumPy arrays outperform Python list-of-lists due to contiguous memory storage.

## Purpose

This project supports the MSCS 532 assignment on optimization techniques in HPC. It demonstrates how memory layout and access patterns affect performance, confirming empirical findings in HPC research.

## Future Work

Implement benchmarks in C/C++ to observe more dramatic performance differences.

Extend to GPU-based arrays using CUDA or CuPy for parallel HPC benchmarks.

Explore additional optimization techniques such as loop tiling and prefetching.

## Author

Nisha – MSCS 532 Student
