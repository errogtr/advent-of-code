def total_joltage(data, seq_len):
    total = 0
    for bank in data.split("\n"):
        joltage = ""
        start, end = 0, len(bank) - seq_len + 1
        for i in range(seq_len):
            window = bank[start:end+i]
            m = max(window)
            joltage += m
            start += window.find(m) + 1
        total += int(joltage)

    return total



def main():
    with open("data") as f:
        data = f.read()

    # ==== PART 1 ====
    print(total_joltage(data, 2))

    # ==== PART 2 ====
    print(total_joltage(data, 12))


if __name__ == "__main__":
    main()
