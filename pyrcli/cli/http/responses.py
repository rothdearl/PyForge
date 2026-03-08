"""Utilities for parsing and validating HTTP response bodies."""

from typing import Final

import requests

from pyrcli.cli import ErrorReporter, JsonArray, JsonObject


def parse_json_body(response: requests.Response, *, on_error: ErrorReporter) -> JsonArray | JsonObject | None:
    """
    Return the JSON body from ``response`` as an object or array, or ``None`` on error.

    - Invokes ``on_error(message)`` if the response body cannot be decoded as JSON.
    - Returns ``None`` if the decoded JSON is not an object or array.
    """
    try:
        decoded_json = response.json()
    except ValueError:
        on_error("unable to decode json from response")
        return None

    if not isinstance(decoded_json, (dict, list)):
        on_error("unexpected response format")
        return None

    return decoded_json


__all__: Final[tuple[str, ...]] = ("parse_json_body",)
