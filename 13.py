# -*- coding: utf-8 -*-
# Time   : 2022/4/25 22:48
# Author : kfu


MAPPING = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
}

SPECIAL_MAPPING = {
    'CM': 900,
    'CD': 400,
    'XC': 90,
    'XL': 40,
    'IX': 9,
    'IV': 4,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        while s:
            for key, value in SPECIAL_MAPPING.items():
                if s.find(key) != -1:
                    s = s.replace(key, '', 1)
                    result += value
            for key, value in MAPPING.items():
                if s.find(key) != -1:
                    s = s.replace(key, '', 1)
                    result += value
        return result


if __name__ == '__main__':
    solution = Solution()
    answer = solution.romanToInt('III')