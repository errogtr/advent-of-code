from datetime import datetime
from importlib import import_module
from pathlib import Path

import click
from pydantic import BaseModel, Field, field_validator

from aoc.constants import ROOT_DIR


class Args(BaseModel):
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
        return "day" + str(self.day).rjust(2, "0")
    
    @field_validator("year", mode="after")
    @classmethod
    def validate_year(cls, value: int) -> int:
        today = datetime.today()
        current_year = today.year
        if value == current_year and today.month != 12:
            raise ValueError("It's not time for this year AoC yet!")
        return value


@click.command()
@click.argument("year")
@click.argument("day")
@click.option("--example", is_flag=True)
def main(year: int, day: int, example: bool):
    args = Args(year=year, day=day)
    puzzle_module = import_module(args.get_puzzle_module())
    puzzle_module.main(args.get_input_path(root=ROOT_DIR, is_example=example))


if __name__ == "__main__":
    main()
