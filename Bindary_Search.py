def search(array , target):
    array.sort()
    left = 0 
    right = len(array) -1 
    while  left <= right:
        mid = (left + right)//2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid -1 
        else: 
          return True 
    return False


search([1,2,-4,-299] , 6)
