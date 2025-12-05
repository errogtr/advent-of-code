import click

from aoc.utils import read_data, timer


@timer
def part1(instructions):
    registers = dict(zip("abcdefgh", [0] * 8))
    current = 0
    mul = 0
    while current < len(instructions):
        instruction = instructions[current]
        op, X, Y = instruction.split()
        Y = registers[Y] if Y.isalpha() else int(Y)
        match op:
            case "set":
                registers[X] = Y
            case "sub":
                registers[X] -= Y
            case "mul":
                registers[X] *= Y
                mul += 1
            case "jnz":
                X = registers[X] if X.isalpha() else int(X)
                if X != 0:
                    current += Y - 1
        current += 1
    return mul


@timer
def part2():
    """
    My input + th instructions consist in a program equivalent to the following:

    ###################################
    1.  b = 108400
    2.  c = 125400
    3.  h = 0
    4.  while True: 
    5.    f, d = 1, 2
    6.    while True:
    7.        e = 2
    8.        while True:
    9.            if d * e == b:
    10.                f = 0
    11.            e += 1
    12.           if e == b:
    13.                break
    14.       d += 1
    15.        if d == b:
    16.            break
    17.    if f == 0:
    18.        h += 1
    19.    if b == c:
    20.        break
    21.    b += 17
    22. return h
    ###################################
    
    This is a very inefficient program that counts the elements of the set (lines 9, 10 17, 18)

        {108400 + 17 * k, k integer in [0, 17000]} & {x | x is NOT prime}

    Here I list the 98 prime numbers inside the range [108400, 125400]:

            108553, 108587, 108791, 108893, 108961, 109063, 109097, 
            109199, 109267, 109471, 109913, 110083, 110321, 110491, 
            110729, 110899, 110933, 111103, 111341, 111409, 111443, 
            111919, 111953, 112327, 112361, 112429, 112939, 113041, 
            113143, 113177, 113279, 113381, 113891, 114197, 114299,
            114571, 114809, 115013, 115183, 115319, 115421, 115523,
            115693, 115727, 115931, 116101, 116747, 116849, 117053, 
            117223, 117427, 117529, 117563, 117937, 118277, 118549, 
            118583, 118787, 119297, 119569, 119671, 119773, 120011, 
            120079, 120181, 120283, 120623, 120691, 120929, 120997, 
            121439, 121507, 121609, 121711, 121949, 122051, 122323, 
            122527, 122561, 122663, 122833, 122867, 123377, 123479, 
            123547, 123581, 123853, 123887, 123989, 124193, 124363, 
            124567, 124601, 124669, 124703, 124771, 124907, 125383

    Since in the interval [108400, 125400] contains 1001 = (108400 - 125400) // 17 + 1 numbers,
    the answer is 903 = 1001 - 98
    """
    return 903

            


@click.command()
@click.option("--example", is_flag=True)
def main(example):
    data = read_data(__file__, example)

    instructions = data.splitlines()

    # ==== PART 1 ====
    print(part1(instructions))

    # ==== PART 2 ====
    print(part2())


if __name__ == "__main__":
    main()
