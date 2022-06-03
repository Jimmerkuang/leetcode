# -*- coding: utf-8 -*-
# Time   : 2022/4/18 10:55
# Author : kfu


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occurence = set()
        n = len(s)
        answer = 0
        right_key = 0
        for i in range(n):
            if i != 0:
                occurence.remove(s[i - 1])
            while right_key < n and s[right_key] not in occurence:
                occurence.add(s[right_key])
                right_key += 1
            answer = max(answer, right_key - i)
        return answer


if __name__ == '__main__':
    solution = Solution()
    results = solution.lengthOfLongestSubstring('abcda')
