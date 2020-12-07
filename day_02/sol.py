import re
from operator import itemgetter
from collections import Counter


def input_reader(filename="./input.txt"):
    """Read an input file into memory

    Example:
        2-8 t: pncmjxlvckfbtrjh
        => {'min': '2', 'max': '8', 'needle': 't', 'haystack': 'pncmjxlvckfbtrjh'}

    :return row: returns matched row as dict
    """
    pattern = r"(?P<min>\d+)-(?P<max>\d+)\s+(?P<needle>[a-z]{1}):\s+(?P<haystack>.+)"
    for row in open(filename, "r"):
        row = row.strip()
        matches = re.match(pattern, row)
        yield matches.groupdict()


def is_password_ok_per_policy_one(password_data):
    """Check if password respects defined policy

    The policy defines that the character should appear not more than max
    times and not less than min times in the password.

    :returns bool:
    """
    _max, _min, needle, haystack = itemgetter("max", "min", "needle", "haystack")(
        password_data
    )
    counts = Counter(haystack)
    needle_freq = counts.get(needle, 0)
    is_valid = needle_freq <= int(_max) and needle_freq >= int(_min)
    return is_valid


def is_password_ok_per_policy_two(password_data):
    """Check if password respects policy

    The policy defines that character should ONLY appear in either the first
    position or the second one and not both. The positions are not zero-based.

    :returns bool:
    """
    pos_1, pos_2, needle, haystack = itemgetter("min", "max", "needle", "haystack")(
        password_data
    )
    is_valid = False
    if (haystack[int(pos_1) - 1] == needle and haystack[int(pos_2) - 1] != needle) or (
        haystack[int(pos_1) - 1] != needle and haystack[int(pos_2) - 1] == needle
    ):
        is_valid = True
    print(is_valid, password_data)
    return is_valid


def process_passwords(policy, passwords=input_reader):
    count = 0
    for password in passwords():
        is_ok = policy(password)
        if is_ok:
            count += 1
    return count


if __name__ == "__main__":
    valid_count = process_passwords(is_password_ok_per_policy_one)
    print(valid_count)
    valid_count = process_passwords(is_password_ok_per_policy_two)
    print(valid_count)
