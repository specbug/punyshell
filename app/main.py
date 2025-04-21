import sys


def main():
    sys.stdout.write("$ ")

    cmd = input()
    if cmd == "exit":
        sys.exit(0)
    print(f"{cmd}: command not found")
    main()


if __name__ == "__main__":
    main()
