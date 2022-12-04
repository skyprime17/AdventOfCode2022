def main():
    xs = [x.strip() for x in open("day4.txt")]
    print(xs)
    count = 0
    for elfPair in xs:
        left, right = elfPair.split(",")
        left_min, left_max = left.split("-")
        right_min, right_max = right.split("-")
        if (int(left_min) >= int(right_min) and int(left_max) <= int(right_max)) or (
                int(left_max) >= int(right_max) and int(left_min) <= int(right_min)):
            count += 1
    print(count)

def main2():
    xs = [x.strip() for x in open("day4.txt")]

    print(xs)
    count = 0
    for elfPair in xs:
        left, right = elfPair.split(",")
        left_min, left_max = left.split("-")
        right_min, right_max = right.split("-")
        if int(left_max) >= int(right_min) and int(right_max) >= int(left_min):
            count += 1
    print(count)

if __name__ == "__main__":
    main()
    main2()
