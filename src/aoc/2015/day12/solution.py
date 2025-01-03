import json


def sum_nums(entry, skip_red=False):
    if isinstance(entry, int):
        return entry

    total = 0
    if isinstance(entry, dict):
        if skip_red and "red" in entry.values():
            return 0
        for sub_entry in entry.values():
            total += sum_nums(sub_entry, skip_red)
    elif isinstance(entry, list):
        for sub_entry in entry:
            total += sum_nums(sub_entry, skip_red)
    return total


with open("data") as f:
    json_doc = json.load(f)

# ==== PART 1 ====
print(sum_nums(json_doc))

# ==== PART 2 ====
print(sum_nums(json_doc, skip_red=True))
