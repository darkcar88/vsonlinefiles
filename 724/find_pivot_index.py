class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        left_sum, right_sum = [0], [0] * length
        
        start, end = 0, 0
        for i in range(1, length):
            start += nums[i - 1]
            left_sum.append(start)
            end += nums[length - i]
            right_sum[length - i - 1] = end
            
            
            
        print(left_sum, right_sum)