import pytest
from suma import suma


def test_suma_positivos():
    assert suma(5, 5) == 10


def test_suma_negativos():
    assert suma(-5, -5) == -10