# -*- coding: utf-8 -*-
# Time   : 2022/4/18 21:24
# Author : kfu


class Solution:
    @staticmethod
    def _expand_around_center(s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self._expand_around_center(s, i, i)
            left2, right2 = self._expand_around_center(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]


if __name__ == '__main__':
    solution = Solution()
    results = solution.longestPalindrome('bb')
