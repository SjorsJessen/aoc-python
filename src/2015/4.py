# --- Day 4: The Ideal Stocking Stuffer ---

# Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all
# the economically forward-thinking little girls and boys.

# To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes.
# The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal.
# To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

# For example:

#     If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...),
#     and it is the lowest such number to do so.
#     If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970;
#     that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

# --- Part Two ---

# Now find one that starts with six zeroes.


import hashlib
from collections.abc import Generator
from typing import Any


def __has_trailing_zeroes(input: str, prefix: str) -> bool:
    return input.startswith(prefix)


def __is_positive_number(num: int) -> bool:
    positive_numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    is_positive: bool = num in positive_numbers
    return is_positive


def __generate_numbers(start: int, end: int) -> Generator[int, Any, None]:
    yield from range(start, end)


def __first_puzzle(input: str, prefix: str) -> None:
    for number in __generate_numbers(start=100_000, end=1_000_000):
        value: str = f"{input}{number}"
        hash = hashlib.md5(value.encode())  # noqa: S324
        hex: str = hash.hexdigest()

        if __has_trailing_zeroes(input=hex, prefix=prefix):
            char: str = hex[len(prefix)]
            if char.isdecimal() and __is_positive_number(int(char)):
                print(f"Best result: {hex}")
                print(f"With number: {number}")


def __second_puzzle(input: str, prefix: str) -> None:
    for number in __generate_numbers(start=100_000, end=10_000_000):
        value: str = f"{input}{number}"
        hash = hashlib.md5(value.encode())  # noqa: S324
        hex: str = hash.hexdigest()

        if __has_trailing_zeroes(input=hex, prefix=prefix):
            print(f"Best result: {hex}")
            print(f"With number: {number}")


if __name__ == "__main__":
    __first_puzzle(input="bgvyzdsv", prefix="00000")
    __second_puzzle(input="bgvyzdsv", prefix="000000")
