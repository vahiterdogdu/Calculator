from calculator import add, subtract, multiply, divide, power

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(5, 4) == 20

def test_divide():
    assert divide(10, 2) == 5
    
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -5) == -10
    assert add(100, 200) == 300

def test_power():
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(10, 0) == 1
    assert power(0, 0) == 1 