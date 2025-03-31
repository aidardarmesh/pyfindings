import dataclasses

from src.laxleague.guardian import Guardian


@dataclasses.dataclass
class Player:
    first_name: str
    last_name: str
    jersey: int
    guardians: list[Guardian] = dataclasses.field(default_factory=list)

    def add_guardian(self, guardian: Guardian):
        self.guardians.append(guardian)
