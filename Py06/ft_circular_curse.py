from alchemy.grimoire import record_spell, validate_ingredients


if __name__ == "__main__":
    print("\n=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    print("validade_ingedients(\"fire_air\"): "
          f"{validate_ingredients('fire air')}")
    print("validate_ingedients(\"dragon scales\"): "
          f"{validate_ingredients('dragon scales')}")

    print("\nTesting spell recording with validation:")
    print("record_spell(\"Fireball\", \"fire air\"): "
          f"{record_spell('Fireball', 'fire air')}")
    print("record_spell(\"Dark Magic\", \"shadow\"): "
          f"{record_spell('Dark Magic', 'shadow')}")

    print("\nTesting late import technique:")
    print("record_spell(\"Lightning\", \"air\"): "
          f"{record_spell('Lightning', 'air')}")

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")
