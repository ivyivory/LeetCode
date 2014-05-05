'''
Created on May 4, 2014

@author: Ivy

http://leetcode.com/2010/04/searching-element-in-rotated-array.html
'''
    
def search(A,target):
    left = 0
    right = len(A)-1
    
    while left <= right:
        mid = left + (right - left)/2
        if A[mid]==target: return mid
        
        #if left half is sorted
        if A[left] <= A[mid]:
            if A[left] <= target and target < A[mid]:
                right = mid-1
            else:
                left = mid+1
        
        #if right half is sorted
        else:
            if A[mid] < target and target <= A[right]:
                left = mid+1
            else:
                right = mid-1
    
    return -1

    
A=[4,5, 6, 7, 0, 1, 2]
A = [3,1]
target = 1
print search(A,target)