import fileutils


def parse_data(lines):
    return [list(map(int, line.split())) for line in lines]


def is_safe(curr, next):
    return 0 < abs(next-curr) < 4


def part_one():
    ans = 0
    data = parse_data(fileutils.read_lines("data/2.txt"))
    
    for nums in data:
        sort_nums = sorted(nums)

        if all(is_safe(x, y) for x, y in zip(nums, nums[1:])) and (nums==sort_nums or nums==sort_nums[::-1]):
            ans+=1

    print(ans)


def part_two():
    ans = 0
    data = parse_data(fileutils.read_lines("data/2.txt"))
    
    for nums in data:
        for i in range(len(nums)):
            temp = nums[:i] + nums[i+1:]
            sort_temp = sorted(temp)

            if all(is_safe(x, y) for x, y in zip(temp, temp[1:])) and (temp==sort_temp or temp==sort_temp[::-1]):
                ans+=1
                break

    print(ans)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
