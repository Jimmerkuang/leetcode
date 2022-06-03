# -*- coding: utf-8 -*-
# Time   : 2022/4/25 14:20
# Author : kfu


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 - 2
        ans = []
        for i in range(r):
            for j in range(0, n - i, t):
                ans.append(s[j + i])
                if 0 < i < r - 1 and j + t - i < n:
                    ans.append(s[j + t - i])
        return ''.join(ans)


if __name__ == '__main__':
    solution = Solution()
    answer = solution.convert('PAYPALISHIRING', 4)