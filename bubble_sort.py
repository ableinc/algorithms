from typing import List

def sort(array: List[int]) -> None:
    """
        Sort array in place using bubble sort
    """
    n: int = len(array)
     
    # Traverse through all array elements
    for i in range(n):
        swapped: bool = False
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j+1]:
                temp: int = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swapped = True
        if swapped == False:
            break


if __name__ == '__main__':
    arr: List[int] = [25,12,64,22,11]
    print(f'Unsorted array: {arr}')
    sort(arr)
    print(f'Sorted array: {arr}')
