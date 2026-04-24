class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        lcm = (a * b) // math.gcd(a, b)
        low = min(a, b)
        high = n * min(a, b)
        while low < high:
            mid = (low + high) // 2
            count = (mid // a) + (mid // b) - (mid // lcm)
            if count < n:
                low = mid + 1
            else:
                high = mid
        return low % MOD