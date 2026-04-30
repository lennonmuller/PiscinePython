import importlib


REQUIRED_LIBS = ["pandas", "numpy", "matplotlib", "requests"]


def check_dependencies():
    print("Checking dependencies:\n")

    available = {}

    for lib in REQUIRED_LIBS:
        try:
            module = importlib.import_module(lib)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {lib} ({version})")
            available[lib] = module
        except ImportError:
            print(f"[MISSING] {lib}")
            available[lib] = None

    return available


def show_install_instructions():
    print("\nTo install dependencies:\n")

    print("Using pip:")
    print("pip install -r requirements.txt\n")

    print("Using Poetry:")
    print("poetry install\n")


def analyze_data(modules):
    np = modules["numpy"]
    pd = modules["pandas"]
    plt = importlib.import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")

    data = np.random.rand(1000)

    df = pd.DataFrame(data, columns=["values"])

    print(f"Processing {len(df)} data points...")

    plt.figure()
    plt.hist(df["values"], bins=30)
    plt.title("Matrix Data Distribution")

    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    print("LOADING STATUS: Loading programs...\n")

    modules = check_dependencies()

    if any(modules[lib] is None for lib in ["pandas", "numpy", "matplotlib"]):
        print("\nSome required dependencies are missing!")
        show_install_instructions()
        return

    analyze_data(modules)


if __name__ == "__main__":
    main()
