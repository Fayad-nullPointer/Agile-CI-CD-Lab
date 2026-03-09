import pytest
#mke sure to import the function you want to test
from main import String_Sum_of_Digits
def test_String_Sum_of_Digits():
    # Test case 1: Basic test case with digits and letters
    assert String_Sum_of_Digits.String_Sum_of_Digits("abc123") == 6, "Test case 1 failed"
    
    # Test case 2: Test case with only digits
    assert String_Sum_of_Digits.String_Sum_of_Digits("456") == 15, "Test case 2 failed"
    
    # Test case 3: Test case with no digits
    assert String_Sum_of_Digits.String_Sum_of_Digits("abcdef") == 0, "Test case 3 failed"
    
    # Test case 4: Test case with special characters and digits
    assert String_Sum_of_Digits.String_Sum_of_Digits("!@#789") == 24, "Test case 4 failed"
    
    # Test case 5: Test case with empty string
    assert String_Sum_of_Digits.String_Sum_of_Digits("") == 0, "Test case 5 failed"
    
    print("All test cases passed!")
#Create tsetfunction using pytest and run the tests
def run_tests():
    pytest.main([__file__])
if __name__ == "__main__":
    run_tests()