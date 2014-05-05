'''
Created on May 4, 2014

@author: Ivy

Do not allocate extra space for another array, 
you must do this in place with constant memory.
allow repeat once (appears twice)
'''

def removeDuplicates(A):
    # using two pointer
    if len(A) <= 2: return len(A)
    cur = 2
    next = 2

    while next <= len(A)-1:
        if A[next] != A[cur-2]:
            A[cur] = A[next]
            cur += 1
        
        next +=1
    
    return cur,A

A = [1,1,2]
A = [1,1,1,2,3]
A = [1,1,2,2,3,4,4,5]
A = [1,1,1,1,3,3]
A = [1,2,2,2]
print removeDuplicates(A)

            
        
    