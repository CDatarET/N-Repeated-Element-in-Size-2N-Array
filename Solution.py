class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        track = []
        for i in range(len(nums)):
            if nums[i] not in track:
                track.append(nums[i])
            else:
                return(nums[i])
        
