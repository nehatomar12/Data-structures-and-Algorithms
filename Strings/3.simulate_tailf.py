"""
Print last k lines from a file

"""

def tailf(k, file_path):
    with open(file_path) as fd:
        lines = fd.readlines()
        start = 0
        end = k
        while end < len(lines):
            start += 1
            end += 1
        for i in range(start, end):
            print(lines[i])

if __name__ == "__main__":
    tailf(k=4, file_path="./data_set/input.txt")