'''
Created on May 4, 2014

@author: Ivy

Implement pow(x, n).
'''

def power(x,n):
    #trivial one
    result = 1
    
    for i in range(n):
        result = result*x
            
    if n < 0:
        result = 1 / result
        
    return result

def power2(x, n):
    # recursion, too slow
    if n==0: return 1
    return power2(x,n-1)*x


def power3(x,n):
    #recursion plus divide and conquer
    if x == 0: return
    if n == 0: return 1
    if n == 1: return x
    if n == -1: return 1.0/x
    
    result = 1
    
    if n%2==0:
        result = power3(x, n/2) * power3(x, n/2)
    else:
        result = power3(x, n/2) * power3(x, n/2) * x
        
             
    
    return result
    
        

print power3(2,-2)