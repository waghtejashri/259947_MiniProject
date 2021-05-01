import calculations

def test_gratuity_calc():
    result = calculations.gratuity_calc(35000, 5, 6, 1)
    assert result == 121153.84615384616

def test_FD():
    result = calculations.FD(150000, 4, 6)
    assert result == 39371.54400000005

def test_roi():
    result = calculations.roi(0, 5, 10)
    assert result == 0.0

def test_emi():
    result = calculations.emi(0, 5, 10)
    assert result == 0.0