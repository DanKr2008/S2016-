import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функція {func.__name__} виконана за {execution_time:.4f} секунд")
        return result

    return wrapper


@measure_time
def sort_numbers(numbers):
    return sorted(numbers)


@measure_time
def sum_numbers(numbers):
    return sum(numbers)


if __name__ == "__main__":
    numbers = list(range(1, 1000000))

    sorted_numbers = sort_numbers(numbers)
    total_sum = sum_numbers(numbers)