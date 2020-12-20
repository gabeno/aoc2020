import re


"""
In [9]: g = re.match(r'(?P<parent>\w+\s\w+)', 'light red bags')

In [10]: g.groupdict()
Out[10]: {'parent': 'light red'}


In [10]: g = re.match(r'^(?P<qty>\d)\s(?P<child>\w+\s\w+)', '1 bright white bag')

In [11]: g.groupdict()
Out[11]: {'qty': '1', 'child': 'bright white'}


{'light red': {'bright white': '1', 'muted yellow': '2'}}
{'dark orange': {'bright white': '3', 'muted yellow': '4'}}
{'bright white': {'shiny gold': '1'}}
{'muted yellow': {'shiny gold': '2', 'faded blue': '9'}}
{'shiny gold': {'dark olive': '1', 'vibrant plum': '2'}}
{'dark olive': {'faded blue': '3', 'dotted black': '4'}}
{'vibrant plum': {'faded blue': '5', 'dotted black': '6'}}
{'faded blue': {}}
{'dotted black': {}}

"""


def read_input(filepath="./input.txt"):
    """Read input and create a tree

    Example:
        light red bags contain 1 bright white bag, 2 muted yellow bags.
        => {'light red': {'bright white': '1', 'muted yellow': '2'}}

        faded blue bags contain no other bags.
        => {'faded blue': {}}
    """
    f = open(filepath, "r").readlines()
    def parse_bags(line):
        d = {}
        line = line.strip()
        parts = line.split(" contain ")
        # print(parts)
        # parent
        g = re.match(r"(?P<parent>\w+\s\w+)", parts[0])
        p = g.groupdict()["parent"]
        d[p] = {}
        # child
        for child in parts[1].split(","):
            # print(child)
            g = re.match(r"^\s?(?P<qty>\d)\s(?P<child>\w+\s\w+)", child)
            if g is not None:
                z = g.groupdict()
                d[p][z["child"]] = z["qty"]
        return d
    return [parse_bags(l) for l in f]


def containing_bags(bag_type, conveyor, bags = []):
    for b in conveyor:
        for k, v in b.items():
            if bag_type in v:
                bags.append(k)
                containing_bags(k, conveyor, bags)
    return set(bags)


def count_contained_bags(bag_type, conveyor):
    """
    for b in conveyor:
        for k, v in b.items():
            if k == bag_type:
                if len(v) == 0:
                    return 0
                # print(k, v)
                _c = 0
                for _b, c in v.items():
                    print(c)
                    _c += int(c)
                    count += count_contained_bags(_b, conveyor, count)
                print(f"inner count: {_c}")
                return _c
    return count
    """

    seen = []
    def find_bag(bag_type, conveyor):
        for bag in conveyor:
            for k, v in bag.items():
                if k == bag_type:
                    print("p", k, v)
                    print("pv", list(map(int, v.values())))
                    if len(v) == 0:
                        return
                    else:
                        _c = 0
                        for _k, _v in v.items():
                            # print("c", _k, _v)
                            if _v.isnumeric():
                                _c += int(_v)
                            find_bag(_k, conveyor)
                        seen.append(_c)

    find_bag(bag_type, conveyor)
    print(seen)


if __name__ == "__main__":
    parsed = read_input("./sample.txt")
    # print(parsed)
    bags = containing_bags("shiny gold", parsed)
    # print(len(bags))
    c = count_contained_bags("shiny gold", parsed)
    print(c)
