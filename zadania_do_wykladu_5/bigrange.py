import sys


def generate_and_sum(n):
    summed = sum(range(1, n + 1))
    print("Suma liczb: ", summed)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        generate_and_sum(n)
    except ValueError:
        sys.exit(1)
