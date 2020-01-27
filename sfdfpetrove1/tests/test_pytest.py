import pytest

import app

WORDS = ['1', '2', '3']

def test_get_random_word():
    word = app.get_random_word(WORDS)
    assert word in WORDS

def test_get_word_display_empty():
    result = app.get_word_display('abc', [])
    assert result == '_ _ _ '

def test_get_word_display_not_empty():
    result = app.get_word_display('abc', ['a', 'c'])
    assert result == 'A _ C '

def test_check_answer_true():
    word1 = 'w1'
    word2 = 'w1'
    result = app.check_answer(word1, word2)
    assert result == True

def test_check_answer_false():
    word1 = 'w1'
    word2 = 'w2'
    result = app.check_answer(word1, word2)
    assert result == False