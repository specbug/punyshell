import sys


def main():
    sys.stdout.write("$ ")

    cmd = input()
    if cmd == "exit 0":
        exit(0)
    elif cmd.startswith("echo"):
        _, *args = cmd.split()
        print(" ".join(args))
    else:
        print(f"{cmd}: command not found")
    main()


if __name__ == "__main__":
    main()
