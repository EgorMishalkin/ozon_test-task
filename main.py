import time
from http import HTTPStatus
import requests
from requests.exceptions import HTTPError


def get_heroes_data(url):
    retries = 3
    retry_codes = [
        HTTPStatus.TOO_MANY_REQUESTS, #429
        HTTPStatus.INTERNAL_SERVER_ERROR, #500
        HTTPStatus.BAD_GATEWAY, #502
        HTTPStatus.SERVICE_UNAVAILABLE, #503
        HTTPStatus.GATEWAY_TIMEOUT, #504
    ]

    # try the request up to three times for retryable HTTP errors
    for n in range(retries):
        try:
            response = requests.get(url, timeout=5)
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
    if gender not in ("Male", "Female"):
        raise ValueError("gender must be Male or Female")

    if not isinstance(has_job, bool):
        raise TypeError("has_job must be bool")

    heroes_data = get_heroes_data(url="https://akabab.github.io/superhero-api/api/all.json")
    highest_height = 0
    highest_hero = None

    for character_stats in heroes_data:
        character_job = character_stats["work"]["occupation"] != "-"

        if character_stats["appearance"]["gender"] == gender:
            if character_job == has_job:
                try:
                    # this line gives character's height in cm
                    character_height = float(character_stats["appearance"]["height"][1].split()[0])
                except (ValueError, IndexError, TypeError, KeyError):
                    # Skip heroes with missing or invalid height
                    continue

                if character_height > highest_height:
                    highest_height = character_height
                    highest_hero = character_stats

    return highest_hero


if __name__ == "__main__":
    character = highest_character('Female', True)
    print(character["name"])
    print(float(character["appearance"]["height"][1].split()[0]))
    print(character["work"]["occupation"])