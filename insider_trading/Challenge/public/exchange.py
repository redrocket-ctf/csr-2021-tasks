import hashlib
import json
import pickle
import secrets
from base64 import b64encode
from typing import List

from Crypto.Cipher import AES
from sage.all import prod
from tqdm import tqdm

import config
from multimap import *


class DHClient:
    def __init__(self, para: Params) -> None:
        self.para = para

    def publish(self) -> Encoding:
        random_value = secrets.randbits(config.ell)
        random_bits = [True if c == "1" else False for c in bin(random_value)[2:]]
        random_bits += [0 for _ in range(config.ell - len(random_bits))]
        self.secret = sample(self.para, random_bits)
        return rerandomize(self.para, self.secret * self.para.y)

    def generate_key(self, pub_vals: List[Encoding]) -> bytes:
        assert len(pub_vals) == config.kappa

        encoded_value = prod(pub_vals, self.secret)
        common_value = extract(self.para, encoded_value)
        return int(common_value).to_bytes(
            common_value.nbits() // 8 + 1, "little", signed=True
        )


def main():
    flag = open("../flag.txt", "r").read().strip()
    key_file = open("params.pub", "rb")

    # Make sage fast
    proof.all(False)

    para: Params = pickle.load(key_file)

    clients = []
    public_values = []
    for i in tqdm(range(config.kappa + 1), "Publish"):
        client = DHClient(para)
        clients.append(client)
        public_values.append(client.publish())
        tqdm.write(f"Client {i}: {public_values[i].value}")

    secret = None
    for i in tqdm(range(config.kappa + 1), "Generate key"):
        new_secret = clients[i].generate_key(public_values[:i] + public_values[i + 1 :])
        if secret:
            assert new_secret == secret
        secret = new_secret

    hash_fcnt = hashlib.sha256()
    hash_fcnt.update(secret)
    key = hash_fcnt.digest()

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(flag.encode())
    json_k = ["nonce", "ciphertext", "tag"]
    json_v = [b64encode(x).decode("utf-8") for x in (cipher.nonce, ciphertext, tag)]
    result = json.dumps(dict(zip(json_k, json_v)))

    open("flag.enc", "w").write(result)


if __name__ == "__main__":
    main()
