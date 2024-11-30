import pytest
from kospk import transfer_word  


def test_transfer_word():
    assert transfer_word("наприклад") == "на-при-клад"
    assert transfer_word("український") == "укра-їн-сь-кий"
    assert transfer_word("розроблення") == "роз-роб-лен-ня"
    assert transfer_word("програми") == "про-гра-ми"
    assert transfer_word("це") == "це"
    assert transfer_word("швидко") == "швид-ко"
    assert transfer_word("лис") == "лис"
    assert transfer_word("кота") == "ко-та"
    assert transfer_word("тест") == "тест"
    assert transfer_word("один") == "о-дин"
    assert transfer_word("привіт") == "при-віт"
    assert transfer_word("маленький") == "ма-лень-кий"  
