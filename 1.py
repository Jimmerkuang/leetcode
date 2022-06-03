# -*- coding: utf-8 -*-
# Time   : 2022/4/18 10:31
# Author : kfu


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, num in enumerate(nums):
            if (diff := target - num) in hashtable:
                return [hashtable[diff], i]
            hashtable[num] = i
        return []


if __name__ == '__main__':
    solution = Solution()
    results = solution.twoSum([2, 7, 13, 15], 9)