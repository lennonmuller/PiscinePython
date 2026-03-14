if __name__ == "__main__":
    classified_path = '../data-generator-tools/classified_data.txt'
    security_path = '../data-generator-tools/security_protocols.txt'

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initialing secure vault access...")
    try:
        with open(classified_path, 'r') as file:
            print("Vault connection established with failsafe protocols")

            print("\nSECURITY EXTRACTION:")
            print(file.read())

        with open(security_path, 'r') as file:
            print("\nSECURE PRESERVATION:")
            print(file.read())

        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")

    except FileNotFoundError:
        print("\nERROR: File not found.")
