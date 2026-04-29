import sys
import importlib


def check_dependency(name: str):
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - Ready")
        return module
    except ImportError:
        print(f"[MISSING] {name} - Not installed")
        print("Install with pip: pip install -r requirements.txt")
        print(f"Install with poetry: poetry add {name}")
        return None


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")

    pandas = check_dependency("pandas")
    numpy = check_dependency("numpy")
    matplotlib = check_dependency("matplotlib")
    requests = check_dependency("requests")

    if not all([pandas, numpy, matplotlib, requests]):
        print("\nMissing required dependencies. Install them and try again.")
        return
    
    