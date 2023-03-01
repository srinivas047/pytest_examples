import ExamplePrograms
import pytest

#Input for the first 2 tests
@pytest.fixture
def inputPower():
    input = [2, 4, 8]
    return input

def test_power(inputPower):
    output = ExamplePrograms.power(inputPower)
    assert output == [4, 16, 64]

def test_aveGrades(inputPower):
    output = ExamplePrograms.aveGrades(inputPower)
    assert output == 14 // 3

def test_reverseString():
    output = ExamplePrograms.reverseString("abcdef")
    assert output == "fedcba"

def test_twoSum():
    output = ExamplePrograms.twoSum([2, 7, 11, 15], 9)
    assert output == [1, 0]

#Input for the next 2 tests
@pytest.fixture
def inputList():
    input = [7,1,5,5,3,6,4]
    return input

def test_maxProfit(inputList):
    output = ExamplePrograms.maxProfit(inputList)
    assert output == 5

def test_containsDuplicates(inputList):
    output = ExamplePrograms.containsDulicates(inputList)
    assert output == True