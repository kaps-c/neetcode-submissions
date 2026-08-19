class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
            '(':')',
            '[':']',
            '{':'}'
            }
        stack_1 = [char for char in s]
        stack_2 = []
        n = len(stack_1)

        for index in range(n):
            popped = stack_1.pop()
            
            if popped in matching:
                matching_bracket = matching[popped]
                if len(stack_2) == 0:
                    return False

                top_element = stack_2[-1]
                if matching_bracket == top_element: 
                    stack_2.pop()
                else: 
                    return False

            else: 
                stack_2.append(popped)

        # edited to be a bit cleaner
        return len(stack_2) == 0
