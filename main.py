from polynomial import Polynomial


def main():
    p1 = Polynomial([1])
    p2 = Polynomial([6, 7, 5, 1, 1])
    # print(p1 + p2)
    # print(1 + p2)
    # print(p1 + 1)
    # print(1 + p1)
    # print(p1 - 1)
    # print(1 - p1)
    # print(p1 - p2)
    d = {x: x * 2 for x in range(1, 10)}
    print(d)
    print(d.values())
    d = sorted(d.items(), key=lambda x: x[0], reverse=True)
    d = [x[1] for x in d]
    print(d)


if __name__ == "__main__":
    main()
