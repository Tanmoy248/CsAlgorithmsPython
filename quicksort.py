# -*- coding: utf-8 -*-
"""
@author: tanmoyt
@description: uses recursive to attain quicksort
"""
import random
from datetime import datetime

start = str(datetime.now().time()).split(':')
def quicksort(A,first,last):
    print "calling parameters",A,first,last
    if first >= last:
        return
    i , j = first, last
    pivot = A[random.randint(first,last)]
    #pivot = A[last]
    while i <= j:
        while A[i] < pivot:
            i+=1
            #print "i:",i
        while A[j] > pivot:
            j-=1
        #print "i,j",i,j
        if i <= j:
            A[i],A[j] = A[j],A[i]
            i,j = i+1, j-1
        #print "intermediate",A
        #print "loop i,j",i,j
    # Using Recursion here    
    quicksort(A,first,j)
    quicksort(A,i,last)

A = [2,8,7,1,3,5,6,4]
#A = [1,1,1,1,1,1,1,1]
quicksort(A,0,len(A)-1)

print A
stop = str(datetime.now().time()).split(':')
print "time taken",float(stop[2]) - float(start[2])
