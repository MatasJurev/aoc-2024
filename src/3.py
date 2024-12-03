import fileutils
import re


def part_one():
    inp = ""
    lines = fileutils.read_lines("data/3.txt")
    for line in lines:
        inp += line
    
    matches = re.findall(r'mul\((\d+),(\d+)\)', inp)
    print(sum(int(x) * int(y) for x, y in matches))


def part_two():
    lines = fileutils.read_lines("data/3.txt")


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
