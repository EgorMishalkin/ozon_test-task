import pytest
import main
from requests.exceptions import HTTPError
from unittest.mock import Mock

data = [{"name": "Test Hero"}]

# class for successful responses
class FakeResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return data


# class for responses with error
class FakeErrorResponse:
    def __init__(self, status_code):
        self.status_code = status_code

    def raise_for_status(self):
        error = HTTPError()
        error.response = self
        raise error


def fake_get(url, timeout):
    return FakeResponse()


def fake_get_404(url, timeout):
    return FakeErrorResponse(404)


def fake_get_500(url, timeout):
    return FakeErrorResponse(500)


def test_data_loaded_successfully(monkeypatch):
    # replace request to API with fake_get to check if get_heroes_data is working properly
    monkeypatch.setattr(main.requests, "get", fake_get)
    result = main.get_heroes_data("fake-url")

    assert result == data


def test_non_retryable_error(monkeypatch):
    monkeypatch.setattr(main.requests, "get", fake_get_404)

    with pytest.raises(HTTPError):
        main.get_heroes_data("fake-url")


def test_error_after_3_attempts(monkeypatch):
    mock_get = Mock(side_effect=fake_get_500)

    monkeypatch.setattr(main.requests, "get", mock_get)
    # disable delays
    monkeypatch.setattr(main.time, "sleep", lambda seconds: None)

    result = main.get_heroes_data("fake-url")

    assert result is None
    assert mock_get.call_count == 3


def test_successful_response_after_retry(monkeypatch):
    mock_get = Mock(side_effect=[FakeErrorResponse(500), FakeResponse()])
    monkeypatch.setattr(main.requests, "get", mock_get)
    monkeypatch.setattr(main.time, "sleep", lambda seconds: None)
    result = main.get_heroes_data("fake-url")

    assert result == data
    assert mock_get.call_count == 2