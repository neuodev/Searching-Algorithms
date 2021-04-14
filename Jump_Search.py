
import math

def jumb_search(array, target):
    block_size = math.sqrt(len(array))
    start = 0
    next_idx = int(block_size)
    while array[next_idx -1] < target: 
         start= next_idx
         if(start >= len(array)): break
         next_idx = block_size
         if next_idx > len(array): next_idx = len(array)
    for n in range(start , next_idx):
        if array[n] == target:
            return n 
    return -1 

jumb_search([1,2,3,4] , 4)