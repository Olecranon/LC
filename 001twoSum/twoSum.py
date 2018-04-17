class Solution:
    
    ## brute force
    '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]    
    '''

    ## use dictionary
    def twoSum(self, nums, target):
        dic = {}
        for i in range(0, len(nums)):
            x = nums[i]
            val = target - x
            if val in dic:
                return [dic[val], i]
            else:
                dic[x] = i


s = Solution()
print s.twoSum([0, 3,1, 3], 6)
