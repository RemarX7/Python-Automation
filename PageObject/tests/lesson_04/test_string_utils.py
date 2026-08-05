import pytest
from PageObject.tests.lesson_04.string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("string, expected", [
    ('skyPro', 'SkyPro'),  # bug01
    ('lesson', 'Lesson'),
    ('alex immortal', 'Alex immortal'),
    ('kerama Marazzi', 'Kerama Marazzi'),  # bug01
    ('вольф 359', 'Вольф 359'),
])
def test_capitalize_positive(string, expected):
    assert string_utils.capitalize(string) == expected

@pytest.mark.positive
@pytest.mark.parametrize('string, expected', [
    ('  cats', 'cats'),
    ('   kuper 12', 'kuper 12'),
    (' 13 Friday', '13 Friday'),
    (' Чёрная пятница 13', 'Чёрная пятница 13')
])
def test_trim_positive(string, expected):
    assert string_utils.trim(string) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, expected", [
    ('', ''),
    ('1lesson', '1lesson'),
    ('  ', '  '),
    ('+', '+'),
    ('?', '?'),
    ('Bug', 'Bug')
])
def test_capitalize_negative(string, expected):
    assert string_utils.capitalize(string) == expected

@pytest.mark.negative
@pytest.mark.parametrize("string, expected", [
    ('   ', ''),
    ('  capcha passed', 'capcha passed'),
    (' number - one', 'number - one'),
    (' Gulliver v2.0 ', 'Gulliver v2.0 '),
    (' Лунтик   ', 'Лунтик   ')
])
def test_trim_negative(string, expected):
    assert string_utils.trim(string) == expected


@pytest.mark.positive_and_negative
@pytest.mark.parametrize('string, symbol, result', [
    ('SkyPro', 'S', True),
    ('Thug4Life', 'L', True),
    ('performance', 'o', True),
    ('+79081832653 number', '+', True),
    ('Луман 16 A', '16', True),
    ('рост 180 см', '180 см', True),
    ('skypro', 'l', False),
    ('jira/confluence', 'J', False),
    ('DevTools', 'i', False),
    (' ', ' ', True)
])
def test_contains(string, symbol, result):
    assert string_utils.contains(string, symbol) == result


@pytest.mark.parametrize('string, symbol, result', [
    ('SkyPro', 'k', 'SyPro'),
    ('SkyPro', 's', 'SkyPro'),
    ('good 5mooning', '5', 'good mooning'),
    (' ', ' ', ''),
    ('', '', ''),
    (' ! ', '!', '  '),
    ('4 / 2 = 2', ' ', '4/2=2'),
    ('hello', 'f', 'hello'),
    ('yes', '', 'yes'),
    ('', 'a', ''),
    ('\n\t\r', '\n', '\t\r'),
    ('😂test😂', '😂', 'test'),
    ("admin' --", "'", "admin --"),
    ("admin' OR '1'='1", "'", "admin OR 1=1"),
    ("'; DROP TABLE users; --", ";", "' DROP TABLE users --")
])
def test_delete_symbols(string, symbol, result):
    assert string_utils.delete_symbol(string, symbol) == result
