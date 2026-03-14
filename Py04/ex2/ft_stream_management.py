import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    try:
        archivist_id = input("Input Stream active. Enter archvist ID: ")
        status = input("Input Stream active. Enter status report: ")

        sys.stdout.write(f"\n[STANDARD] Archive status from {archivist_id}: "
                         f"{status}")
        sys.stderr.write("\n[ALERT] System diagnostic: "
                         "Communication channels verified")
        sys.stdout.write("\n[STANDARD] Data transmission complete\n")

    except ValueError:
        sys.stdout.write("\nERROR: Communication failed")
    finally:
        sys.stdout.write("\nThree-channel communitcation test successful.")
