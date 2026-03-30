from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
from .Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===\n")

    print("Buiding deck with different card types...")
    spell = SpellCard("Lightning Bolt", 3, "Common", "damage")
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    artifact = ArtifactCard("Mana Crystal", 2, "Common", 5,
                            "Permanent: +1 mana per turn")

    deck = Deck()

    for type in spell, creature, artifact:
        deck.add_card(type)

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:\n")

    deck.shuffle()

    mana = 20

    for _ in range(len(deck.card_list)):
        draw_card = deck.draw_card()
        if isinstance(draw_card, CreatureCard):
            print(f"Drew: {draw_card.name} (Creature)")
        elif isinstance(draw_card, ArtifactCard):
            print(f"Drew: {draw_card.name} (Artifact)")
        elif isinstance(draw_card, SpellCard):
            print(f"Drew: {draw_card.name} (Spell)")
        else:
            print("Error: Could not find type of card")

        is_playable = draw_card.is_playable(mana)
        if is_playable:
            print(f"Play result: {draw_card.play({})}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
