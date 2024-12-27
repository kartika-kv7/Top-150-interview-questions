class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # Handle cases where k is greater than the array length.
        
        # Reverse the entire array.
        nums.reverse()
        # Reverse the first k elements.
        nums[:k] = reversed(nums[:k])
        # Reverse the rest of the array.
        nums[k:] = reversed(nums[k:])
        """
        Do not return anything, modify nums in-place instead.
        """
        