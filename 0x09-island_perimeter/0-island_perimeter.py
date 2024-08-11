#!/usr/bin/python3
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    result = [1] * len(nums)
    for i, num in enumerate(nums):
        for j, x in enumerate(result):
            if j != i:
                result *= x 

    return result

result = productExceptSelf([1,2,3,4])
print(result)
