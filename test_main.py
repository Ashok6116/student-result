from main import calculate_result

def test_pass():
    assert calculate_result(75) == "Pass"

def test_fail():
    assert calculate_result(30) == "Fail"

def test_boundary():
    assert calculate_result(40) == "Pass"