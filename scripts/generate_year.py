import click

from aoc.constants import ROOT_DIR, SOLUTIONS_TEMPLATE
from aoc.models import YearDayModel
from aoc.utils import day_dir


@click.command()
@click.argument("year", type=int)
def main(year: int):
    year_dir = ROOT_DIR / str(year)
    
    max_day = 25 if year < 2025 else 12  # :(
    for day in range(1, max_day + 1):
        # validate year
        YearDayModel(year=year, day=day)

        # create day folder
        day_dirname = year_dir / day_dir(day)
        day_dirname.mkdir(parents=True, exist_ok=True)

        # create input files templates
        example_fp = day_dirname / "example"
        if not example_fp.exists():
            with example_fp.open("w") as f:
                f.write("")

        data_fp = day_dirname / "data"
        with data_fp.open("w") as f:
            f.write("")

        # create solution file template
        solution_fp = day_dirname / "solution.py"
        if not solution_fp.exists():
            with solution_fp.open("w") as f:
                f.write(SOLUTIONS_TEMPLATE)


if __name__ == "__main__":
    main()
