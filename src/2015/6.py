# --- Day 6: Probably a Fire Hazard ---

# Because your neighbors keep defeating you in the holiday house decorating contest year after year,
# you've decided to deploy one million lights in a 1000x1000 grid.

# Furthermore, because you've been especially nice this year,
# Santa has mailed you instructions on how to display the ideal lighting configuration.

# Lights in your grid are numbered from 0 to 999 in each direction;
# the lights at each corner are at 0,0, 0,999, 999,999, and 999,0.
# The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs.
# Each coordinate pair represents opposite corners of a rectangle, inclusive;
# a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square.
# The lights all start turned off.

# To defeat your neighbors this year,
# all you have to do is set up your lights by doing the instructions Santa sent you in order.

# For example:

#     turn on 0,0 through 999,999 would turn on (or leave on) every light.
#     toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on,
#     and turning on the ones that were off.
#     turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

# After following the instructions, how many lights are lit?

import re
from dataclasses import dataclass
from pathlib import Path

from utils.filehandler import INPUT_2015, FileHandler

Position = tuple[int, int]
State = str


@dataclass
class Instruction:
    """Instruction."""

    start_point: Position
    end_point: Position
    state: str


find_positions_pattern = r"\d+"
find_state_pattern = r"\b(on|off|toggle)\b"


def __extract_instruction(line: str) -> Instruction:
    positions: list[int] = re.findall(find_positions_pattern, line)
    states: list[str] = re.findall(find_state_pattern, line, flags=re.IGNORECASE)
    start_pos_x, start_pos_y, end_pos_x, end_pos_y = positions
    return Instruction(
        start_point=(int(start_pos_x), int(start_pos_y)), end_point=(int(end_pos_x), int(end_pos_y)), state=states[0]
    )


def __create_lights(start_point: Position, end_point: Position) -> dict[Position, State]:
    return {
        (x, y): "off" for x in range(start_point[0], end_point[0] + 1) for y in range(start_point[1], end_point[1] + 1)
    }


def __get_grid_positions(start_point: Position, end_point: Position) -> list[Position]:
    return [(x, y) for x in range(start_point[0], end_point[0] + 1) for y in range(start_point[1], end_point[1] + 1)]


def __first_puzzle(lines: str) -> None:
    instructions: list[Instruction] = [__extract_instruction(line) for line in lines]
    lights: dict[tuple[int, int], str] = __create_lights(start_point=(0, 0), end_point=(999, 999))

    for instruction in instructions:
        grid_positions: list[Position] = __get_grid_positions(
            start_point=instruction.start_point, end_point=instruction.end_point
        )
        for position in grid_positions:
            if lights.get(position):
                if instruction.state == "toggle":
                    lights[position] = "on" if lights[position] == "off" else "off"
                else:
                    lights[position] = instruction.state
            else:
                lights.update({position: instruction.state})

    total: int = len([state for state in lights.values() if state == "on"])
    print(total)


def __second_puzzle(input: str) -> None: ...


if __name__ == "__main__":
    file_path = Path(f"{INPUT_2015}/6.txt")
    input: str = FileHandler.read_lines(file_path=file_path)
    __first_puzzle(lines=input)
    __second_puzzle(input=input)
