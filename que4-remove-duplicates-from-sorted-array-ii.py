class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 0
        count = 0

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                count = 1  # New element, reset count
            else:
                count += 1

            if count <= 2:  # Write only if count is <= 2
                nums[k] = nums[i]
                k += 1

        return k