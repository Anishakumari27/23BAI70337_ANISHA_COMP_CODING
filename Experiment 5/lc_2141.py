class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        def check(mid):
            summ=0
            for b in batteries:
                summ+=min(b,mid)
            if summ>=n*mid:
                return True
            else:
                return False
        low=1
        high=sum(batteries)//n
        ans=0
        while low<=high:
            mid=low+(high-low)//2
            if check(mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
        