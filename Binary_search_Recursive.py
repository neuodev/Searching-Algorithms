def search(array, target):
    return searchHelper(array, target, 0 , len(array) -1 )

def searchHelper(array, target ,left , right):
    if(left > right): return False
    mid = (left + right)//2 
    if array[mid] < target:
        return searchHelper(array,target,mid+1 ,right)
    elif array[mid] > target:
        return searchHelper(array, target, left , mid-1)
    else: return True


print(search([1,2,3,4,4,5,6,7] , 1))