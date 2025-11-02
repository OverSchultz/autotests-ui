def test_sum2():
    assert 2 + 3 == 5, "[Error] сравнение не дало ожидаемого результата"

def test_not_sum2():
    assert 2 + 3 != 6, "[Error] сравнение не дало ожидаемого результата"

def test_error():
    assert 2 == 4, "[Error] сравнение не дало ожидаемого результата"

def test_print():
    print("Hello World")