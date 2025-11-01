from lenormju.meteo import should_i_bring_a_jacket

import requests
import pytest


def test__should_i_bring_a_jacket__definitely() -> None:
    should_i = should_i_bring_a_jacket()
    assert should_i == "Definitely!"


def test__should_i_bring_a_jacket__probably() -> None:
    should_i = should_i_bring_a_jacket()
    assert should_i == "Probably"


def test__should_i_bring_a_jacket__just_in_case() -> None:
    should_i = should_i_bring_a_jacket()
    assert should_i == "Just in case ?"


def test__should_i_bring_a_jacket__no_need() -> None:
    should_i = should_i_bring_a_jacket()
    assert should_i == "No need"


def test__should_i_bring_a_jacket__connection_error() -> None:
    with pytest.raises(requests.ConnectionError, match="Max retries exceeded"):
        should_i_bring_a_jacket()
