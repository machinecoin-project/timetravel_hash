import timetravel_hash
from binascii import unhexlify, hexlify

import unittest

# machinecoin block #900000
# moo@b1:~/.machinecoin$ machinecoind getblockhash 1
# 9ef2a0f1cda866165aaeb72396ae3881171f5a0b2a9c012bea6f3ec23d3eee13
# moo@b1:~/.machinecoin$ machinecoind getblock 9ef2a0f1cda866165aaeb72396ae3881171f5a0b2a9c012bea6f3ec23d3eee13
# {
#   "hash": "9ef2a0f1cda866165aaeb72396ae3881171f5a0b2a9c012bea6f3ec23d3eee13",
#   "confirmations": 22059,
#   "strippedsize": 1119,
#   "size": 2343,
#   "weight": 5700,
#   "height": 900000,
#   "version": 536870912,
#   "versionHex": "20000000",
#   "merkleroot": "1dd20594fa290ff369770f1c4268c539e3da311cd5b6b8ef6173dd1a00225cc7",
#   "tx": [
#     "b97524fa6340277a34c622bcc26401f32e1ec5fb8919d3fb851aefb8400f46f6",
#     "a92dde3b409a8bfd4760e9e1c557966029d7eb424be7a3f66651dc1217673c9f",
#     "1adde16d0f425c6c7c6fba82a0a2997e391847299337e0e01f9ef34386983eae"
#   ],
#   "time": 1589414512,
#   "mediantime": 1589413634,
#   "nonce": 2397519618,
#   "bits": "1d03cb3f",
#   "difficulty": 0.2635749017652098,
#   "chainwork": "000000000000000000000000000000000000000000000000034b77cae23b03b7",
#   "nTx": 3,
#   "previousblockhash": "3f956e3813a06b8973875552ec6bc5db5c8d0ef251efe06a16c42def050977a7",
#   "nextblockhash": "42110a2892e783570bf6ba3ef0c445187581c6eede66d10f146838e524fba39e"
# }

header_hex = ("00000020" +
    "a7770905ef2dc4166ae0ef51f20e8d5cdbc56bec52558773896ba013386e953f" +
    "c75c22001add7361efb8b6d51c31dae339c568421c0f7769f30f29fa9405d21d"
    "708abc5e" +
    "3fcb031d" +
    "023fe78e")
best_hash = '13ee3e3dc23e6fea2b019c2a0b5a1f178138ae9623b7ae5a1666a8cdf1a0f29e'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_timetravel_hash(self):
        self.pow_hash = hexlify(timetravel_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash.decode(), self.best_hash)


if __name__ == '__main__':
    unittest.main()

