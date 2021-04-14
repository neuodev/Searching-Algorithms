def search(array, target):
    for i in range(len(array)):
        if target == array[i]: return i 
    return False

print(search([1,2,3,4] , 4)) 
print(search([1,2,3,4] , -1)) 
print(search([] , -1)) 