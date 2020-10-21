import string

import pytest
import python_analyser


def test_count_lines():
    assert python_analyser.count_lines("simple_file.py") == 5
    assert python_analyser.count_lines("to_analyse.py") == 269


def test_count_not_empty_lines():
    assert python_analyser.count_not_empty_lines("simple_file.py") == 4
    assert python_analyser.count_not_empty_lines("to_analyse.py") == 238


def test_count_comment_lines():
    assert python_analyser.count_comment_lines("simple_file.py") == 2
    assert python_analyser.count_comment_lines("to_analyse.py") == 40


def test_count_code_lines():
    assert python_analyser.count_code_lines("simple_file.py") == 2
    assert python_analyser.count_code_lines("to_analyse.py") == 198


def test_count_words():
    assert python_analyser.count_words("simple_file.py") == 11
    assert python_analyser.count_words("to_analyse.py") == 1167


def test_count_word():
    assert python_analyser.count_word("simple_file.py", "def") == 1
    assert python_analyser.count_word("to_analyse.py", "def") == 14


def test_count_comment_words():
    assert python_analyser.count_comment_words("simple_file.py") == 4
    assert python_analyser.count_comment_words("to_analyse.py") == 273


def test_count_syntax_word():
    assert python_analyser.count_syntax("simple_file.py", "def") == 1
    assert python_analyser.count_syntax("to_analyse.py", "def") == 14
