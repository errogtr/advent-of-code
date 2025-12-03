from pathlib import Path


def day_dir(day: int):
    return "day" + str(day).rjust(2, "0")


def read_data(path: str, example: bool = False) -> str:
    fname = "example" if example else "data"
    with open(Path(path).parent / fname) as f:
        data = f.read()
    return data
