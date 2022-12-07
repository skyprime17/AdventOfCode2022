from collections import defaultdict
from typing import List


def main():
    xs = [x.strip() for x in open("day7.txt")]

    filesystem = {}
    current_path: List[str] = []

    for log in xs:
        if log.startswith("$ ls"):
            continue
        if log.startswith("$ cd"):
            prefix, cmd, dirname = log.split()
            if dirname != "..":
                current_path.append(dirname + " ")
            if dirname == "..":
                current_path.pop()
        if not log.startswith("$") and not log.startswith("dir"):
            file_size, file_name = log.split()
            filesystem["".join(current_path) + file_name] = int(file_size)

    directories = defaultdict(int)

    for key in filesystem:
        for idx, _ in enumerate(key.split()[:-1]):
            directories["".join(key.split()[:idx + 1])] += filesystem[key]

    print(directories)
    print("Result 1 ", sum(filter(lambda x: x <= 100_000, directories.values())))


def main2():
    xs = [x.strip() for x in open("day7.txt")]

    filesystem = {}
    current_path: List[str] = []

    for log in xs:
        if log.startswith("$ ls"):
            continue
        if log.startswith("$ cd"):
            prefix, cmd, dirname = log.split()
            if dirname != "..":
                current_path.append(dirname + " ")
            if dirname == "..":
                current_path.pop()
        if not log.startswith("$") and not log.startswith("dir"):
            file_size, file_name = log.split()
            filesystem["".join(current_path) + file_name] = int(file_size)

    directories = defaultdict(int)

    for key in filesystem:
        for idx, _ in enumerate(key.split()[:-1]):
            directories["".join(key.split()[:idx + 1])] += filesystem[key]

    print(directories)
    root = max(directories.values())
    print("Result 2 ", min(list(filter(lambda x: (70000000 - root + x) >= 30000000, directories.values()))))


if __name__ == "__main__":
    main()
    main2()
