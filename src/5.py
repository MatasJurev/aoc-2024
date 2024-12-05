import fileutils
#kairej didesnis uz desinej

def parse_data(lines):
    rules, pages = [], []

    for line in lines:
        if "|" in line:
            rules.append(tuple(int(i) for i in line.split("|")))
        if "," in line:
            pages.append([int(i) for i in line.split(",")])

    return rules, pages


def part_one():
    ans = 0
    rules, pages = parse_data(fileutils.read_lines("data/5.txt"))
    print(rules)
    print(pages)

    for page in pages:
        pi = page[0]
        good = True

        for i in range(1, len(page)):
            rule = ()
            for r in rules:
                if pi in r and i in r:
                    rule = r
                    break
            if :
                good = False
                break
            pi = i

        if good:
            ans += page[len(page)//2+1]

    print(ans)


def part_two():
    ans = 0
    lines = fileutils.read_lines("data/5.txt")


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
