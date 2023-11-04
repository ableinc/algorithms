from typing import List

def sort(array: List[int]) -> None:
    """
        Sort array in place using merge sort
        Description:
        
        Merge Sort is a sorting algorithm that is based on the Divide and
        Conquers paradigm. In this algorithm, the array is initially
        divided into two equal halves and then they are combined in a
        sorted manner.
    """
    if len(array) > 1:
        # Finding the mid of the array
        mid = len(array)//2
        # Dividing the array into 2 halves
        left = array[:mid]
        right = array[mid:]
        # Sort the first half recursively
        sort(left)
        # Sort the second half recursively
        sort(right)
        
        i: int = 0
        j: int = 0
        k: int = 0
        
        # Copy data to temp arrays Left[] and Right[]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        
        # Checking if any element was left
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1



if __name__ == '__main__':
    arr: List[int] = [25,12,64,22,11]
    print(f'Unsorted array: {arr}')
    sort(arr)
    print(f'Sorted array: {arr}')
