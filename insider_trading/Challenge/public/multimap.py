from __future__ import annotations

from typing import List, Union

from sage.all import *

import config


class Params:
    def __init__(self) -> None:
        self.x_0 = 1
        self.xp = []
        self.x = []
        self.y = 0
        self.zerotest = 0


class Encoding:
    def __init__(self, value: Integer, level: int, params: Params) -> None:
        self.value = Zmod(params.x_0)(value)
        self.level = level
        self.params = params

    def __add__(self, other: Encoding) -> Encoding:
        assert self.level == other.level
        return Encoding(self.value + other.value, self.level, self.params)

    def __sub__(self, other: Encoding) -> Encoding:
        assert self.level == other.level
        return Encoding(self.value - other.value, self.level, self.params)

    def __mul__(self, other: Union[Encoding, Integer]) -> Encoding:
        return Encoding(self.value * other.value, self.level + other.level, self.params)

    def __pow__(self, exp: int) -> Encoding:
        return Encoding(self.value ** exp, self.level * exp, self.params)


def centered_random(nBytes: int) -> Integer:
    return ZZ.random_element(2 ** nBytes) - (1 << (nBytes - 1))


def mod_near(i: int, m: int) -> Integer:
    i = ZZ(i)
    res = i % m
    if res > m // 2:
        res -= m
    return res


# This function transforms a random bit vector into a random level 0 encoding
# Note that this is not necessarily uniform due to small ell optimization
def sample(para: Params, message: List[bool]) -> Encoding:
    assert len(message) == config.ell

    res = Encoding(0, 0, para)
    for i, b in enumerate(message):
        if b:
            res += para.xp[i]

    return res


def rerandomize(para: Params, ciphertext: Encoding) -> Encoding:
    assert ciphertext.level == 1

    res = Encoding(0, 1, para)
    res += para.x[randrange(config.delta)]

    return ciphertext + res


def zerotest(para: Params, ciphertext: Encoding) -> Integer:
    assert ciphertext.level <= config.kappa

    return mod_near(
        ciphertext.value
        * (para.y ** (config.kappa - ciphertext.level)).value
        * para.zerotest,
        para.x_0,
    )


def extract(para: Params, ciphertext: Encoding) -> Integer:
    return zerotest(para, ciphertext) >> (para.x_0.nbits() - config.sessionKeyBits)
