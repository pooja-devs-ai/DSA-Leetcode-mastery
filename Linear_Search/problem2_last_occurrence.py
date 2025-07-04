# Restored cleanly after cache issue

''' 
Problem 2: Last Occurrence of a Target Element

Given an array of integers and a target value. 
Return the index of the last occurrence of the target in the array. 
If the target does not exist, return -1.
'''
#This problem can also be solved using a list .
# A list that contains all the indices of the target present in the array.
# Then returns the last element's index which is the last occurrence of the target.

def last_occurrence_index(arr,target):
    last_index=-1                       #a variable is used to update the index value in the loop,if target is not found it returns -1
    for i,value in enumerate(arr):
        if value==target:
            last_index=i                   #index will be updated everytime the target is encountered
    return last_index                      # The index at which the target has lastly occurred will be returned by the function

arr=[5,16,20,1,3,16,4]
target=16
result=last_occurrence_index(arr,target)

if result!=-1:                            
    print(f"the last occurrence of the element {target} is at {result} index.")
else:
    print(f"The element {target} is not found in the array.")