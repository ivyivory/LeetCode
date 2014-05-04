'''
Created on May 4, 2014

@author: Ivy

Remove Element
http://oj.leetcode.com/problems/remove-element/
'''


def removeElement(A,elem):
    i=0
    j=len(A)-1
    length = len(A)
    while j>=i: #search from two ends
        if A[i]==elem: 
            if A[j]==elem:
                j=j-1
            else:
                A[i],A[j] = A[j],A[i]
                i=i+1
                j=j-1
            
            length = length -1
            
        else:
            i=i+1
                
    return length

A = [0,4,4,5,4,4,0]
elem = 4
print removeElement(A,elem)