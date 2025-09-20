from pathlib import Path

from utils.filehandler import INPUT_2015, FileHandler

type Position = tuple[int, int]
type PresentCount = int

directions: dict[str, Position] = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, 1),
    "v": (0, -1),
}


def __first_puzzle(input: str) -> None:
    houses: dict[Position, PresentCount] = {}
    current_pos: Position = (0, 0)

    for char in input:
        next_pos: Position = directions[char]
        current_pos = (current_pos[0] + next_pos[0], current_pos[1] + next_pos[1])
        houses[current_pos] = houses.get(current_pos, 1)
    print(len(houses))


if __name__ == "__main__":
    file_path = Path(f"{INPUT_2015}/3.txt")
    input: str = FileHandler.read(file_path=file_path).strip()
    __first_puzzle(input=input)
