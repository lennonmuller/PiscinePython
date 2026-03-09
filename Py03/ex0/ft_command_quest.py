import sys


def main() -> None:
    print("=== Command Quest ===")

    args = sys.argv
    program_name = args[0]
    arg_v = args[1:]

    if len(arg_v) == 0:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {len(args)}")
        return

    print(f"Program name: {program_name}")
    print(f"Arguments received: {len(arg_v)}")

    i = 1
    for arg in arg_v:
        print(f"Argument {i}: {arg}")
        i += 1

    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    main()
