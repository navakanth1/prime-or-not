import pytest

import pri

@pytest.mark.parametrize("a, b", [(3, True), (5, False), (2, False), (202, False), (11, True)])
def test_prime(a,b):
    result = pri.checkPrime(a)
    assert result == b
