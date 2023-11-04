from typing import List

def sort(array: List[int]) -> None:
    """
        Sort array in place using selection sort
        Description:

        Selection sort is a sorting technique in which
        we find the minimum element in every iteration
        and place it in the array beginning from the
        first index. Thus, a selection sort also gets
        divided into a sorted and unsorted subarray.
    """
    for i in range(len(array)):
        # Find the minimum element in remaining unsorted array
        min_idx: int = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        # Swap the minimum element with the first element
        temp: int  = array[min_idx]
        array[min_idx] = array[i]
        array[i] = temp


if __name__ == '__main__':
    arr: List[int] = [25,12,64,22,11]
    print(f'Unsorted array: {arr}')
    sort(arr)
    print(f'Sorted array: {arr}')
