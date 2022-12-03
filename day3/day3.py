from collections import defaultdict


def main():
    with open("day3.txt", 'r') as file:
        xs = [x.strip() for x in file.readlines()]

    result_dict = defaultdict(int)
    for bagpack in xs:
        half = int(len(bagpack) / 2)
        left = set(bagpack[:half])
        right = set(bagpack[half:])
        result_dict[left.intersection(right).pop()] += 1

    prio_sum = 0
    for k, v in result_dict.items():
        if k >= 'a':
            prio_sum += v * (ord(k) - ord('a') + 1)
            print(k, ord(k) - ord('a') + 1)
        else:
            prio_sum += v * (ord(k) - ord('A') + 27)
            print(k, ord(k) - ord('A') + 27)

    print(prio_sum)


def main2():
    with open("day3.txt", 'r') as file:
        xs = [x.strip() for x in file.readlines()]

    prio_sum = 0
    three_elves = []
    for bagpack in xs:
        three_elves.append(bagpack)
        if len(three_elves) == 3:
            xy = set(three_elves[0]) & set(three_elves[1]) & set(three_elves[2])
            k = xy.pop()
            if k >= 'a':
                prio_sum += (ord(k) - ord('a') + 1)
                print(k, ord(k) - ord('a') + 1)
            else:
                prio_sum += (ord(k) - ord('A') + 27)
                print(k, ord(k) - ord('A') + 27)
            three_elves = []
    print(prio_sum)


if __name__ == "__main__":
    main2()
