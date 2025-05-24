class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        map1=Counter(nums1)
        map2=Counter(nums2)
        map3=Counter(nums3)
        result=[]
        for key in map1.keys():
            if key in map2 or key in map3:
                result.append(key)
        for key in map2.keys():
            if key in map1 or key in map3:
                result.append(key)
        return list(set(result))