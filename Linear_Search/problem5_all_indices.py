''' Problem Statement:

-->Given an array of integers and a target value,
-->return a list of all indices where the target appears in the array.
-->If the target does not exist in the array, return an empty list.'''

#making use of an empty list to store all the indices of the target from the array.

def find_all_indices(arr,target):
    all_indices=[]
    for i,value in enumerate(arr):          #range can also be used in place of enumerate()
        if value==target:
            all_indices.append(i)

    return all_indices

array=[34,5,21,78,5,65,8,9,5,2]
target=5
result=find_all_indices(array,target)

if target in array:
    print(f" The target element {target} is present at {result} indices.")
else:
    print(f" The target element is not found in the array so the list all_indices is {result}.")

# File restored and committed successfully