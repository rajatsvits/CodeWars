The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max

def maxSequence(arr):
    return max(maxSequence(arr[1:]), max(reduce(lambda sums, n: sums + [sums[-1]+n], arr, [0]))) if arr else 0

def max_sequence(arr):
    print(arr)
    if len(arr)==0:
        return 0
    max_ending=0
    max_so_far=0
    start=0
    end=0
    s=0
    for i in range(0,len(arr)):
        max_ending+=arr[i]
        if max_so_far < max_ending:
            max_so_far=max_ending
            start=s
            end=i
        if max_ending < 0:
            max_ending=0
            s=i+1
    if start==end and arr[start]<0:
        return 0
        
    return sum(arr[start:end+1])
        
        
