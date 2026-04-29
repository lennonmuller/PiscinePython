import sys
import os
import site


def in_virtualenv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    print("Welcome to the construct")

    if not in_virtualenv():
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Enviroment: None detected\n")
        print("WARNING: You're in the global enviroment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
        return

    env_path = sys.prefix
    env_name = os.path.basename(env_path)

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Enviroment: {env_name}")
    print(f"Environmental path: {env_path}")
    print("\nSUCCESS: You're in a isolated enviroment!")
    print("Safe to install packages without affecting the global system.\n")
    print("Package installation path:")
    for p in site.getsitepackages():
        print(p)


if __name__ == "__main__":
    main()
