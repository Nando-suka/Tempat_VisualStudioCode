def printLargest (arr):
    arr_size = len(arr)

    if arr_size < 3:
        print("Invalid Input")
        return
    
    third = first = second = float('-inf')

    for i in range (arr_size):
        if arr [i] > first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] > second and arr [i] != first:
            third = second
            second = arr[i]
        elif arr[i] > third and arr[i] != second and arr[i] != first:
            third = arr[i]

    print("Three large elements are ", first, second, third)

# Inisial
arr = [12,13,1,10,34,11,34]
printLargest(arr)

# Linear Search Python
def search (arr, N, x):
    for i in range(0,N):
        if (arr[i] == x):
            return i
    return -1

if __name__ == "__main__":
    arr = [2,3,4,10,40]
    x = 11
    N = len(arr)

    # memanggil fungsi
    result = search(arr, N, x)
    if (result == -1):
        print("Element is not present in array")
    else:
        print("Element is present in array", result)

# peak element search
array1 = [10,20,30]
n = 3
x = len (array1)

def peak (array1,n,x):
    for i in range(0,x):
        if array1[i] < array1[i + 1]:



peak(array1,n,x)