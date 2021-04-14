def search(array, num):
    for i in range(len(array)):
        if num == array[i]: return i 
    return False

print(search([1,2,3,4] , 4)) 
print(search([1,2,3,4] , -1)) 
print(search([] , -1)) 