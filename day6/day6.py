def main():
    xs = [x.strip() for x in open("day6.txt")][0]
    print(xs)
    for idx,pack in enumerate(xs):
        packet = list(xs[idx:idx+14:])
        if len(packet) == len(set(packet)):
            print(idx+14)
            break


if __name__ == "__main__":
    main()