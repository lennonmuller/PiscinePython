import functools
import time
from typing import Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        timer = time.perf_counter() - start
        print(f"Spell completed in {timer:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                power = next(
                    (arg for arg in args if isinstance(arg, int)), None
                    )
            if power is None or power < min_power:
                return ("Insufficient power for this spell")
            return (func(*args, **kwargs))
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"attempt {attempt}/{max_attempts}")
            return (f"Spell casting failed after {max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return (all(char.isalpha() or char.isspace() for char in name))

    @power_validator(6)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power")


@spell_timer
def fireball(target: str) -> str:
    time.sleep(0.1)
    return f"Fireball cast on {target}!"


@retry_spell(max_attempts=3)
def unstable_spell() -> str:
    raise RuntimeError("Spell failed")


@retry_spell(max_attempts=3)
def stable_spell() -> str:
    return ("Waaaaaaagh spelled !")


def main() -> None:
    print("Testing spell timer...")
    result = fireball("Goblin")
    print("Result:", result)
    print()

    print("Testing retrying spell...")
    print(unstable_spell())
    print()
    print(stable_spell())
    print()

    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("A1"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
