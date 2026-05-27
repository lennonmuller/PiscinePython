from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Any


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    capitain = "capitain"
    commander = "commander"


class CrewMember(BaseModel):
    number_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)


@model_validator(mode="after")
def validation_rules(self) -> "SpaceMission":
    if not self.mission_id.startwith("M"):
        raise ValueError('Mission ID must start with "M".')
    cap_or_com = {Rank.capitain, Rank.commander}
    if not any(m.rank in cap_or_com for m in self.crew):
        raise ValueError('Must have at least one Commander or Captain.')
    if self.duration_days > 365:
        experienced = sum(1 for m in self.crew if m.years_experience >= 5)
        ratio = experienced / len(self.crew)
        if ratio < 0.5:
            raise ValueError(
                "Long missions (365+ days) need 50% experienced crew"
                )
    inactive = [m.name for m in self.crew if not self.is_active]
    if inactive:
        raise ValueError(
            "All crew members must be active."
        )
    return self


def main() -> None:
    print("Space Mission Crew Validation")
    print(30*"=")

    valid_mission = SpaceMission(
        mission_id="M2024_TITAN",
        mission_name="Solar Observatory Research Mission",
        destination="Solar Observatory",
        launch_date="2024-03-30T00:00:00",
        duration_days=451,
        crew=[
            CrewMember(
                number_id="CM001",
                name="Sarah Williams",
                rank="capitain",
                age=43,
                specialization="Mission Command",
                years_experience=19,
                is_active=True
            ),
            CrewMember(
                number_id="CM002",
                name="Juninho cancelado",
                rank="cadet",
                age=43,
                specialization="cancelado",
                years_experience=30,
                is_active=True
            ),
            CrewMember(
                number_id="CM004",
                name="David Smith",
                rank="commander",
                age=27,
                specialization="Security",
                years_experience=15,
                is_active=True
            )
        ],
        mission_status="planned",
        budget_millions=2208.1
    )

    print("Valid Mission Created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: {valid_mission.budget_millions}")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    for m in valid_mission.crew:
        print(f"- {m.name} ({m.rank}) - {m.specialization}")
    print(30*"=")

    print("Expected validation error:")
    try:
        valid_mission = SpaceMission(
            mission_id="M2024_INVALID",
            mission_name="Solar Observatory Research Mission",
            destination="Solar Observatory",
            launch_date="2024-03-30T00:00:00",
            duration_days=451,
            crew=[
                CrewMember(
                    number_id="MD005",
                    name="Sei la",
                    rank="cadet",
                    age=43,
                    specialization="Mission Command",
                    years_experience=19,
                    is_active=False
                )
            ],
            mission_status="planned",
            budget_millions=2208.1
        )
    except ValidationError as e:
        msg = e.errors()[0].get("msg", "")
        if msg.startswith("Value error, "):
            msg = msg[len("Value error, "):]
        print(msg)


if __name__ == "__main__":
    main()
