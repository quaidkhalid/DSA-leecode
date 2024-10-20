class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 1, n - 2
        while left <= right:
            mid = left + (right - left)//2 # left +right //2
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid-1] < arr[mid]:
                left = mid + 1
            else:
                right = mid -1
        
        