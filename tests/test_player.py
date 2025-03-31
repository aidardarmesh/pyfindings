from src.laxleague.guardian import Guardian
from src.laxleague.player import Player


def test_construction():
    p = Player("Felicity", "Smith", 16)
    assert p.first_name == "Felicity"
    assert p.last_name == "Smith"
    assert p.jersey == 16
    assert [] == p.guardians


def test_add_guardian():
    g = Guardian("Mary", "Allen")
    p = Player("Felicity", "Smith", 16)
    p.add_guardian(g)
    assert [g] == p.guardians
