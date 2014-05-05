'''
Created on May 4, 2014

@author: Ivy

Do not allocate extra space for another array, 
you must do this in place with constant memory.
'''

def removeDuplicates(A):
    # using two pointer
    if len(A) < 2: return len(A)
    cur = 0
    next = 1
    
    while next <= len(A)-1:
        if A[cur] == A[next]:
            next += 1
        else:
            A[cur+1] = A[next]
            cur +=1
            next +=1
    
    return cur+1

def remove(A):
    if len(A) < 2: return len(A)
    cur = 1
    next = 1
    
    while next < len(A):
        if A[next] != A[cur-1]:
            A[cur]=A[next]
            cur+=1
        
        next+=1
    
    return cur

A = [1,1,2]
A = [1,1,1,2,3]
A = [1,1,2,2,3,4,4,5]
#print removeDuplicates(A)
print remove(A)

            
        
    