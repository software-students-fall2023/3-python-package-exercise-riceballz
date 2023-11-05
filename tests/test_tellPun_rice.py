from src.riceinfo.rice import riceinfo
from src.riceinfo.rice import punsDict
from src.riceinfo.rice import Pun
import pytest

class Tests:
    def test_pun_short(self):
        actual = riceinfo.tellPun(self)
        assert isinstance(actual, str), f"Expected tellPun(PunType) to return a string. Instead it returned a {actual}"
        pytest.assert_in(actual, punsDict[Pun.SHORT]), f"Expected tellPun(SHORT) to return a short pun. Instead it didn't return the correct type"

    def test_pun_medium(self):
        actual = riceinfo.tellPun(self)
        assert isinstance(actual, str), f"Expected tellPun(PunType) to return a string. Instead it returned a {actual}"
        pytest.assert_in(actual, punsDict[Pun.MEDIUM]), f"Expected tellPun(MEDIUM) to return a medium pun. Instead it didn't return the correct type"

    def test_pun_long(self):
        actual = riceinfo.tellPun(self)
        assert isinstance(actual, str), f"Expected tellPun(PunType) to return a string. Instead it returned a {actual}"
        pytest.assert_in(actual, punsDict[Pun.LONG]), f"Expected tellPun(LONG) to return a long pun. Instead it didn't return the correct type"
        
    def test_pun_dad(self):
        actual = riceinfo.tellPun(self)
        assert isinstance(actual, str), f"Expected tellPun(PunType) to return a string. Instead it returned a {actual}"
        pytest.assert_in(actual, punsDict[Pun.DAD]), f"Expected tellPun(DAD) to return a dad pun. Instead it didn't return the correct type"
        
    def test_pun_rhyme(self):
        actual = riceinfo.tellPun(self)
        assert isinstance(actual, str), f"Expected tellPun(PunType) to return a string. Instead it returned a {actual}"
        pytest.assert_in(actual, punsDict[Pun.RHYME]), f"Expected tellPun(RHYME) to return a rhyme pun. Instead it didn't return the correct type"
        
    def test_pun_invalid(self):
        actual = riceinfo.tellPun(self)
        assert isinstance(actual, str), f"Expected tellPun(PunType) to return a string. Instead it returned a {actual}"
        assert actual == "not a valid PUN TYPE", f"Expected tellPun(PunType) to return an error message. Instead it returned {actual}"