from math import ceil
import time

my_list = [x for x in range(2000000)]

def binary_search(array, item):
    if len(array) == 0:
        return "No items in the list"

    half = ceil(len(array) / 2) - 1

    if array[half] == item:
        return f"Found item: {item}"
    elif item > array[half]:
        new_list = array[half + 1:]
        return binary_search(new_list, item)
    elif item < array[half]:
        new_list = array[:half]
        return binary_search(new_list, item)

start = time.time()
x = binary_search(my_list, 2)
end = time.time()
print(f"Searched: {x}, found in: {end - start}")