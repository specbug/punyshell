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
        _, *args = cmd.split()
        sh_builtin = args[0] if args else ""
        if sh_builtin == "echo":
            print("echo is a shell builtin")
        elif sh_builtin == "exit":
            print("exit is a shell builtin")
        elif sh_builtin == "type":
            print("type is a shell builtin")
        else:
            print(f"{sh_builtin}: not found")

    else:
        print(f"{cmd}: command not found")
    main()


if __name__ == "__main__":
    main()
