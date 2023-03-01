import ExamplePrograms

def test_power():
    output = ExamplePrograms.power([2, 4, 8])
    assert output == [4, 16, 64]

def test_aveGrades():
    output = ExamplePrograms.aveGrades([2, 4, 8])
    assert output == 14 // 3

def test_reverseString():
    output = ExamplePrograms.reverseString("abcdef")
    assert output == "fedcba"

def test_twoSum():
    output = ExamplePrograms.twoSum([2, 7, 11, 15], 9)
    assert output == [1, 0]

def test_maxProfit():
    output = ExamplePrograms.maxProfit([7,1,5,3,6,4])
    assert output == 5