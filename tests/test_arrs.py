from utils import arrs


# В данном случае тест не проходил из-за того, что не учтено то, что в языке питон индексы начинаются с 0. Т.е.
# элемент с индексом 1 в списке [1, 2, 3] это 2, а не 3.
# def test_get():
#     assert arrs.get([1, 2, 3], 1, "test") == 3
#     assert arrs.get([], 0, "test") == "test"

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
