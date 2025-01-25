import random
import time
import numpy as np
import matplotlib.pyplot as plt


# Функція для рандомізованого QuickSort
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)


def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)


# Функція для детермінованого QuickSort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def deterministic_quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        deterministic_quick_sort(arr, low, pi - 1)
        deterministic_quick_sort(arr, pi + 1, high)


# Генерація випадкових масивів
array_sizes = [10_000, 50_000, 100_000, 500_000]
random_arrays = {
    size: np.random.randint(1, 1_000_000, size).tolist() for size in array_sizes
}


# Функція для заміру часу
def measure_time(sort_function, arr):
    arr_copy = arr.copy()
    start_time = time.time()
    sort_function(arr_copy, 0, len(arr_copy) - 1)
    end_time = time.time()
    return end_time - start_time


# Збір результатів
results = []

for size, arr in random_arrays.items():
    rand_time = sum(measure_time(randomized_quick_sort, arr) for _ in range(5)) / 5
    det_time = sum(measure_time(deterministic_quick_sort, arr) for _ in range(5)) / 5
    results.append((size, rand_time, det_time))

# Виведення результатів у потрібному форматі
for size, rand_time, det_time in results:
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {det_time:.4f} секунд")
    print()

# Побудова графіку
plt.figure(figsize=(10, 6))
plt.plot(
    [r[0] for r in results],
    [r[1] for r in results],
    label="Рандомізований QuickSort",
    marker="o",
)
plt.plot(
    [r[0] for r in results],
    [r[2] for r in results],
    label="Детермінований QuickSort",
    marker="o",
)

plt.title("Порівняння рандомізованого та детермінованого QuickSort")
plt.xlabel("Розмір масиву")
plt.ylabel("Середній час виконання (секунди)")
plt.legend()
plt.grid()
plt.show()
