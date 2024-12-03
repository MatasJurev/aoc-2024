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
    inp = ""
    for line in fileutils.read_lines("data/3.txt"):
        inp += line
    
    matches = re.findall(r'(mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))', inp)
    ans = 0
    mul_enabled = True

    for match in matches:
        for el in match:
            if 'mul' in el and mul_enabled:
                a, b = map(int, el.replace("mul(", "").replace(")", "").split(","))
                ans += a * b
                break
            elif el == "do()":
                mul_enabled = True
                break
            elif el == "don't()":
                mul_enabled = False
                break
    
    print(ans)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
