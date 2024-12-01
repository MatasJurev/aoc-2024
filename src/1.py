import fileutils


def part_two():
    data = fileutils.read_data("data/1.txt")
    list1, list2 = [], []

    for line in data:
        line = line.split()
        list1.append(int(line[0]))
        list2.append(int(line[1]))

    sim_score = sum([list1[i]*list2.count(list1[i]) for i in range(len(list1))])
    print(sim_score)


def part_one():
    data = fileutils.read_data("data/1.txt")
    list1, list2 = [], []

    for line in data:
        line = line.split()
        list1.append(int(line[0]))
        list2.append(int(line[1]))

    list1.sort()
    list2.sort()

    sum_dist = sum([abs(list1[i]-list2[i]) for i in range(len(list1))])
    print(sum_dist)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
