class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        test = x if x > 0 else -x

        result = 0

        while test > 0:
            result = result * 10 + test % 10
            test = int(test / 10)

        if x > 0:
            return result
        else:
            return -result


test = 1534236469
result = Solution().reverse(test)
print(result)