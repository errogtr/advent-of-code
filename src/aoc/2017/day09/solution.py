from pathlib import Path

    
def main(input_path: Path):
    with input_path.open() as f:
        stream = f.read()
    
    scores = list()
    total_score = 0
    total_garbage = 0
    garbage = False
    while stream:
        c, stream = stream[0], stream[1:]

        if c == "!":
            stream = stream[1:]

        elif garbage and c != ">":
            total_garbage += 1

        elif c == "<":
            garbage = True
        
        elif c == ">":
            garbage = False

        elif c == "{":
            scores.append(scores[-1] + 1 if scores else 1)

        elif c == "}":             
            total_score += scores.pop()
        

    # ==== PART 1 ====
    print(total_score)

    # ==== PART 2 ====
    print(total_garbage)

