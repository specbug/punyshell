import sys


def main():
    sys.stdout.write("$ ")

    cmd = input()
    if cmd == "exit 0":
        exit(0)
    elif cmd.startswith("echo"):
        _, *args = cmd.split()
        print(" ".join(args))
    elif cmd.startswith("type"):
        if cmd == "type echo":
            print("echo is a shell builtin")
        elif cmd == "type exit":
            print("exit is a shell builtin")
        elif cmd == "type type":
            print("type is a shell builtin")
        else:
            print(f"{cmd}: not found")

    else:
        print(f"{cmd}: command not found")
    main()


if __name__ == "__main__":
    main()
