from operacoes import soma, subtrai, divide, multiplica, eleva
import pytest

def test_soma():
    assert soma(2, 2) == 4
    assert soma(2, 0) == 2

def test_subtrai():
    assert subtrai(5, 2) == 3
    assert subtrai(0, 2) == -2
    assert subtrai(2, 0) == 2

def test_multiplica():
    assert multiplica(1, 0) == 0
    assert multiplica(0, 1) == 0
    assert multiplica(1, 2) == 2

def test_divide():
    assert divide(3, 2) == 1.5
    assert divide(0, 2) == 0
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)

def test_eleva():
    assert eleva(0, 0) == 1
    assert eleva(0, 1) == 0
    assert eleva(2, 0) == 1
    assert eleva(2, 1) == 2
    assert eleva(2, 2) == 4
    
