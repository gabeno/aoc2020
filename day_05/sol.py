import math


def read_boarding_passes(filepath="./input.txt"):
    with open(filepath, "r") as f:
        return map(lambda x: x.strip(), f.readlines())


def get_seat_id(boarding_pass):
    assert len(boarding_pass) == 10
    row = boarding_pass[:8]
    col = boarding_pass[-3:]

    def search_row(row, low, high):
        if len(row) == 1:
            if row[0] == "F":
                return min(low, high)
            return max(low, high)
        midpoint = math.ceil((high - low) / 2)
        # print(row, low, high, midpoint)
        if row[0] == "F":
            return search_row(row[1:], low, high - midpoint)
        elif row[0] == "B":
            return search_row(row[1:], low + midpoint, high)

    def search_col(col, low, high):
        if len(col) == 1:
            if col[0] == "R":
                return max(low, high)
            return min(low, high)

        midpoint = math.ceil((high - low) / 2)
        # print(col, low, high, midpoint)
        if col[0] == "L":
            return search_col(col[1:], low, high - midpoint)
        elif col[0] == "R":
            return search_col(col[1:], low + midpoint, high)

    row = search_row(row, 0, 127)
    col = search_col(col, 0, 7)
    # print(row, col)
    return row * 8 + col


def get_seat(seat_ids):
    sorted_ids = sorted(seat_ids)
    all_seats = list(range(sorted_ids[0], sorted_ids[-1] + 1))
    # print(len(sorted_ids))
    # print(len(all_seats))
    return set(sorted_ids) ^ set(all_seats)


if __name__ == "__main__":
    passes = read_boarding_passes()
    # print(passes)
    seat_ids = [get_seat_id(_pass) for _pass in passes]
    max_seat = max(seat_ids)
    print(max_seat)
    my_seat = get_seat(seat_ids)
    print(my_seat)
