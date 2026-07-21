import time
from http import HTTPStatus

import requests
from requests.exceptions import HTTPError

url = "https://akabab.github.io/superhero-api/api/all.json"
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
        print("Success!", data[0])
        break

    except HTTPError as exc:
        code = exc.response.status_code

        if code in retry_codes:
            # retry after n seconds
            time.sleep(n)
            continue

        raise