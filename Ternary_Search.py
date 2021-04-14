def search(array, target):
    left = 0 
    right = len(array) -1 
    partition_size = (right - left) // 3
    mid1 = left + partition_size
    mid2 = right - partition_size 

    while True:
        if target > array[mid2]:
