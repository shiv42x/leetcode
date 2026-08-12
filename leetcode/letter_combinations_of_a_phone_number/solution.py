def letterCombinations(self, digits: str) -> List[str]:
    digit_to_letters = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }
    result = []
    
    def backtrack(digits, string):
        if len(digits) == 0:
            result.append(string)
            return

        for i, letter in enumerate(digit_to_letters[int(digits[0])]):
            # strip first digit, 'lock' a choice for that, and explore that choice
            backtrack(digits[1:], string + digit_to_letters[int(digits[0])][i])

    for letter in digit_to_letters[int(digits[0])]:
        backtrack(digits[1:], letter)
    return result