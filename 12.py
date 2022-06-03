# -*- coding: utf-8 -*-
# Time   : 2022/4/25 22:12
# Author : kfu


NUMS = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
ROMANS = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')


class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        while num > 0:
            for i, n in enumerate(NUMS):
                if num >= n:
                    result.append(ROMANS[i])
                    num -= n
                    break
        return ''.join(result)


if __name__ == '__main__':
    solution = Solution()
    answer = solution.intToRoman(3)