from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -6, "test") == "test"
    assert arrs.get(['1', 2, 3], 0, 'test') == '1'
    assert arrs.get([1, 2, 3], -1) == None
    assert arrs.get([1, 2, 3], -3, 'test') == 'test'
    assert arrs.get([1, 2, 3], 2, 'test') == 3
    assert arrs.get([], -5, 'test') == 'test'
    assert arrs.get([1, 2, 3], 0, 'test') == 1





def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 2) == [3, 4]
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3], 1, -2) == []
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([], 0, -1) == []
    assert arrs.my_slice([-1, -2, -3], 0) == [-1, -2, -3]
    assert arrs.my_slice([1, 2, 3], 1, -2) == []
    assert arrs.my_slice([1, 2, 3], 0, -1) == [1, 2]
    assert arrs.my_slice([-6], -2) == [-6]

