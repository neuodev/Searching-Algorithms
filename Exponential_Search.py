
from Binary_search_Recursive import searchHelper

def search(array , target):
    bound = 1 
    while bound < len(array) and array[bound] < target:
        bound *= 2 
        left = bound // 2
        right = min(bound, len(array)) 
        return searchHelper(array, target, left , right)