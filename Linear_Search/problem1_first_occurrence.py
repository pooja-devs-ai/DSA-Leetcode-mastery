# Restored cleanly after cache issue


''' Problem 1: First Occurrence of a Target Element

Given an array of integers and a target value. 
Return the index of the first occurrence of the target in the array. If it does not exist, return -1.'''

#this code is effecient when the list contains duplicates of the target

def first_occurrence_index(arr,target):
    for i,value in enumerate(arr):                #using enumaerate in place of range is more readable and efficient
        if value==target:                         #checks whether the element is equals to the target
            return i                              #breaks the loop and returns the element's index once it encounters the target in the first occurrence
    return -1                                    #returns -1 if the target is not present in the array

arr=[2,3,4,3,5,6,7]
target=3
result=first_occurrence_index(arr,target)

if result!=-1:                                     #if target is present
    print(f'The first occurrence of the target {target} is at {result} index.')

else:
    print(f"Target {target} is not found in the array.")