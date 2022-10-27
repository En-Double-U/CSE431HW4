
import time
from matplotlib.pyplot import margins
from numpy import insert, random
# MergeSort in Python
# Source: https://www.programiz.com/dsa/merge-sort

def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

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
    # Size 1
    print("Size 1")
    mArray = random.randint(10000, size=(1))
    iArray = mArray.copy()

    mStart = time.time()
    mergeSort(mArray)
    mEnd = time.time()

    mTime = mEnd - mStart

    iStart = time.time()
    insertionSort(iArray)
    iEnd = time.time()

    iTime = iEnd - iStart

    print("Mergesort Time: ", mTime)
    print("Insertionsort Time: ", iTime)
    

    # Size 10
    print("\nSize 10")
    mTime = 0
    iTime = 0
    for i in range(10000):
        tempMArray = random.randint(10000, size=(10))
        tempIArray = tempMArray.copy()

        tempMStart = time.time()
        mergeSort(tempMArray)
        tempMEnd = time.time()
        mTime += (tempMEnd - tempMStart)

        tempIStart = time.time()
        insertionSort(tempIArray)
        tempIEnd = time.time()
        iTime += (tempIEnd - tempIStart)

    print("Mergesort Time: ", mTime/10000)
    print("Insertionsort Time: ", iTime/10000)

    if mTime > iTime:
        print("Insertion sort is faster")
    else:
        print("Merge sort is faster")

    # Size 25
    print("\nSize 25")
    mTime = 0
    iTime = 0
    for i in range(10000):
        tempMArray = random.randint(10000, size=(25))
        tempIArray = tempMArray.copy()

        tempMStart = time.time()
        mergeSort(tempMArray)
        tempMEnd = time.time()
        mTime += (tempMEnd - tempMStart)

        tempIStart = time.time()
        insertionSort(tempIArray)
        tempIEnd = time.time()
        iTime += (tempIEnd - tempIStart)

    print("Mergesort Time: ", mTime/10000)
    print("Insertionsort Time: ", iTime/10000)

    if mTime > iTime:
        print("Insertion sort is faster")
    else:
        print("Merge sort is faster")

    # Size 30
    print("\nSize 30")
    mTime = 0
    iTime = 0
    for i in range(10000):
        tempMArray = random.randint(10000, size=(30))
        tempIArray = tempMArray.copy()

        tempMStart = time.time()
        mergeSort(tempMArray)
        tempMEnd = time.time()
        mTime += (tempMEnd - tempMStart)

        tempIStart = time.time()
        insertionSort(tempIArray)
        tempIEnd = time.time()
        iTime += (tempIEnd - tempIStart)

    print("Mergesort Time: ", mTime/10000)
    print("Insertionsort Time: ", iTime/10000)

    if mTime > iTime:
        print("Insertion sort is faster")
    else:
        print("Merge sort is faster")


    # Size 32
    print("\nSize 32")
    mTime = 0
    iTime = 0
    for i in range(10000):
        tempMArray = random.randint(10000, size=(32))
        tempIArray = tempMArray.copy()

        tempMStart = time.time()
        mergeSort(tempMArray)
        tempMEnd = time.time()
        mTime += (tempMEnd - tempMStart)

        tempIStart = time.time()
        insertionSort(tempIArray)
        tempIEnd = time.time()
        iTime += (tempIEnd - tempIStart)

    print("Mergesort Time: ", mTime/10000)
    print("Insertionsort Time: ", iTime/10000)

    if mTime > iTime:
        print("Insertion sort is faster")
    else:
        print("Merge sort is faster")

    # Size 33
    print("\nSize 33")
    mTime = 0
    iTime = 0
    for i in range(10000):
        tempMArray = random.randint(10000, size=(33))
        tempIArray = tempMArray.copy()

        tempMStart = time.time()
        mergeSort(tempMArray)
        tempMEnd = time.time()
        mTime += (tempMEnd - tempMStart)

        tempIStart = time.time()
        insertionSort(tempIArray)
        tempIEnd = time.time()
        iTime += (tempIEnd - tempIStart)

    print("Mergesort Time: ", mTime/10000)
    print("Insertionsort Time: ", iTime/10000)

    if mTime > iTime:
        print("Insertion sort is faster")
    else:
        print("Merge sort is faster")


    # Size 35
    print("\nSize 35")
    mTime = 0
    iTime = 0
    for i in range(10000):
        tempMArray = random.randint(10000, size=(35))
        tempIArray = tempMArray.copy()

        tempMStart = time.time()
        mergeSort(tempMArray)
        tempMEnd = time.time()
        mTime += (tempMEnd - tempMStart)

        tempIStart = time.time()
        insertionSort(tempIArray)
        tempIEnd = time.time()
        iTime += (tempIEnd - tempIStart)

    print("Mergesort Time: ", mTime/10000)
    print("Insertionsort Time: ", iTime/10000)

    if mTime > iTime:
        print("Insertion sort is faster")
    else:
        print("Merge sort is faster")


    # Size 50
    print("\nSize 50")
    mTime = 0
    iTime = 0
    for i in range(10000):
        tempMArray = random.randint(10000, size=(50))
        tempIArray = tempMArray.copy()

        tempMStart = time.time()
        mergeSort(tempMArray)
        tempMEnd = time.time()
        mTime += (tempMEnd - tempMStart)

        tempIStart = time.time()
        insertionSort(tempIArray)
        tempIEnd = time.time()
        iTime += (tempIEnd - tempIStart)

    print("Mergesort Time: ", mTime/10000)
    print("Insertionsort Time: ", iTime/10000)

    if mTime > iTime:
        print("Insertion sort is faster")
    else:
        print("Merge sort is faster")


    # Size 100
    print("\nSize 100")
    mTime = 0
    iTime = 0
    for i in range(10000):
        tempMArray = random.randint(10000, size=(100))
        tempIArray = tempMArray.copy()

        tempMStart = time.time()
        mergeSort(tempMArray)
        tempMEnd = time.time()
        mTime += (tempMEnd - tempMStart)

        tempIStart = time.time()
        insertionSort(tempIArray)
        tempIEnd = time.time()
        iTime += (tempIEnd - tempIStart)


    print("Mergesort Time: ", mTime/10000)
    print("Insertionsort Time: ", iTime/10000)

    if mTime > iTime:
        print("Insertion sort is faster")
    else:
        print("Merge sort is faster")


    
if __name__ == '__main__':
    main()