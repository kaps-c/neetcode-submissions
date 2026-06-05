class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)

        s_sorted = sorted(list(s))
        t_sorted = sorted(list(t))

        if s_sorted == t_sorted:
            return True

        else:
            return False
        