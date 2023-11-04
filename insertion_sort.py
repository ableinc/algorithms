from typing import List

def sort(array: List[int]) -> None:
    """
        Sort array in place using insertion sort
        Description:
        
        Insertion sort is a simple sorting algorithm that works similarly 
        to the way you sort playing cards in your hands. The array is
        virtually split into a sorted and an unsorted part. Values from
        the unsorted part are picked and placed at the correct position in
        the sorted part.
    """
    # Traverse through 1 to length of array
    for i in range(1, len(array)):
        
        key: int = array[i]
        
        # Move elements from array[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j: int = i-1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


if __name__ == '__main__':
    arr: List[int] = [25,12,64,22,11]
    print(f'Unsorted array: {arr}')
    sort(arr)
    print(f'Sorted array: {arr}')
