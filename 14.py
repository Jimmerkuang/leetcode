# -*- coding: utf-8 -*-
# Time   : 2022/4/25 23:26
# Author : kfu


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        if not strs or not s:
            return ''
        else:
            result = ''
            for j in range(len(s)):
                pre_s = s[j]
                for i, _ in enumerate(strs):
                    if j >= len(strs[i]) or strs[i][j] != pre_s:
                        return result
                result += pre_s
            return result


if __name__ == '__main__':
    solution = Solution()
    answer = solution.longestCommonPrefix(['ab', 'a'])