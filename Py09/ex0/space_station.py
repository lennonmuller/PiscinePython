from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print(30*"=")

    valid_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.fromisoformat("2026-05-24T14:30:00"),
        is_operational=True,
        notes="Nominal operation",
    )

    print("Valid station created:")
    print(f"ID: {valid_station.station_id}")
    print(f"Name: {valid_station.name}")
    print(f"Crew: {valid_station.crew_size} people")
    print(f"Power: {valid_station.power_level}%")
    print(f"Oxygen: {valid_station.oxygen_level}%")
    print(
        "Status:", "Operational\n"
        if valid_station.is_operational else "Not operational"
    )
    print(20*"=")

    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="BADID01",
            name="International Space Station",
            crew_size=20,
            power_level=185.5,  # invalid (> 100)
            oxygen_level=92.3,
            last_maintenance=datetime.fromisoformat("2026-05-24T14:30:00"),
        )
    except ValidationError as e:
        msg = e.errors()[0].get("msg", "")
        if msg.startswith("Value error, "):
            msg = msg[len("Value error, "):]
        print(msg)


if __name__ == "__main__":
    main()
