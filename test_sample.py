import sample
def test_calculate_grade_REQ01():
    result = []
    test_result = "A"
    marks = 90
    result = sample.calculate_grade(90)
    assert (result == test_result)

def test_calculate_grade_REQ02():
    result = []
    test_result = "B+"
    marks = 75
    result = sample.calculate_grade(75)
    assert (result == test_result)

def test_calculate_grade_REQ03():
    result = []
    test_result = "B"
    marks = 70
    result = sample.calculate_grade(70)
    assert (result == test_result)

def test_calculate_grade_REQ04():
    result = []
    test_result = "passed"
    marks = 50
    result = sample.calculate_grade(50)
    assert (result == test_result)

def test_calculate_grade_REQ05():
    result = []
    test_result = "failed"
    marks = 40
    result = sample.calculate_grade(40)
    assert (result == test_result)

def test_calculate_grade_REQ06():
    result = []
    test_result = ""
    marks = -3
    result = sample.calculate_grade(-3)
    assert (result == test_result)