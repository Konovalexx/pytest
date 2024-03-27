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

def test_slice_start_none():
    assert arrs.my_slice([1, 2, 3, 4, 5], None, 3) == [1, 2, 3]

def test_slice_end_none():
    assert arrs.my_slice([1, 2, 3, 4, 5], 2, None) == [3, 4, 5]

def test_slice_both_none():
    assert arrs.my_slice([1, 2, 3, 4, 5], None, None) == [1, 2, 3, 4, 5]

def test_slice_end_none():
    assert arrs.my_slice([1, 2, 3, 4, 5], 2, None) == [3, 4, 5]

def test_slice_negative_indices():
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]

def test_slice_start_greater_than_end():
    assert arrs.my_slice([1, 2, 3, 4, 5], 3, 2) == []

def test_slice_empty_list():
    assert arrs.my_slice([], 1, 2) == []
    assert arrs.my_slice([], 0, 0) == []

def test_slice_edge_cases():
    assert arrs.my_slice([1, 2, 3, 4, 5], 5, 5) == []
    assert arrs.my_slice([1, 2, 3, 4, 5], 5, 6) == []