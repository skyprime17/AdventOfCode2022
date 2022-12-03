def main():
    with open("day2.txt", 'r') as file:
        xs = [x.strip() for x in file.readlines()]
        print(xs)

    ways = {
        "X": 1,  # rock
        "Y": 2,  # paper
        "Z": 3  # scissor
    }

    result = 0

    for round_ in xs:
        match_count = 0
        match = round_.split(" ")
        match_count += ways.get(match[1])

        if match[1] == "X" and match[0] == "A":
            match_count += 3
        elif match[1] == "X" and match[0] == "C":
            match_count += 6
        elif match[1] == "Y" and match[0] == "A":
            match_count += 6
        elif match[1] == "Y" and match[0] == "B":
            match_count += 3
        elif match[1] == "Z" and match[0] == "B":
            match_count += 6
        elif match[1] == "Z" and match[0] == "C":
            match_count += 3
        result += match_count

    print(result)


def main2():
    with open("day2.txt", 'r') as file:
        xs = [x.strip() for x in file.readlines()]
        print(xs)

    ways = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    decision2 = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }

    result = 0

    for round_ in xs:
        match_count = 0
        match = round_.split(" ")
        match_count += decision2.get(match[1])
        decision = match[1]
        if decision == "X" and match[0] == "A":
            match_count += 3
        elif decision == "X" and match[0] == "B":
            match_count += 1
        elif decision == "X" and match[0] == "C":
            match_count += 2
        if decision == "Z" and match[0] == "A":
            match_count += 2
        elif decision == "Z" and match[0] == "B":
            match_count += 3
        elif decision == "Z" and match[0] == "C":
            match_count += 1
        elif decision == "Y":
            match_count += ways.get(match[0])
        result += match_count


    print(result)


if __name__ == "__main__":
    main2()
