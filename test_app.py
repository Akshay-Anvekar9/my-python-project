from app import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0




from app import add
def test_add():
    assert add(2,3) == 5
    assert add(-1, 1) == 0

