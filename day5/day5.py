"""
[V]     [B]                     [F]
[N] [Q] [W]                 [R] [B]
[F] [D] [S]     [B]         [L] [P]
[S] [J] [C]     [F] [C]     [D] [G]
[M] [M] [H] [L] [P] [N]     [P] [V]
[P] [L] [D] [C] [T] [Q] [R] [S] [J]
[H] [R] [Q] [S] [V] [R] [V] [Z] [S]
[J] [S] [N] [R] [M] [T] [G] [C] [D]
Crates removed from day5.txt :/
"""

crates_string = [
    "JHPMSFNV",
    "SRLMJDQ",
    "NQDHCSWB",
    "RSCL",
    "MVTPFB",
    "TRQNC",
    "GVR",
    "CZSPDLR",
    "DSJVGPBF"
]

def main():
    crates = [list(x) for x in crates_string]
    xs = [x.strip() for x in open("day5.txt")]

    for instruction in xs:
        split_inst = instruction.split()
        move_, from_, to_ = int(split_inst[1]), int(split_inst[3]), int(split_inst[5])

        for i in range(move_):
            crates[to_ - 1].append(crates[from_ - 1].pop())
    print("".join([x.pop() for x in crates]))


def main2():
    crates = [list(x) for x in crates_string]
    xs = [x.strip() for x in open("day5.txt")]

    for instruction in xs:
        split_inst = instruction.split()
        move_, from_, to_ = int(split_inst[1]), int(split_inst[3]), int(split_inst[5])

        crates[to_ - 1] += crates[from_ - 1][-move_:]
        for i in range(move_):
            crates[from_ - 1].pop()

    print("".join([x.pop() for x in crates]))


if __name__ == "__main__":
    main()
    main2()
