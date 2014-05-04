'''
Created on May 4, 2014

@author: Ivy
Pascal's Triangle
http://oj.leetcode.com/problems/pascals-triangle/
'''


def generate(numRows):
    if numRows<0: return "Error"
    result=[[1]]*numRows
    templist=[1,1]
    for i in range(1,numRows+1):
        newlist = [1]*i
        if i>=3:
            for j in range(2,i):
                newlist[j-1] = templist[j-1]+templist[j-2]
            
        result[i-1] = newlist
        templist = newlist
        
    return result

print generate(0)
print generate(5)
