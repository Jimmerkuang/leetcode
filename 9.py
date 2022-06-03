# -*- coding: utf-8 -*-
# Time   : 2022/4/25 14:56
# Author : kfu


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x % 10 == 0:
            return False
        rev = 0
        while rev < x:
            digit = x % 10
            rev = 10 * rev + digit
            if rev < x:
                x = x // 10
        if rev == x:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    answer = solution.isPalindrome(0)