class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(min(len(word) for word in strs)):
            found_difference = False

            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    found_difference = True
                    break

            if found_difference:
                break

            prefix += strs[0][i]

        return prefix
        
