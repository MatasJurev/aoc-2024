def read_lines(filename):
    return [i.replace("\n", "") for i in open(filename, "r").readlines()]
