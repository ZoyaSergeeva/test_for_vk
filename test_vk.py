import pytest


def test1():# негативный тест
    s="i like python"
    try:
        assert ("dont"in s)
    except AssertionError:
        pass


def test2():# позитивный тест
    d = dict(one='1', two='2')
    assert d['one'] == '1'


def yeah_or_no(str):# функция для 3го теста
    if str == "Y":
        return "Yes"
    elif str == "N":
        return "No"
    else:
        return "?"


@pytest.mark.parametrize("input,expected_output",
                             [("Y", "Yes"),("N", "No"), ("T", "?")])#задание тестовых данных для теста
def test3(input,expected_output):# третий тест, позитивный
    result = yeah_or_no(input)
    print(f"input: {input}, output: {result}, expected: {expected_output}") # вывод результата
    assert result == expected_output # проверка, сравнение фактического и ожидаемого результата
