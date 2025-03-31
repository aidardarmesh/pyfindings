import pytest

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


def test_guardians():
    p = Player("Felicity", "Smith", 16)
    g1 = Guardian("Mary", "Allen")
    p.add_guardians([g1])
    g2 = Guardian("John", "Smith")
    g3 = Guardian("Jennifer", "Smith")
    p.add_guardians([g2, g3])
    assert [g1, g2, g3] == p.guardians


def test_primary_guardian():
    p = Player("Felicity", "Smith", 16)
    g1 = Guardian("Mary", "Allen")
    p.add_guardians([g1])
    g2 = Guardian("John", "Smith")
    g3 = Guardian("Jennifer", "Smith")
    p.add_guardians([g2, g3])
    assert g1 == p.primary_guardian
