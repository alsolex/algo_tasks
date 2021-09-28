from typing import List


class Solution:
    def __init__(self):
        self.morse_alphabet = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_words = set()
        for word in words:
            morse_word = "".join(
                [self.morse_alphabet[ord(ch) - ord("a")] for ch in word]
            )
            morse_words.add(morse_word)
        return len(morse_words)


def main():
    words = [word for word in input("Enter words: ").split()]
    foo = Solution()
    print("Answer: ", foo.uniqueMorseRepresentations(words))


if __name__ == "__main__":
    main()
