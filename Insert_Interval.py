'''
Created on May 4, 2014

@author: Ivy
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
'''def overlap(interval,number):
    if interval.start <= number and interval.end >= number:
        return True
    else:
        return False'''

def insert(intervals, newInterval):
    result = []
    for item in intervals:
        if item.end < newInterval.start:
            #if newinterval < interval
            result.append(item)
        
        elif item.start > newInterval.end:
            # if interval > new interval
            # new interval already passed, add newinterval to result, update newinterval
            result.append(newInterval)
            newInterval = item
            
        else:
            #update newinterval
            newInterval.start = min(item.start,newInterval.start)
            newInterval.end = max(item.end,newInterval.end)
               
    result.append(newInterval)
    return result

intervals=[Interval(1,2),Interval(3,5),Interval(6,7),Interval(8,10)]#,Interval(12,16)]
newInterval = Interval(4,9)
#intervals = [Interval(1,3),Interval(6,9)]
#newInterval = Interval(2,5)

result = insert(intervals,newInterval)
for item in result:
    print item.start
    print item.end
        
        
        