import pytest
from main import string2int, int2string, encrypt_data, decrypt_data

def test_string2int():
    assert string2int("ABC") == [65, 66, 67]

def test_int2string():
    assert int2string([65, 66, 67]) == "ABC"

def encrypt_data_test():
    assert encrypt_data("ABC", (5, 77)) == [65, 66, 67]

def decrypt_data_test():
    assert decrypt_data([65, 66, 67], (29, 77)) == "ABC"

if __name__ == "__main__":
    pytest.main()