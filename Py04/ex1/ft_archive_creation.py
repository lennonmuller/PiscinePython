def ft_archive_creation() -> None:
    file_path = 'data-generator-tools/new_discovery.txt'
    file_name = 'new_discovery.txt'
    text = ("[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee\n")

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    if file_path:
        print(f"Initializing new storage unit: {file_name}")
        try:
            with open(file_path, 'w') as file:
                print("Storage created successfully...\n")
                print("Inscribing preservation data...")
                file.write(text)

            with open(file_path, 'r') as file:
                print(f"{file.read()}")

            print("Data inscription complete. Storage unit sealed.")
            print(f"Archive {file_name} ready for long-term preservation.")
        except FileExistsError:
            print("ERROR: Data inscription failed. Try again")


if __name__ == "__main__":
    ft_archive_creation()
