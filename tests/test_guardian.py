from src.laxleague.guardian import Guardian


def test_construction():
    g = Guardian("Mary", "Allen")
    assert g.first_name == "Mary"
    assert g.last_name == "Allen"
