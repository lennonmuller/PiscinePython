from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int):
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int):
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int):
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int):
        results = []
        for s in spells:
            results.append(s(target, power))
        return results
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} with {power} power"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def lightning(target: str, power: int) -> str:
    return f"Lightning shocks {target} for {power} damage"


def strong_enough(target: str, power: int) -> bool:
    return power >= 50


def main():
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print("Combined spell result:", combined("Dragon", 40))
    print()

    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print("Original:", fireball("Orc", 10))
    print("Amplified:", mega_fireball("Orc", 10))
    print()

    print("Testing conditional caster...")
    conditional_fireball = conditional_caster(strong_enough, fireball)
    print(conditional_fireball("Goblin", 20))
    print(conditional_fireball("Goblin", 80))
    print()

    print("Testing spell sequence...")
    seq = spell_sequence([fireball, heal, lightning])
    print(seq("Troll", 30))
    print()


if __name__ == "__main__":
    main()
