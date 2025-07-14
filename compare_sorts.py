import time
import tracemalloc
import random
from merge_sort import merge_sort
from quick_sort import quick_sort

def measure_performance(func, data):
    tracemalloc.start()
    start_time = time.perf_counter()
    func(data[:])  # Copy to avoid side effects
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return round((end_time - start_time) * 1000, 3), round(peak / 1024, 3)  # ms, KB

def test_and_compare():
    size = 1000
    datasets = {
        "Sorted": list(range(size)),
        "Reverse Sorted": list(range(size, 0, -1)),
        "Random": random.sample(range(size * 2), size)
    }

    algorithms = {
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    for label, data in datasets.items():
        print(f"\nDataset: {label}")
        for name, func in algorithms.items():
            time_ms, mem_kb = measure_performance(func, data)
            print(f"{name:<12} | Time: {time_ms} ms | Memory: {mem_kb} KB")

if __name__ == "__main__":
    test_and_compare()
