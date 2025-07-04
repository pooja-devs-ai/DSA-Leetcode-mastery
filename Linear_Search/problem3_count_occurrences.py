''' Problem Statement:

-->Given an array of integers and a target value,
-->count how many times the target appears in the array.
-->Return the count. If the target does not exist, return 0.'''

#this problem is approached by the solution that makes use of a variable which is incremeneted whenever the target is found in the array.

def count_occurrences(arr,target):
    count_occurrence=0
    for value in enumerate(arr):
        if value==target:
            count_occurrence+=1          #incremenets by 1 each time whenever the condition becomes True
    return count_occurrence

arr=[2,6,8,4,2,3,0,2,1,2]
target=2
result=count_occurrences(arr,target)

if result!=0:
    print(f"The target element {target} is found {result} times in the array.")    #according to our input this will be output
else:
    print(f"The target element {target} is not found in the array.")
    #if given arr=[2,3,4,7,9,5] and target=1,the output will be else clause