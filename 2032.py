class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums3 = list(set(nums3))

        if len(set(nums1 + nums2)) < len(nums1) + len(nums2):
            print("1 e 2 diferentes")
        if len(set(nums1 + nums3)) < len(nums1) + len(nums3):
            print("1 e 3 diferentes")
        if len(set(nums2 + nums3)) < len(nums2) + len(nums3):
            print("2 e 3 diferentes")

        return []

        

s = Solution()
result = s.twoOutOfThree([1,1,3,2], [2,3], [3])
print(result)
        