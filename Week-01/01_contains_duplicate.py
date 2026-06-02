# Problem: LeetCode #217 - Contains Duplicate
# Difficulty: Easy

def containsDuplicate(nums):
    # TODO: Write your brute force solution first tomorrow!
    pass

# Test Cases for tomorrow morning
print(containsDuplicate([1, 2, 3, 1]))  # Expected output: True
print(containsDuplicate([1, 2, 3, 4]))  # Expected output: False

# leetcode problem number (#217)
#217. Contains Duplicate Given an integer array nums, return true if any value appears at least twice in the array
# , and return false if every element is distinct.

def contideupicate(num):
    for L in range(len(num)):
        for R in range(L+1,len(num)):
            if num[L]==num[R]:
                return True
    return False
print(contideupicate([1,2,3,1]))
print(contideupicate([1,2,3,4]))
