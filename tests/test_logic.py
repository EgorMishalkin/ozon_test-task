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
            "work": {"occupation": "Planet Devour"}
        },
        {
            "name": "Hero Two",
            "appearance": {
                "gender": "Male",
                "height": ["6'10", "210 cm"]
            },
            "work": {"occupation": "Teacher"}
        },
        {
            "name": "Hero Three",
            "appearance": {
                "gender": "Male",
                "height": ["8'2", "250 cm"]
            },
            "work": {"occupation": "-"}
        },
        {
            "name": "Hero Four",
            "appearance": {
                "gender": "Female",
                "height": ["8'2", "175 cm"]
            },
            "work": {"occupation": "Streamer"}
        },
        {   "name": "Hero Five",
            "appearance": {
                "gender": "Female",
                "height": ["8'2", "200 cm"]
            },
            "work": {"occupation": "-"}
        },
        {   "name": "Hero Six",
            "appearance": {
                "gender": "Female",
                "height": ["8'2", "180 cm"]
            },
            "work": {"occupation": "-"}},
    ]


# 4 tests below are the all possible scenarios with valid gender and work
def test_highest_employed_male(monkeypatch):
    monkeypatch.setattr(main,"get_heroes_data", fake_get_heroes_data)

    result = main.highest_character("Male", True)

    assert result is not None
    assert result["name"] == "Hero Two"


def test_highest_unemployed_male(monkeypatch):
    monkeypatch.setattr(main,"get_heroes_data", fake_get_heroes_data)

    result = main.highest_character("Male", False)

    assert result is not None
    assert result["name"] == "Hero Three"


def test_highest_unemployed_female(monkeypatch):
    monkeypatch.setattr(main,"get_heroes_data", fake_get_heroes_data)
    result = main.highest_character("Female", False)

    assert result is not None
    assert result["name"] == "Hero Five"


def test_highest_employed_female(monkeypatch):
    monkeypatch.setattr(main,"get_heroes_data", fake_get_heroes_data)
    result = main.highest_character("Female", True)

    assert result is not None
    assert result["name"] == "Hero Four"


def test_invalid_gender():
    with pytest.raises(ValueError):
        main.highest_character("-", True)


def test_invalid_has_job():
    with pytest.raises(TypeError):
        main.highest_character("Male", "True")


def test_skip_invalid_height(monkeypatch):
    def fake_get_invalid_height_data(url):
        return [
            {
                "name": "Hero One",
                "appearance": {
                    "gender": "Male",
                    "height": ["-", "-"]
                },
                "work": {"occupation": "Planet Devour"}
            },
            {
                "name": "Hero Two",
                "appearance": {
                    "gender": "Male",
                    "height": ["6'10", "210 cm"]
                },
                "work": {"occupation": "Teacher"}
            }
        ]

    monkeypatch.setattr(main,"get_heroes_data", fake_get_invalid_height_data)

    result = main.highest_character("Male", True)

    assert result["name"] == "Hero Two"