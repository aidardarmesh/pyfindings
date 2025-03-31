import dataclasses

from src.laxleague.guardian import Guardian


@dataclasses.dataclass
class Player:
    first_name: str
    last_name: str
    jersey: int
    guardians_list: list[Guardian] = dataclasses.field(default_factory=list)

    def add_guardian(self, guardian: Guardian):
        self.guardians_list.append(guardian)

    def add_guardians(self, guardians: list[Guardian]):
        self.guardians_list.extend(guardians)

    @property
    def primary_guardian(self):
        return self.guardians_list[0]
