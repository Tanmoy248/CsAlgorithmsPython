# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 21:29:02 2019

@author: Tanmoy
"""

# Implementation of insertion sort

arrayOfNumbers = list("432561")
print ("Print the length of input array" , len(arrayOfNumbers))

def insertionSort(arrayOfNumbers, keyIndex):
    if (keyIndex > 0):
        sortedList = arrayOfNumbers[0:keyIndex]
        key = arrayOfNumbers[keyIndex]
        print ("sorted list" , sortedList)
        print key
        
        #now compare key with all elements in sortedList
        counter = 0
        while(counter < len(arrayOfNumbers[0:keyIndex])):
            if (key < arrayOfNumbers[counter]):
                temp = arrayOfNumbers[counter]
                arrayOfNumbers[counter] = key
                key = temp
            counter = counter + 1
        #print keyIndex
        arrayOfNumbers[keyIndex] = key
        print arrayOfNumbers
                
if __name__ == '__main__':
    keyIndex = 0
    # Best case, only the array is iterated once. So it is O(n).
    # Worst case, the element will compared with all elements in the sorted part of array
    # This would mean , that the worst case complexity is O(n^2)
    while (keyIndex < len(arrayOfNumbers)):
        insertionSort(arrayOfNumbers, keyIndex)
        keyIndex += 1
    
    
    