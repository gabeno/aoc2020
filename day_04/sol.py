import re

REQUIRED_FIELDS = set(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
OPTIONAL_FIELDS = ("cid")

def read_input(file_path=".input.txt/"):
    lines = open(file_path).readlines()
    passports = []
    passport = ""
    for idx, line in enumerate(lines):
        if len(line.strip()):
            passport += line
            if idx == len(lines) - 1:
                passports.append(passport)
        else:
            passports.append(passport)
            passport = ""

    passports = [p.replace("\n", " ").strip() for p in passports]
    #print(passports)
    return passports

def count_valid(passports, validator):
    r = [validator(p.split(" ")) for p in passports]
    # print(r)
    return r.count(True)

def is_valid(p):
    """Check valid passports

    Valid passports must have fields: byr, iyr, eyr, hgt, hcl, ecl, pid
    and optionally cid
    """
    fields = set()
    [fields.add(f.split(":")[0]) for f in p if f.split(":")[0] not in OPTIONAL_FIELDS]
    return len(fields & REQUIRED_FIELDS) == len(REQUIRED_FIELDS)

def is_valid_strict(p):
    """Check valid passports

    Valid passports must have fields: byr, iyr, eyr, hgt, hcl, ecl, pid
    and optionally cid

    field validation rules:
        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.
    """
    field_validators = {
        "byr": lambda v: len(v) == 4 and 1920 <= int(v) <= 2002,
        "iyr": lambda v: len(v) == 4 and 2010 <= int(v) <= 2020,
        "eyr": lambda v: len(v) == 4 and 2020 <= int(v) <= 2030,
        "hgt": lambda v: int(v.replace("cm", "")) <= 193 and int(v.replace("cm", "")) >= 150 if "cm" in v else int(v.replace("in", "")) <= 76 and int(v.replace("in", "")) >= 59,
        "hcl": lambda v: bool(re.match(r"^#[a-f0-9]{6}$", v)),
        "ecl": lambda v: v in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
        "pid": lambda v: bool(re.match(r"^[0-9]{9}$", v)),
    }
    valid = all([field_validators[f.split(":")[0]](f.split(":")[1]) for f in p if f.split(":")[0] not in OPTIONAL_FIELDS])
    # print(field_validators['hgt']('76in'))
    return valid and is_valid(p)


if __name__ == "__main__":
    passports = read_input("./input.txt")
    count = count_valid(passports, is_valid)
    print(count)

    passports = read_input("./input.txt")
    count = count_valid(passports, is_valid_strict)
    print(count)
