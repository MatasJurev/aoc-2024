import fileutils


def part_one():
    lines = fileutils.read_lines("data/4simple.txt")
    n = 4
    total = 0
    len_lines = len(lines)
    print(lines)

    #construct a string of 4 adjacent elements either horizontally, vertically or diagonally
    # for i in range(len_lines):
    #     for j in range(len_lines):
    #         words = []
    #         #horizontal
    #         words.append(lines[i][j:j+4])
    #         #vertical
    #         words.append(lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j])
    #         #diagonal
    #         words.append(lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3])
    #         words.append(lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3])
            
    #         for word in words:
    #             if word == "XMAS" or word == "SAMX":
    #                 total += 1

    for i in range(len_lines):
        for j in range(len_lines):
            words = []
            # Horizontal
            if j + n <= len_lines:
                words.append([lines[i][j + i] for i in range(n)])
            # Vertical
            if i + n <= len_lines:
                words.append([lines[i + i][j] for i in range(n)])
            # Diagonal (down-right)
            if i + n <= len_lines and j + n <= len_lines:
                words.append([lines[i + i][j + i] for i in range(n)])
            # Diagonal (up-right)
            if i - n + 1 >= 0 and j + n <= len_lines:
                words.append([lines[i - i][j + i] for i in range(n)])
            
            for word in words:
                word = ''.join(word)
                if word == "XMAS" or word == "SAMX":
                    total += 1

    print(total)


def part_two():
    lines = fileutils.read_lines("data/4.txt")


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
