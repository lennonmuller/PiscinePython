from typing import Callable, Any
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == "add":
        return functools.reduce(operator.add, spells)
    if operation == "multiply":
        return functools.reduce(operator.mul, spells)
    if operation == "max":
        return functools.reduce(lambda a, b: a if a > b else b, spells)
    if operation == "min":
        return functools.reduce(lambda a, b: a if a < b else b, spells)
    raise ValueError(f"Can't handle operation: {operation}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire = functools.partial(base_enchantment, 50, "Fire")
    water = functools.partial(base_enchantment, 50, "Water")
    darkmagic = functools.partial(base_enchantment, 50, "DarkMagic")
    return {"fire": fire, "water": water, "darkmagic": darkmagic}


def base_enchantment(power: int, element: str, target: str) -> str:
    return (
        element + " enchantment hits " + target + " with "
        + str(power) + " power"
    )


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci cant be negative")
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispactcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispactcher.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispactcher.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispactcher.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispactcher


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print()

    print("Testing memoized fibonacci...")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
    print()

    print("Testing spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch([1, 2, 3]))
    print(dispatch({"x": 1}))
    print()

    print("Testing partial enchanter...")
    enchants = partial_enchanter(base_enchantment)
    print(enchants["fire"]("Sword"))
    print(enchants["water"]("Shield"))


if __name__ == "__main__":
    main()
