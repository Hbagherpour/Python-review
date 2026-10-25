

from tools.returns import calculate_return

def test_price_rise():
    assert calculate_return(100, 110) == 10.0

def test_price_fall():
    assert calculate_return(100, 90) == -10.0