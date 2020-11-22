"""
1450. Number of Students Doing Homework at a Given Time
Given two integer arrays startTime and endTime and given an integer queryTime.
The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

"""


class Solution:
    def busyStudent(self, startTime, endTime, queryTime: int) -> int:
        count=0
        for i in range(len(endTime)):
            if endTime[i]-queryTime>=0:
                if startTime[i]<=queryTime:
                    count=count+1
                else:
                    i=i+1
            else:
                i=i+1
        return count

s=Solution()
output=s.busyStudent([9,8,7,6,5,4,3,2,1],[10,10,10,10,10,10,10,10,10],5)
print(output)

