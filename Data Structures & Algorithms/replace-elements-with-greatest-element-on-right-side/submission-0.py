class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            num = arr[i+1]
            for j in range(i+1, len(arr)):
                if num < arr[j]:
                    num = arr[j]
            arr[i] = num
            print(arr)
        arr[-1] = -1
        return arr