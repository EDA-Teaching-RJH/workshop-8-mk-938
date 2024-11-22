import pytest
from Calculator import add, sub, div, mult
def test_add():
    assert add(1,1) == 2
    assert add(2,1) == 3
    assert add(0,0) == 0

def test_sub():
    assert sub(1,1) == 0
    assert sub(10,3) == 7
    assert sub(0,0) == 0
   
def test_div():
    assert div(10,2) == 5
    assert div(2,1) == 2
    with pytest.raises(ZeroDivisionError): 
        div(2,0)
  
def test_mult():
    assert mult(10,1) == 10
    assert mult(5,0) == 0
    assert mult(7,3) == 21

