class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        s_sorted = sorted(s_list)
        t_sorted = sorted(t_list)

        if s_sorted == t_sorted:
            return True

        return False


