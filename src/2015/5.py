# --- Day 5: Doesn't He Have Intern-Elves For This? ---

# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

#     It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#     It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#     It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

# For example:

#     ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...),
#     and none of the disallowed substrings.
#     aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
#     jchzalrnumimnmhp is naughty because it has no double letter.
#     haegwjzuvuyypxyu is naughty because it contains the string xy.
#     dvszwmarrgswjxmb is naughty because it contains only one vowel.

# How many strings are nice?

import string
from pathlib import Path

from utils.filehandler import INPUT_2015, FileHandler

bad_words: list[str] = ["ab", "cd", "pq", "xy"]
vowels: list[str] = ["a", "e", "i", "o", "u"]
alphabet = string.ascii_lowercase
duplicates: list[str] = [char + char for char in alphabet]


def __has_bad_words(line: str) -> bool:
    return any(bad_word in line for bad_word in bad_words)


def __has_duplicates(line: str) -> bool:
    return any(duplicate in line for duplicate in duplicates)


def __has_enough_vowels(line: str) -> bool:
    minimum: int = 3
    found_vowels: list[str] = [char for char in line if char in vowels]
    return len(found_vowels) >= minimum


def __is_nice_line(line: str) -> bool:
    return __has_bad_words(line) is False and __has_enough_vowels(line) and __has_duplicates(line)


def __first_puzzle(lines: str) -> None:
    nice_lines: list[str] = [line for line in lines if __is_nice_line(line=line.strip())]
    print(len(nice_lines))


def __second_puzzle(input: str) -> None: ...


if __name__ == "__main__":
    file_path = Path(f"{INPUT_2015}/5.txt")
    input: str = FileHandler.read_lines(file_path=file_path)
    __first_puzzle(lines=input)
    __second_puzzle(input=input)
