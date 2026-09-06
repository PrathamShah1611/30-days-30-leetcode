class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack:
                    return False

                last = stack.pop()

                if last != pairs[i]:
                    return False

        return len(stack) == 0
        
