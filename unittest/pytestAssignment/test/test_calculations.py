import pytest

from src.calculations import add,square,divide

#sumofnumbers
def test_sum():
    assert add(3,5)==8

#assert fail
def test_upper_fail():
    assert "hello".upper()=="hello"

#fixture
@pytest.fixture
def number_list():
    return [1,2,3]


def test_list_length(number_list):
    assert len(number_list)==3


#parametrize
@pytest.mark.parametrize("input,expected",[
    (2,4),
    (3,9),
    (4,16)
])

#square
def test_square(input, expected):
    assert square(input)==expected

#exception handle
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(10,0)