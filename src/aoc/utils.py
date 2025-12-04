from functools import wraps
from pathlib import Path
from time import time


def day_dir(day: int):
    return "day" + str(day).rjust(2, "0")


def read_data(path: str, example: bool = False) -> str:
    fname = "example" if example else "data"
    with open(Path(path).parent / fname) as f:
        data = f.read()
    return data


def timer(fn):
    @wraps(fn)
    def _decorator(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        elapsed = time() - start
        print("=================================================")
        print(f"Execution time for {fn.__name__}: {elapsed:.3f}s")
        return result

    return _decorator
