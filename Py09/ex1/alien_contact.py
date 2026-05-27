from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def validate_business_rules(self) -> "AlienContact":
        # rule: id must start with AC
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')

        # rule 2: pyshical contact must be verified
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        # rule 3: telepathic requires >= witnesses
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )

        # rule 4: Strong signal 7> should include message
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print(30*"=")

    valid_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.fromisoformat("2026-05-25T17:00:00"),
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greeting from zeta Reticuli",
        is_verified=False,
    )

    print("Valid contacr report:")
    print(f"ID: {valid_contact.contact_id}")
    print(f"Type: {valid_contact.contact_type.value}")
    print(f"Location: {valid_contact.location}")
    print(f"Signal: {valid_contact.signal_strength}/10")
    print(f"Duration: {valid_contact.duration_minutes} minutes")
    print(f"Witnesses: {valid_contact.witness_count}")
    print(f"Message: {valid_contact.message_received!r}\n")
    print(30*"=")
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2026_999",
            timestamp=datetime.fromisoformat("2026-05-13T10:00:00"),
            location="Somewhere in the desert",
            contact_type=ContactType.telepathic,
            signal_strength=6.0,
            duration_minutes=30,
            witness_count=2,  # invalid (< 3 for telepathic)
            message_received=None,
            is_verified=False,
        )
    except ValidationError as e:
        msg = e.errors()[0].get("msg", "")
        if msg.startswith("Value error, "):
            msg = msg[len("Value error, "):]
        print(msg)


if __name__ == "__main__":
    main()
