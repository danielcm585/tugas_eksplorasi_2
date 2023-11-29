import time
from memory_profiler import memory_usage

def benchmark(func):
    def wrapper(*args, **kwargs):
        # Start time
        start_time = time.time()

        # Start memory usage
        start_memory = memory_usage(-1, interval=0.001, timeout=1)

        # Execute the function
        result = func(*args, **kwargs)

        # End time
        end_time = time.time()

        # End memory usage
        end_memory = memory_usage(-1, interval=0.001, timeout=1)

        # Calculate total time and memory used
        total_time = end_time - start_time
        total_memory = max(end_memory) - min(start_memory)

        print(f"Function {func.__name__} took {total_time:.4f} seconds and used {total_memory:.4f} MiB of memory")

        return result

    return wrapper

# Example usage
@benchmark
def example_function():
    # Some code here
    pass
