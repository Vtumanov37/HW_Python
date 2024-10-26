import pytest

from StringUtils import StringUtils

StringUtils = StringUtils()


@pytest.mark.parametrize('input_str, result', [("sdfsdf", "Sdfsdf"), ("VITYA", "Vitya"), ("123", "123"), ("", "")])
def test_capitalize1(input_str, result):
    assert StringUtils.capitilize(input_str) == result


@pytest.mark.parametrize('input_str, result', [(" sdfsdf", "sdfsdf"), (" VITYA", "VITYA"), (" 123", "123"), ("", "")])
def test_trim(input_str, result):
    assert StringUtils.trim(input_str) == result


@pytest.mark.parametrize('input_str, input_del, result', [("a123,bqa,c,d", ",", ["a123", "bqa", "c", "d"])])
def test_list(input_str, input_del, result):
    assert StringUtils.to_list(input_str, input_del) == result


@pytest.mark.parametrize('input_str, input_symbol, result', [('elfihgofdkjg', 'g', True), ('elfihgofdkjg', 'a', False)])
def test_contains(input_str, input_symbol, result):
    assert StringUtils.contains(input_str, input_symbol) == result


@pytest.mark.parametrize('input_str, input_del, result', [("Санкт-Петербург", "Санкт-", "Петербург")])
def test_delete_symbol(input_str, input_del, result):
    assert StringUtils.delete_symbol(input_str, input_del) == result


@pytest.mark.parametrize('input_str, input_symbol, result', [('elfihgofdkjg', 'e', True), ('elfihgofdkjg', 'a', False)])
def test_starts_with(input_str, input_symbol, result):
    assert StringUtils.starts_with(input_str, input_symbol) == result


@pytest.mark.parametrize('input_str, input_symbol, result', [('elfihgofdkjg', 'g', True), ('elfihgofdkjg', 'a', False)])
def test_end_with(input_str, input_symbol, result):
    assert StringUtils.end_with(input_str, input_symbol) == result


@pytest.mark.parametrize('input_str, result', [('', True), (' ', True), ('elfihgofdkjg', False)])
def test_is_empty(input_str, result):
    assert StringUtils.is_empty(input_str) == result


@pytest.mark.parametrize('input_str, input_del, result', [(["a123", "bqa", "c", "d"], ",", "a123,bqa,c,d"),
                                                          (["Санкт", "Петербург"], "-", "Санкт-Петербург")])
def test_list_to_string(input_str, input_del, result):
    assert StringUtils.list_to_string(input_str, input_del) == result
