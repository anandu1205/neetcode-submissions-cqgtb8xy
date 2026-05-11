class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()

        pointer1 = 0
        pointer2 = 0

        result = []

        length1 = len(nums1)
        length2 = len(nums2)

        while pointer1 < length1 and pointer2 < length2:

            if nums1[pointer1] == nums2[pointer2]:

                if nums1[pointer1] not in result:
                    result.append(nums1[pointer1])

                pointer1 += 1
                pointer2 += 1

            elif nums1[pointer1] < nums2[pointer2]:
                pointer1 += 1

            else:
                pointer2 += 1

        return result