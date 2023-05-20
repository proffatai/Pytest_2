import math

def test_sqrt_failure():
    num=25
    assert math.sqrt(num) == 6

def test_square_failure():
    assert 7*7 == 40

def test_equality_pass():
    assert 10 == 10


# During test execution, use the command: `pytest test_failure.py --maxfail=1`
#The test execution will stop once 1 test fails and it wont proceed to run the rest of the test