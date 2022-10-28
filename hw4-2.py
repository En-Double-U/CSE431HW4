
import time
from matplotlib.pyplot import margins
from numpy import insert, random
# MergeSort in Python
# Source: https://www.programiz.com/dsa/merge-sort

def TimSort(array, k):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        if len(L) < k:
            insertionSort(L)
        else:
            TimSort(L, k)
        
        if len(M) < k:
            insertionSort(M)
        else:
            TimSort(M, k)
        # mergeSort(L)
        # mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1



# Insertion sort in Python
# Source: https://www.programiz.com/dsa/insertion-sort

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key





def main():
    TimArray = random.randint(10000, size=(1000))

    # Flex Point = 1
    print("Flex Point = 1")
    tempArray1 = TimArray.copy()
    start = time.time()
    TimSort(tempArray1, 1)
    end = time.time()
    ttime = end - start
    print(ttime)

    # Flex Point = 10
    print("Flex Point = 10")
    ttime = 0
    for i in range(10000):
        TimArray = random.randint(10000, size=(1000))
        tempArray1 = TimArray.copy()
        start = time.time()
        TimSort(tempArray1, 10)
        end = time.time()
        ttime += end - start
    print(ttime/10000)

    # Flex Point = 25
    print("Flex Point = 25")
    ttime = 0

    for i in range(10000):
        TimArray = random.randint(10000, size=(1000))
        tempArray1 = TimArray.copy()
        start = time.time()
        TimSort(tempArray1, 25)
        end = time.time()
        ttime += end - start
    print(ttime/10000)

    # Flex Point = 30
    print("Flex Point = 30")
    ttime = 0

    for i in range(10000):
        TimArray = random.randint(10000, size=(1000))
        tempArray1 = TimArray.copy()
        start = time.time()
        TimSort(tempArray1, 30)
        end = time.time()
        ttime += end - start
    print(ttime/10000)

    # Flex Point = 32
    print("Flex Point = 32")
    ttime = 0
    
    for i in range(10000):
        TimArray = random.randint(10000, size=(1000))
        tempArray1 = TimArray.copy()
        start = time.time()
        TimSort(tempArray1, 32)
        end = time.time()
        ttime += end - start
    print(ttime/10000)

    # Flex Point = 33
    print("Flex Point = 33")
    ttime = 0

    for i in range(10000):
        TimArray = random.randint(10000, size=(1000))
        tempArray1 = TimArray.copy()
        start = time.time()
        TimSort(tempArray1, 33)
        end = time.time()
        ttime += end - start
    print(ttime/10000)

    # Flex Point = 35
    print("Flex Point = 35")
    ttime = 0

    for i in range(10000):
        TimArray = random.randint(10000, size=(1000))
        tempArray1 = TimArray.copy()
        start = time.time()
        TimSort(tempArray1, 35)
        end = time.time()
        ttime += end - start
    print(ttime/10000)

    # Flex Point = 50
    print("Flex Point = 50")
    ttime = 0

    for i in range(10000):
        TimArray = random.randint(10000, size=(1000))
        tempArray1 = TimArray.copy()
        start = time.time()
        TimSort(tempArray1, 50)
        end = time.time()
        ttime += end - start
    print(ttime/10000)

    # Flex Point = 100
    print("Flex Point = 100")
    ttime = 0

    for i in range(10000):
        TimArray = random.randint(10000, size=(1000))
        tempArray1 = TimArray.copy()
        start = time.time()
        TimSort(tempArray1, 100)
        end = time.time()
        ttime += end - start
    print(ttime/10000)




    
    
if __name__ == '__main__':
    main()