from datetime import datetime
from pathlib import Path
from pydantic import BaseModel, Field, field_validator

from aoc.utils import day_dir


class YearDayModel(BaseModel):
    year: int = Field(ge=2015)
    day: int = Field(gt=0, le=25)

    def get_puzzle_module(self) -> str:
        return f"aoc.{self.year}.{self._day_dir()}.solution"

    def get_input_path(self, root: Path, is_example: bool) -> str:
        puzzle_dir = root / str(self.year) / self._day_dir()
        if is_example:
            return puzzle_dir / "example"
        return puzzle_dir / "data"

    def _day_dir(self):
        return day_dir(self.day)

    @field_validator("year", mode="after")
    @classmethod
    def validate_year(cls, value: int) -> int:
        today = datetime.today()
        current_year = today.year
        if value == current_year and today.month != 12:
            raise ValueError("It's not time for this year AoC yet!")
        return value
