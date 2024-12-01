def read_data(filename):
    return [i.replace("\n", "") for i in open(filename, "r").readlines()]
