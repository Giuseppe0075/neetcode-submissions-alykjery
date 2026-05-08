class Solution:
    

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        result = [""]

        for digit in digits:
            tmp = []
            for currStr in result:
                for char in mapping[digit]:
                    tmp.append(currStr + char)
            result = tmp

        return result
