

lines_seen = set()
with open("./data_set/input.txt") as f:
    for line in f.readlines():
        if line not in lines_seen:
            lines_seen.add(line)

print(lines_seen)