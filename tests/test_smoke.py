import main


def test_smoke_employed_female():
    result = main.highest_character("Female", True)
    # # result is not None and is a dictionary
    assert result is not None
    assert isinstance(result, dict)
    # all main variables exist
    assert "name" in result
    assert "appearance" in result
    assert "work" in result
    # hero is employed_female
    assert result["appearance"]["gender"] == "Female"
    assert result["work"]["occupation"] != "-"
    # height returns with float > 0
    height = float(result["appearance"]["height"][1].split()[0])
    assert height > 0



