import base64
from Crypto.Cipher import AES


class ApimUtil:
    encodings = "utf-8"
    key = bytes("F914EDA9CBB2E9E6D754535780D11BB7", encodings)  # should retrieve from secret manager
    init_vector = bytes("FBF9833BFCA3A232", encodings)  # should retrieve from secret manager
    mac_len = 14
    crypto = AES.new(key, AES.MODE_GCM, init_vector, mac_len=mac_len)

    @classmethod
    def encrypt(cls, text):
        byte_text = bytes(text, cls.encodings)
        cipher_text, tag = cls.crypto.encrypt_and_digest(byte_text)
        return base64.b64encode(cipher_text + tag).decode(cls.encodings)

    @classmethod
    def decrypt(cls, base64_text):
        cipher_text_with_tag = base64.b64decode(base64_text)
        tag = cipher_text_with_tag[-cls.mac_len:]
        cipher_text = cipher_text_with_tag[:-cls.mac_len]
        return (
            AES.new(cls.key, AES.MODE_GCM, cls.crypto.nonce, mac_len=cls.mac_len)
            .decrypt_and_verify(cipher_text, tag)
            .decode(cls.encodings)
        )


xx = ApimUtil.encrypt("000000005000")
yy = ApimUtil.decrypt("F7oF191x8fj3C6TYR7b+cbFjK8VS")
print(xx)
print(yy)


