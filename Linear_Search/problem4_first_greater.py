''' Problem Statement:

-->Given an array of integers and a target value,
-->find and return the first element in the array that is strictly greater than the target.
-->If no such element exists, return -1.'''

#this problem is approached by using a for loop and a comparison operator(>) to check the condition

def greater_than_target(arr,target):
    for value in arr:              #enumaerate() can also be used
        if value>target:
            return value
        
    return -1

array=[4,3,89,76,23,39,85]
target=76
result=greater_than_target(array,target)

if result!=-1:
    print(f"The first greatest element which is strictly greater than the target {target} is {result}.")
else:
    print(f"There are no greater numbers than target {target} in the array. ")
    #if the array consists only the target being the greatest than other elements,else clause is printed.
