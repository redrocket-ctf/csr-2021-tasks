import pickle
from re import X
from typing import List

from sage.all import *
from tqdm import tqdm

import config
from multimap import Encoding, Params, centered_random


class PrivParams:
    def __init__(self):
        self.p = []
        self.crtCoeffs = []
        self.g = []
        self.z = 0
        self.zinv = 0
        self.A = None


def gen_params() -> Params:
    # Make sage fast
    proof.all(False)

    para = Params()
    privPara = PrivParams()

    # Generate p_i
    # Optimization: p_i's might be generated as products of primes to speed up computation
    n_iter = config.eta // config.etp

    assert config.eta % config.etp == 0

    for i in tqdm(range(config.n), "p_i"):
        p_i = 1
        for j in range(n_iter):
            p_i *= next_prime(ZZ.random_element(2 ** config.etp))
        privPara.p.append(p_i)

    para.x_0 = prod(privPara.p)

    # Generate CRT coefficients
    for i in tqdm(range(config.n), "CRT"):
        q = ZZ(para.x_0 / privPara.p[i])
        privPara.crtCoeffs.append(q.inverse_mod(privPara.p[i]) * q)

    # Generate g_i
    for i in tqdm(range(config.n), "g_i"):
        privPara.g.append(next_prime(ZZ.random_element(2 ** config.alpha)))

    # Generate z
    while True:
        privPara.z = Zmod(para.x_0).random_element()
        try:
            privPara.zinv = privPara.z ** -1
            break
        except ZeroDivisionError:
            pass

    # Generate A
    privPara.A = matrix(
        ZZ, config.ell, config.n, lambda i, j: centered_random(config.alpha)
    )

    # Generate xp_i
    for row in tqdm(privPara.A.rows(), "x'_i"):
        para.xp.append(encrypt_with_priv_key(privPara, para, row, config.rho, 0))

    # Generate x_i
    for i in tqdm(range(config.delta), "x_i"):
        para.x.append(
            encrypt_with_priv_key(privPara, para, vector(ZZ, config.n), config.rho, 1)
        )

    # Generate y
    para.y = encrypt_with_priv_key(privPara, para, [1] * config.n, config.rho, 1)

    # Generate zerotest
    para.zerotest = 0
    z_kappa = privPara.z ** config.kappa

    for i in tqdm(range(config.n), "zerotest"):
        t_res = privPara.g[i].inverse_mod(privPara.p[i])
        t_res = (
            ZZ(mod(t_res * z_kappa, privPara.p[i]))
            * centered_random(config.hBits)
            * ZZ(para.x_0 / privPara.p[i])
        )
        para.zerotest += t_res

    return para


def encrypt_with_priv_key(
    privPara: PrivParams, para: Params, message: List[Integer], nSize: int, level: int
) -> Encoding:
    assert len(message) == config.n

    res = Zmod(para.x_0)(0)
    for i in range(config.n):
        # Calculate level 0 encodings in Z/(p_i)Z and map to Z/(x_0)Z
        res += (
            message[i] + privPara.g[i] * centered_random(nSize)
        ) * privPara.crtCoeffs[i]

    res *= privPara.zinv ** level

    return Encoding(res, level, para)


if __name__ == "__main__":
    params = gen_params()

    dest_pub = open("params.pub", "wb")
    pickle.dump(params, dest_pub)
