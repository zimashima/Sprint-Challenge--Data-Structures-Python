import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    smaller = []
    larger = []
    for i in range(1, len(arr)):
        if arr[i] <= pivot:
            smaller.append(arr[i])
        else:
            larger.append(arr[i])
    return quicksort(smaller) + [pivot] + quicksort(larger)

names_2 = quicksort(names_2)



def binary_search(arr, target):
    
  low = 0
  high = len(arr)-1

  while low < high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return target
    elif target < arr[mid]:
      high = mid
    else:
      low = mid+1

for name in names_1:
    if name == binary_search(names_2, name):
        duplicates.append(name)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
