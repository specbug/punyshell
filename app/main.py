import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")

    # Wait for user input
    while True:
        cmd = input()
        print(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
