import pytest
from string_utils import StringUtils

# CAPITILIZE
# 1. ПОЗИТИВНЫЙ: Тестируем строку, где все буквы - строчные
def test_capitilize_all_lowercase():
    string_util = StringUtils()
    res = string_util.capitilize('hello')
    assert res == 'Hello'

# 2. ПОЗИТИВНЫЙ: Тестируем строку, где все буквы - прописные
def test_capitilize_all_uppercase():
    string_util = StringUtils()
    res = string_util.capitilize('GOODBYE')
    assert res == 'GOODBYE'
# Ошибка - принимает все прописные и возвращает первую прописную с остальными строчными (которые изначально тоже были прописными). Так задуманно?

# 3. ПОЗИТИВНЫЙ: Тестируем строку c числами
def test_capitilize_ints_as_string():
    string_util = StringUtils()
    res = string_util.capitilize('777')
    assert res == '777'

# 4. ПОЗИТИВНЫЙ: Тестируем строку c пробелами
def test_capitilize_string_with_spaces():
    string_util = StringUtils()
    res = string_util.capitilize('have a good day!')
    assert res == 'Have a good day!'

# 5. НЕГАТИВНЫЙ: пустая строка
@pytest.mark.xfail
def test_capitilize_empty_string():
    string_util = StringUtils()
    res = string_util.capitilize('')
    assert res == ''
# Ждем ошибку?

# 6. НЕГАТИВНЫЙ: пробелы
@pytest.mark.xfail
def test_capitilize_all_spaces():
    string_util = StringUtils()
    res = string_util.capitilize('     ')
    assert res == '     '
# Ждем ошибку?

# 7. НЕГАТИВНЫЙ: None
def test_capitilize_none():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.capitilize(None)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 8. НЕГАТИВНЫЙ: Тип данных - int
def test_capitilize_int():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.capitilize(76544)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 9. НЕГАТИВНЫЙ: Тип данных - Boolean
def test_capitilize_boolean():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.capitilize(True)
# Ожидаемая ошибка - функция не принимает этот тип данных





# TRIM
# 10. ПОЗИТИВНЫЙ: Тестируем строку с пробелами вначале
def test_trim_string_with_spaces_at_the_beginning():
    string_util = StringUtils()
    res = string_util.trim('     Hello')
    assert res == 'Hello'

# 11. ПОЗИТИВНЫЙ: Тестируем строку без пробелов в начале
def test_trim_string_without_spaces_at_the_beginning():
    string_util = StringUtils()
    res = string_util.trim('Hello')
    assert res == 'Hello'

# 12. ПОЗИТИВНЫЙ: Тестируем строку c пробелами в конце
def test_trim_string_without_spaces_at_the_end():
    string_util = StringUtils()
    res = string_util.trim('Hello     ')
    assert res == 'Hello     '

# 13. ПОЗИТИВНЫЙ: Тестируем строку c числами
def test_trim_ints_as_string():
    string_util = StringUtils()
    res = string_util.trim('     675849')
    assert res == '675849'

# 14. НЕГАТИВНЫЙ: пустая строка
@pytest.mark.xfail
def test_trim_empty_string():
    string_util = StringUtils()
    res = string_util.trim('')
    assert res == ''
# Ждем ошибку?

# 15. НЕГАТИВНЫЙ: пробелы
@pytest.mark.xfail
def test_trim_all_spaces():
    string_util = StringUtils()
    res = string_util.trim('     ')
    assert res == '     '
# Ошибка: убирает пробелы вообще. Ошибка ли? Ждем ошибку?

# 16. НЕГАТИВНЫЙ: None
def test_trim_none():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.trim(None)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 17. НЕГАТИВНЫЙ: Тип данных - int
def test_trim_int():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.trim(76544)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 18. НЕГАТИВНЫЙ: Тип данных - Boolean
def test_trim_boolean():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.trim(True)
# Ожидаемая ошибка - функция не принимает этот тип данных





# TO_LIST
# 19. ПОЗИТИВНЫЙ: Тестируем текст без указанного разделителя
def test_to_list_string_without_specific_delimeter():
    string_util = StringUtils()
    res = string_util.to_list('Hello,My,Name,Is,John')
    assert res == ['Hello', 'My', 'Name', 'Is', 'John']

# 20. ПОЗИТИВНЫЙ: Тестируем текст с определенным разделителем
def test_to_list_string_with_specific_delimeter():
    string_util = StringUtils()
    res = string_util.to_list('Hello/My/Name/Is/Lily', '/')
    assert res == ['Hello', 'My', 'Name', 'Is', 'Lily']

# 21. ПОЗИТИВНЫЙ: Тестируем текст с числами как строками
def test_to_list_ints_as_string():
    string_util = StringUtils()
    res = string_util.to_list('9,8,7,6,5')
    assert res == ['9', '8', '7', '6', '5']

# 22. ПОЗИТИВНЫЙ: Тестируем текст с пробелами
def test_to_list_string_with_spaces():
    string_util = StringUtils()
    res = string_util.to_list('Good   ,   Day,Ladies  , & ,  Gentlemen  ')
    assert res == ['Good   ', '   Day', 'Ladies  ', ' & ', '  Gentlemen  ']

# 23. НЕГАТИВНЫЙ: пустая строка
@pytest.mark.xfail
def test_to_list_empty_string():
    string_util = StringUtils()
    res = string_util.to_list('')
    assert res == []
# Ждем ошибку?

# 24. НЕГАТИВНЫЙ: пробелы
@pytest.mark.xfail
def test_to_list_all_spaces():
    string_util = StringUtils()
    res = string_util.to_list('     ')
    assert res == [     ]
# Ждем ошибку?

# 25. НЕГАТИВНЫЙ: None
def test_to_list_none():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.to_list(None)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 26. НЕГАТИВНЫЙ: Тип данных - int
def test_to_list_int():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.to_list(543672)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 27. НЕГАТИВНЫЙ: Тип данных - Boolean
def test_to_list_boolean():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.to_list(False)
# Ожидаемая ошибка - функция не принимает этот тип данных





# CONTAINS
# 28. ПОЗИТИВНЫЙ: Тестируем текст, где искомый символ содержится в тексте
def test_contains_string_contains_symbol():
    string_util = StringUtils()
    res = string_util.contains('Gratitude', 't')
    assert res == True

# 29. ПОЗИТИВНЫЙ: Тестируем текст, где искомый символ не содержится в тексте
def test_contains_string_does_not_contain_symbol():
    string_util = StringUtils()
    res = string_util.contains('Gratitude', 'F')
    assert res == False

# 30. ПОЗИТИВНЫЙ: Тестируем текст с числами как строками
def test_contains_ints_as_string():
    string_util = StringUtils()
    res = string_util.contains('76543', '7')
    assert res == True

# 31. ПОЗИТИВНЫЙ: Тестируем текст с пробелами
def test_contains_string_with_spaces():
    string_util = StringUtils()
    res = string_util.contains('Have a good day!', 'g')
    assert res == True

# 32. ПОЗИТИВНЫЙ: Тестируем текст c несколькими искомыми символами
def test_contains_string_with_several_symbols():
    string_util = StringUtils()
    res = string_util.contains('Have a wonderful day!', 've a wond')
    assert res == True

# 33. НЕГАТИВНЫЙ: не указан искомый символ(ы)
def test_contains_no_symbol_mentioned():
    string_util = StringUtils()
    with pytest.raises(TypeError):
        string_util.contains('Crumbles')
# Ошибка, нет обязательного аргумента

# 34. НЕГАТИВНЫЙ: пустая строка
@pytest.mark.xfail
def test_contains_empty_string():
    string_util = StringUtils()
    res = string_util.contains('', '')
    assert res == True
# Ждем ошибку?

# 35. НЕГАТИВНЫЙ: пробелы
@pytest.mark.xfail
def test_contains_all_spaces():
    string_util = StringUtils()
    res = string_util.contains('     ', ' ')
    assert res == True
# Ждем ошибку?

# 36. НЕГАТИВНЫЙ: None
def test_contains_none():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.contains(None, None)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 37. НЕГАТИВНЫЙ: Тип данных - int
def test_contains_int():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.contains(876543, 54)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 38. НЕГАТИВНЫЙ: Тип данных - Boolean
def test_contains_boolean():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.contains(False, True)
# Ожидаемая ошибка - функция не принимает этот тип данных





# DELETE_SYMBOL
# 39. ПОЗИТИВНЫЙ: Тестируем текст, где искомый символ содержится в тексте
def test_delete_symbol_string_contains_symbol():
    string_util = StringUtils()
    res = string_util.delete_symbol('Gorgeous', 'g')
    assert res == 'Goreous'

# 40. ПОЗИТИВНЫЙ: Тестируем текст с числами как строками
def test_delete_symbol_ints_as_string():
    string_util = StringUtils()
    res = string_util.delete_symbol('98765', '7')
    assert res == '9865'

# 41. ПОЗИТИВНЫЙ: Тестируем текст с пробелами
def test_delete_symbol_string_with_spaces():
    string_util = StringUtils()
    res = string_util.delete_symbol('Brace yourself', 'B')
    assert res == 'race yourself'

# 42. ПОЗИТИВНЫЙ: Тестируем текст c несколькими удаляемыми символами
def test_delete_symbol_string_with_several_symbols():
    string_util = StringUtils()
    res = string_util.delete_symbol('Diving deeper and deeper', 'r and d')
    assert res == 'Diving deepeeeper'

# 43. Позитивный: Тестируем текст, где искомый символ не содержится в тексте
def test_delete_symbol_string_does_not_contain_symbol():
    string_util = StringUtils()
    res = string_util.delete_symbol('Gratitude', 's')
    assert res == 'Gratitude'

# 44. НЕГАТИВНЫЙ: не указан удаляемый символ(ы)
def test_delete_symbol_no_symbol_mentioned():
    string_util = StringUtils()
    with pytest.raises(TypeError):
        string_util.delete_symbol('Grateful')
# Ошибка, нет обязательного аргумента

# 45. НЕГАТИВНЫЙ: пустая строка
@pytest.mark.xfail
def test_delete_symbol_empty_string():
    string_util = StringUtils()
    res = string_util.delete_symbol('', '')
    assert res == ''
# Ждем ошибку?

# 46. НЕГАТИВНЫЙ: пробелы
@pytest.mark.xfail
def test_delete_symbol_all_spaces():
    string_util = StringUtils()
    res = string_util.delete_symbol('     ', ' ')
    assert res == ''
# Ждем ошибку?

# 47. НЕГАТИВНЫЙ: None
def test_delete_symbol_none():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.delete_symbol(None, None)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 48. НЕГАТИВНЫЙ: Тип данных - int
def test_delete_symbol_int():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.delete_symbol(8765, 5)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 49. НЕГАТИВНЫЙ: Тип данных - Boolean
def test_delete_symbol_boolean():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.delete_symbol(False, True)
# Ожидаемая ошибка - функция не принимает этот тип данных





# STARTS_WITH
# 50. ПОЗИТИВНЫЙ: Тестируем текст, где заданный символ является начальным (Прописная буква)
def test_starts_with_where_symbol_corresponds_uppercase():
    string_util = StringUtils()
    res = string_util.starts_with('Glory', 'G')
    assert res == True

# 51. ПОЗИТИВНЫЙ: Тестируем текст, где заданный символ является начальным (Строчная буква)
def test_starts_with_where_symbol_corresponds_lowercase():
    string_util = StringUtils()
    res = string_util.starts_with('fateful', 'f')
    assert res == True

# 52. ПОЗИТИВНЫЙ: Тестируем текст, где заданный символ не является начальным
def test_starts_with_where_symbol_does_not_correspond():
    string_util = StringUtils()
    res = string_util.starts_with('Glory', 'L')
    assert res == False

# 53. ПОЗИТИВНЫЙ: Тестируем текст с числами как строками
def test_starts_with_ints_as_string():
    string_util = StringUtils()
    res = string_util.starts_with('123456', '1')
    assert res == True

# 54. ПОЗИТИВНЫЙ: Тестируем текст с пробелами
def test_starts_with_string_with_spaces():
    string_util = StringUtils()
    res = string_util.starts_with('Tastes like strawberries', 'T')
    assert res == True

# 55. ПОЗИТИВНЫЙ: пробел перед текстом
def test_starts_with_space_before_string():
    string_util = StringUtils()
    res = string_util.starts_with(' On a summer evening', ' ')
    assert res == True

# 56. НЕГАТИВНЫЙ: несколько начальных символов
@pytest.mark.xfail
def test_starts_with_several_symbols():
    string_util = StringUtils()
    res = string_util.starts_with('And it sounds just like a song', 'And')
    assert res == True
# Ждем ошибку?

# 57. НЕГАТИВНЫЙ: не указан проверяемый начальный символ
def test_starts_with_no_symbol_mentioned():
    string_util = StringUtils()
    with pytest.raises(TypeError):
        string_util.starts_with('Summertime')
# Ошибка, нет обязательного аргумента

# 58. НЕГАТИВНЫЙ: пустая строка
@pytest.mark.xfail
def test_starts_with_empty_string():
    string_util = StringUtils()
    res = string_util.starts_with('', '')
    assert res == True
# Ждем ошибку?

# 59. НЕГАТИВНЫЙ: пробелы
@pytest.mark.xfail
def test_starts_with_all_spaces():
    string_util = StringUtils()
    res = string_util.starts_with('     ', ' ')
    assert res == True
# Ждем ошибку?

# 60. НЕГАТИВНЫЙ: None
def test_starts_with_none():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.starts_with(None, None)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 61. НЕГАТИВНЫЙ: Тип данных - int
def test_starts_with_int():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.starts_with(9876, 9)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 62. НЕГАТИВНЫЙ: Тип данных - Boolean
def test_starts_with_boolean():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.starts_with(False, True)
# Ожидаемая ошибка - функция не принимает этот тип данных





# END_WITH
# 63. ПОЗИТИВНЫЙ: Тестируем текст, где заданный символ является конечным (Прописная буква)
def test_end_with_where_symbol_corresponds_uppercase():
    string_util = StringUtils()
    res = string_util.end_with('sadnesS', 'S')
    assert res == True

# 64. ПОЗИТИВНЫЙ: Тестируем текст, где заданный символ является конечным (Строчная буква)
def test_end_with_where_symbol_corresponds_lowercase():
    string_util = StringUtils()
    res = string_util.end_with('White', 'e')
    assert res == True

# 65. ПОЗИТИВНЫЙ: Тестируем текст, где заданный символ не является конечным
def test_end_with_where_symbol_does_not_correspond():
    string_util = StringUtils()
    res = string_util.end_with('Mustang', 'c')
    assert res == False

# 66. ПОЗИТИВНЫЙ: Тестируем текст с числами как строками
def test_end_with_ints_as_string():
    string_util = StringUtils()
    res = string_util.end_with('3425', '5')
    assert res == True

# 67. ПОЗИТИВНЫЙ: Тестируем текст с пробелами
def test_end_with_string_with_spaces():
    string_util = StringUtils()
    res = string_util.end_with("You don't have to say you love me", "e")
    assert res == True

# 68. ПОЗИТИВНЫЙ: пробел после текста
def test_end_with_space_after_string():
    string_util = StringUtils()
    res = string_util.end_with("You don't have to say nothing ", " ")
    assert res == True

# 69. НЕГАТИВНЫЙ: несколько конечных символов
@pytest.mark.xfail
def test_end_with_several_symbols():
    string_util = StringUtils()
    res = string_util.end_with("You don't have to say you're mine", "ine")
    assert res == True
# Ждем ошибку?

# 70. НЕГАТИВНЫЙ: не указан проверяемый начальный символ
def test_end_with_no_symbol_mentioned():
    string_util = StringUtils()
    with pytest.raises(TypeError):
        string_util.end_with('Honey')
# Ошибка, нет обязательного аргумента

# 71. НЕГАТИВНЫЙ: пустая строка
@pytest.mark.xfail
def test_end_with_empty_string():
    string_util = StringUtils()
    res = string_util.end_with('', '')
    assert res == True
# Ждем ошибку?

# 72. НЕГАТИВНЫЙ: пробелы
@pytest.mark.xfail
def test_end_with_all_spaces():
    string_util = StringUtils()
    res = string_util.end_with('     ', ' ')
    assert res == True
# Ждем ошибку?

# 73. НЕГАТИВНЫЙ: None
def test_end_with_none():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.end_with(None, None)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 74. НЕГАТИВНЫЙ: Тип данных - int
def test_end_with_int():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.end_with(9876, 6)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 75. НЕГАТИВНЫЙ: Тип данных - Boolean
def test_end_with_boolean():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.end_with(False, True)
# Ожидаемая ошибка - функция не принимает этот тип данных





# IS_EMPTY
# 76. ПОЗИТИВНЫЙ: Строка пустая
def test_is_empty_string_is_empty():
    string_util = StringUtils()
    res = string_util.is_empty('')
    assert res == True

# 77. ПОЗИТИВНЫЙ: Пробелы
def test_is_empty_all_spaces():
    string_util = StringUtils()
    res = string_util.is_empty('    ')
    assert res == True

# 78. ПОЗИТИВНЫЙ: Непустая строка
def test_is_empty_string_is_not_empty():
    string_util = StringUtils()
    res = string_util.is_empty('Adore')
    assert res == False

# 79. ПОЗИТИВНЫЙ: Непустая строка с пробелами
def test_is_empty_string_is_not_empty_with_spaces():
    string_util = StringUtils()
    res = string_util.is_empty('I will walk through fire for you')
    assert res == False

# 80. ПОЗИТИВНЫЙ: Тестируем текст с числами как строками
def test_is_empty_ints_as_string():
    string_util = StringUtils()
    res = string_util.is_empty('777565748')
    assert res == False

# 81. НЕГАТИВНЫЙ: None
def test_is_empty_none():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.is_empty(None)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 82. НЕГАТИВНЫЙ: Тип данных - int
def test_is_empty_int():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.is_empty(98764563)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 83. НЕГАТИВНЫЙ: Тип данных - Boolean
def test_is_empty_boolean():
    string_util = StringUtils()
    with pytest.raises(AttributeError):
        string_util.is_empty(False)
# Ожидаемая ошибка - функция не принимает этот тип данных




# LIST_TO_STRING
# 84. ПОЗИТИВНЫЙ: Список из строковых значений, без указания разделителя
def test_list_to_string_with_str_no_specific_joiner():
    string_util = StringUtils()
    res = string_util.list_to_string(['Just', 'let', 'me', 'adore', 'you'])
    assert res == 'Just, let, me, adore, you'

# 85. ПОЗИТИВНЫЙ: Список из строковых значений с указанием особого разделителя
def test_list_to_string_with_str_with_specific_joiner():
    string_util = StringUtils()
    res = string_util.list_to_string(['Just', 'let', 'me', 'adore', 'you'], '--')
    assert res == 'Just--let--me--adore--you'

# 86. ПОЗИТИВНЫЙ: Список из числовых значений, без указания разделителя
def test_list_to_string_with_int_no_specific_joiner():
    string_util = StringUtils()
    res = string_util.list_to_string([7,8,9,6,5])
    assert res == '7, 8, 9, 6, 5'

# 87. ПОЗИТИВНЫЙ: Список из числовых значений с указанием особого разделителя
def test_list_to_string_with_int_with_specific_joiner():
    string_util = StringUtils()
    res = string_util.list_to_string([3,2,1,0], '*')
    assert res == '3*2*1*0'

# 88. ПОЗИТИВНЫЙ: Список из булевых значений, без указания разделителя
def test_list_to_string_with_bool_no_specific_joiner():
    string_util = StringUtils()
    res = string_util.list_to_string([True,True,False])
    assert res == 'True, True, False'

# 89. ПОЗИТИВНЫЙ: Список из булевых значений с указанием особого разделителя
def test_list_to_string_with_bool_with_specific_joiner():
    string_util = StringUtils()
    res = string_util.list_to_string([True,False,False], ' ^ ')
    assert res == 'True ^ False ^ False'

# 90. НЕГАТИВНЫЙ: Пустой список
def test_list_to_string_empty_list():
    string_util = StringUtils()
    res = string_util.list_to_string([])
    assert res == ''
# Ждем ошибку?

# 91. НЕГАТИВНЫЙ: str
@pytest.mark.xfail
def test_list_to_string_str():
    string_util = StringUtils()
    res = string_util.list_to_string('Cinema')
    assert res == '     '
# Должна быть ошибка

# 92. НЕГАТИВНЫЙ: None
def test_list_to_string_none():
    string_util = StringUtils()
    with pytest.raises(TypeError):
        string_util.list_to_string(None)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 93. НЕГАТИВНЫЙ: Тип данных - int
def test_list_to_string_int():
    string_util = StringUtils()
    with pytest.raises(TypeError):
        string_util.list_to_string(8763)
# Ожидаемая ошибка - функция не принимает этот тип данных

# 94. НЕГАТИВНЫЙ: Тип данных - Boolean
def test_list_to_string_boolean():
    string_util = StringUtils()
    with pytest.raises(TypeError):
        string_util.list_to_string(False)
# Ожидаемая ошибка - функция не принимает этот тип данных