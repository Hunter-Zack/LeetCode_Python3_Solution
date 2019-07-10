# -*- coding：utf-8 -*-
# &Author  AnFany

# 16_3Sum Closest 最接近的三数之和

# 思路类似于15题


class Solution:
    def threeSumClosest(self, nums, target):
        length = len(nums)
        if length <= 3:
            return sum(nums)
        # 将数据序列排序
        nums.sort()
        result_p = []  # 添加三数之和和target的差，正负分别存储
        result_n = []
        # 先选中一个one
        for one in range(length):
            if one > 0 and nums[one] == nums[one-1]:  # 防止出现重复求和
                continue
            two = one + 1
            three = length - 1
            # 固定one，寻找第二个和第三个
            while two < three:
                # 计算三者的和
                number_sum = nums[one] + nums[two] + nums[three]
                # 如果等于target
                if number_sum == target:
                    return target
                # 如果大于target，three对应的变小
                elif number_sum > target:
                    three -= 1
                    result_p.append(number_sum - target)  # 存储正的
                # 如果小于target，two对应的变大
                else:
                    two += 1
                    result_n.append(number_sum - target)  # 存储负的
        # 选择最接近的
        if result_p:
            if result_n:
                min_p, max_n = min(result_p), max(result_n)
                if abs(min_p) > abs(max_n):
                    return target + max_n
                else:
                    return target + min_p
            else:
                return target + min(result_p)
        else:
            return target + max(result_n)
            # 不会全为空



