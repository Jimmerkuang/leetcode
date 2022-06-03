# -*- coding: utf-8 -*-
# Time   : 2022/4/25 15:09
# Author : kfu


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp, rp = 0, len(height) - 1
        lh, rh = height[lp], height[rp]
        ans = 0
        while (l := rp - lp) > 0:
            if lh <= rh:
                area = l * lh
                lp += 1
                lh = height[lp]
            else:
                area = l * rh
                rp -= 1
                rh = height[rp]
            ans = ans if ans > area else area
        return ans

