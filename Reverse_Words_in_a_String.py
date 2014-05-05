'''
Created on May 4, 2014

@author: Ivy
'''


def reverseString(s):
    #function to reverse string
    
    #change string into list
    s = list(s)
    for i in range(len(s)/2):
        s[i], s[len(s)-1-i]= s[len(s)-1-i],s[i]

    #change list back to string
    s = "".join(s)
    return s

def reverseSentence(s):
    result = ""
    #reverse the whole sentence
    s = reverseString(s)

    #the start and end location of a word, set to -1
    st = -1
    ed = -1
    for i in range(len(s)):
        #if current location is first char and not space, update st
        if i==0 and s[i]!=" ": st = i
        
        #if the next char is the beginning of a word 
        if i!=len(s)-1 and s[i]==" " and s[i+1] != " ": st = i+1
        
        #if the next char is space, then current location is the end of the word
        #due to the Python feature, has to +1 here 
        if i!=len(s)-1 and s[i]!=" " and s[i+1] == " ": ed = i+1
            
        
        #if current location is the last char
        if i==len(s)-1:
            #if last char is not space and it is end of a word
            if s[i]!=" " and st!=-1: 
                ed = i+1
            #if last char is not space and it is a single char word
            if s[i]!=" " and st==-1:
                st = i
                ed = i+1

        #if we find a word
        if st!= -1 and ed != -1:
            stringlist = s[st:ed]
            string = "".join(stringlist)
            word = reverseString(string)
            # add the word into the result and put a space here
            result = result + word+" "
            st = -1
            ed = -1
    
    # delete the last space
    #if result and result[len(result)-1]==" ":
    result = result[:-1]
    return result

#another way:
#return ' '.join(s.strip().split()[::-1])

#print reversehelper("abcde")
s = " the sky   is blue "
s = "1 "
print reverseSentence(s)
#print ' '.join(s.strip().split()[::-1])
