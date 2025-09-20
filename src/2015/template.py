from pathlib import Path

from utils.filehandler import INPUT_2015, FileHandler


def __first_puzzle(input: str) -> None: ...


def __second_puzzle(input: str) -> None: ...


if __name__ == "__main__":
    file_path = Path(f"{INPUT_2015}/3.txt")
    input: str = FileHandler.read(file_path=file_path)
