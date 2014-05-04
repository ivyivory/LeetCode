'''
Created on May 4, 2014

@author: Ivy

Roman to Integer
http://oj.leetcode.com/problems/roman-to-integer/
'''
def RomanToInt(s):
    roman = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    sub = {'I':1, 'X':10, 'C':100}

    sumint = 0
    for i in range(len(s)):
        if i!= len(s)-1 and s[i] in sub and roman[s[i+1]]>roman[s[i]]:
                sumint=sumint-roman[s[i]]
        else:
            sumint=sumint+roman[s[i]]
                
                
    return sumint

s='MMMCMXCIX'
print RomanToInt(s)