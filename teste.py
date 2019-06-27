import pytest
from principal import somar
from principal import subtrair
from principal import multiplicar

def test_somar():
    assert somar(2,3)==5

def test_subtrair():
    assert subtrair(1,1)==0

def test_multiplicar():
    assert multiplicar(2,6)==12

