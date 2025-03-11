def binary_search(arr, left, right, target):
    if left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, left, mid - 1, target)
        else:
            return binary_search(arr, mid + 1, right, target)
    else:
        return -1

arr = list(map(int, input("Enter sorted elements of the array: ").split()))
target = int(input("Enter the target value: "))
result = binary_search(arr, 0, len(arr) - 1, target)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found in the array.")
