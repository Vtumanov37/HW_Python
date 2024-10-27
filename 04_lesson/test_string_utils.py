import pytest

from StringUtils import StringUtils

StringUtils = StringUtils()


# Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
    #Positive
@pytest.mark.parametrize('input_str, result', [("sdfsdf", "Sdfsdf"), ("VITYA", "Vitya")])
def test_capitalize_positive(input_str, result):
    assert StringUtils.capitilize(input_str) == result

    #Negative
@pytest.mark.parametrize('input_str, result', [("123", "123"), ("", ""), (" ", " ")])
def test_capitalize_negative(input_str, result):
    assert StringUtils.capitilize(input_str) == result


# Принимает на вход текст и удаляет пробелы в начале, если они есть
    #Positive
@pytest.mark.parametrize('input_str, result', [(" sdfsdf", "sdfsdf"), (" VITYA", "VITYA")])
def test_trim_positive(input_str, result):
    assert StringUtils.trim(input_str) == result

    #Negative
@pytest.mark.parametrize('input_str, result', [(" 123", "123"), ("", ""), (" ", "")])
def test_trim_negative(input_str, result):
    assert StringUtils.trim(input_str) == result


# Принимает на вход текст с разделителем и возвращает список строк
    #Positive
@pytest.mark.parametrize('input_str, input_del, result', [("a123,bqa,c,d", ",", ["a123", "bqa", "c", "d"])])
def test_list(input_str, input_del, result):
    assert StringUtils.to_list(input_str, input_del) == result

    #Negative
@pytest.mark.parametrize('input_str, input_del, result', [("+,-,/,%", ",", ["+", "-", "/", "%"])])
def test_list(input_str, input_del, result):
    assert StringUtils.to_list(input_str, input_del) == result


# Возвращает `True`, если строка содержит искомый символ и `False` - если нет

@pytest.mark.parametrize('input_str, input_symbol, result', [('elfihgofdkjg', 'g', True), ('elfihgofdkjg', 'a', False)])
def test_contains(input_str, input_symbol, result):
    assert StringUtils.contains(input_str, input_symbol) == result



# Удаляет все подстроки из переданной строки

@pytest.mark.parametrize('input_str, input_del, result', [("Санкт-Петербург", "Санкт-", "Петербург")])
def test_delete_symbol(input_str, input_del, result):
    assert StringUtils.delete_symbol(input_str, input_del) == result


# Возвращает `True`, если строка начинается с заданного символа и `False` - если нет

@pytest.mark.parametrize('input_str, input_symbol, result', [('elfihgofdkjg', 'e', True), ('elfihgofdkjg', 'a', False)])
def test_starts_with(input_str, input_symbol, result):
    assert StringUtils.starts_with(input_str, input_symbol) == result


# Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет

@pytest.mark.parametrize('input_str, input_symbol, result', [('elfihgofdkjg', 'g', True), ('elfihgofdkjg', 'a', False)])
def test_end_with(input_str, input_symbol, result):
    assert StringUtils.end_with(input_str, input_symbol) == result


# Возвращает `True`, если строка пустая и `False` - если нет
    #Positive
@pytest.mark.parametrize('input_str, result', [('', True), (' ', True), ('elfihgofdkjg', False)])
def test_is_empty(input_str, result):
    assert StringUtils.is_empty(input_str) == result

    #Negative
@pytest.mark.parametrize('input_str, result', [(' ', True), ('B', False)])
def test_is_empty(input_str, result):
    assert StringUtils.is_empty(input_str) == result



# Преобразует список элементов в строку с указанным разделителем
    #Positive
@pytest.mark.parametrize('input_str, input_del, result', [(["a123", "bqa", "c", "d"], ",", "a123,bqa,c,d"),
                                                          (["Санкт", "Петербург"], "-", "Санкт-Петербург")])
def test_list_to_string(input_str, input_del, result):
    assert StringUtils.list_to_string(input_str, input_del) == result
