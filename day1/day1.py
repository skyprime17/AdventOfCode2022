def main():
    with open("day1.txt", 'r') as file:
        xs = [x.rstrip() for x in file.readlines()]
        print(xs)

    current_elf = 0
    result = []

    for calorie in xs:
        if not calorie:
            result.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(calorie)

    print(max(result))
    result.sort()
    print(sum(result[-3:]))

if __name__ == "__main__":
    main()
