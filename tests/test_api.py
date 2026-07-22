import pytest
import main
from requests.exceptions import HTTPError

data = [{"name": "Test Hero"}]

class FakeResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return data


def fake_get(url):
    return FakeResponse()


class FakeErrorResponse:
    status_code = 404

    def raise_for_status(self):
        error = HTTPError()
        error.response = self
        raise error


def fake_get_404(url):
    return FakeErrorResponse()


def test_data_loaded_successfully(monkeypatch):
    monkeypatch.setattr(main.requests, "get", fake_get)

    result = main.get_heroes_data("fake-url")

    assert result == data


def test_non_retryable_error(monkeypatch):
    monkeypatch.setattr(main.requests, "get", fake_get_404)

    with pytest.raises(HTTPError):
        main.get_heroes_data("fake-url")