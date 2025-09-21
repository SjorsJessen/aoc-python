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
