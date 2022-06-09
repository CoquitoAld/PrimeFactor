import calculator #Import the calculator module (calculator.py)

def test_two_plus_two():
    """
    Asserts that given the parameters 2 and 2, the add
    function should return 4.
    """
    assert claculator.add(2,2) == 4

def test_five_plus_seven():
    assert calculator.add(5,7) == 12
