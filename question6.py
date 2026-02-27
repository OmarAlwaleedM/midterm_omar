# Question 6 — Which is NOT a palindrome?

def palindrome(word):
    """
    Determines if a word is a palindrome
    :param word: the word to check
    :return: True if palindrome, False otherwise
    """
    if word == word[::-1]:
        return True
    else:
        return False


# Test the actual exam options
tests = [
    "7489617719749244646336564429479177169847",
    "6593036601359343374664733439531066303956",
    "8025833559061079503003059701609553385208",
    "5485839837501070045005400701057389385845",
]
for t in tests:
    print(f"palindrome('{t}') = {palindrome(t)}")

# Answer: "7489617719749244646336564429479177169847"
