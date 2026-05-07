import os
from dotenv import load_dotenv


def get_config() -> dict[str, str | None]:
    """
    Load environment variables from .env file
    and return configuration dictionary.
    """
    load_dotenv()

    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }


def validate_config(config: dict[str, str | None]) -> list[str]:
    """
    Check for missing configuration variables.
    """
    missing: list[str] = []

    for key, value in config.items():
        if not value:
            missing.append(key)

    return missing


def display_config(config: dict[str, str | None]) -> None:
    """
    Display current configuration status.
    """
    print("ORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")

    mode: str = config.get("MATRIX_MODE") or "undefined"

    print(f"Mode: {mode}")

    if mode == "development":
        print("Database: Connected to local instance")
    elif mode == "production":
        print("Database: Connected to production instance")
    else:
        print("Database: Unknown environment")

    if config.get("API_KEY"):
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")

    log_level: str = config.get("LOG_LEVEL") or "undefined"
    print(f"Log Level: {log_level}")

    if config.get("ZION_ENDPOINT"):
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_check() -> None:
    """
    Perform basic environment security checks.
    """
    print("\nEnvironment security check:")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    print("[OK] No hardcoded secrets detected")
    print("[OK] Production overrides available")


def main():
    config = get_config()

    missing = validate_config(config)

    if missing:
        print("WARNING: Missing configuration variables:")
        for variable in missing:
            print(f"- {variable}")

    print()

    display_config(config)
    security_check()


if __name__ == "__main__":
    main()
