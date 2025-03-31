import pytest

from src.laxleague.guardian import Guardian
from src.laxleague.player import Player


@pytest.fixture
def player_one() -> Player:
    return Player("Felicity", "Smith", 16)


@pytest.fixture
def guardians_list() -> list[Guardian]:
    g1 = Guardian("Mary", "Allen")
    g2 = Guardian("John", "Smith")
    g3 = Guardian("Jennifer", "Smith")
    return [g1, g2, g3]
