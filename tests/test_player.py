from src.laxleague.guardian import Guardian
from tests.conftest import player_one, guardians_list


def test_construction(player_one):
    assert player_one.first_name == "Felicity"
    assert player_one.last_name == "Smith"
    assert player_one.jersey == 16
    assert [] == player_one.guardians_list


def test_add_guardian(player_one, guardians_list):
    guardians_list[0] = Guardian("Mary", "Allen")
    player_one.add_guardian(guardians_list[0])
    assert [guardians_list[0]] == player_one.guardians_list


def test_guardians(player_one, guardians_list):
    player_one.add_guardians([guardians_list[0]])
    player_one.add_guardians([guardians_list[1], guardians_list[2]])
    assert guardians_list == player_one.guardians_list


def test_primary_guardian(player_one, guardians_list):
    player_one.add_guardians([guardians_list[0]])
    player_one.add_guardians([guardians_list[1], guardians_list[2]])
    assert guardians_list[0] == player_one.primary_guardian
