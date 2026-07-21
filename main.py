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
    highest_hero = None
    highest_height = 0
    return

# heroes_data = get_heroes_data("https://akabab.github.io/superhero-api/api/all.json")
# print(heroes_data)
# for character_stats in heroes_data:
#    print(character_stats["name"])
#    print(character_stats["appearance"]["gender"])
#    print(float(character_stats["appearance"]["height"][1].split()[0]))
#    print(character_stats["work"]["occupation"])