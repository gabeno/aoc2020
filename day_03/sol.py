from pathlib import Path
from functools import reduce


def parse_forest(filepath="./input.txt"):
    with open(filepath, "r") as f:
        lines = (f.readlines())
        forest = [line.strip() for line in lines]
    return forest


def count_trees(forest):
    l = len(forest)
    w = len(forest[0])

    indices = [(x, (x * 3) % w) for x in range(0, l)]
    trees = [forest[l][i] for (l, i) in indices]
    count_trees = trees.count("#")
    return count_trees


def count_any_trees(forest, slope):
    l = len(forest)
    w = len(forest[0])
    right, down = slope
    indices = [(x * down, (x * right) % w) for x in range(0, -(l // -down))]
    trees = [forest[l][i] for (l, i) in indices]
    count_trees = trees.count("#")
    return count_trees

def combined_product(forest, slopes):
    counts = [count_any_trees(forest, slope) for slope in slopes]
    print(counts)
    return reduce(lambda a, b: a*b, counts)



if __name__ == "__main__":
    forest = parse_forest("./input.txt")
    count = count_trees(forest)
    print(count)
    count = count_any_trees(forest, (1, 2))
    print(count)
    product = combined_product(forest, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])
    print(product)
