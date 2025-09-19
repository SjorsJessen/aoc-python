# --- Day 1: Not Quite Lisp ---

# Santa is trying to deliver presents in a large apartment building,
# but he can't find the right floor - the directions he got are a little confusing.
# He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

# An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

# The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

# For example:

#     (()) and ()() both result in floor 0.
#     ((( and (()(()( both result in floor 3.
#     ))((((( also results in floor 3.
#     ()) and ))( both result in floor -1 (the first basement level).
#     ))) and )())()) both result in floor -3.

# To what floor do the instructions take Santa?

from pathlib import Path

from src.utils.filehandler import INPUT_2015, FileHandler


def __first_puzzle(input: str) -> None:
    starting_point: int = 0
    directions: dict[str, int] = {
        "(": 1,
        ")": -1,
    }

    for char in input:
        direction: int = directions[char]
        starting_point += direction
    print(starting_point)


if __name__ == "__main__":
    file_path = Path(f"{INPUT_2015}/1.txt")
    input: str = FileHandler.read(file_path=file_path)

    __first_puzzle(input=input)
