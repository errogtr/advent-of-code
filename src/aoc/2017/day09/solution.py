from pathlib import Path

    
def main(input_path: Path):
    with input_path.open() as f:
        stream = f.read()
    
    score = 0
    total_score = 0
    total_garbage = 0
    garbage_starts = 0
    garbage = False
    group_start = list()
    i = 0
    while stream:
        c = stream[i]

        if c == "!":
            stream = stream[:i] + stream[i+2:]

        elif garbage and c != ">":
            i += 1
            total_garbage += 1

        elif c == "<":
            garbage_starts = i
            garbage = True
            i += 1
        
        elif c == ">":
            garbage = False
            stream = stream[:garbage_starts] + stream[i+1:]
            i = garbage_starts

        elif c == "{" and not garbage:
            score += 1
            group_start.append(i)
            i += 1

        elif c == "}" and not garbage:             
            current_group_start = group_start.pop()
            total_score += score
            stream = stream[:current_group_start] + stream[i+1:]
            i = current_group_start
            score -= 1
        
        else:
            stream = stream[:i] + stream[i+1:]
        

    print(total_score)

    print(total_garbage)

