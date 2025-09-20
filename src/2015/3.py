from dataclasses import dataclass
from pathlib import Path

from utils.filehandler import INPUT_2015, FileHandler

type Position = tuple[int, int]


@dataclass
class House:
    """House object."""

    position: Position
    amount_of_presents: int


directions: dict[str, Position] = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, 1),
    "v": (0, -1),
}

if __name__ == "__main__":
    file_path = Path(f"{INPUT_2015}/3.txt")
    input: str = FileHandler.read(file_path=file_path)

    houses: list[House] = []
    pos_x: int = 0
    pos_y: int = 0

    for char in input:
        new_pos: Position = directions[char]
        pos_x += new_pos[0]
        pos_y += new_pos[1]
        current_pos: tuple[int, int] = (pos_x, pos_y)

        if current_pos in [house.position for house in houses]:
            house: House = next(house for house in houses if house.position == current_pos)
            house.amount_of_presents += 1
        else:
            houses.append(House(position=current_pos, amount_of_presents=1))

    total: int = len([house for house in houses if house.amount_of_presents >= 1])
    print(total)
