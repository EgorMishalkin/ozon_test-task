import pytest

import main


def fake_get_heroes_data(url):
    # fake data to check if logic works correctly
    return [
        {
            "name": "Hero One",
            "appearance": {
                "gender": "Male",
                "height": ["5'11", "180 cm"]
            },
            "work": {
                "occupation": "Planet Devour"
            }
        },
        {
            "name": "Hero Two",
            "appearance": {
                "gender": "Male",
                "height": ["6'10", "210 cm"]
            },
            "work": {
                "occupation": "Teacher"
            }
        },
        {
            "name": "Hero Three",
            "appearance": {
                "gender": "Male",
                "height": ["8'2", "250 cm"]
            },
            "work": {
                "occupation": "-"
            }
        },

        {
            "name": "Hero Four",
            "appearance": {
                "gender": "Female",
                "height": ["8'2", "175 cm"]
            },
            "work": {
                "occupation": "Streamer"
            }},

        {   "name": "Hero Five",
            "appearance": {
                "gender": "Female",
                "height": ["8'2", "200 cm"]
            },
            "work": {
                "occupation": "-"
            }},

        {"name": "Hero Six",
            "appearance": {
                "gender": "Female",
                "height": ["8'2", "180 cm"]
            },
            "work": {
                "occupation": "-"
            }},

    ]


def test_highest_employed_male(monkeypatch):
    monkeypatch.setattr(main,"get_heroes_data",fake_get_heroes_data)

    result = main.highest_character("Male", True)

    assert result is not None
    assert result["name"] == "Hero Two"


def test_highest_unemployed_male(monkeypatch):
    monkeypatch.setattr(main,"get_heroes_data",fake_get_heroes_data)

    result = main.highest_character("Male", False)

    assert result is not None
    assert result["name"] == "Hero Three"


def test_highest_unemployed_female(monkeypatch):
    monkeypatch.setattr(main,"get_heroes_data",fake_get_heroes_data)
    result = main.highest_character("Female", False)

    assert result is not None
    assert result["name"] == "Hero Five"


def test_highest_employed_female(monkeypatch):
    monkeypatch.setattr(main,"get_heroes_data", fake_get_heroes_data)
    result = main.highest_character("Female", True)

    assert result is not None
    assert result["name"] == "Hero Four"


#  highest_character returns None in that case
def test_highest_employed_unknown_gender(monkeypatch):
    monkeypatch.setattr(main,"get_heroes_data", fake_get_heroes_data)
    with pytest.raises(ValueError):
        main.highest_character("Unknown", True)


def test_invalid_gender():
    with pytest.raises(ValueError):
        main.highest_character("-", True)


def test_invalid_has_job():
    with pytest.raises(TypeError):
        main.highest_character("Male", "True")
