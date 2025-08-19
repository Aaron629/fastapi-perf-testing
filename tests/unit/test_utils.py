import pytest
from app.utils import add

@pytest.mark.unit
def test_add_positive():
    assert add(2, 3) == 5

@pytest.mark.unit
def test_add_negative():
    assert add(-2, -3) == -5
