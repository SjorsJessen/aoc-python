"""Utility functions which handles file reading module."""

from pathlib import Path
from typing import Final

INPUT_2015: Final[str] = "input/2015"


class FileHandler:
    """Class which handles file reading."""

    @staticmethod
    def read(file_path: Path) -> str:
        """Read the contents of a file."""
        with Path.open(file_path, encoding="utf-8") as file:
            contents: str = file.read()

        return contents

    @staticmethod
    def read_lines(file_path: Path) -> list[str]:
        """Read the contents of a file."""
        with Path.open(file_path, encoding="utf-8") as file:
            contents: list[str] = file.readlines()

        return contents
