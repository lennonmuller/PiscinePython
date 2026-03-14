def handle_crisis(file_x: str) -> None:
    print(f"CRISIS ALERT: Attempting access to {file_x}...")
    try:
        with open(file_x, 'r') as file:
            print((f"SUCCESS: Archive recevered - \"{file.read().strip()}\""))
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    finally:
        print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    files = ['../lost_archive.txt',
             '../data-generator-tools/classified_data.txt',
             '../data-generator-tools/standard_archive.txt']

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    for file in files:
        handle_crisis(file)
