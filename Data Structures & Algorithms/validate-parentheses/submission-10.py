class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
            '(':')',
            '[':']',
            '{':'}'
            }
        stack = []

        for char in reversed(s):
            if char in matching:
                matching_bracket = matching[char]
                if len(stack) == 0:
                    return False

                top_element = stack[-1]
                if matching_bracket == top_element: 
                    stack.pop()
                else: 
                    return False

            else: 
                stack.append(char)

        # edited to be a bit cleaner
        return len(stack) == 0