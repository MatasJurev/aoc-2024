import fileutils


def part_one():
    lines = fileutils.read_lines("data/4.txt")
    n = len(lines) # Both x and y are 140
    print(lines, n)
    print(lines[139][139])
    word = ""
    total = 0

    #construct a string of 4 adjacent elements either horizontally, vertically or diagonally
    for i in range(n):
        for j in range(n):
            #horizontal
            if j < n - 3:
                word = lines[i][j:j+4]
            #vertical
            if i < n - 3:
                word = lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j]
            #diagonal
            if i < n - 3 and j < n - 3:
                word = lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3]
            if i < n - 3 and j > 2:
                word = lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3]
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
