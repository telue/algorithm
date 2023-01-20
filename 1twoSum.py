# 时间：20230119
# 题目：2数之和
# 力扣网址：https://leetcode.cn/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1.遍历列表
        for i in range(len(nums)):
            # 2.计算需要找到的下一个目标数字
            res = target-nums[i]
                # 3.遍历剩下的元素，查找是否存在该数字
            if res in nums[i+1:]:
                # 4.若存在，返回答案。这里由于是两数之和，可采用.index()方法
                # 4.1.获得目标元素在nums[i+1:]这个子数组中的索引后，还需加上i+1才是该元素在nums中的索引
                return [i, nums[i+1:].index(res)+i+1]