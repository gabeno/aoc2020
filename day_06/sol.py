def parse_answers(filepath="./input.txt"):
    _f = open(filepath, "r")
    txt = _f.read().replace("\n\n", "---").replace("\n", " ").strip()
    data = txt.split("---")
    return data

def get_counts_anyone(lines):
    counts = [len(set(line.replace(" ", ""))) for line in lines]
    return sum(counts)

def get_counts_everyone(lines):
    counts = []
    for group in lines:
        size = len(group.split(" "))
        # print(size)
        answers = {}
        count = 0
        for answer in group.replace(" ", ""):
            if answer in answers:
                answers[answer] += 1
            else:
                answers[answer] = 1
        # print(answers)
        for a in answers:
            if answers[a] == size:
                count += 1
            else:
                count += 0
        # print(count)
        counts.append(count)
    print(counts)
    return sum(counts)


if __name__ == "__main__":
    lines = parse_answers()
    c = get_counts_anyone(lines)
    # print(c)
    c = get_counts_everyone(lines)
    print(c)
