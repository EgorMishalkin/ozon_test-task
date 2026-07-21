import time
from http import HTTPStatus
import requests
from requests.exceptions import HTTPError


def get_heroes_data(url):
    retries = 3
    retry_codes = [
        HTTPStatus.TOO_MANY_REQUESTS,
        HTTPStatus.INTERNAL_SERVER_ERROR,
        HTTPStatus.BAD_GATEWAY,
        HTTPStatus.SERVICE_UNAVAILABLE,
        HTTPStatus.GATEWAY_TIMEOUT,
    ]

    for n in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data

        except HTTPError as exc:
            code = exc.response.status_code

            if code in retry_codes:
                # retry after n seconds
                time.sleep(n)
                continue

            raise
    return None


def highest_character(gender, has_job):
    heroes_data = get_heroes_data(url="https://akabab.github.io/superhero-api/api/all.json")
    highest_height = 0
    highest_hero = None
    for character_stats in heroes_data:
        character_job = character_stats["work"]["occupation"] != "-"

        if character_stats["appearance"]["gender"] == gender:
            if character_job == has_job:
                character_height = float(character_stats["appearance"]["height"][1].split()[0])
                if character_height > highest_height:
                    highest_height = character_height
                    highest_hero = character_stats
    return highest_hero


if __name__ == "__main__":
    character = highest_character('Female', True)
    print(character["name"])
    print(float(character["appearance"]["height"][1].split()[0]))
    print(character["work"]["occupation"])