if __name__ == "__main__":
    file_path = 'data-generator-tools/ancient_fragmen.txt'

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {file_path}")
    try:
        with open(file_path, 'r') as file:
            print("Connection established...")
            print("\nRECOVERED DATA:")
            print(f"{file.read()}")
            print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("\nERROR: Storage vault not found. Run data_generator.py"
              " and then recovery data.")
