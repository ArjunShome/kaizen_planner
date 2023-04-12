import binascii
import json

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import unpad, pad


class AppCryptor(object):

    @staticmethod
    def get_aes_key_iv_pair_by_password(password, salt_bytes=8, key_bytes=32):
        salt = Random.new().read(salt_bytes)
        aes_key = PBKDF2(password, salt, key_bytes)

        aes_iv = binascii.hexlify(Random.new().read(AES.block_size)).decode()
        aes_key = binascii.hexlify(aes_key).decode()

        return aes_iv, aes_key

    @staticmethod
    def generate_key(key_bytes=32):
        _key = Random.get_random_bytes(key_bytes)
        _key = binascii.hexlify(_key)
        return _key.decode()

    @staticmethod
    def generate_iv(iv_bytes=16):
        _iv = Random.get_random_bytes(iv_bytes)
        _iv = binascii.hexlify(_iv)
        return _iv.decode()

    @staticmethod
    def get_aes_key_iv_pair_random(key_bytes=32, iv_bytes=16):
        aes_key = AppCryptor.generate_key(key_bytes)
        aes_iv = AppCryptor.generate_iv(iv_bytes)

        return aes_iv, aes_key

    @staticmethod
    def encrypt(data_str, aes_key, aes_iv):
        key = binascii.unhexlify(aes_key)
        iv = binascii.unhexlify(aes_iv)
        aes = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
        encrypted = aes.encrypt(pad(data_str.rstrip().encode(), block_size=AES.block_size))
        return binascii.hexlify(encrypted).decode()

    @staticmethod
    def decrypt(data_str, aes_key, aes_iv):
        key = binascii.unhexlify(aes_key)
        iv = binascii.unhexlify(aes_iv)
        enc = binascii.unhexlify(data_str)

        aes = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
        decrypted = aes.decrypt(enc)
        decrypted_text = unpad(decrypted, block_size=AES.block_size).decode()
        try:
            json_obj = json.loads(decrypted_text)
        except json.JSONDecodeError as e:
            return decrypted_text
        else:
            return json_obj
