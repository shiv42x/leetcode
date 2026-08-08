class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_ptr = m - 1
        nums2_ptr = n - 1

        for i in range(n + m - 1, -1, -1):
            if nums1_ptr < 0:
                nums1[i] = nums2[nums2_ptr]
                nums2_ptr -= 1
                continue
            if nums2_ptr < 0:
                nums1[i] = nums1[nums1_ptr]
                nums1_ptr -= 1
                continue

            if nums1[nums1_ptr] >= nums2[nums2_ptr]:
                nums1[i] = nums1[nums1_ptr]
                nums1_ptr -= 1
            else:
                nums1[i] = nums2[nums2_ptr]
                nums2_ptr -= 1