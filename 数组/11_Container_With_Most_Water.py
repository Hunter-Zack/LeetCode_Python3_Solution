# -*- coding：utf-8 -*-
# &Author  AnFany

# 11_Container_With_Most_Water 盛最多水的容器



class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 利用双指针的方法：最左端和最右端2个指针，也就是列表的索引。
        # 所围成的区域的面积  等于  两个索引相见得到的差 乘以 两个索引对应的较小值
        # 靠拢的原则是，具有较小值的索引 向较大值的索引靠拢，直到索引差为1
        # 并且实时更新获得的最大的面积

        # 最大面积
        max_area = 0
        # 获得列表长度
        length = len(height)
        if length <= 1:
            return max_area

        start_index = 0  # 最左端
        end_index = len(height) - 1  # 最右端

        while end_index - start_index >= 1:
            start_num, end_num = height[start_index], height[end_index]

            if start_num > end_num:
                max_area = max(max_area, end_num * (end_index - start_index))  # 计算面积
                end_index -= 1  # 小值的索引 向大值的索引靠拢
            else:
                max_area = max(max_area, start_num * (end_index - start_index))  # 计算面积
                start_index += 1  # 小值的索引 向大值的索引靠拢

        return max_area




