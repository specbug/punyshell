import sys


def main():
    sys.stdout.write("$ ")

    cmd = input()
    print(f"{cmd}: command not found")
    main()


if __name__ == "__main__":
    main()
