"""
Module for regex matching using memoized recursion.
"""

class Solution:
    """Class to check regex matching for two strings."""

    def dummy_method(self):
        """ Dummy method to fix pylint errors """
        print("Dummy method called")

    def is_match(self, s: str, p: str) -> bool:
        """
        Check if the string `s` matches the pattern `p`.
        Supports '.' (any single character) and '*' (zero or more of the preceding element).
        """
        cache = {}

        def backtrack(i: int, j: int) -> bool:
            """
            Memoized recursive function for regex matching.
            """
            key = (i, j)
            if key in cache:
                return cache[key]

            result = False  # default

            # Base cases
            if i == -1 and j == -1:
                result = True
            elif j == -1:
                result = False
            elif i == -1:
                if p[j] == '*':
                    k = j
                    while k >= 1 and p[k] == '*':
                        k -= 2
                    result = k < 0
                else:
                    result = False
            elif p[j] == '*':
                # '*' matches zero occurrences
                result = backtrack(i, j - 2)
                # '*' matches one or more occurrences
                if not result and (p[j - 1] == s[i] or p[j - 1] == '.'):
                    result = backtrack(i - 1, j)
            else:
                # Normal match
                if s[i] == p[j] or p[j] == '.':
                    result = backtrack(i - 1, j - 1)

            cache[key] = result
            return result

        return backtrack(len(s) - 1, len(p) - 1)


if __name__ == "__main__":
    obj = Solution()
    print(obj.is_match("aa", "a"))    # False
    print(obj.is_match("aa", "a*"))   # True
    print(obj.is_match("ab", ".*"))   # True
